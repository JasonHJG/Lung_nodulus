# Lung_nodulus
Detection of lung nodulus with keras

### read.py 
Create the train and validation data. I take 3 slices from each patch. Each slice is the middle slice in the stack of images. I use 2400 slices for training and 1200 for validation due to limited CPU power. I notice that this data set has approximately 3:1 ratio for negative vs positive. Thereofore, the ratio I use for this binary classification is 1:1 in training and 3:1 in validation. 

### lung_nodulus.py
Build the model. The model has two convolutional layers and one pooling layer. I use data amplification for my model (each image can produce 8 more images). To test the performance, I use 50 epochs and achieved an average accuracy about 90%.

### model.h5
The model I trained.

### history.csv
Training history, including training and validation accuracy for each epoch
