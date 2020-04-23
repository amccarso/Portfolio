#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 17 20:46:13 2018

@author: austinmccarson
"""

import tensorflow as tf

tensor = tf.constant('Hello World!')
tensor_value = tf.numpy()
print(tensor_value)