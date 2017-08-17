
# Project 3: Wrangle OpenStreetMap Data
--------

By: Garrett Busch

Date: July 31 2017

### Map Location: Toledo, Ohio US

The location I selected was Toledo, Ohio, my birthplace. While being partially influenced from where I grew up, I also saw this as an opportunity to pay homeage to an area that has special significance in parts of American history.

Below are some of the preliminary scripts I compilied as part of the case study.


```python
import os
```


```python
import mapparser
```

    {'member': 20936,
     'meta': 1,
     'nd': 275130,
     'node': 217631,
     'note': 1,
     'osm': 1,
     'relation': 550,
     'tag': 163430,
     'way': 29155}
    


```python
import tags
```

    {'lower': 83727, 'lower_colon': 73543, 'other': 6159, 'problemchars': 1}
    


```python
import audit
```

    defaultdict(<type 'set'>, {'A': set(['Executive Pkwy #A']), 'Pike': set(['Fremont Pike']), 'North': set(['Expressway Drive North']), 'OH)': set(['US 20 (OH)']), '300': set(['N Michigan St #300']), 'Hwy': set(['Airport Hwy']), 'St': set(['Elm St']), 'Rd': set(['N Lallendorf Rd', 'Brown Rd']), 'Summit': set(['North Summit']), 'Way': set(['Discovery Way', 'South Wilkerson Way', 'North Wilkerson Way', 'Michael Owens Way']), 'Ave': set(['Rushland Ave', 'Glendale Ave', 'W Central Ave']), 'ave': set(['Glendale ave']), 'Streetw': set(['West South Boundary Streetw']), 'South': set(['3570 Expressway Drive South']), '3615': set(['3615'])})
    

### Main problem with OpenStreetMap
---------
After downloading the dataset and running it against a my data.py file, below are the problems that I will look to correct and/or build upon further:

* Abbr street names ('St.', 'St', 'ST', 'Ave', 'Ave.', 'Pkwy', 'Ct', 'Sq', etc).

### Abbr street names
In reviewing the data, I will look to cleanse and abbreviate on street types. A few of the common occurances of abbreviation are based around: Street, Avenue, Parkway, Road, Court, Drive, Highway and Square. In the audit.py file I was able to discern which areas may be problematic based on the regex string used. The end result is the conversion of one abbreviated version of a street name to an imporved (Standard) version of the street name. 

An example of such a conversion would be 'N Summit St' -> 'N Summit Street'

## SQL Database

I will now look to incorporate into a local SQL db instance. While running data.py, this script creates various csv files that may be easily incorporated into my sql database. The main reasoning for this being that they are in a tabular format, which differs from the dictionaries that they are stored in at runtime.

### Create SQL Database and Tables


```python
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
```

### Loading the Database


```python
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
```

### File sizes:


```python
#import os
print('The ToledoArea.osm file is {} MB'.format(os.path.getsize('ToledoArea.osm')/1.0e6))
print('The Area.db file is {} MB'.format(os.path.getsize('Area.db')/1.0e6))
print('The nodes.csv file is {} MB'.format(os.path.getsize('nodes.csv')/1.0e6))
print('The nodes_tags.csv file is {} MB'.format(os.path.getsize('nodes.csv')/1.0e6))
print('The ways.csv file is {} MB'.format(os.path.getsize('ways.csv')/1.0e6))
print('The ways_tags.csv is {} MB'.format(os.path.getsize('ways_tags.csv')/1.0e6))
print('The ways_nodes.csv is {} MB'.format(os.path.getsize('ways_nodes.csv')/1.0e6)) # Convert from bytes to MB
```

    The ToledoArea.osm file is 52.963594 MB
    The Area.db file is 36.421632 MB
    The nodes.csv file is 18.420488 MB
    The nodes_tags.csv file is 18.420488 MB
    The ways.csv file is 1.762024 MB
    The ways_tags.csv is 4.956072 MB
    The ways_nodes.csv is 6.457787 MB
    

