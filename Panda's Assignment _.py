#!/usr/bin/env python
# coding: utf-8

# In[2]:


#Import from CSV
import pandas as pd
import sqlite3 as sql
import csv
df = pd.read_csv(r"C:\Users\User\Downloads\Teacher_Data.csv")
print(df)


# In[79]:


#show columns
df.columns


# In[3]:


#remove column
df.drop( 'County (centroid)', inplace=True, axis=1)
df


# In[7]:


df.columns


# In[8]:


df.tail()


# In[9]:


df.head()


# In[10]:


df.describe()


# In[11]:


df.columns.tolist()


# In[12]:


import sqlite3
#connecting to sqlite3 and creating database
conn = sqlite3.connect('School.db')
#creating cursor object
mycursor = conn.cursor()
# Creating teacher_Data table
mycursor.execute(''' CREATE TABLE IF NOT EXISTS Teacher_Data 
            (COUNTY TEXT NOT NULL,
             School_Type TEXT NOT NULL,
             Employment_Body TEXT NOT NULL,
             No_of_Teachers INT NOT NULL,
             Year DATETIME NOT NULL);''')
conn.commit()
print("School Database Created")


# In[113]:


df.to_sql('Teacher_Data', conn, if_exists='replace', index = False)


# In[22]:


import webbrowser
conn = sqlite3.connect('School.db')
mycursor = conn.cursor()

Mwalimu = []
tbl='<tr><td>County</td><td>School_type</td><td>Employment_Body</td><td>Number_of_Teachers</td><td>Year</td></tr>'
Mwalimu.append(tbl)
mycursor.execute("SELECT * FROM Teacher_Data") 
for row in mycursor.fetchall():
    a = "<tr><td>%s</td>"%row[0]
    Mwalimu.append(a)
    b = "<td>%s</td>"%row[1]
    Mwalimu.append(b)
    c = "<td>%s</td>"%row[2]
    Mwalimu.append(c)
    d = "<td>%s</td>"%row[3]
    Mwalimu.append(d)
    e = "<td>%s</td></tr>"%row[4]
    Mwalimu.append(e)
   
html = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta cSharset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>EDUCATION DATA</title>
</head>
<body>
<h1>SECONDARY SCHOOLS DATA IN KENYA</h1>
<table border = "1" style="background-color:#CED8F6">
<thead><caption><h2> SECONDARY SCHOOLS DATA IN KENYA </h2></caption></thead>
%s
</table>
</body>
</html>
'''%(Mwalimu)
fname='School.html'
def main (html,fname): 
    output = open(fname,"w")
    output.write(html)
    output.close()
main(html,fname)
webbrowser.open(fname)
conn.commit()
conn.close()
    
    


# In[26]:


html = df.to_html()
  
# write html to file
text_file = open("index.html", "w")
text_file.write(html)
text_file.close()
webbrowser.open_new_tab('index.html')

