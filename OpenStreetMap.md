
# Project 3: Wrangle OpenStreetMap Data

--------

By: Garrett Busch
Date: July 31 2017 (start date)
      August 16 2017 (1st submission)

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
import users
```

    set(['1007528',
         '1012362',
         '103253',
         '105255',
         '1052823',
         '105946',
         '10786',
         '1084189',
         '1087647',
         '1100566',
         '1108251',
         '1149057',
         '1160977',
         '118021',
         '1188270',
         '119881',
         '120146',
         '120468',
         '1217437',
         '1218455',
         '1219882',
         '1235102',
         '123633',
         '1240849',
         '1240864',
         '128186',
         '130472',
         '131059',
         '1330847',
         '135163',
         '135329',
         '13832',
         '1448808',
         '145231',
         '1469704',
         '147510',
         '1494110',
         '152289',
         '153669',
         '1554107',
         '160138',
         '1605815',
         '160949',
         '161619',
         '161951',
         '16319',
         '164817',
         '164928',
         '1651798',
         '165855',
         '165869',
         '16591',
         '16669',
         '1679',
         '169004',
         '1694420',
         '1703333',
         '1717101',
         '1718513',
         '1723055',
         '1739369',
         '1751737',
         '1760083',
         '1778799',
         '178186',
         '1783785',
         '178785',
         '1796970',
         '1802220',
         '18069',
         '181135',
         '1823346',
         '1824494',
         '1829683',
         '1832883',
         '1854065',
         '1859152',
         '1884025',
         '1891499',
         '1943799',
         '19492',
         '19697',
         '1975220',
         '1983696',
         '1996396',
         '2012449',
         '2041119',
         '2044483',
         '205523',
         '205715',
         '2063187',
         '207745',
         '207857',
         '2086951',
         '21067',
         '2118267',
         '2118269',
         '212111',
         '2137840',
         '2146750',
         '214969',
         '219968',
         '2209894',
         '2219338',
         '2226712',
         '224440',
         '2318',
         '232126',
         '2332775',
         '2362216',
         '237316',
         '2376',
         '2377377',
         '2378047',
         '2389415',
         '2406578',
         '24126',
         '24247',
         '243003',
         '2441939',
         '2467736',
         '2468986',
         '2471547',
         '2508151',
         '2511706',
         '2512300',
         '25504',
         '2554698',
         '2568511',
         '262151',
         '26299',
         '2644101',
         '2655992',
         '2709057',
         '2748195',
         '2761000',
         '2772299',
         '2772907',
         '280679',
         '28145',
         '2823295',
         '28237',
         '28378',
         '2847988',
         '28559',
         '2856076',
         '2862845',
         '2901303',
         '2902924',
         '2905914',
         '290680',
         '2919575',
         '2925215',
         '2929338',
         '293624',
         '2944689',
         '296768',
         '2974383',
         '297482',
         '2975766',
         '307520',
         '308181',
         '310589',
         '31231',
         '315015',
         '3151684',
         '3208194',
         '3216582',
         '321862',
         '3232636',
         '327131',
         '3273170',
         '3277198',
         '32952',
         '330773',
         '331252',
         '336460',
         '33757',
         '339581',
         '3478684',
         '349027',
         '3490471',
         '3526564',
         '3582',
         '36038',
         '360392',
         '36121',
         '364790',
         '366931',
         '37392',
         '3771923',
         '3822292',
         '38487',
         '3860505',
         '3877019',
         '38784',
         '393740',
         '3938633',
         '3962',
         '398086',
         '401813',
         '4018842',
         '402624',
         '403569',
         '404532',
         '4046988',
         '406589',
         '4115',
         '414318',
         '42429',
         '4328783',
         '4363',
         '43641',
         '436419',
         '437598',
         '440010',
         '44200',
         '44217',
         '44949',
         '451048',
         '451693',
         '4595039',
         '4629254',
         '463545',
         '4667454',
         '4713067',
         '4713657',
         '4729128',
         '4730232',
         '4732',
         '4733791',
         '473471',
         '4737536',
         '4739616',
         '475877',
         '47892',
         '4801391',
         '4847896',
         '4930970',
         '4957930',
         '4971978',
         '498214',
         '5007222',
         '5011036',
         '5012861',
         '5047830',
         '5078634',
         '5078686',
         '51045',
         '510836',
         '5115349',
         '5157485',
         '516',
         '5181599',
         '5184124',
         '5184171',
         '5206281',
         '521692',
         '5224025',
         '52797',
         '5359',
         '5372696',
         '53848',
         '53907',
         '5446055',
         '558778',
         '5611',
         '5633666',
         '5634116',
         '5748',
         '583595',
         '595998',
         '597190',
         '597941',
         '599436',
         '608137',
         '616774',
         '618377',
         '625032',
         '63107',
         '645457',
         '645538',
         '645569',
         '665748',
         '666892',
         '675227',
         '67862',
         '6993',
         '703517',
         '7050',
         '706170',
         '70696',
         '711971',
         '712208',
         '7168',
         '7203',
         '722137',
         '722816',
         '7412',
         '74937',
         '757042',
         '76002',
         '7659',
         '772637',
         '78656',
         '81676',
         '83501',
         '83725',
         '837425',
         '84054',
         '85673',
         '86504',
         '8703',
         '88164',
         '88337',
         '8909',
         '901360',
         '90510',
         '92274',
         '94578',
         '953610',
         '967832',
         '980384'])
    


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

Where OpenStreetMap may look to improve upon their offering is in giving better access to updating by local invividuals. Computer algorithms are certainly a steadfast way to handling a bulk of the information; however, local individuals with knowledge of new/current/non-existant business is much more likely to occur via human manipulation.

Within my own personal regard, I highly value a project such as this. I've long held interest in mapping and related technologies, to which, this project highly relies on individuals' contributions. In light of further advancement I would offer up that this project would also stand to incorporate links to more business, school, office, etc..


