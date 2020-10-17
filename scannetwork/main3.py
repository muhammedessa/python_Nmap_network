import nmap
from pymongo import MongoClient
import json


def database_updates(packet):
    client = MongoClient('localhost', 27017)
    db = client['networkdata']
    collect = db['networkstatus']
    app_json = json.dumps(packet)
    collect.insert_one({"packet": app_json})


def scan_network():
    nm = nmap.PortScanner()
    scan_range = nm.scan(hosts="192.168.0.104")
    # data = scan_range['scan']
    # for key in data:  #print keys
    #     print(key)

    # for key in data:
    #     print(key, '->', data[key])

    # for item in data.items():   #<class 'tuple'>
    #     print(item)

    #print(data.keys())   #dict_keys

    # for key in data.keys():
    #     print(key, '->', data[key])

    #print(data.values())  # dict_keys

    # for value in data.values():
    #     print(value['addresses'])
    #     print('status: ', value['status']['state'])
    #     print(value['tcp'])

  #  database_updates(data)


scan_network()
