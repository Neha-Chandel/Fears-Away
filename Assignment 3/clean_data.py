import pandas as pd
import numpy as np


crime_dataset_path = (r'C:\Users\chand\OneDrive\Desktop\Boston Crime Dataset.csv')  
crime_data = pd.read_csv(crime_dataset_path)

crime = crime_data.copy()
crime.head()
crime.info()

cop_dataset_path = (r'C:\Users\chand\OneDrive\Desktop\cops_info.csv')  
cop_data = pd.read_csv(cop_dataset_path, encoding="utf8")

data1 = (r'C:\Users\chand\OneDrive\Desktop\Addresses.csv')  
d_data = pd.read_csv(data1, encoding="utf8")

cops = cop_data.copy()
cops.head()
cops.info()

#Function to fetch missing values from Dataset 1
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
def missing_cols(d_data):
    '''prints out columns with its amount of missing values'''
    total = 0
    for col in d_data.columns:
        missing_vals = d_data[col].isnull().sum()
        total += missing_vals
        if missing_vals != 0:
            print(f"{col} => {d_data[col].isnull().sum()}")
    print ('total missing values found :', total)
    if missing_vals == 0:
        print("All missing values identified")
missing_cols(d_data)
# Drop unnecessary columns that are not important
crime.dropna(axis=0, how="any", subset='OFFENSE_CODE_GROUP',inplace=True)
crime1 = crime.copy()
drop_cols = ['OFFENSE_CODE' ,'DAY_OF_WEEK','REPORTING_AREA','OCCURRED_ON_DATE','SHOOTING','UCR_PART','Lat', 'Long', 'Location']
crime.drop(drop_cols, axis=1, inplace=True)
drope_cols = ['INCIDENT_NUMBER','OFFENSE_DESCRIPTION','DISTRICT' ,'REPORTING_AREA','OCCURRED_ON_DATE','SHOOTING','YEAR','MONTH','DAY_OF_WEEK','HOUR','UCR_PART','Lat', 'Long','Location']
crime.drop_duplicates(subset='INCIDENT_NUMBER', inplace=True)
crime1.drop(drope_cols, axis=1, inplace=True)
d_data.drop_duplicates(subset='street', inplace=True)
d_data.dropna(axis=0, how="any", subset='Nbhd',inplace=True)

# Drop unnecessary columns that are not important
#crime.dropna(axis=0, how="any", subset='OFFENSE_CODE_GROUP',inplace=True)
#crime1 = crime.copy()
dropc_cols = ['url',  'org_url' ,'doa','total','regular','retro','other','overtime', 'state','injured', 'detail','quinn','details_count', 'articles_officers_count', 'articles_officers_to_review_count', 'ia_score', 'field_contacts_count', 'incidents_count', 'swats_count', 'citations_count']
cops.drop(dropc_cols, axis=1, inplace=True)
cops.dropna(axis=0, how="any",inplace=True)


cops.head(50000).to_csv(r'C:\Users\chand\OneDrive\Desktop\cops_information.csv', index=False)
crime.to_csv(r'C:\Users\chand\OneDrive\Desktop\incidents.csv', index=False)
crime1.to_csv(r'C:\Users\chand\OneDrive\Desktop\incident_type.csv', index=False)
d_data.to_csv(r'C:\Users\chand\OneDrive\Desktop\locations.csv', index=False)

print (cops)
