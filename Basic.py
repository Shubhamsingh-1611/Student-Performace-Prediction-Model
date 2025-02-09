import tensorflow
import keras
import pandas as pd
import numpy as np
import sklearn
from sklearn import linear_model
from sklearn.utils import shuffle

data = pd.read_csv("student-mat.csv" ,sep=";")
# print(data.head())
data= data[["G1","G2","G3","studytime","failures","absences"]]
# print(data.head())
predict = "G3"
x = np.array(data.drop([predict],1))
y = np.array(data[predict])

x_tarin,x_test,y_tarin,y_test = sklearn.model_selection.train_test_split(x,y, test_size=0.1)

linear = linear_model.LinearRegression()

linear.fit(x_tarin,y_tarin)
acc = linear.score(x_test,y_test)
print(acc)
predictions = linear.predict(x_test)

for x in range(len(predictions)):
    print(predictions[x],x_test[x],y_test[x])