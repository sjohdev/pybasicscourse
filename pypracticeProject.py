# An international firm that is looking to expand its business in
# different countries across the world has recruited you. You have been hired as
# a junior Data Engineer and are tasked with creating a script
# that can extract the list of the top 10 largest economies of the world in
# descending order of their GDPs in Billion USD (rounded to 2 decimal places)
# , as logged by the International Monetary Fund (IMF).
import numpy as np
import pandas as pd

# We may use pandas.read_html() function in python to
# extract all the tables in the web page directly:
url='https://web.archive.org/web/20230902185326/https://en.wikipedia.org/wiki/List_of_countries_by_GDP_%28nominal%29'
tables = pd.read_html(url)

# We know that the table we want is table #3 on the webpage: 
df = tables[3] # the required table will have index 2

# Replace the column headers with column numbers
df.columns = range(df.shape[1])

# Retain columns with index 0 and 2 (name of country and value of GDP quoted by IMF)
df = df[[0, 2]]

# Retain the Rows with index 1 to 10, indicating the top 10 economies of the world.
df = df.iloc[1:11, :]

# Assign column names as "Country" and "GDP (Million USD)"
df.columns = ['Country', 'GDP (Million USD)']
#print(df)

# Modify the GDP column of the DataFrame, converting the value available
# in Million USD to Billion USD. Use the round() method of Numpy library to
# round the value to 2 decimal places. Modify the header of the DataFrame to
# GDP (Billion USD).

# Change the data type of the 'GDP (Million USD)' column to integer. Use astype() method.
df['GDP (Million USD)'] = df['GDP (Million USD)'].astype(int)

# Convert the GDP value in Million USD to Billion USD
df[['GDP (Million USD)']] = df[['GDP (Million USD)']]/1000

# Use numpy.round() method to round the value to 2 decimal places.
df[['GDP (Million USD)']] = np.round(df[['GDP (Million USD)']], 2)

# Rename the column header from 'GDP (Million USD)' to 'GDP (Billion USD)'
df.columns = ['Country', 'GDP (Billion USD)']
print(df)

# Load the DataFrame to the CSV file named "Largest_economies.csv"
df.to_csv('./Largest_economies.csv')


