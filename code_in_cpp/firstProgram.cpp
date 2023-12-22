#include <iostream>
#include <opencv2/core/core.hpp>
#include <opencv2/highgui/highgui.hpp>
#include <opencv2/imgcodecs/imgcodecs.hpp>
using namespace cv;
using namespace std;

int main(int argc, char** argv)
{
    Mat img = imread("./doctor.jpg");
    imshow("Window", img);
    //wait key is need when we whant to use GUI event
    //for exemple showing a image
    waitKey(0);
    //the zero means that the image will be show untill we get
    //any key press
}
