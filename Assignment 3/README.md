## CRIME DATASET FEARS AWAY

### Overview: Gathering, Scraping, Munging, and Cleaning Data

Assemble data on crime from variety of sources: 

#### Crime Dataset obtained from Kagle : https://www.kaggle.com/datasets/AnalyzeBoston/crimes-in-boston
#### Officers Information obtained from Analyze Boston : https://data.boston.gov/dataset/boston-police-department-fio
#### Neighbourhoods in Boston obtained from ArcGIS Hub : https://hub.arcgis.com/datasets/boston::city-of-boston-managed-streets/explore?location=42.312533%2C-71.087353%2C12.51

After gathering the data, we must reformat it to meet the database schema.

The data should be cleansed, and all null values and empty values should be handled.

After Auditing the data you need to use SQL to insert the data into your database.

Program Flow Details 

### Step 1 : The sources from data was collected are mentioned above.

Depending on the data collected 4 csv files are created.

1. incidents.csv 
2. cops_information.csv
3. incident_type.csv
4. location.csv

All the files are uploaded in the folder.

### Step 2 : Cleaning Data

Data has been cleaned by using clean_data.py python script.


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

#Drop unnecessary columns that are not important from crime dataset

crime.dropna(axis=0, how="any", subset='OFFENSE_CODE_GROUP',inplace=True)
crime.drop_duplicates(subset='INCIDENT_NUMBER', inplace=True)
crime1 = crime.copy()
drop_cols = ['OFFENSE_CODE' ,'DAY_OF_WEEK','REPORTING_AREA','INCIDENT_DATE','SHOOTING','UCR_PART','Lat', 'Long', 'Location']
crime.drop(drop_cols, axis=1, inplace=True)

#Drop unnecessary columns that are not important from crime dataset making ready for incidents type

dropping_cols = ['OFFENSE_DESCRIPTION','DISTRICT' ,'REPORTING_AREA','INCIDENT_DATE','SHOOTING','YEAR','MONTH','STREET','DAY_OF_WEEK','HOUR','UCR_PART','Lat', 'Long','Location']
crime1.drop(dropping_cols, axis=1, inplace=True)

#Cleaning address file

address.drop_duplicates(subset='ZIP5', inplace=True)
address.drop('street',  axis=1, inplace=True)
address.dropna(axis=0, how="any", subset='Nbhd',inplace=True)

#Drop unnecessary columns that are not important from cops dataset

dropc_cols = ['url',  'org_url' ,'doa','total','regular','retro','other','overtime', 'state','injured', 'detail','quinn','details_count', 'articles_officers_count', 'articles_officers_to_review_count', 'ia_score', 'field_contacts_count', 'incidents_count', 'swats_count', 'citations_count']
cops.drop(dropc_cols, axis=1, inplace=True)
cops.dropna(axis=0, how="any",inplace=True)

print(crime)
print(crime1)
print (cops)
print(address)

cops.head(50000).to_csv(r'C:\Users\chand\OneDrive\Desktop\cops_information.csv', index=False)
crime.to_csv(r'C:\Users\chand\OneDrive\Desktop\incidents.csv', index=False)
crime1.to_csv(r'C:\Users\chand\OneDrive\Desktop\incident_type.csv', index=False)
address.to_csv(r'C:\Users\chand\OneDrive\Desktop\locations.csv', index=False)



#### The screen prints of all the script working fine can be found in Run_Scripts.pdf

### Step 3 : Audit Validity,Audit Consistency, Audit Completeness

All the parameters have taken care while cleaning the data and after the files are generated it consits all the valid, consistent and complete data.

Did not use BFILL and FFILL because it hampers the quality of data the null values for which no information was found are removed and others are replaced with the matching data

### Step 4 : Inserting data into the table

Used python script to INSERT data into the respective tables. The create queries can be found in Create_Queries.pdf

import mysql.connector
import csv
import pandas as pd

#establishing connection
conn=mysql.connector.connect(host='localhost', username='root', password='admin', database='fear_away', allow_local_infile=True)
my_cursor=conn.cursor()

