from djitellopy import Tello
from time import sleep
import sys
import cv2

drone = Tello()
drone.connect()
print(drone.get_battery())
drone.set_video_direction(Tello.CAMERA_FORWARD)
drone.set_video_resolution(Tello.RESOLUTION_480P)
drone.streamon()
drone.takeoff()
roll, pitch, throttle, yaw = 0, 0, 0, 0
key = -1
while key != 27:
    frame = drone.get_frame_read().frame
    frame = frame[0:478, 0:648]
    frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
    cv2.imshow("Camera", frame)
    if key == ord('a'):
        roll = -15
    elif key == ord('d'):
        roll = 15
    elif key == ord('w'):
        pitch = 15
    elif key == ord('s'):
        pitch = -15
    elif key == ord('r'):
        throttle = 15
    elif key == ord('f'):
        throttle = -15
    elif key == ord('q'):
        yaw = -15
    elif key == ord('e'):
        yaw = 15
    elif key == 32:
        roll, pitch, throttle, yaw = 0, 0, 0, 0
    drone.send_rc_control(roll, pitch, throttle, yaw)
    key = cv2.waitKey(1)
drone.send_rc_control(0, 0, 0, 0)
drone.land()
print(drone.get_battery())
cv2.destroyAllWindows()
drone.end()
sys.exit()