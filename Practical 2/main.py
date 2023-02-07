from Iris import *
import os
import matplotlib.pyplot as plt
import numpy as np

# Getting file name
current_dir = os.path.abspath(os.path.dirname(__file__))
csv_file_path = current_dir + "/dirty_iris.csv"

# Reading File
csv_file = open(csv_file_path,'r')
# Creating File
new_csv_file = open(current_dir + "/iris_clean.csv","w")
record = csv_file.readline()
new_csv_file.write(record)
record = csv_file.readline()

RECORDSSIZE = 0
GOODRECORDS = 0
CONSTRAINTSVIOLATED = [0,0,0,0,0]
SepalLengths = []
labels = ["Species Rule Voilation", "Positive Value Rule Voilation", "Petal Length Rule Voilation", "Sepal Length Rule Voilation", "Length Rule Voilation"]


while record:
    SepalLength, SepalWidth, PetalLength, PetalWidth, Species = record.split(",")
    Species = Species[1:-2]
    flower = Iris(SepalLength, SepalWidth, PetalLength, PetalWidth, Species)
    RECORDSSIZE += 1
    record = csv_file.readline()
    if flower.isComplete():
        GOODRECORDS += 1
        SepalLengths.append(flower.sepalLength)
        result = flower.checkConstraints()
        for i in range(len(result)):
            CONSTRAINTSVIOLATED[i] += result[i]
    else:
        flower.cleanData()
    new_csv_file.write(str(flower))

csv_file.close()
new_csv_file.close()

try:
    PercentageOfGoodRecords = GOODRECORDS/RECORDSSIZE * 100
    print("Total Records: {}\nGood Records: {}\nPercetage of Complete Records: {}%".format(RECORDSSIZE, GOODRECORDS,PercentageOfGoodRecords))
except:
    print ("The file is empty.")

for i in range(5):
    print("{} : {}".format(labels[i], CONSTRAINTSVIOLATED[i]))

# Visualistion
data = np.array(CONSTRAINTSVIOLATED)
plt.bar(labels, CONSTRAINTSVIOLATED)
plt.show()
plt.boxplot(SepalLengths, notch=True)
# plt.pie(data, labels = labels, shadow = True)
plt.show()