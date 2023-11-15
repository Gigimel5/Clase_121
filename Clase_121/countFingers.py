import cv2
import mediapipe as mp

mp_drawing=mp.solutions.drawing_utils
mp_hands=mp.solutions.hands

hands=mp_hands.Hands(min_detection_confidence=0.8,min_tracking_confidence=0.5)

tipIds=[4,8,12,16,20]

cam = cv2.VideoCapture(0)
def countFingers(image,hand_landmarks,handNo=0):
    landmarks=hand_landmarks[handNo].landmark
    fingers=[]
    for lm_index in tipIds:
        finger_tip_y=landmarks[lm_index].y
        finger_bottom_y=landmarks[lm_index-2].y
        thumb_tip_x=landmarks[lm_index].x
        thumb_bottom_x=landmarks[lm_index-2].x
        if(lm_index!=4):
            if(finger_tip_y<finger_bottom_y):
                fingers.append(1)
                print("Dedo con id ",lm_index," Está abierto")
            if(finger_tip_y>finger_bottom_y):
                fingers.append(1)
                print("Dedo con id ",lm_index," Está cerrado")

def drawHandLandmarks(image,hand_landmarks):
    if(hand_landmarks): 
        for landmarks in hand_landmarks:
            mp_drawing.draw_landmarks(image,landmarks,mp_hands.HAND_CONNECTIONS)

while True:
    success,image=cam.read()
    image=cv2.flip(image,1)
    results=hands.process(image)
    hand_landmarks=results.multi_hand_landmarks
    drawHandLandmarks(image,hand_landmarks)
    cv2.imshow("Camara: ",image)
    key=cv2.waitKey(1)
    if(key==32):
        break
cv2.destroyAllWindows()