#Reading incidents file
csv_data1 = (csv.reader(open(r'C:\Users\chand\OneDrive\Desktop\incidents.csv',encoding="utf8")))

#Reading incidents type file
csv_data2 = (csv.reader(open(r'C:\Users\chand\OneDrive\Desktop\incident_type.csv', encoding="utf8")))

#Reading cops information file
csv_data3 = (csv.reader(open(r'C:\Users\chand\OneDrive\Desktop\cops_information.csv', encoding="utf8")))

#Reading locations
csv_data4 = (csv.reader(open(r'C:\Users\chand\OneDrive\Desktop\locations.csv', encoding="utf8")))

#store headers and rows

header = next(csv_data1)
header = next(csv_data2)
header = next(csv_data3)
header = next(csv_data4)

print ("importing the file 1")
#Inserting into incidents
for row in csv_data1:
    print(row)
    my_cursor.execute("INSERT INTO incidents (incident_number, incident_code_group, incident_desc, incident_district, incident_year ,incident_month, incident_hour, location, zip) VALUES(%s, %s, %s, %s, %s, %s, %s,%s, %s)", row)
print ("Loaded in incidents Database")

#Inserting into incident type
for row in csv_data2:
    print(row)
    my_cursor.execute("INSERT INTO incident_type (incident_id, incident_code, incident_type, locality) VALUES(%s, %s, %s,%s)", row)
print ("Loaded in incident_type Database")

#Inserting into cops
for row in csv_data3:
    print(row)
    my_cursor.execute("INSERT INTO cops_info (cop_id, cop_badge, cop_name, cop_title , cop_district, zip_code, neighborhood) VALUES(%s, %s, %s, %s, %s, %s, %s)", row)
print ("Loaded in cops Database")

#Inserting intolocation
for row in csv_data4:
    print(row)
    my_cursor.execute("INSERT INTO location (neighbourhood, zip_code, street) VALUES(%s, %s,%s)", row)
print ("Loaded in location Database")

conn.commit()
conn.close()


### Step 5 : Use Cases and SQL Queries 

#### The pdf is uploaded Usecases_SQL_Queries.pdf along with database screenshot of all the queries running fine.
### https://github.com/Neha-Chandel/Fears-Away/blob/main/Assignment%203/Usecases_SQL_Queries.pdf

#### Use Case 1: View the total number of incidents in Boston
Description: User views the total number of incidents in last 5 years.
Actor: User 
Steps:
Actor action: User views the total number of incidents. 
System Response: Incidents for a Boston location are displayed.
Post Condition: System displays all the incidents reported for Boston location.

Count the total number of incidents occured in boston in last 5 years?

SELECT count(incident_number)
FROM incidents
where incident_year between 2018 and 2022;
 
#### Use Case2: User views top 5 neighborhoods in Boston for highest crime incidents.
Description: User views the top 5 neighborhoods with highest number of incidents.
Actor: User
Precondition:
Steps:
Actor action: User views top 5 locations.
System Response: Incidents for top 5 locations are displayed.
Post Condition: System displays all the incidents reported for user searched criteria.

List the top 5 neighborhoods in Boston with highest crime incidents?

SELECT l.neighborhood, count(i.incident_number) as total_incidents
FROM location l RIGHT JOIN incidents i
ON l.zip_code = i.zip
where i.incident_year = 2022
group by neighborhood 
order by count(i.incident_number) desc
limit 5; 

#### Use Case3: User views the harassment incidents in Boston.
Description: User views the harassment incidents in Boston along with streets.
Actor: User
Precondition:
Steps:
Actor action: User views the harassment incidents per street.
System Response: Harassment incidents are displayed.
Post Condition: System displays all the incidents reported for user searched criteria.

Count the harassment incidents on Boston streets 

SELECT l.neighborhood, t.incident_type, count(i.incident_number) as total_incidents
FROM incidents i LEFT JOIN incident_type t
ON t.incident_id = i.incident_number
LEFT JOIN location l
ON l.zip_code = i.zip
where t.incident_type = 'Harassment'
group by l.neighborhood
order by count(i.incident_number) desc;

