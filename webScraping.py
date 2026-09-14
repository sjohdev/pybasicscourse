#----------------------------------------------------------------------------------
# Web Scraping Guide/Examples:
#----------------------------------------------------------------------------------
from bs4 import BeautifulSoup # this module helps in web scrapping.
import requests  # this module helps us to download a web page


#----------------------------------------------------------------------------------
# EXAMPLE 1: Downloading And Scraping The Contents Of A Web Page
url = "https://www.ibm.com"
r = requests.get(url, timeout=30)
r.raise_for_status()
data = r.text
soup = BeautifulSoup(data,"html.parser")  # create a soup object using the variable 'data'
links = soup.find_all('a', href=True)  # in html anchor/link is represented by the tag <a>
print("Total links found:", len(links))
for link in links[:20]:  # print the first 20 links
    print(link.get('href'))

# Scrape all images Tags
images = soup.find_all('img')  # in html image is represented by the tag <img>
print("Total images found:", len(images))
for img in images[:10]:  # print the first 10 images
    print(img.get('src'))

#----------------------------------------------------------------------------------
# EXAMPLE 2: Scrape data from HTML tables
#The below url contains an html table with data about colors and color codes.
url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DA0321EN-SkillsNetwork/labs/datasets/HTMLColorCodes.html"
# get the contents of the webpage in text format and store in a variable called data
r = requests.get(url, timeout=30)
r.raise_for_status()
data = r.text
soup = BeautifulSoup(data,"html.parser")
#find a html table in the web page
table = soup.find('table') # in html table is represented by the tag <table>

#Get all rows from the table
for row in table.find_all('tr'): # in html table row is represented by the tag <tr>
    # Get all columns in each row.
    cols = row.find_all('td') # in html a column is represented by the tag <td>
    if len(cols) < 4:
        continue # skip header or incomplete rows
    color_name = cols[2].get_text(strip=True) # store the value in column 3 as color_name
    color_code = cols[3].get_text(strip=True) # store the value in column 4 as color_code
    print("{}--->{}".format(color_name, color_code))
#----------------------------------------------------------------------------------





# DETAILED INSTRUCTIONS: 

html="<!DOCTYPE html><html><head><title>Page Title</title></head><body><h3><b id='boldest'>Lebron James</b></h3><p> Salary: $ 92,000,000 </p><h3> Stephen Curry</h3><p> Salary: $85,000, 000 </p><h3> Kevin Durant </h3><p> Salary: $73,200, 000</p></body></html>"

# Parse html string with BSoup:
soup = BeautifulSoup(html, 'html.parser')

# First, the document is converted to Unicode (similar to ASCII) and
# HTML entities are converted to Unicode characters.
# Beautiful Soup transforms a complex HTML document into a
# complex tree of Python objects.

# We can use the method prettify() to display the HTML in the nested structure:
print(soup.prettify())

# The Tag object corresponds to an HTML tag in the original document,
# for example, the tag title.
tag_object=soup.title
print("tag object:",tag_object)

# If there is more than one Tag with the same name, the first element with that
# Tag name is called.
tag_object=soup.h3
tag_object

# the Tag object is a tree of objects. We can access the child of the tag
# or navigate down the branch as follows:
tag_child =tag_object.b
tag_child

# You can access the parent with the  parent
parent_tag=tag_child.parent
parent_tag

# this is identical to:
tag_object

# tag_object parent is the body element.
tag_object.parent

# tag_object sibling is the paragraph element
sibling_1=tag_object.next_sibling
sibling_1

# sibling_2 is the header element, which is also a
# sibling of both sibling_1 and tag_object
sibling_2=sibling_1.next_sibling
sibling_2

# Use the object sibling_2 and the method next_sibling to
# find the salary of Stephen Curry:
salary_tag=sibling_2.next_sibling
salary_tag

# If the tag has attributes, the tag id="boldest" has an attribute id
# whose value is boldest. You can access a tag’s attributes by treating
# the tag like a dictionary:
tag_child['id']

# You can access that dictionary directly as attrs:
tag_child.attrs

# We can also obtain the content of the attribute of the tag
# using the Python get() method:
tag_child.get('id')

# A string corresponds to a bit of text or content within a tag.
# Beautiful Soup uses the NavigableString class to contain this text.
# In our HTML we can obtain the name of the first player by
# extracting the string of the Tag object tag_child as follows:
tag_string=tag_child.string
tag_string

