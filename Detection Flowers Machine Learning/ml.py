#Creating a Machine Learning Model to classify the species of flower
#Importing Important libraries
import pandas as pd
import numpy as np
#Exploring the Data
from sklearn.datasets import load_iris
iris_dataset= load_iris()
#printing the keys of iris dataset
print("Keys of iris_dataset:\n{}".format(iris_dataset.keys()))
#Looking at Different keys present in iris dataset
#Printing DESCR key
print(iris_dataset['DESCR'][:193]+"\n")
#Printing Target_Names key
print("Target names:{}".format(iris_dataset['target_names']))
#Printing Features_Name key
print("Features Name:\n{}".format(iris_dataset['feature_names']))
#printing Data key
print("Type of data: {}".format(type(iris_dataset['data'])))
#printing Shape of data
print("shape of data:{}".format(iris_dataset['data'].shape))
#printing 1st five rows of data
print("1st five rows of data:\n{}".format(iris_dataset['data'][:5]))
#printing types of target
print("Types of target:{}".format(type(iris_dataset['target'])))
#printing Shape of Target
print("shape of target:{}".format(iris_dataset['target'].shape))
#printing Target
print("Target:\n{}".format(iris_dataset['target']))
#importing train_test_split function to split the data
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(
    iris_dataset['data'], iris_dataset['target'], random_state=0)
    #printing the shape of splitted train and test data
print("X_train shape:{}".format(X_train.shape))
print("y_train shape:{}".format(y_train.shape))
print("X_test shape:{}".format(X_test.shape))
print("y_test shape:{}".format(y_test.shape))
#Creating the kNearest Machine Learning Model
from sklearn.neighbors import KNeighborsClassifier
knn= KNeighborsClassifier(n_neighbors=3)
#Training the model
knn.fit(X_train,y_train)
#Making predictions
#Printing the shape of array
X_new= np.array([[5,2.9,1,0.2]])
print("X_new.shape:{}".format(X_new.shape))
#Prediction
Prediction = knn.predict(X_new)
print("Prediction:{}".format(Prediction))
print("Predicted target name:{}".format(iris_dataset['target_names'][Prediction]))
#Evaluating the Model
y_pred = knn.predict(X_test)
print("Test set predictions:\n{}".format(y_pred))
#finding the mean value of the prediction to find the accuracy of the model
print("Test set score:{}".format(np.mean(y_pred == y_test)))