### # Nodes


```python
cur.execute("SELECT COUNT(*) FROM nodes;")
print(cur.fetchall())
```

    [(217631,)]
    

### # Ways


```python
cur.execute("SELECT COUNT(*) FROM ways;")
print(cur.fetchall())
```

    [(29155,)]
    

### # Unique Users


```python
cur.execute("SELECT COUNT(DISTINCT(e.uid)) FROM (SELECT uid FROM nodes UNION ALL SELECT uid FROM ways) e;")
print(cur.fetchall())
```

    [(310,)]
    

### Top 10 contributing users


```python
import pprint
cur.execute("SELECT e.user, COUNT(*) as num FROM (SELECT user FROM nodes UNION ALL SELECT user FROM ways) e GROUP BY e.user ORDER BY num DESC LIMIT 10;")
pprint.pprint(cur.fetchall())
```

    [('smlyons77', 83314),
     ('woodpeck_fixbot', 35450),
     ('BranchLine', 25433),
     ('Johnny Mapperseed', 15095),
     ('a_white', 13308),
     ('iKJames', 9571),
     ('42429', 6313),
     ('nsommers', 5207),
     ('Walleye2013', 4084),
     ('DougPeterson', 3786)]
    

### Number of Chipotle


```python
cur.execute("SELECT COUNT(*) FROM nodes_tags WHERE value LIKE '%Chipotle%';")
print(cur.fetchall())
```

    [(4,)]
    

## Further Data Exploration

### Top 5 Most Popular Fast Food Chain


```python
cur.execute ("SELECT nodes_tags.value, COUNT(*) as num FROM nodes_tags JOIN (SELECT DISTINCT(id) \
              FROM nodes_tags WHERE value='fast_food') i ON nodes_tags.id=i.id WHERE nodes_tags.key='name' \
              GROUP BY nodes_tags.value ORDER BY num DESC LIMIT 5;")

pprint.pprint(cur.fetchall())
```

    [("McDonald's", 6),
     ('Taco Bell', 4),
     ("Wendy's", 4),
     ("Arby's", 3),
     ('Subway', 3)]
    

### Top Common Church Names


```python
cur.execute ("SELECT nodes_tags.value, COUNT(*) as num FROM nodes_tags JOIN (SELECT DISTINCT(id) \
             FROM nodes_tags WHERE value LIKE '%church%') i ON nodes_tags.id=i.id WHERE nodes_tags.key='name' \
             GROUP BY nodes_tags.value ORDER BY num DESC LIMIT 4;")

pprint.pprint(cur.fetchall())
```

    [('Church of the Living God', 3),
     ('First Congregational Church', 2),
     ('Hope United Methodist Church', 2),
     ('Zion United Methodist Church', 2)]
    

### Thought/Reflection

In review of this analysis I can see that this mapset is far from complete. With regards to the information that was present, I believe much of this was factual. This dataset while being geographicaly on-point suffers from a lack of continuous updating and various conventions of summarizing that information. Partly the main reason why this project has fallen short would be with respect to the Google Maps project. With regards to map completeness, not many projects hold a candle to Google Maps.

### Solution to the underserved dataset
My solution to this would be to use various api's in the Google and Apple maps realm to combat this lack of data. With that, there would be many other sources including: ArcGis, Government Agencies, Shipping Companies, etc.. In essence, my way of attacking this behind the curve would becoming comfartable with those whom make a business out of comprehensive map technologies.

**Benefits**
* Credible-extensive data sources
* Latest and greatest
* Open source means people can make it into what they want

**Issues**
* Terminology-Terminology-Terminology: Everyone has a different way of explaining/storing and therefore capturing
* Futher refining

Within my own personal regard, I highly value a project such as this. I've long held interest in mapping and related technologies, to which, this project highly relies on individuals' contributions. This is a project I would highly consider coming back to for further advancement.


