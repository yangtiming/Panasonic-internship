# Panasonic-internship
Panasonic internship - face detection &amp;&amp; covid -19 health checking


## Introduction

#### Project purpose:
Realize the integrated detection of station face and health code travel

#### Main Functions of the project:
Realize the call of face recognition, face library management (face increase and delete)

Realize the QR code recognition and GIF, name, green code detection of Liao Shitong health code

## Development environment

#### Hardware Development environment
Raspberry pi 4b

display

camera

#### Software development environment
Python-Pyqt5

Opencv

Raspberry Pi Linux

<img src="https://github.com/yangtiming/Panasonic-internship/blob/master/imgs/IMG_5746.JPG" width="600px">


## GUI and Function Introduction
#### Interface flow chart
<img src="https://github.com/yangtiming/Panasonic-internship/blob/master/imgs/IMG_5748.JPG" width="600px">

#### detection panel
detect face first, and detect the healthy code second

<img src="https://github.com/yangtiming/Panasonic-internship/blob/master/imgs/IMG_5749.JPG" width="600px">

#### Page for registering administrator accounts
administrator accounts can be registered here.

<img src="https://github.com/yangtiming/Panasonic-internship/blob/master/imgs/IMG_5750.JPG" width="600px">

#### Passenger information entry

<img src="https://github.com/yangtiming/Panasonic-internship/blob/master/imgs/IMG_5751.JPG" width="600px">

## Algorithm implementation

#### face detection 

In order to accurately and quickly recognize faces, we use Baidu-face api.

<img src="https://github.com/yangtiming/Panasonic-internship/blob/master/imgs/IMG_5752.JPG" width="600px">

#### Health Code Identification:color identification

In order to Identify green color, RGB is transformed to HSV. And then we use cv2.inRange() to identify finally.

<img src="https://github.com/yangtiming/Panasonic-internship/blob/master/imgs/IMG_5753.JPG" width="600px">

#### Health Code Identification: dynamic identification && name identification
Firstly, use formula(1)(2) to locate the loaction of name and time.

Secondly, use Mean hash algorithm to make sure  time is dynamic. 

Finally, use Three histogram algorithm to make sure Passenger name is Passenger information entried before. 
<img src="https://github.com/yangtiming/Panasonic-internship/blob/master/imgs/IMG_5754.JPG" width="600px">
<img src="https://github.com/yangtiming/Panasonic-internship/blob/master/imgs/IMG_5755.JPG" width="600px">



