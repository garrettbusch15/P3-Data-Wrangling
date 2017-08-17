
# coding: utf-8

# # Project 3: Wrangle OpenStreetMap Data
# 
# --------

# By: Garrett Busch
# Date: July 31 2017 (start date)
#       August 16 2017 (1st submission)

# ### Map Location: Toledo, Ohio US
# 
# The location I selected was Toledo, Ohio, my birthplace. While being partially influenced from where I grew up, I also saw this as an opportunity to pay homeage to an area that has special significance in parts of American history.

# Below are some of the preliminary scripts I compilied as part of the case study.

# In[1]:


import os


# In[2]:


import mapparser


# In[3]:


import tags


# In[4]:


import users


# In[5]:


import audit


# ### Main problem with OpenStreetMap
# ---------
# After downloading the dataset and running it against a my data.py file, below are the problems that I will look to correct and/or build upon further:
# 
# * Abbr street names ('St.', 'St', 'ST', 'Ave', 'Ave.', 'Pkwy', 'Ct', 'Sq', etc).

# ### Abbr street names
# In reviewing the data, I will look to cleanse and abbreviate on street types. A few of the common occurances of abbreviation are based around: Street, Avenue, Parkway, Road, Court, Drive, Highway and Square. In the audit.py file I was able to discern which areas may be problematic based on the regex string used. The end result is the conversion of one abbreviated version of a street name to an imporved (Standard) version of the street name. 
# 
# An example of such a conversion would be 'N Summit St' -> 'N Summit Street'

# ## SQL Database
# 
# I will now look to incorporate into a local SQL db instance. While running data.py, this script creates various csv files that may be easily incorporated into my sql database. The main reasoning for this being that they are in a tabular format, which differs from the dictionaries that they are stored in at runtime.

# ### Create SQL Database and Tables

# In[6]:


import sqlite3
import csv
from pprint import pprint

sqlite_file = "Area.db"
conn = sqlite3.connect(sqlite_file)
conn.text_factory = str
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS nodes')
cur.execute('DROP TABLE IF EXISTS ways')
cur.execute('DROP TABLE IF EXISTS nodes_tags')
conn.commit()

cur.execute('''
    Create Table nodes(id INTEGER, 
                       lat REAL, 
                       lon REAL, 
                       user TEXT, 
                       uid INTEGER, 
                       version TEXT, 
                       changeset INTEGER, 
                       timestamp TEXT)
''')
cur.execute('''
    Create Table ways(id INTEGER, 
                      user TEXT, 
                      uid INTEGER, 
                      version TEXT, 
                      changeset INTEGER, 
                      timestamp TEXT)
''')
cur.execute('''
    Create Table nodes_tags(id INTEGER, 
                            key TEXT, 
                            value TEXT, 
                            type TEXT)
''')

conn.commit()


# ### Loading the Database

# In[7]:


with open('nodes.csv','r') as bk:
    reader = csv.DictReader(bk)
    to_db = [(i['id'], i['lat'], i['lon'], i['user'], i['uid'], i['version'], i['changeset'], i['timestamp']) for i in reader]
    cur.executemany("INSERT INTO nodes(id, lat, lon, user, uid, version, changeset, timestamp) VALUES (?,?,?,?,?,?,?,?);", to_db)

with open('ways.csv','r') as bk:
    reader = csv.DictReader(bk)
    to_db = [(i['id'], i['user'], i['uid'], i['version'], i['changeset'], i['timestamp']) for i in reader]
    cur.executemany("INSERT INTO ways(id, user, uid, version, changeset, timestamp) VALUES (?,?,?,?,?,?);", to_db)
    
with open('nodes_tags.csv','r') as bk:
    reader = csv.DictReader(bk)
    to_db = [(i['id'], i['key'], i['value'], i['type']) for i in reader]
    cur.executemany("INSERT INTO nodes_tags(id, key, value, type) VALUES (?,?,?,?);", to_db)
    
conn.commit()


# ### File sizes:

# In[8]:


#import os
print('The ToledoArea.osm file is {} MB'.format(os.path.getsize('ToledoArea.osm')/1.0e6))
print('The Area.db file is {} MB'.format(os.path.getsize('Area.db')/1.0e6))
print('The nodes.csv file is {} MB'.format(os.path.getsize('nodes.csv')/1.0e6))
print('The nodes_tags.csv file is {} MB'.format(os.path.getsize('nodes.csv')/1.0e6))
print('The ways.csv file is {} MB'.format(os.path.getsize('ways.csv')/1.0e6))
print('The ways_tags.csv is {} MB'.format(os.path.getsize('ways_tags.csv')/1.0e6))
print('The ways_nodes.csv is {} MB'.format(os.path.getsize('ways_nodes.csv')/1.0e6)) # Convert from bytes to MB


# ### # Nodes

# In[9]:


cur.execute("SELECT COUNT(*) FROM nodes;")
print(cur.fetchall())


# ### # Ways

# In[10]:


cur.execute("SELECT COUNT(*) FROM ways;")
print(cur.fetchall())


# ### # Unique Users

# In[11]:


cur.execute("SELECT COUNT(DISTINCT(e.uid)) FROM (SELECT uid FROM nodes UNION ALL SELECT uid FROM ways) e;")
print(cur.fetchall())


# ### Top 10 contributing users

# In[12]:


import pprint
cur.execute("SELECT e.user, COUNT(*) as num FROM (SELECT user FROM nodes UNION ALL SELECT user FROM ways) e GROUP BY e.user ORDER BY num DESC LIMIT 10;")
pprint.pprint(cur.fetchall())


# ### Number of Chipotle

# In[13]:


cur.execute("SELECT COUNT(*) FROM nodes_tags WHERE value LIKE '%Chipotle%';")
print(cur.fetchall())


# ## Further Data Exploration

# ### Top 5 Most Popular Fast Food Chain

# In[14]:


cur.execute ("SELECT nodes_tags.value, COUNT(*) as num FROM nodes_tags JOIN (SELECT DISTINCT(id)               FROM nodes_tags WHERE value='fast_food') i ON nodes_tags.id=i.id WHERE nodes_tags.key='name'               GROUP BY nodes_tags.value ORDER BY num DESC LIMIT 5;")

pprint.pprint(cur.fetchall())


# ### Top Common Church Names

# In[15]:


cur.execute ("SELECT nodes_tags.value, COUNT(*) as num FROM nodes_tags JOIN (SELECT DISTINCT(id)              FROM nodes_tags WHERE value LIKE '%church%') i ON nodes_tags.id=i.id WHERE nodes_tags.key='name'              GROUP BY nodes_tags.value ORDER BY num DESC LIMIT 4;")

pprint.pprint(cur.fetchall())


# ### Thought/Reflection
# 
# In review of this analysis I can see that this mapset is far from complete. With regards to the information that was present, I believe much of this was factual. This dataset while being geographicaly on-point suffers from a lack of continuous updating and various conventions of summarizing that information. Partly the main reason why this project has fallen short would be with respect to the Google Maps project. With regards to map completeness, not many projects hold a candle to Google Maps.
# 
# Where OpenStreetMap may look to improve upon their offering is in giving better access to updating by local invividuals. Computer algorithms are certainly a steadfast way to handling a bulk of the information; however, local individuals with knowledge of new/current/non-existant business is much more likely to occur via human manipulation.
# 
# Within my own personal regard, I highly value a project such as this. I've long held interest in mapping and related technologies, to which, this project highly relies on individuals' contributions. In light of further advancement I would offer up that this project would also stand to incorporate links to more business, school, office, etc..

# 
