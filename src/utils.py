import pandas as pd

def process_team_data (sheet_data):

    str_name = sheet_data[0][0]

    for i in range(1, len(sheet_data)):
        curr_name = sheet_data[i][0]

        if curr_name == "" or curr_name == '':
            sheet_data[i][0] = str_name
        else:
            str_name = curr_name

    return sheet_data


def get_allo_data_json_form_index (sheet_data, index):

    bouf_data = sheet_data[index]

    data = {
        "time" : bouf_data[0],
        "name" : bouf_data[1],
        "building" : bouf_data[2],
        "room_num" : bouf_data[3],
        "allo" : bouf_data[4],
    }

    return data




  
    