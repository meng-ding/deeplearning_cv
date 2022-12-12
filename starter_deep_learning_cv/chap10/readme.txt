Neural Network

activation functions: step, sigmoid, taan; ReLU, Leaky ReLU, ELU
suggestions for choosing activation functions: 
starting with a ReLU to obtain a baseline accuracy.

1. perceptron algorithm

1.1 AND、OR、XOR datasets
1.2 Perceptron Architecture
1.3 Perceptron Training Procedure and the Delta Rule
1.4 Perceptron Training Termination

Tips:
1. For keras_mnist, # dataset = datasets.fetch_mldata("MNIST Original") # does not work since As of version 0.20, 
sklearn deprecates fetch_mldata function and adds fetch_openml instead.

replace by # dataset = fetch_openml('mnist_784') #

2. "plt.plot(np.arange(0, 100), H.history["acc"], label="train_acc")" does not work.
print(H.history[-1]) find that label'name is "accuracy" instead of "acc".

NN: dataset, loss, model, optimization

Weight Initialization, constant initialization, Uniform and Normal Distributions, LeCun Uniform and Normal, 
Glorot/Xavier Uniform and Normal (author suggest), He et al./Kaiming/MSRA Uniform and Norma (suggest for ReLu), 

