#!/usr/bin/python

"""
    Skeleton code for k-means clustering mini-project.
"""




import pickle
import numpy
import matplotlib.pyplot as plt
import sys
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit

data_dict = pickle.load( open("../final_project/final_project_dataset.pkl", "r") )
### there's an outlier--remove it!
data_dict.pop("TOTAL", 0)


### the input features we want to use
### can be any key in the person-level dictionary (salary, director_fees, etc.)
feature_1 = "salary"
feature_2 = "exercised_stock_options"
poi  = "poi"
features_list = [poi, feature_1, feature_2]
data = featureFormat(data_dict, features_list )
poi, finance_features = targetFeatureSplit( data )


from sklearn.preprocessing import MinMaxScaler
salary_scaler = MinMaxScaler()
stock_scaler = MinMaxScaler()

salaries= []
stocks = []
for f1, f2 in finance_features:
    salaries.append(float(f1))
    stocks.append(float(f2))

rescaled_salary = salary_scaler.fit_transform(salaries)
rescaled_stock = stock_scaler.fit_transform(stocks)

print 'salary transform', salary_scaler.transform([200000.])
print 'stock transform', stock_scaler.transform([1000000.])
