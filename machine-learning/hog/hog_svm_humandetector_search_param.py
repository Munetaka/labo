import cv2
import itertools

# load images
image_list = {}
# sample1.jpg' うまくいくやつ
# sample2.jpg' 前向き
# line_sample1.jpg # 横向き
# line_sample2.jpg # 前向き2
image_list = {
    'sample1': cv2.imread('sample1.jpg'),
    'sample2': cv2.imread('sample2.jpg'),
    'line_sample1': cv2.imread('line_sample1.jpg'),
    'line_sample2': cv2.imread('line_sample2.jpg')
    }


# change gray scale
detect_image_list = {}
for key, img in image_list.items():
    gray_image = gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    detect_image_list[key] = gray_image


# initialize hog settings
hog_list = {
    'default': cv2.HOGDescriptor((64,128), (16,16), (8,8), (8,8), 9),
    'daimler': cv2.HOGDescriptor((48,96), (16,16), (8,8), (8,8), 9),
    'custom': cv2.HOGDescriptor((32,64), (8,8), (4,4), (4,4), 9)
    }


# set model
def set_hog_model(hog, type='default'):
    if type in ('default', 'custom'):
        hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
    elif type == 'daimler':
        hog.setSVMDetector(cv2.HOGDescriptor_getDaimlerPeopleDetector())
    else:
        print(type, 'is not exist')
        exit()
    # return hog


# detect images
def detect(detect_image_list):
    hit_threshold_list = [-0.4, 0, 0.4, 1]
    win_stride_list = [(4,4), (2,2), (1,1)]
    final_threshold_list = [2, 4]
    locations_list = {}

    for name, img in detect_image_list.items():
        for hog_kind, hog in hog_list.items():
            set_hog_model(hog, hog_kind)

            for final_threshold, win_stride, hit_threshold in itertools.product(final_threshold_list, win_stride_list, hit_threshold_list):
                hog_params = {
                    'hitThreshold': hit_threshold,
                    'winStride': win_stride,
                    'finalThreshold': final_threshold,
                    'padding': None,
                    'scale': 1.05,
                    }
                key = 'h' + str(hit_threshold) + '-s' + str(max(win_stride)) + '-f' + str(final_threshold)

                '''
                # print(help(hog.detectMultiScale))
                detectMultiScale(...) method of cv2.HOGDescriptor instance
                    detectMultiScale(img[, hitThreshold[, winStride[, padding[, scale[, finalThreshold[, useMeanshiftGrouping]]]]]]) -> foundLocations, foundWeights
                '''
                locations, weights = hog.detectMultiScale(img, **hog_params) 
                output_name = name + '_' + hog_kind + '_' + key + '.jpg'
                locations_list[output_name] = {
                    'org_image_name': name,
                    'locations': locations
                    }
                rectangle_multi(image_list[name], locations, output_name)
    return locations_list


# draw rectangle on image
def rectangle_multi(image, locations, output_name):
    for (x, y, w, h) in locations:
        cv2.rectangle(image, (x, y), (x + w, y + h), (0,255,0), 2)
        cv2.imshow(output_name, image)
        cv2.imwrite(output_name, image)
    # cv2.waitKey(0)
    cv2.destroyAllWindows()

locations_list = detect(detect_image_list)

# rectangle_multi(image_list, location_list)
exit()

# locations, weights = hog.detectMultiScale(detect_image) # default
# locations, weights = hog.detectMultiScale(detect_image, 0, None, None, 1.05, 2, False) # default


