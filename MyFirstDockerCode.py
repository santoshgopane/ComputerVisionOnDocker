import os
import warnings

warnings.simplefilter("ignore", category=FutureWarning)

os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"

import cv2
import numpy as np
from numpy import expand_dims
from PIL import Image
from sklearn.preprocessing import Normalizer

# import tensorflow as tf
from tensorflow import keras
import pickle
import sys

import subprocess

print("Hey there from Santosh :) - 11")
print(os.path.exists("facenet_keras1.h5"))
print(os.path.exists("facenet_keras.h5"))
print(os.path.exists("NNmodelv2.h5"))
print(os.path.exists("NNmodelv21.h5"))
print(os.path.exists("FaceDetectionModelV4.model"))
print(os.path.exists("FaceDetectionModelV41.model"))

LoadedModel = pickle.load(open("FaceDetectionModelV4.model", "rb"))
print("SUCCESS!")
FaceTracker = keras.models.load_model("NNmodelv2.h5")

print("SUCCESS!")

KerasModel = keras.models.load_model("facenet_keras.h5")
print("SUCCESS!")