type(tag_string)
# A NavigableString is similar to a Python string or Unicode string.
# To be more precise, the main difference is that it also supports
# some BeautifulSoup features. We can convert it to string object:
unicode_string = str(tag_string)
unicode_string
type(unicode_string)

#----------------------------------------------------------------------------------

# Filters allow you to find complex patterns, the simplest filter is a string.
# In this section we will pass a string to a different filter method and
# Beautiful Soup will perform a match against that exact string.
table="<table><tr><td id='flight'>Flight No</td><td>Launch site</td> <td>Payload mass</td></tr><tr> <td>1</td><td><a href='https://en.wikipedia.org/wiki/Florida'>Florida<a></td><td>300 kg</td></tr><tr><td>2</td><td><a href='https://en.wikipedia.org/wiki/Texas'>Texas</a></td><td>94 kg</td></tr><tr><td>3</td><td><a href='https://en.wikipedia.org/wiki/Florida'>Florida<a> </td><td>80 kg</td></tr></table>"
table_bs = BeautifulSoup(table, 'html.parser')

# The find_all() method looks through a tag’s descendants and retrieves
# all descendants that match your filters. The Method signature is
# find_all(name, attrs, recursive, string, limit, **kwargs)

# When we set the name parameter to a tag name, the method will extract
# all the tags with that name and its children.
table_rows=table_bs.find_all('tr')
table_rows

# The result is a Python Iterable just like a list, each element is a tag object:
first_row =table_rows[0]
first_row
print(type(first_row))

# we can obtain the child:
first_row.td

# If we iterate through the list, each element corresponds to a row in the table:
for i,row in enumerate(table_rows):
    print("row",i,"is",row)

# As row is a cell object, we can apply the method find_all to it and extract
# table cells in the object cells using the tag td, this is all the children with
# the name td. The result is a list, each element corresponds to a cell
# and is a Tag object, we can iterate through this list as well.
# We can extract the content using the string attribute.
for i,row in enumerate(table_rows):
    print("row",i)
    cells=row.find_all('td')
    for j,cell in enumerate(cells):
        print('colunm',j,"cell",cell)

# If we use a list we can match against any item in that list:
list_input=table_bs .find_all(name=["tr", "td"])
list_input

# If the argument is not recognized it will be turned into a filter
# on the tag’s attributes. For example with the id argument,
# Beautiful Soup will filter against each tag’s id attribute.
# For example, the first td elements have a value of id of flight,
# therefore we can filter based on that id value.
table_bs.find_all(id="flight")

# We can find all the elements that have links to the Florida Wikipedia page:
list_input=table_bs.find_all(href="https://en.wikipedia.org/wiki/Florida")
list_input

# If we set the href attribute to True, regardless of what the value is,
# the code finds all tags with href value:
table_bs.find_all(href=True)

# Find all the <a> tags without href value :
table_bs.find_all(lambda tag: tag.name == "a" and not tag.has_attr("href"))

# Find all the elements that do not contain any links
table_bs.find_all(lambda tag: tag.name != "a" and not tag.find('a'))

# Using the soup object soup, find the element with the
# id attribute content set to "boldest"
soup.find_all(id="boldest")

# With string you can search for strings instead of tags,
# where we find all the elments with Florida:
table_bs.find_all(string="Florida")

# The find_all() method scans the entire document looking for results.
# If you are looking for one element, you can use the find() method
# to find the first element in the document. Consider the following two tables:
two_tables="<h3>Rocket Launch </h3><p><table class='rocket'><tr><td>Flight No</td><td>Launch site</td> <td>Payload mass</td></tr><tr><td>1</td><td>Florida</td><td>300 kg</td></tr><tr><td>2</td><td>Texas</td><td>94 kg</td></tr><tr><td>3</td><td>Florida </td><td>80 kg</td></tr></table></p><p><h3>Pizza Party  </h3><table class='pizza'><tr><td>Pizza Place</td><td>Orders</td> <td>Slices </td></tr><tr><td>Domino's Pizza</td><td>10</td><td>100</td></tr><tr><td>Little Caesars</td><td>12</td><td >144 </td></tr><tr><td>Papa John's </td><td>15 </td><td>165</td></tr>"
two_tables_bs= BeautifulSoup(two_tables, 'html.parser')
two_tables_bs.find("table")

# We can filter on the class attribute to find the second table,
# but because class is a keyword in Python, we add an underscore
# to differentiate them.
two_tables_bs.find("table",class_='pizza')















