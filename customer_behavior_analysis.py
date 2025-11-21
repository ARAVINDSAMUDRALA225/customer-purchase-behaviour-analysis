# # Importing required libraries
# import pandas as pd
# a=pd.read_csv("C:\\Users\\Aravind\\OneDrive\\Desktop\\Customer_Shopping_Behavior.csv")
# df=pd.DataFrame(a)
# print(df.head())
# df.info()
# print(df.describe(include="all"))
# print(df.isnull().sum())
# df["Review Rating"]=df.groupby('Category')['Review Rating'].transform (lambda x: x.fillna(x.median()))
# print(df.isnull().sum())
# df.columns=df.columns.str.lower()
# df.columns=df.columns.str.replace(' ','_')
# print(df.columns)
# df=df.rename(columns={'purchase_amount_(usd)':'purchase_amount'})
# print(df.columns)

# #create a column age_group
# labels=["Young Adult",'Adult','Middle-aged','Senior']
# df['age_group']=pd.qcut(df['age'],q=4,labels=labels) 
# print(df[['age','age_group']].head(20)) 

# #create column purchase_frequency_days
# frequency_mapping={
#     'Fortnightly': 14,
#     'Weekly': 7,
#     'Monthly': 30,
#     'Quarterly':90,
#     'Bi-Weekly':14,
#     'Annually': 365,
#     'Every 3 Months':90
# }

# df['purchase_frequency_days']=df['frequency_of_purchases'].map(frequency_mapping)
# print(df[['purchase_frequency_days','frequency_of_purchases']].head(10))
# # print(df[['discount_applied','promo_code_used']].head(10))

# # print((df['discount_applied'] == df['promo_code_used']).all())

# print(df[['discount_applied','promo_code_used']].head(10))
# print((df['discount_applied'] == df['promo_code_used']).all())
# df = df.drop('promo_code_used', axis=1)
# print(df.columns)

# from sqlalchemy import create_engine
# import urllib.parse

# username = "root"
# password = urllib.parse.quote("Believeit@0824")   # URL encoded
# host = "localhost"
# port = "3306"
# database = "customer_behaviour"

# connection_str = f"mysql+pymysql://{username}:{password}@{host}:{port}/{database}"
# engine = create_engine(connection_str)

# table_name = "customer"
# df.to_sql(table_name, engine, if_exists="replace", index=False)

# print("Data uploaded successfully!")
# print(pd.read_sql("SELECT * FROM customer LIMIT 5;", engine))

# Importing required libraries
import pandas as pd

# Reading the dataset
a = pd.read_csv("C:\\Users\\Aravind\\OneDrive\\Desktop\\Customer_Shopping_Behavior.csv")
df = pd.DataFrame(a)

# Display first 5 rows of the dataset
print(df.head())

# Display dataset information (columns, data types, null counts)
df.info()

# Statistical summary of all columns
print(df.describe(include="all"))

# Checking missing values
print(df.isnull().sum())

# Filling missing Review Rating values with median rating per category
df["Review Rating"] = df.groupby('Category')['Review Rating'].transform(lambda x: x.fillna(x.median()))
print(df.isnull().sum())

# Converting column names to lowercase and replacing spaces with underscores
df.columns = df.columns.str.lower()
df.columns = df.columns.str.replace(' ', '_')
print(df.columns)

# Renaming purchase amount column for simplicity
df = df.rename(columns={'purchase_amount_(usd)': 'purchase_amount'})
print(df.columns)

# Creating age group categories using quartiles
labels = ["Young Adult", 'Adult', 'Middle-aged', 'Senior']
df['age_group'] = pd.qcut(df['age'], q=4, labels=labels)
print(df[['age', 'age_group']].head(20))

# Mapping purchase frequency text to numerical day values
frequency_mapping = {
    'Fortnightly': 14,
    'Weekly': 7,
    'Monthly': 30,
    'Quarterly': 90,
    'Bi-Weekly': 14,
    'Annually': 365,
    'Every 3 Months': 90
}

df['purchase_frequency_days'] = df['frequency_of_purchases'].map(frequency_mapping)
print(df[['purchase_frequency_days', 'frequency_of_purchases']].head(10))

# Checking correlation between discount_applied and promo_code_used
print(df[['discount_applied', 'promo_code_used']].head(10))
print((df['discount_applied'] == df['promo_code_used']).all())

# Dropping promo_code_used since both contain identical values
df = df.drop('promo_code_used', axis=1)
print(df.columns)

# ---------------------------------------------
# Uploading Data to MySQL Database
# ---------------------------------------------

from sqlalchemy import create_engine
import urllib.parse

# Database credentials
username = "root"
password = urllib.parse.quote("Believeit@0824")  # URL encoded
host = "localhost"
port = "3306"
database = "customer_behaviour"

# Creating MySQL connection string
connection_str = f"mysql+pymysql://{username}:{password}@{host}:{port}/{database}"
engine = create_engine(connection_str)

table_name = "customer"

# Uploading dataframe to MySQL table (replacing if table exists)
df.to_sql(table_name, engine, if_exists="replace", index=False)

print("Data uploaded successfully!")

# Fetch first 5 rows from MySQL to verify successful upload
print(pd.read_sql("SELECT * FROM customer LIMIT 5;", engine))
