# Read data from CSV file

# csv_path = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/LXjSAttmoxJfEG6il1Bqfw/Product-sales.csv'
# df = pd.read_csv(csv_path)

from pyodide.http import pyfetch
import pandas as pd

filename = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/LXjSAttmoxJfEG6il1Bqfw/Product-sales.csv"

async def download(url, filename):
    response = await pyfetch(url)
    if response.status == 200:
        with open(filename, "wb") as f:
            f.write(await response.bytes())


await download(filename, "Product-sales.csv")
df = pd.read_csv("Product-sales.csv")

# Print first five rows of the dataframe
df.head()

#-----------------------------------------------------------------------

# Read data from Excel File and print the first five rows
xlsx_path = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/n9LOuKI9SlUa1b5zkaCMeg/Product-sales.xlsx'

await download(xlsx_path, "Product-sales.xlsx")
df = pd.read_excel("Product-sales.xlsx")
df.head()


# Get the column as a series
x = df['Product']
x
type(x)

# Get the column as a dataframe
x = df[['Quantity']]
x
type(x)

# Access to multiple columns
y = df[['Product','Category', 'Quantity']]
y

# Access the value on the second row and the third column
df.iloc[1,2]

# Access the column using the name
df.loc[1, 'Product']

# Slicing the dataframe
df.iloc[0:2, 0:3]

# Slicing the dataframe using name
df.loc[0:2, 'OrderID':'Category']

# Get non-adjacent columns: 
q=df[['Product', 'Quantity']]
q

# Use the following list to convert the dataframe index df 
# to characters and assign it to df_new; find the element 
# corresponding to the row index a and column 'CustomerCity'. 
# Then select the rows a through d for the column 'CustomerCity'
df_new=df
df_new.index=new_index
df_new.loc['a', 'CustomerCity']
df_new.loc['a':'d', 'CustomerCity']
