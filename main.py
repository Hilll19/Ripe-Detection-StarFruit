import cv2

def colorProfiles(n):
    if n == 0 :
        name = "Unripe"
        hsv_lower = ( 28,46,45)
        hsv_upper = (70,255,255)
        return (name,hsv_lower,hsv_upper)
    if n == 1 :
        name = "Ripe"
        hsv_lower = ( 18,85,0)
        hsv_upper = (28,255,255)
        return (name,hsv_lower,hsv_upper)

frame = cv2.imread("starfruit3.jpg")
hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
rects = {}

for i in range(2):
	name, hsv_lower, hsv_upper = colorProfiles(i)
	mask = cv2.inRange(hsv,hsv_lower,hsv_upper)
	conts, herirarchy = cv2.findContours(mask.copy(),cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
	biggest = sorted(conts,key = cv2.contourArea,reverse=True)[0]
	rect = cv2.boundingRect(biggest)
	x,y,w,h = rect
	cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,255),2)
	cv2.putText(frame, name, (x,y),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),2)

cv2.imshow("Image",frame)
cv2.imshow("Progress Ripe",mask)
cv2.waitKey(0)
cv2.destroyAllWindows()