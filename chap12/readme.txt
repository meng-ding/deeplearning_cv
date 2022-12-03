ImportError: cannot import name 'img_to_array' from 'keras.preprocessing.image'

check tf version: python -c 'import tensorflow as tf; print(tf.__version__)'
2.11.0
use: from tensorflow.keras.utils import img_to_array

The `lr` argument is deprecated, use `learning_rate` instead.

Bus error (core dumped)???