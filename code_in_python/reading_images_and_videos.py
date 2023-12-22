import cv2 as cv

""" 
    the opencv function IMREAD, read an image and return to us the image as a matrix 
    of pixels, so the first image that we are going to read is the Doctor who's image
    that is in the photos folter
"""

#doctorWhoImage = cv.imread('photos/doctor.jpg');

""" 
    But what if we whant to show this image ? 
    We can do it but using the function IMSHOW
    to use this function we pass two parameters: the window's name and the matrix of pixels
    that we whant to show, remember, here, a matrix of pixels is our image
"""

#cv.imshow("Doctor who", doctorWhoImage);

""" 
    but to show the image we need to add another functions
    the WAITKEY function
    with this function opencv will wait for some press in a key in the keyboard
    when we pass the value 0 we goona wait for a infinite amount of time

"""
#cv.waitKey(0);

""" 
    Now lets move on and try to read videos
    To read a video we can use the function VIDEOCAPTURE
    we can pass an integer or a path to video that we wanna load
    The path we all know for what it is
    but what about the integer ? 
    well, when we whant to load a video from the camera that we have atached to the
    computer we pass a integer to the function, the number 0 refers to the main camera
    atached to the computer web, we can pass 0,1,2,3....
    each number refers to the order of the camera connected to computer
    for exemple, if you to connect to with second camera connected to your computer 
    you must call the function passing 1 as the argument
"""

capture = cv.VideoCapture('videos/DoctorWhoOp.mp4');

""" 
    To read the video, talking in a simply way, we are gonna read the video frame by frame
    in a while, with the function capture.read() that will return each video's frame to us
    to show each frame we will use the same function we used to show an image
    the imshow()
    and we will put a if with the condition, if the key 'D' is press than stop the while
    in the end of the loop we need to release the video capture and
    destroy all the windows instances that we have
"""

while True:
    isTrue, frame = capture.read();
    if isTrue:
        cv.imshow("Video",frame);
        if cv.waitKey(20) & 0xFF==ord('d'):
            break

capture.release();
cv.destroyAllWindows();

