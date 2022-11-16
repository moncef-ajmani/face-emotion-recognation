# Face Emotion Recognition

## Overview

In this project, I have build a convolutional neural network (CNN) model which can classify the emotions of a person from a live video.
The dataset used for this project is the fer2013 dataset.

## Requirements

* numpy
* keras
* open cv

## Dataset

The fer2013 dataset consists of 35,887 grayscale, 48x48 sized images of human faces. The data consists of 5 classes:

*   0=Angry
*   1=Happy
*   2=Neutral
*   3=Sad
*   4=Surprise


There are 28,709 images in the training set and 3,178 images in the public test set. The private test set has 3,351 images.

## Model

I have used the MobileNetV2 model as the base model and have added some fully connected layers on top of it. I have used softmax as the activation function for the output layer.

I have used the Adam optimizer and the sparse categorical cross entropy loss function.

The model achieves an accuracy of 64.68% on the public test set and 65.13% on the private test set.

## Usage

* Run the following command to install the required libraries:

```
pip install -r requirements.txt
```

* Run the app.py file to test the Modal with the following command:

```
python app.py
```
