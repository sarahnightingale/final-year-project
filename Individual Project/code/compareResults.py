#set filename to the standalone output file
standaloneFilename = 'MediumNaiveBayesOutput.txt'

#read in the file, removing any symbols
with open(standaloneFilename) as f:
        standalone =  f.readlines()
        standalone = ([i.strip('(), \n') for i in standalone])
        standalone = ([i.replace(',', '') for i in standalone])

#remove the last item in the list, in this case the accuracy print out
standalone.pop()

#split the list into two, one containing the predictions, and one containing the actual categories
std1 = ([i.split(' ')[0] for i in standalone])
std2 = ([i.split(' ')[1] for i in standalone])

#set the filename to the spark output file
sparkFilename = './Prediction/part-00000'

#read in the file, removing any symbols
with open(sparkFilename) as f:
        spark =  f.readlines()
        spark = ([i.strip('(), \n') for i in spark])
        spark = ([i.replace(',', '') for i in spark])

#split the list into two, one containing the predictions, and one containing the actual categories
spk1 = ([i.split(' ')[0] for i in spark])
spk2 = ([i.split(' ')[1] for i in spark])

#calculate the length of the list
length = len(spk1)

x = 0
same_prediction = 0

#for each item in the spark list, compare the prediction and actual category. If they match add one to the variable containing the number of same predictions
while x < length:
        if ((spk1[x] == std1[x]) & (spk2[x]  == std2[x])):
                match = True
                print match
                same_prediction = same_prediction + 1
                x = x + 1
        else:
                match = False
                print match
                x = x + 1

	#write out if each prediction was the same or not to a file
        text_file = open("PredictionComparison.txt", "a")
        text_file.write("Same Prediction is %s \n" % (match))
        text_file.close()

#calculate the percentage of same predictions made
accuracy = float(same_prediction) / length

#write out percentage of same predictions to a text file
text_file = open("PredictionComparison.txt", "a")
text_file.write("Prediction Similarity is %s \n" % (accuracy))
text_file.close()
