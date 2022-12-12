cnn: local invariance and compositionality; build edges from pixels, shapes from edges, and then complex objects from shapes

image convolutions？
cross-correlation？we don’t have to “ﬂip” the kernel relative to the input when applying cross-correlation

Specified kernal: blurring (average smoothing, Gaussian smoothing, median smoothing, etc.), edge detection (Laplacian, Sobel, Scharr, Prewitt, etc.), and sharpening

A convolution: An input image; A kernel matrix that we are going to apply to the input image; An output image to store the output of the image convolved with the kernel.

CNNS: CONV, ACT/RELU, POOL, FC, BN, DO 
1 kernal 1 depth?

depth, stride, zero-padding

The number of ﬁlters K, The receptive ﬁeld size F, The stride S, The amount of zero-padding P.

INPUT => CONV => RELU => POOL => CONV => RELU => POOL => FC
Type #1: F = 3,S = 2 which is called overlapping pooling
Type #2: F = 2,S = 2 which is called non-overlapping pooling
smaller input images F = 2,S = 1

INPUT => CONV => RELU => BN ...

CONV => RELU => POOL => FC => DO => FC => DO => FC

INPUT => [[CONV => RELU]*N => POOL?]*M => [FC => RELU]*K => FC

shallow CNN with only one CONV layer (N = M = K = 0)
INPUT => CONV => RELU => FC

AlexNet-like [94] CNN architecture
INPUT => [CONV => RELU => POOL] * 2 => [CONV => RELU] * 3 => POOL 
=> [FC => RELU => DO] * 2 => SOFTMAX

VGGNet
INPUT => [CONV => RELU] * 2 => POOL 
=> [CONV => RELU] * 2 => POOL 
=> [CONV => RELU] * 3 => POOL 
=> [CONV => RELU] * 3 => POOL 
=> [FC => RELU => DO] * 2 => SOFTMAX


Rules of Thumb:
1. input layer should be square. 32 × 32, 64 × 64, 96 × 96, 224 × 224, 227 × 227 and 229 × 229

2. the input layer should also be divisible by two multiple times after the ﬁrst CONV operation is applied.

3. your CONV layers should use smaller ﬁlter sizes such as 3 × 3 and 5 × 5. Tiny 1×1 ﬁlters are used to learn local features, but only in your more advanced network architectures.
after this initial CONV layer the ﬁlter size should drop dramatically, otherwise you will reduce the spatial dimensions of your volume too quickly.

4. use a stride of S = 1 for CONV layers, at least for smaller spatial input volumes 

5. personal preference is to apply zero-padding to my CONV layers to ensure the output dimension size matches the input dimension size
6. use POOL layers (rather than CONV layers) reduce the spatial dimensions of your inpu
7. using BN in nearly all situations.
8. place the batch normalization after the activation


qt.qpa.plugin: Could not load the Qt platform plugin "xcb" in "" even though it was found.
for me: udo apt-get install '^libxcb.*-dev' libx11-xcb-dev libglu1-mesa-dev libxrender-dev libxi-dev libxkbcommon-dev libxkbcommon-x11-dev

and 

find libSM.so.6: cannot open shared object file: No such file or directory
do: sudo apt-get install libsm6

fail

pip install pipreqs
pipreqs .
pip install -r requirements.txt

unissued...................................QWQ