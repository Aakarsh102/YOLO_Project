# from roboflow import Roboflow
# rf = Roboflow(api_key="NgYavDeQYGnJD55b8LiN")
# project = rf.workspace("first-sixpi").project("hand-fist-computer")
# version = project.version(2)
# dataset = version.download("yolov5")
import cv2

cap = cv2.VideoCapture(1)
if not cap.isOpened():
    print("Cannot open camera")
    exit()
while True:
    ret, frame = cap.read()
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
