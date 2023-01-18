import os
from People import *

# Getting file name
current_dir = os.path.abspath(os.path.dirname(__file__))
text_file_path = current_dir + "/people.txt"

# Reading File
text_file = open(text_file_path,'r')
data_set = text_file.readlines()
data_set = data_set[1:]

for record in data_set:
    if record[-1] == "\n":
        record = record[0:-1]
    print(record, "~ ", end="")
    data_Object = record.split(" ")
    peopleObject = People(data_Object[0], data_Object[1], data_Object[2], data_Object[3], data_Object[4])
    result = peopleObject.validateE()
    print(result)
    del peopleObject
