#Importing the required libraries
import json

#Opening the json file in read mode
with open('2nd assignment\ex5.json', 'r') as file:
    ex5 = json.load(file)

#Showing the data in the json file and adding a new batter named "Coffee" for the donut with name "Old Fashioned"
for i in ex5:
    if i['name'] == 'Old Fashioned':
        x=i['batters']['batter']
        
        print("\nThe data in the json file ('Batter') is:")
        print(x)
        
        print("\nAppending Coffee to the batter list:")
        x.append({'id': '1005', 'type': 'Coffee'})
        print(x)
        print("\n")
        break
    
#Writing the updated data back to the file
with open('2nd assignment\ex5.json', 'w') as file:
    json.dump(ex5, file)        




#Question :
"""
For this assignment, let’s use example 5. Store the example 5 json in a file ex5.json.
Read the json using python, store in a dictionary named ex5
Write a code to add a batter named Coffee for “donut” with name “Old Fashoined”.
Replace the ex5.json with the new data.

DataSampleSet: https://opensource.adobe.com/Spry/samples/data_region/JSONDataSetSample.html

"""