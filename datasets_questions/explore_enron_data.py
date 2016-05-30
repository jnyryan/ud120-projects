#!/usr/bin/python

"""
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000

"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

# print all keys in the dict
#for d in enron_data: print d

# print first data point
print enron_data[enron_data.keys()[0]]

print "Number of data points", len(enron_data)

print "Features per data point", len(enron_data[enron_data.keys()[0]])

poi = 0
for d in enron_data.iteritems():
    if d[1]['poi'] == True:
        poi=poi+1
print "Number of Persons of interest in Dataset:", poi

print "Total Stock Value of James Prentice", enron_data["PRENTICE JAMES"]["total_stock_value"]

print "Emails from Wesley Colwell to POI", enron_data["COLWELL WESLEY"]["from_this_person_to_poi"]

print "Stock options of Jeffrey Skilling", enron_data["SKILLING JEFFREY K"]["exercised_stock_options"]

print "Total Paid to Lay, Skilling and Fastow", enron_data["LAY KENNETH L"]["total_payments"], enron_data["SKILLING JEFFREY K"]["total_payments"], enron_data["FASTOW ANDREW S"]["total_payments"]

hasSalary = 0
hasEmail = 0
for d in enron_data.iteritems():
    if d[1]['salary'] != 'NaN':
        hasSalary=hasSalary+1
    if d[1]['email_address'] != 'NaN':
        hasEmail=hasEmail+1
print "Number of people without Quantified Salary", hasSalary
print "Number of people without Email Addrees", hasEmail

hasNoPayments = 0.0
for d in enron_data.iteritems():
    if d[1]['total_payments'] == 'NaN':
        hasNoPayments=hasNoPayments+1.0
print "% of people with NaN as their total in payments", hasNoPayments, round(hasNoPayments/len(enron_data) * 100,2) , "%"

poiHasNoPayments = 0.0
for d in enron_data.iteritems():
    if d[1]['total_payments'] == 'NaN' and d[1]['poi'] == True:
        poiHasNoPayments=poiHasNoPayments+1.0
print "% of POI with NaN as their total in payments", round(poiHasNoPayments/len(enron_data) * 100,2), "%"

# 10 more POIs

enron_data['person 1'] = { 'total_payments': 'NaN', 'poi': True, 'total_stock_value' : 'NaN'}
enron_data['person 2'] = { 'total_payments': 'NaN', 'poi': True, 'total_stock_value' : 'NaN'}
enron_data['person 3'] = { 'total_payments': 'NaN', 'poi': True, 'total_stock_value' : 'NaN'}
enron_data['person 4'] = { 'total_payments': 'NaN', 'poi': True, 'total_stock_value' : 'NaN'}
enron_data['person 5'] = { 'total_payments': 'NaN', 'poi': True, 'total_stock_value' : 'NaN'}
enron_data['person 6'] = { 'total_payments': 'NaN', 'poi': True, 'total_stock_value' : 'NaN'}
enron_data['person 7'] = { 'total_payments': 'NaN', 'poi': True, 'total_stock_value' : 'NaN'}
enron_data['person 8'] = { 'total_payments': 'NaN', 'poi': True, 'total_stock_value' : 'NaN'}
enron_data['person 9'] = { 'total_payments': 'NaN', 'poi': True, 'total_stock_value' : 'NaN'}
enron_data['person 10'] = { 'total_payments': 'NaN', 'poi': True, 'total_stock_value' : 'NaN'}

hasNoPayments = 0.0
newPoi = 0.0
enron_data
for d in enron_data.iteritems():
    if d[1]['poi'] == True:
        newPoi=newPoi+1
    if d[1]['total_payments'] == 'NaN':
        hasNoPayments=hasNoPayments+1.0      
print "Number of new people " + str(len(enron_data)) + " with NaN as their total in payments", hasNoPayments

poiHasNoPayments = 0.0
newPoi = 0.0
enron_data
for d in enron_data.iteritems():
    if d[1]['poi'] == True:
        newPoi=newPoi+1
    if d[1]['total_payments'] == 'NaN' and d[1]['poi'] == True:
        poiHasNoPayments=poiHasNoPayments+1.0      
print "Number of POI " + str(newPoi) + " with NaN as their total in payments", poiHasNoPayments


poiHasNoStock = 0.0
newPoi = 0.0
for d in enron_data.iteritems():
    if d[1]['poi'] == True:
        newPoi=newPoi+1
    if d[1]['total_stock_value'] == 'NaN' and d[1]['poi'] == True:
        poiHasNoStock=poiHasNoStock+1.0
print "% of new POI " + str(newPoi) + " with NaN as their total stock value", round(poiHasNoStock/len(enron_data) * 100,2), "%"

