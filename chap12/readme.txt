ImportError: cannot import name 'img_to_array' from 'keras.preprocessing.image'

check tf version: python -c 'import tensorflow as tf; print(tf.__version__)'
2.11.0
use: from tensorflow.keras.utils import img_to_array

The `lr` argument is deprecated, use `learning_rate` instead.

Bus error (core dumped)???


----------------------------------
lsb_release -a : Ubuntu 19.10
lspci | grep VGA : 19:00.0 VGA compatible controller: NVIDIA Corporation TU102 [GeForce RTX 2080 Ti] (rev a1)
nvcc --version/sudo apt --fix-broken install/sudo apt install nvidia-cuda-toolkit/ :Cuda compilation tools, release 7.5, V7.5.17

----------------------------------------------------
cuda install https://docs.nvidia.com/cuda/cuda-installation-guide-linux/index.html
uname -m : x86_64
uname -r : 5.3.0-19-generic

-----------------------------------------
unable to install libpng12.so.0': no such file or directory on ubuntu 19.10
https://askubuntu.com/questions/1194386/how-to-correctly-install-libpng12-0-on-the-ubuntu-19-10
------------------------------------------

https://stackoverflow.com/questions/53422407/different-cuda-versions-shown-by-nvcc-and-nvidia-smi
cuda version
-----------------------------------------------