#### Use Case4: User views the officers details deployed for a particular location.
Description: User views the officers details for a neighborhood in Boston.
Actor: User
Precondition:
Steps:
Actor action: User views officers details.
System Response: All the officers details along with name and title are displayed.
Post Condition: System displays all the details requested by the user.

Who are the cops in charge for Roxbury?

SELECT  c.cop_name, c.cop_title, l.neighborhood
FROM cops_info c  
left JOIN location l
ON c.zip_code = l.zip_code
where l.neighborhood = 'Roxbury'
order by c.cop_name;
 
#### Use Case5: User views the incidents for a particular street happened in a year.
Description: User views the incidents details with respect to street.
Actor: User
Precondition:
Steps:
Actor action: User views the incidents for Adams St.
System Response: Incidents happened in Adams St are displayed.
Post Condition: System displays all the incidents reported for user searched criteria.

What is the most recurring incident on Adams Street in a one year period.

SELECT count(incident_number), t.incident_type
FROM incidents i LEFT JOIN incident_type t
ON i.location = t.locality
where t.locality = 'ADAMS ST' and incident_year between 2020 and 2021
group by t.incident_type
order by count(i.incident_number) desc
limit 1;


 
#### Use Case6: User views the details of the street along with neighborhood and zipcode which marked the highest number of incidents in last 5 year.
Description: User views the incidents details with respect to time period.
Actor: User
Precondition:
Steps:
Actor action: User views the highest number of incidents for a time frame.
System Response: Which street had highest number of incidents in last 5 years id displayed.
Post Condition: System displays all the incidents reported for user searched criteria.

The above use case determines the highly unsafe street in Boston.

SELECT count(i.incident_number) as incident_count, i.location, l.neighbourhood, l.zip_code
FROM  incidents i RIGHT JOIN location l
ON i.zip = l.zip_code
where incident_year <= 2022 and incident_year >=2018
group by i.location, l.neighbourhood, l.zip_code
order by count(incident_number) desc
limit 1;

 
#### Use Case7: User views the details of the year with highest number of incidents.
Description: User views the incidents details with respect to year.
Actor: User
Precondition:
Steps:
Actor action: User views the highest number of incidents for a particular year.
System Response: Which year marked the highest number of incidents are displayed.
Post Condition: System displays all the incidents reported for user searched criteria.

Which year marks the highest number of incidents?

SELECT count(i.incident_number) as incident_count, i.incident_year
FROM  incidents i RIGHT JOIN location l
ON i.location = l.street
where i.location = l.street
group by i.incident_year
order by count(incident_number) desc
limit 1;

#### Use Case8: User views the details of the time when most incidents happened.
Description: User views the incidents details with respect to hour.
Actor: User
Precondition:
Steps:
Actor action: User views the highest number of incidents between a particular  hour.
System Response: The range of hours marked the highest number of incidents are displayed.
Post Condition: System displays all the incidents reported for user searched criteria.

Between what hours of day most incidents happen?

SELECT count(i.incident_number) as incident_count, i.incident_hour, l.neighbourhood, l.street 
FROM  incidents i RIGHT JOIN location l
ON i.location = l.street
where i.location = l.street
group by i.incident_hour, l.neighbourhood, l.street
order by count(incident_number) desc
limit 1;
 
#### Use Case9: User views the number of incidents happened after midnight.
Description: User views the incidents details happened after midnight.
Actor: User
Precondition:
Steps:
Actor action: User views the highest number of incidents after midnight.
System Response: All the incidents happened after midnight are displayed.
Post Condition: System displays all the incidents reported for user searched criteria.

How many incidents happen after midnight night?

SELECT count(incident_number) from incidents
where incident_hour between 1 and 6
group by incident_hour
order by count(incident_number) desc;

### Step 6 : All the results for the queries from Assignment 2 is uploaded and can be found in Assignment2_queries.pdf

### Step 7 : No review comments to work upon was recieved from Assignment 2.
