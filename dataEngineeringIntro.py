# Introduction to Handling data files with different formats
import pandas as pd
from pyodide.http import pyfetch
import numpy as np
import json
import xml.etree.ElementTree as ET
from PIL import Image
import matplotlib.pyplot as plt
import seaborn as sns

# Ex 0. Pandas Read \n Save functions:
# CSV
# pd.read_csv()
# df.to_csv()

# JSON
# pd.read_json()
# df.to_json()

# Excel
# pd.read_excel()
# df.to_excel()

# HDF
# pd.read_hdf()
# df.to_hdf()

# SQL
# pd.read_sql()
# df.to_sql()
#------------------------------------------------------------------------------

# Ex 1. Download .csv file and read into Python as a Pandas DataFrame:
filename = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%205/data/addresses.csv"
async def download(url, filename):
    response = await pyfetch(url)
    if response.status == 200:
        with open(filename, "wb") as f:
            f.write(await response.bytes())

await download(filename, "addresses.csv")
df = pd.read_csv("addresses.csv", header=None)
# re-label columns from indices to text:
df.columns =['First Name', 'Last Name', 'Location ', 'City', 'State', 'Area Code']
df
#------------------------------------------------------------------------------

# Ex 2. Transform pandas DataFrame using custom function:
#creating a dataframe
df=pd.DataFrame(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), columns=['a', 'b', 'c'])
df
#applying the transform function (out = in +10)
df = df.transform(func = lambda x : x + 10)
df
#applying another transform (out = sqrt(in))
result = df.transform(func = ['sqrt'])
result
#------------------------------------------------------------------------------

# Ex 3. Writing JSON to a file:
person = {
    'first_name' : 'Mark',
    'last_name' : 'abc',
    'age' : 27,
    'address': {
        "streetAddress": "21 2nd Street",
        "city": "New York",
        "state": "NY",
        "postalCode": "10021-3100"
    }
}
with open('person.json', 'w') as f:  # writing JSON object
    json.dump(person, f)

# Serializing json  
json_object = json.dumps(person, indent = 4) 
# Writing to sample.json 
with open("sample.json", "w") as outfile: 
    outfile.write(json_object)
print(json_object)
#------------------------------------------------------------------------------

# Ex 4. Reading JSON from a file:
# Opening JSON file 
with open('sample.json', 'r') as openfile: 
    # Reading from json file 
    json_object = json.load(openfile) 
print(json_object) 
print(type(json_object))
#------------------------------------------------------------------------------

# Ex 5. Read Excel file (XLSX):
filename = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%205/data/file_example_XLSX_10.xlsx"
async def download(url, filename):
    response = await pyfetch(url)
    if response.status == 200:
        with open(filename, "wb") as f:
            f.write(await response.bytes())

await download(filename, "file_example_XLSX_10.xlsx")
df = pd.read_excel("file_example_XLSX_10.xlsx")
df
#------------------------------------------------------------------------------

# Ex 6. Create new XML file using Pythons built-in xml.etree.ElementTree (ET):
# create the file structure
employee = ET.Element('employee')
details = ET.SubElement(employee, 'details')
first = ET.SubElement(details, 'firstname')
second = ET.SubElement(details, 'lastname')
third = ET.SubElement(details, 'age')
first.text = 'Shiv'
second.text = 'Mishra'
third.text = '23'

# create a new XML file with the results
mydata1 = ET.ElementTree(employee)
# myfile = open("items2.xml", "wb")
# myfile.write(mydata)
with open("new_sample.xml", "wb") as files:
    mydata1.write(files)
#------------------------------------------------------------------------------

# Ex 7. Read XML file with xml.etree.ElementTree (ET):
filename = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%205/data/Sample-employee-XML-file.xml"
async def download(url, filename):
    response = await pyfetch(url)
    if response.status == 200:
        with open(filename, "wb") as f:
            f.write(await response.bytes())

await download(filename, "Sample-employee-XML-file.xml")

# Parse the XML file
tree = etree.parse("Sample-employee-XML-file.xml")
# Get the root of the XML tree
root = tree.getroot()
# Define the columns for the DataFrame
columns = ["firstname", "lastname", "title", "division", "building", "room"]
# Collect one row (a list of values) per employee
rows = []
for node in root:
    rows.append([node.find(col).text for col in columns])
# Create the DataFrame once from the collected rows
dataframe = pd.DataFrame(rows, columns=columns)
dataframe
#------------------------------------------------------------------------------

# Ex 8. Read XML file with Pandas:
df=pd.read_xml("Sample-employee-XML-file.xml", xpath="/employees/details")
#------------------------------------------------------------------------------

# Ex 9. Load and display image in python
filename = "https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/dog-puppy-on-garden-royalty-free-image-1586966191.jpg"
async def download(url, filename):
    response = await pyfetch(url)
    if response.status == 200:
        with open(filename, "wb") as f:
            f.write(await response.bytes())

await download(filename, "./dog.jpg")
# Read image 
img = Image.open('./dog.jpg','r') 
# Output Images 
img.show()
#------------------------------------------------------------------------------

# Ex 10. Perform basic data analysis on real-world dataset:
filename = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%205/data/diabetes.csv"
async def download(url, filename):
    response = await pyfetch(url)
    if response.status == 200:
        with open(filename, "wb") as f:
            f.write(await response.bytes())

await download(filename, "diabetes.csv")
df = pd.read_csv("diabetes.csv")
# show the first 5 rows using dataframe.head() method
print("The first 5 rows of the dataframe") 
df.head(5)
df.shape
df.info()
df.dtypes
# Pandas describe() is used to view some basic statistical details
# like percentile, mean, standard deviation, etc. of a data frame or
# a series of numeric values. When this method is applied to a series of
# strings, it returns a different output
df.describe()
# find null-values (missing data)
missing_data = df.isnull()
missing_data.head(5)
# count missing values
for column in missing_data.columns.values.tolist():
    print(column)
    print (missing_data[column].value_counts())
    print("")
#------------------------------------------------------------------------------

# Ex 11. Visualize dataset using a pie-chart: 
labels= 'Not Diabetic','Diabetic'
plt.pie(df['Outcome'].value_counts(),labels=labels,autopct='%0.02f%%')
plt.legend()
plt.show()
