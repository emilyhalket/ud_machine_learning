import numpy
import pickle

data_dict = pickle.load( open("../final_project/final_project_dataset.pkl", "r") )
### there's an outlier--remove it!
data_dict.pop("TOTAL", 0)


max_stock = 0
min_stock = 100000
for value in data_dict.values():
    if value['exercised_stock_options'] != 'NaN':
        if value['exercised_stock_options'] > max_stock:
            max_stock = value['exercised_stock_options']
        if value['exercised_stock_options'] < min_stock:
            min_stock = value['exercised_stock_options']


max_salary = 0
min_salary = 100000
for value in data_dict.values():
    if value['salary'] != 'NaN':
        if value['salary'] > max_salary:
            max_salary = value['salary']
        if value['salary'] < min_salary:
            min_salary = value['salary']


data = [115, 140, 175]
scaled = []
for i in data:
    scaled.append((i-min(data))/float(max(data)-min(data)))
print scaled


# tests of your feature scaler--line below is input data

print featureScaling(data)