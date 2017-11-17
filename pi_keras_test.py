#!/usr/bin/env python

#https://elitedatascience.com/keras-tutorial-deep-learning-in-python#step-3

import keras
print(keras.__version__)

import numpy as np
import time


np.random.seed(123)

from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Dropout
from keras.layers import Activation
from keras.layers import Flatten
from keras.layers import Convolution2D
from keras.layers import MaxPooling2D
from keras.utils import np_utils


from keras.datasets import mnist

# Load pre-shuffled MNIST data into train and test sets
(X_train, y_train), (X_test, y_test) = mnist.load_data()

print(type(X_train))
print(X_train.shape)


# from matplotlib import pyplot as plt
# plt.imshow(X_train[0])
#
# time.sleep(10)

#even though the images are grey scale we still need a dimention for the image depth
X_train = X_train.reshape(X_train.shape[0],1,28,28)
X_test = X_test.reshape(X_test.shape[0],1,28,28)


print("X data after reshaping %s" % str(X_train.shape))


X_train = X_train.astype('float32')
X_test = X_test.astype('float32')
X_train /= 255
X_test /= 255

print(y_train.shape)

# Convert 1-dimensional class arrays to 10-dimensional class matrices
Y_train = np_utils.to_categorical(y_train, 10)
Y_test = np_utils.to_categorical(y_test, 10)


print("Y data after reshaping to categorical %s" % str(Y_train.shape))


# Its Model time

model = Sequential()

model.add(Convolution2D(32, (3, 3) , activation='relu', input_shape=(1,28,28), dim_ordering="th"))

print(model.output_shape)
# (None, 32, 26, 26)


model.add(Convolution2D(32, (3, 3), activation='relu'))

#https://elitedatascience.com/keras-tutorial-deep-learning-in-python#step-7
