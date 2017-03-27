import base64

img_file = 'test.jpg'
iopen = open(img_file, 'rb').read()
b64 = base64.encodestring(iopen)
b64_urlsafe = base64.urlsafe_b64encode(iopen)


print(b64_urlsafe)
output = open('decoded.jpg', 'wb')
output.write(base64.urlsafe_b64decode(b64_urlsafe))
output.close()

exit()
try:
    # python2
    print('base64(python2) = ' + b64)
except TypeError:
    # python3
    print('base64(python3) = ' + b64.decode('utf8'))
