import cv2

img = cv2.imread("art6.jpg")

def viewimg(img, name_win):
    cv2.namedWindow(name_win, cv2.WINDOW_NORMAL)
    cv2.imshow(name_win, img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def grayImg():
    grayimage = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    viewimg(grayimage, "img градациях серого")
def xbImg():
    ret, thresholdimage = cv2.threshold(img, 127, 255, 0)
    viewimg(thresholdimage, "Чёрно-белый img")
def blurImg():
    blurr = cv2.GaussianBlur(img, (93, 93), 0)
    viewimg(blurr, "Размытый img")
def textImg():
    out = img.copy()
    cv2.putText(out, "text art", (100, 2500),cv2.FONT_HERSHEY_SIMPLEX, 15, (255, 255, 255), 40)
    viewimg(out, "img с текстом")
def lineImg():
    output = img.copy()
    cv2.line(output, (0, 0), (2592, 2592), (0, 0, 255), 30)
    viewimg(output, "img line")
grayImg()
xbImg()
blurImg()
textImg()
lineImg()

