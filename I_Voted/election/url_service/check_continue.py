import time
import json

filename_uuidlist = 'uuid_continue_list.json'

def add_to_continue_list(request_uuid, email):
    time_stamp = time.time()
    with open(filename_uuidlist, 'r') as uuid_list:
        uuid_data = json.load(uuid_list)

    uuid_data[request_uuid] = [email,time_stamp]
    with open(filename_uuidlist,'w') as uuid_list:
        json.dump(uuid_data,uuid_list,indent=4)

def get_uuid_from_list(request_uuid):
    with open(filename_uuidlist,'r') as uuid_list:
        uuid_data = json.load(uuid_list)
    try:
        value_list = uuid_data[request_uuid]
    except KeyError:
        return None
    
    email = value_list[0]
    time_stamp_start = value_list[1]
    time_stamp_end = time.time()
    uuid_data.pop(request_uuid)
    with open(filename_uuidlist,'w') as uuid_list:
        json.dump(uuid_data,uuid_list,indent=4)
    print(time_stamp_end-time_stamp_start, time_stamp_end-time_stamp_start <= 3600)
    return [email, time_stamp_end-time_stamp_start > 3600]
