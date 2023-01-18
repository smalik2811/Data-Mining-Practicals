import os
import matplotlib.pyplot as plt
import numpy as np
from People import *

# Getting file name
current_dir = os.path.abspath(os.path.dirname(__file__))
text_file_path = current_dir + "/people.txt"

# Reading File
text_file = open(text_file_path,'r')
record = text_file.readline()
record = text_file.readline()

people_summary= {True: 0, False: 0}
labels = ["Ruleset Passed", "Ruleset Failed"]

while record != "":
    if record[-1] == "\n":
        record = record[0:-1]

    print(record, "~ ", end="")
    data_Object = record.split(" ")

    peopleObject = People(data_Object[0], data_Object[1], data_Object[2], data_Object[3], data_Object[4])
    result = peopleObject.validateE()

    people_summary[result] += 1
    print(result)

    del peopleObject
    record = text_file.readline()

text_file.close()

# Summary
print("-----Summary-----")
print("Number of records Passed Ruleset E: ", people_summary[True])
print("Number of records Failed Ruleset E: ", people_summary[False])

# Visualistion
data = np.array([people_summary[True], people_summary[False]])
plt.pie(data, labels = labels, shadow = True)
plt.show()
