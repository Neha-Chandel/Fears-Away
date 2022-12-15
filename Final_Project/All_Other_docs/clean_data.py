
import pandas as pd
import numpy as np

#Reading crime dataset

crime_dataset_path = (r'C:\Users\chand\OneDrive\Desktop\Boston Crime Dataset.csv')  
crime_data = pd.read_csv(crime_dataset_path)

#Copying the file into a new dataframe
crime = crime_data.copy()

#Displaying header and info
crime.head()
crime.info()

#Reading cops database
cop_dataset_path = (r'C:\Users\chand\OneDrive\Desktop\cops_info.csv')  
cop_data = pd.read_csv(cop_dataset_path, encoding="utf8")
cops = cop_data.copy()
cops.head()
cops.info()

#Reading addresses dataset
address_dataset_path = (r'C:\Users\chand\OneDrive\Desktop\Addresses.csv')  
address_data = pd.read_csv(address_dataset_path, encoding="utf8")
address = address_data.copy()
address.head()
address.info()

#Function to fetch missing values from crime dataset
def missing_cols(crime):
    '''prints out columns with its amount of missing values'''
    total = 0
    for col in crime.columns:
        missing_vals = crime[col].isnull().sum()
        total += missing_vals
        if missing_vals != 0:
            print(f"{col} => {crime[col].isnull().sum()}")
    print ('total missing values found :', total)
    if missing_vals == 0:
        print("All missing values identified")
missing_cols(crime)
print (crime)

#Function to fetch missing values from cops dataset
def missing_cops_cols(cops):
    '''prints out columns with its amount of missing values'''
    total = 0
    for col in cops.columns:
        missing_cops_vals = cops[col].isnull().sum()
        total += missing_cops_vals
        if missing_cops_vals != 0:
            print(f"{col} => {cops[col].isnull().sum()}")
    print ('total missing values found :', total)
    return cops.replace('"', '')
    if missing_cops_vals == 0:
        print("All missing values identified")
missing_cops_cols(cops)

#Function to fetch missing values from address dataset
def missing_cols(address):
    '''prints out columns with its amount of missing values'''
    total = 0
    for col in address.columns:
        missing_vals = address[col].isnull().sum()
        total += missing_vals
        if missing_vals != 0:
            print(f"{col} => {address[col].isnull().sum()}")
    print ('total missing values found :', total)
    if missing_vals == 0:
        print("All missing values identified")
missing_cols(address)

# Drop unnecessary columns that are not important from crime dataset
crime.dropna(axis=0, how="any", subset='OFFENSE_CODE_GROUP',inplace=True)
crime.drop_duplicates(subset='INCIDENT_NUMBER', inplace=True)
crime1 = crime.copy()
drop_cols = ['OFFENSE_CODE' ,'DAY_OF_WEEK','REPORTING_AREA','INCIDENT_DATE','SHOOTING','UCR_PART','Lat', 'Long', 'Location']
crime.drop(drop_cols, axis=1, inplace=True)

# Drop unnecessary columns that are not important from crime dataset making ready for incidents type
dropping_cols = ['OFFENSE_DESCRIPTION','DISTRICT' ,'REPORTING_AREA','INCIDENT_DATE','SHOOTING','YEAR','MONTH','DAY_OF_WEEK','HOUR','UCR_PART','Lat', 'Long','Location','ZIP']
crime1.drop(dropping_cols, axis=1, inplace=True)

#Cleaning address file

address.drop_duplicates(subset='ZIP5', inplace=True)
address.dropna(axis=0, how="any", subset='Nbhd',inplace=True)
address.dropna(axis=0, how="any", subset='ZIP5',inplace=True)

# Drop unnecessary columns that are not important from cops dataset

dropc_cols = ['url',  'org_url' ,'doa','total','regular','retro','other','overtime', 'state','injured', 'detail','quinn','details_count', 'articles_officers_count', 'articles_officers_to_review_count', 'ia_score', 'field_contacts_count', 'incidents_count', 'swats_count', 'citations_count']
cops.drop(dropc_cols, axis=1, inplace=True)
cops.dropna(axis=0, how="any", inplace=True)

print(crime)
print(crime1)
print (cops)
print(address)

cops.head(50000).to_csv(r'C:\Users\chand\OneDrive\Desktop\cops_information.csv', index=False)
crime.to_csv(r'C:\Users\chand\OneDrive\Desktop\incidents.csv', index=False)
crime1.to_csv(r'C:\Users\chand\OneDrive\Desktop\incident_type.csv', index=False)
address.to_csv(r'C:\Users\chand\OneDrive\Desktop\locations.csv', index=False)

