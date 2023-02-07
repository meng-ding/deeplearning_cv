how do we train multiple networks? In general, we have two options:

1. Run the script we use to train a single network multiple times, changing the path to the output serialized model weights to be unique for each run.

2. Create a separate Python script that uses for loop to train N networks and outputs the serialized model at the end of each iteration.