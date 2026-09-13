import pandas as pd

#Define a dictionary 'x'
x = {'Name': ['Rose','John', 'Jane', 'Mary'], 'ID': [1, 2, 3, 4], 'Department': ['Architect Group', 'Software Group', 'Design Team', 'Infrastructure'], 
      'Salary':[100000, 80000, 50000, 60000]}

#casting the dictionary to a DataFrame
df = pd.DataFrame(x)

#display the result df
df

#Retrieving the "ID" column and assigning it to a variable x
x = df[['ID']]
x

#check the type of x
type(x)

#Retrieving the Department, Salary and ID columns and assigning it to a variable z
z = df[['Department','Salary','ID']]
z

# Get the Student column as a series Object
y = df['Department']
y
type(y)

# Access the value on the first row and the third column
df.iloc[0,2]

# Access the column using the name
df.loc[0, 'Department']

# change index column: 
df2=df
df2=df2.set_index("Name")

#Display the first 5 rows of new dataframe
df2.head()

#Now, let us access the column using the name
df2.loc['Mary']

# iloc example to get the Salary of Mary in the newly created dataframe df2
df2.iloc[0:2]

# Slicing: iloc slicing does NOT include the stop bound BUT loc slicing does: 

# let us do the slicing using old dataframe df
df.iloc[0:2, 0:3]

#let us do the slicing using loc() function on old dataframe df where index column is having labels as 0,1,2
df.loc[0:2,'ID':'Department']

#let us do the slicing using loc() function on new dataframe df2 where index column is Name having labels: Rose, John and Jane
df2.loc['Rose':'Jane', 'ID':'Department']

# Using loc() function, do slicing on old dataframe df to retrieve the Name, ID and department of index column having labels as 2,3
df.loc[2:3, 'Name':'Department']


