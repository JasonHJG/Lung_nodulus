# Lung_nodulus
Detection of lung nodulus with deep learning

# read.py 
Create the train and validation data. In the project I use, due to limited CPU power, I use only 2400 for training and 1200 for validation. This data set has approximately 3:1 ratio for negative vs positive. Thereofore, the ratio I use for this binary classification is 1:1 in training and 3:1 in validation. 

# lung_nodulus.py
Build the model. The model has two convolutional layers and one maxpooling layer.
