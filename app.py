import cv2
import numpy as np
from keras.models import load_model


new_model =load_model('./Final_model.h5')
font_scale = 1.5
font = cv2.FONT_HERSHEY_PLAIN
rectangle_bgr = (255, 255, 255)
img = np.zeros((500, 500))
text = "Some text in a box!"
(text_width, text_height) = cv2.getTextSize(text, font, fontScale=font_scale, thickness=1)[0]
text_offset_x = 10
text_offset_y = img.shape[0] - 25
box_coords = ((text_offset_x, text_offset_y), (text_offset_x + text_width + 2, text_offset_y - text_height -2))
cv2.rectangle(img, box_coords[0], box_coords[1], rectangle_bgr, cv2.FILLED)
cv2.putText(img, text, (text_offset_x, text_offset_y), font, fontScale=font_scale, color=(0, 0, 0),thickness=1)

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    raise IOError("Cannot open webcam")

def addText(status):
    cv2.rectangle(frame, (x,y), (x+w, y+h), (0, 255, 0))
    cv2.putText(frame,status,(x,y),cv2.FONT_ITALIC,1.5,(0,255,0),2)
while True:
    _,frame = cap.read()
    faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    try:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    except:
        pass
    faces = faceCascade.detectMultiScale(gray,1.1,4)
    for x,y,w,h in faces:
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]
        facess = faceCascade.detectMultiScale(roi_gray)
    if len(facess) == 0:
        print("Face not detected")
    else:
        ex,ey,ew,eh = facess[0]
        face_roi = roi_color[ey: ey+eh, ex:ex + ew]
        final_image = cv2.resize(face_roi, (224,224))
        final_image = np.expand_dims(final_image,axis=0)
        final_image = final_image/255.0
        Predictions = new_model.predict(final_image)
        print(Predictions)
        emotions = ["Angry","Happy","Neutral","Sad","Surprise"]
        # results=imagenet_utils.decode_predictions(Predictions)
        print(emotions[np.argmax(Predictions)])
        addText(emotions[np.argmax(Predictions)])
        cv2.imshow('Face Emotion Recognition', frame)
    if cv2.waitKey(2) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
