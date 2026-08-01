import cv2
import mediapipe as mp
import pyvjoy
cam=cv2.VideoCapture(1)
hands = mp.solutions.hands.Hands(
    static_image_mode = False,
    max_num_hands = 1,
    min_detection_confidence = 0.5,
    min_tracking_confidence = 0.45
)
center=0.49
dead_zone=0.03
samples = []
calibrating = False
steering=0
left_limit = 0.33
right_limit = 0.36
print(pyvjoy.HID_USAGE_X)
j = pyvjoy.VJoyDevice(1)
mp_draw = mp.solutions.drawing_utils
while True:
    if cam.isOpened():
        success,frame=cam.read()
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = hands.process(rgb)
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                mp_draw.draw_landmarks(
                frame,
                hand_landmarks,
                mp.solutions.hands.HAND_CONNECTIONS
                )
                palm = hand_landmarks.landmark[9]
                if calibrating:
                    samples.append(palm.x)
                if len(samples)>=30:
                    center = sum(samples) / len(samples)
                    calibrating = False
                    samples = []
                    print("Calibration Complete!")
                    print(round(center, 3))
                    
                
                
                offset = palm.x - center
                
                if abs(offset)<dead_zone:
                    offset=0
                
                if offset<0:
                    steering=offset/left_limit
                else:
                    steering=offset/right_limit
                steering = max(-1, min(1, steering))
                axis = int((steering + 1) * 32767.5)
            j.set_axis(pyvjoy.HID_USAGE_X, axis)
            
        dot_x = 320 + steering * 220

               

        cv2.line(frame, (100, 450), (540, 450), (255, 255, 255), 3)   
        cv2.circle(frame,(int(dot_x), 450), 10, (0, 0, 255), -1)             
        cv2.imshow("i dont like onine on cooked daal",frame)

        c=cv2.waitKey(1)
        if c==ord('q'):
            break
        if c==ord('c'):
                calibrating = True
                samples = []
        
                
        


cam.release()