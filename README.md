# dlib-HOGandCNN-faceDectection
This code uses the dlib library for detecting frontal faces in images.
The HOG frontal face detector uses the algorithm called Histogram of Oriented Gradients for face detection. It is faster than the CNN face detection model but is less accurate.
It is accessible as dlib.get_frontal_face_detector() and is included with the dlib installation, i.e., we don't need model weights for prediction.

For a better accuracy, we can use the CNN face detection, which as it's name suggests, uses the Convolutional Neural Network for face detection.
In my code, I've used the mmod_human_face_detector.dat file, which is a pretrained file for model weights, and can be downloaded easily from any web resource.
For using the CNN face detector, the dlib installation must be configured for using the GPU, i.e., it should be CUDA enabled, else the prediction will be too slow.
To prevent any such cases, you can also use Google Colab.

![hog_face_detection](https://user-images.githubusercontent.com/63373905/125340559-38940880-e370-11eb-9b47-dff4510a7f8f.png)
The above picture is a result of using the HOG face detector.


![cnn_face_detection](https://user-images.githubusercontent.com/63373905/125340663-5d887b80-e370-11eb-8b43-83492431b981.png)

The above picture is the result of using the CNN face detector. We can clearly see the difference between the HOG and CNN detector. The CNN face detector works even if the
face is half visible or even at some other angle or facing the other direction other than front.
