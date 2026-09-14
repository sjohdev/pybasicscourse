import requests
import os 
from PIL import Image
from IPython.display import IFrame



#-----------------------------------------------------------------------------------------
# Receive Text from the web: 

url='https://www.ibm.com/'
r=requests.get(url)

# Request code 2xx (200, 201,.., 299) means Success:
r.status_code

# View request headers:
print(r.request.headers)

# Print request body
print("request body:", r.request.body)

# View Response headers:
header=r.headers
print(r.headers)

# obtain the date the request was sent using the key Date
header['Date']

# Content-Type indicates the type of data:
header['Content-Type']

# You can also check the encoding:
r.encoding

# Since  the Content-Type is text/html we can use the attribute text to
# display the HTML in the body. We can review the first 100 characters:
r.text[0:100]

#---------------------------------------------------------------------------------------

# Receive Images from the web:
# Use single quotation marks for defining string
url='https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/IDSNlogo.png'
r=requests.get(url)
print(r.headers)
r.headers['Content-Type']

# An image is a response object that contains the image as a bytes-like object.
# As a result, we must save it using a file object. First, we specify the file path and name
path=os.path.join(os.getcwd(),'image.png')

# We save the file, in order to access the body of the response we use the attribute
# content then save it using the open function and write method
with open(path,'wb') as f: # 'with' automatically closes the file when exiting the clause
    f.write(r.content)

# View the image:
Image.open(path)
#---------------------------------------------------------------------------------------

# How to download the txt file in the given link.
url='https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%205/data/Example1.txt'
path=os.path.join(os.getcwd(),'Example1.txt')
r=requests.get(url)
with open(path,'wb') as f:
    f.write(r.content)
#---------------------------------------------------------------------------------------

# You can use the GET method to modify the results of your query, for example
# retrieving data from an API. We send a GET request to the server. Like before
# we have the Base URL, in the Route we append /get, this indicates we would like to preform
# a GET request:

url_get='https://httpbin.org/get'
#A query string is a part of a uniform resource locator (URL),
# this sends other information to the web server.
# To create a Query string, add a dictionary.
# The keys are the parameter names and the values are
# the value of the Query string:
payload={"name":"Joseph","ID":"123"}
# Then passing the dictionary payload to the params parameter of the  get() function:
r=requests.get(url_get,params=payload)

# We can print out the URL and see the name and values.
r.url

# There is no request body.
print("request body:", r.request.body)

# We can print out the status code.
print(r.status_code)

# We can view the response as text
print(r.text)

r.headers['Content-Type']

# Since the content 'Content-Type' is in the JSON format
# we can use the method json(), it returns a Python dict:
r.json()

# The key args has the name and values:
r.json()['args']
#---------------------------------------------------------------------------------------

# POST requests:
# Like a GET request, a POST is used to send data to a server, but the POST request
# sends the data in a request body. In order to send the Post Request in Python,
# in the URL we change the route to POST:
url_post='https://httpbin.org/post'

# This endpoint will expect data as a file or as a form. A form is convenient way to
# configure an HTTP request to send data to a server.
# To make a POST request we use the post() function, the variable payload is passed to
# the parameter  data:
r_post=requests.post(url_post,data=payload)

# POST request has no name or value pairs: 
print("POST request URL:", r_post.url)
print("GET request URL:", r.url)

# only the POST request has a body:
print("POST request body:",r_post.request.body)
print("GET request body:",r.request.body)

# We can view the form as well:
r_post.json()['form']






