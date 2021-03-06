#!/usr/bin/env python

# Copyright 2017 Vertex.AI
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


def scale_dataset(x_train):
    import numpy as np
    # Upscale image size by a factor of 10
    x_train = np.repeat(np.repeat(x_train, 10, axis=1), 10, axis=2)
    # Crop the images to 299 x 299 and normalize
    return (x_train[:, 10:10 + 299, 10:10 + 299]) / 255.


def build_model():
    import keras.applications as kapp
    return kapp.inception_v3.InceptionV3()
