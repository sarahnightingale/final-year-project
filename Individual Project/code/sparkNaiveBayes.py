from pyspark.mllib.classification import NaiveBayes, NaiveBayesModel
from pyspark.mllib.linalg import Vectors
from pyspark.mllib.regression import LabeledPoint
from pyspark import SparkContext, SparkConf
import os, tempfile

#sets SparkContext to be used as sc
sc =SparkContext()

#passes in the text file, identifies features and labels from the dataset and returns an RDD with a labeled point
def parseLine(line):
    parts = line.split(',')
    features = Vectors.dense([float(x) for x in parts[0:2]])
    label = float(parts[3])
    return LabeledPoint(label, features)

#takes the input text files and maps them using the parseLine function
training = sc.textFile('training.txt').map(parseLine)
test = sc.textFile('testing.txt').map(parseLine)

# Train a naive Bayes model.
model = NaiveBayes.train(training, 1.0)

# Make predictions using the test data
predictionAndLabel = test.map(lambda p : (model.predict(p.features), p.label))

#Calculates the accuracy of the predictions made
accuracy = 1.0 * predictionAndLabel.filter(lambda (x, v): x == v).count() / test.count()

#print the accuracy of the predictions
print('model accuracy {}'.format(accuracy))

#combine the output into one text file and write results to it
predictionAndLabel.coalesce(1).saveAsTextFile("./Prediction")
