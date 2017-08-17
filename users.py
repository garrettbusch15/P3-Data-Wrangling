import xml.etree.cElementTree as ET
import pprint

def get_user(element):
    """ Return a set of unique user IDs """
    return


def process_map(filename):
    users = set()
    for _, element in ET.iterparse(filename):
        if 'uid' in element.attrib.keys():
            users.add(element.attrib['uid'])
        
    return users
pprint.pprint(process_map('ToledoArea.osm'))