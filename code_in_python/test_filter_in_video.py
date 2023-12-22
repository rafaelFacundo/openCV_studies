import cv2 as cv

doctorWhoOpennig = cv.VideoCapture("videos/DoctorWhoOp.mp4");

while True:
    stillHaveFramesToRead, currentFrame = doctorWhoOpennig.read();
    if stillHaveFramesToRead:
        currentFrameFiltered = cv.Canny(currentFrame, 125,175);
        cv.imshow("Doctor Who", currentFrameFiltered);
        if cv.waitKey(20) & 0xFF==ord('d'):
            break

doctorWhoOpennig.release();
cv.destroyAllWindows();