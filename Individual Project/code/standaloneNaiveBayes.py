import numpy as np
from numpy import genfromtxt
import csv
from createDataset import testing, training, dataset, filename

#this function cretes the categories list and populates it with all categories found in the dataset
def getCategories(dataset,noOfAttributes):
        i = 0
        categories = []
        while i < len(dataset):
                categories.append(dataset[i, noOfAttributes])
                i = i + 1
        categories_set = set(categories)
        categories = list(categories_set)
	print categories
        return categories

#this function uses the training set to calculate the p_category for each category. This is how many times each category is present in the dataset
def trainData(no_of_test, no_of_category, categories, totalTraining, trainingSet):
        no_of_training = 0
        no_of_attrib = 0
        p_category = 0.0
        num_category = 0
        while no_of_training < totalTraining:
              if categories[no_of_category] == trainingSet[no_of_training][3]:
                      num_category = num_category + 1
                      no_of_training = no_of_training + 1
              else:
                      num_category = num_category + 0
                      no_of_training = no_of_training + 1

        p_category = float(num_category) / float(len(trainingSet))

        no_of_attrib = no_of_attrib + 1
        return p_category, num_category


#this function calculates the probability of each attribute belonging to each category, and then us-es that and the previously calculated p_category to give a prediction value.
def calculateProbability(no_of_test, testSet, no_of_attrib, noOfAttributes, trainingSet, p_category, num_category):

        no_of_training = 0
        count = []
        i = 0
        count.append(i)

        while no_of_training < totalTraining:
                if (np.all(testSet[no_of_test, no_of_attrib] == trainingSet[no_of_training, no_of_attrib]) & np.all(categories[no_of_category] == trainingSet[no_of_training, noOfAttributes])):

                        count[i] = count[i] + 1
                        no_of_training = no_of_training + 1
                else:
                        no_of_training = no_of_training + 1

        p_category *= float(count[i] + 3) / (float(num_category + 3))

	return p_category

#this function calculates the accuracy of the predictions made by the algorithm
def getAccuracy(no_of_test, testSet, classifiction, accurate, k):

        if (testSet[no_of_test,3] == classification):
                accurate[k] = accurate[k] + 1
        else:
                accurate[k] = accurate[k] + 0
        return accurate


#Calculates the number of attributes in the file
with open(filename, 'r') as f:
        reader = csv.reader(f, delimiter=',', skipinitialspace=True)
        firstRow = next(reader)
        noOfColumns = len(firstRow)
        noOfAttributes = noOfColumns - 1

#Split the dataset into 60% training and 40% test data
length = len(dataset)
trainingLength = length * 0.6
testingLength = length * 0.4

trainingSet, testSet = training, testing

#Calculate number of training and test data
totalTraining = len(trainingSet)
totalTest = len(testSet)

#get the categories from the dataset
categories = getCategories(dataset, noOfAttributes)
length_of_categories = len(categories)

no_of_test = 0
no_of_training = 0

i = 0

accurate = []
k = 0
accurate.append(k)

p_category = []

#passes all the data to the functions where the calculations are done
while no_of_test < totalTest:
        result = []
        for no_of_category in categories:
                no_of_attrib = 0 
                p_category, num_category = trainData(no_of_test, no_of_category, categories, totalTraining, trainingSet)

                while no_of_attrib <= noOfAttributes:
                        p_category = (calculateProbability(no_of_test, testSet, no_of_attrib, noOfAttributes, trainingSet, p_category, num_category))
                        no_of_attrib = no_of_attrib + 1

#p_categories from each category are saved into the results list to be used later
                result.append(p_category)
                no_of_category = no_of_category + 1

#the prediction is made by finding the highest p_category value in the results list and its position within the list.
        classificationVal = float(max(result))
        classification = result.index(max(result))

        stringVal = str(classificationVal)
        actualResult = float(testSet[no_of_test,3])
        stringResult = str(actualResult)

        #accuracy is calculated for the prediction 
        accuracy = getAccuracy(no_of_test, testSet, classification, accurate, k)

	floatClass = float(classification)
        stringClass = str(floatClass)

        text_file = open("SmallNaiveBayesOutput.txt", "a")
        text_file.write("(%s, %s) \n" % (stringClass, stringResult))
        text_file.close()

        no_of_test = no_of_test + 1

#total accuracy of the predictions made is calcuated
totalAccuracy = float(accuracy[k]) / totalTest

print 'Accuracy of Predictions', totalAccuracy

text_file = open("SmallNaiveBayesOutput.txt", "a")
text_file.write("Accuracy: %s." % (totalAccuracy))
text_file.close()
