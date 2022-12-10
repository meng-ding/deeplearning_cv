the process of learning rate scheduling as:
1. Finding a set of reasonably “good” weights early in the training process with a higher learning rate.
2. Tuning these weights later in the process to ﬁnd more optimal weights using a smaller learning rate.

two primary types of learning rate schedulers:
1. Learning rate schedulers that decrease gradually based on the epoch number (like a linear, polynomial, or exponential function).
2. Learning rate schedulers that drop based on speciﬁc epoch (such as a piecewise function).

The Standard Decay Schedule in Keras/Step-based Decay