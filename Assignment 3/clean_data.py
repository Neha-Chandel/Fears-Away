import pandas as pd
import numpy as np


crime_dataset_path = (r'C:\Users\chand\OneDrive\Documents\csv_2017_2021.csv')  
crime_data = pd.read_csv(crime_dataset_path, encoding="utf8")

crime = crime_data.copy()
crime.head()
crime.info()

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
# Drop unnecessary columns that are not important
colsToDrop = ["Unnamed: 0", 'SHOOTING','UCR_PART','Lat', 'Long', 'Location']
crime.drop(colsToDrop, axis=1, inplace=True)
crime.dropna(axis=0, how="any", subset='OFFENSE_CODE_GROUP',inplace=True)
print (crime)

crime.to_csv(r'C:\Users\chand\OneDrive\Documents\csv_2017_2021_cleaned.csv', index=False)

