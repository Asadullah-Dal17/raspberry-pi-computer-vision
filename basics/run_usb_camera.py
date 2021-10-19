
import cv2 as cv
import time
starting_time = time.time()
cap = cv.VideoCapture(0)
frame_counter = 0
while True:
    ret, frame = cap.read()
    frame_counter += 1
    #print(frame_counter)
    fps = frame_counter / (time.time()- starting_time)
    #print(fps)

    cv.putText(frame, f'FPS: {round(fps,1)}', (30,40), cv.FONT_HERSHEY_SIMPLEX,0.6 ,(0,255, 0),2)
    cv.imshow("frame", frame)
    key = cv.waitKey(1)
    if key ==ord('q'):
        break
cv.destroyAllWindows()
cap.release()
    

