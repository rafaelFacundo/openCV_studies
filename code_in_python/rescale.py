import cv2 as cv

""" 
    it works with video, live videos and images
"""
def rescaleFrame(frame, scale=0.75):

    width = int(frame.shape[1] * scale);
    height = int(frame.shape[0] * scale);
    dimensions = (width, height);
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

capture = cv.VideoCapture('videos/DoctorWhoOp.mp4');

while True:
    isTrue, frame = capture.read();
    if isTrue:
        resized_frame = rescaleFrame(frame, scale=1.5)
        cv.imshow("Video",resized_frame);
        if cv.waitKey(20) & 0xFF==ord('d'):
            break

capture.release();
cv.destroyAllWindows();

""" only videos """
def changeRes(width, height):
    capture.set(3,width);
    capture.set(4,height);