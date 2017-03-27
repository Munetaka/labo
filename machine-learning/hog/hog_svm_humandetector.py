import cv2



# load image
image = cv2.imread('line_sample1.jpg') # 横向き
image = cv2.imread('line_sample2.jpg') # 前向き
image = cv2.imread('sample1.jpg') # うまくいくやつ
image = cv2.imread('sample2.jpg') # 前向き2
detect_image = image

# change gray scale
gray_image = gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
detect_image = gray_image


# initialize hog settings
# hog = cv2.HOGDescriptor() # default
# hog = cv2.HOGDescriptor((64,128), (16,16), (8,8), (8,8), 9) # default
# hog = cv2.HOGDescriptor((48,96), (16,16), (8,8), (8,8), 9) # for daimler
hog = cv2.HOGDescriptor((32,64), (8,8), (4,4), (4,4), 9) # for custom


# set model
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
# hog.setSVMDetector(cv2.HOGDescriptor_getDaimlerPeopleDetector())


# detect
hog_params = {'hitThreshold': 0, 'winStride': None, 'padding': None, 'scale': 1.05, 'finalThreshold': 2, 'useMeanshiftGrouping': False} # default
# hog_params = {'hitThreshold': 0, 'winStride': (4,4), 'padding': None, 'scale': 1.05, 'finalThreshold': 2, 'useMeanshiftGrouping': False} # custom h0-s4-f2
# hog_params = {'hitThreshold': 0, 'winStride': (2,2), 'padding': None, 'scale': 1.05, 'finalThreshold': 2, 'useMeanshiftGrouping': False} # custom h0-s2-f2
# hog_params = {'hitThreshold': 0, 'winStride': (1,1), 'padding': None, 'scale': 1.05, 'finalThreshold': 2, 'useMeanshiftGrouping': False} # custom h0-s1-f2
# hog_params = {'hitThreshold': 1, 'winStride': (4,4), 'padding': None, 'scale': 1.05, 'finalThreshold': 2, 'useMeanshiftGrouping': False} # custom h1-s4-f2
# hog_params = {'hitThreshold': 1, 'winStride': (2,2), 'padding': None, 'scale': 1.05, 'finalThreshold': 2, 'useMeanshiftGrouping': False} # custom h1-s2-f2
# hog_params = {'hitThreshold': 1, 'winStride': (1,1), 'padding': None, 'scale': 1.05, 'finalThreshold': 2, 'useMeanshiftGrouping': False} # custom h1-s1-f2
# hog_params = {'hitThreshold': 0.4, 'winStride': (4,4), 'padding': None, 'scale': 1.05, 'finalThreshold': 2, 'useMeanshiftGrouping': False} # custom h0.4-s4-f2
# hog_params = {'hitThreshold': 0.4, 'winStride': (2,2), 'padding': None, 'scale': 1.05, 'finalThreshold': 2, 'useMeanshiftGrouping': False} # custom h0.4-s2-f2
# hog_params = {'hitThreshold': 0.4, 'winStride': (1,1), 'padding': None, 'scale': 1.05, 'finalThreshold': 2, 'useMeanshiftGrouping': False} # custom h0.4-s1-f2

'''
# print(help(hog.detectMultiScale))
detectMultiScale(...) method of cv2.HOGDescriptor instance
    detectMultiScale(img[, hitThreshold[, winStride[, padding[, scale[, finalThreshold[, useMeanshiftGrouping]]]]]]) -> foundLocations, foundWeights
'''
# locations, weights = hog.detectMultiScale(detect_image) # default
# locations, weights = hog.detectMultiScale(detect_image, 0, None, None, 1.05, 2, False) # default
locations, weights = hog.detectMultiScale(detect_image, **hog_params) # default
for (x, y, w, h) in locations:
    cv2.rectangle(image, (x, y), (x + w, y + h), (0,255,0), 2)

cv2.imshow("human detection", image)
cv2.waitKey(0)

# save image
cv2.imwrite('result1.jpg', image)

# cv2.imwrite('default.jpg', image) # D-D-D
# cv2.imwrite('daimler_default.jpg', image) # L-L-D
# cv2.imwrite('custome_default.jpg', image) # U-D-D

# D-D-D base
# cv2.imwrite('default-h0-s4-f2.jpg', image) # hit:0, s(4,4), final:2
# cv2.imwrite('default-h0-s2-f2.jpg', image) # hit:0, s(2,2), final:2
# cv2.imwrite('default-h0-s1-f2.jpg', image) # hit:0, s(1,1), final:2

# U-D-D base
# cv2.imwrite('custom-h0-s4-f2.jpg', image) # hit:0, s(4,4), final:2
# cv2.imwrite('custom-h0-s2-f2.jpg', image) # hit:0, s(2,2), final:2
# cv2.imwrite('custom-h0-s1-f2.jpg', image) # hit:0, s(1,1), final:2

# cv2.imwrite('custom-h1-s4-f2.jpg', image) # hit:1, s(4,4), final:2
# cv2.imwrite('custom-h1-s2-f2.jpg', image) # hit:1, s(2,2), final:2
# cv2.imwrite('custom-h1-s1-f2.jpg', image) # hit:1, s(1,1), final:2

# cv2.imwrite('custom-h0.4-s4-f2.jpg', image) # hit:0.4, s(4,4), final:2
# cv2.imwrite('custom-h0.4-s2-f2.jpg', image) # hit:0.4, s(2,2), final:2
# cv2.imwrite('custom-h0.4-s1-f2.jpg', image) # hit:0.4, s(1,1), final:2


cv2.destroyAllWindows()
