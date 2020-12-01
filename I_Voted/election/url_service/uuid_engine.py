import re
import uuid
import json


def new_id(email):
    _uuid_string = str(uuid.uuid4())
    with open("uuid_list.json", 'r') as uuid_json:
        uuid_data = json.load(uuid_json)
        for val in uuid_data.values():
            if val == email:
                print(email+' is already in the uuid_list\n')
                return None
        uuid_data[_uuid_string] = email
    with open("uuid_list.json",'w') as uuid_json:
        json.dump(uuid_data,uuid_json,indent=4)
    return _uuid_string

def search_id(request_id):
    pattern = r'[0-9A-F]{8}-[0-9A-F]{4}-4[0-9A-F]{3}-[89AB][0-9A-F]{3}-[0-9A-F]{12}'
    _list_matches = re.split(pattern,request_id)
    if _list_matches[0] != request_id:
        return False
    
    with open('uuid_list.json') as uuid_json:
        uuid_data = json.load(uuid_json)

    for _id in uuid_data.keys():
        if request_id == _id:
            email = uuid_data[_id]
            uuid_data.pop(_id)
            with open('uuid_list.json','w') as uuid_json:
                json.dump(uuid_data,uuid_json,indent=4)
            print(email)
            return email
    print("None")
    return None