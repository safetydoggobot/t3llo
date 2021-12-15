from djitellopy import tello
import cv2
import KeyPressModule as kp
import time

kp.init()

tello = Tello()
tello.connect()
print(tello.get_battery())
tello.streamon()
global img
        
def getKeyboardInput():
    lr, fb, ud, yv = 0, 0, 0, 0
    speed = 50

    if kp.getKey("LEFT"): lr = -speed
    elif kp.getKey("RIGHT"): lr = speed

    if kp.getKey("UP"): fb = speed
    elif kp.getKey("DOWN"): fb = -speed

    if kp.getKey("w"): ud = speed
    elif kp.getKey("s"): ud = -speed

    if kp.getKey("a"): yv = -speed
    elif kp.getKey("d"): yv = speed

    if kp.getKey("q"): tello.land()
    if kp.getKey("e"): tello.takeoff()
        
    if kp.getKey("z"):
        cv2.imwrite(f'Resources/Images/{time.time()}.jpg', img)

    return [lr, fb, ud, yv]

while True:
        vals = getKeyboardInput();
        tello.send_rc_control(vals[0], vals[1], vals[2], vals[3]);
        
        img = tello.get_frame_read().frame
        img = cv2.resize(img, (360, 240))
        cv2.imshow("Image", img)
        cv2.waitKey(1)
        sleep(0.05)
