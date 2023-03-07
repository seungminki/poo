import requests
import re
import sys
import os
import sqlite3
from dotenv import load_dotenv

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
load_dotenv()

CERTIFICATION_KEY = os.environ['TRAIN_KEY']


def get_station_number(STATION_NAME):
    conn = sqlite3.connect('../result.db')
    c = conn.cursor()
    c.execute(f'SELECT * FROM station WHERE stationname = :NAME', {'NAME': STATION_NAME})

    station_number = c.fetchone()[2]
    return int(station_number)

def get_current_location(MSG, SEC, SEARCH_STATION_NUMBER):
    if SEC == '0':
        if ('[' in MSG) & ('(' in MSG):
            num = re.search('(?<=\[).+(?=\])', MSG).group()
        
        elif '전역' in MSG:
            num = '1'
            
        else:
            num = '0'

    else:
        if '(' in MSG:
            station_name = re.findall('\(.+(?=\))', MSG)[0].lstrip('(')
            trains_station_number = get_station_number(station_name)
            search_station_number = int(SEARCH_STATION_NUMBER[-3:])
            num = abs(trains_station_number - search_station_number)

        else:
            num = '0'

    return int(num)
        
def get_destination(MSG):
    if ' ' in MSG:
        des = re.search('.+(?= )', MSG).group()
    else:
        des = MSG

    return des

def convert_status_code_to_str(MSG):
    # (0:진입, 1:도착, 2:출발, 3:전역출발, 4:전역진입, 5:전역도착, 99:운행중)
    
    if MSG == '0':
        msg = '진입'

    elif MSG == '1':
        msg = '도착'
        
    elif MSG == '2':
        msg = '출발'

    elif MSG == '3':
        msg = '전역 출발'

    elif MSG == '4':
        msg = '전역 진입'

    elif MSG == '5':
        msg = '전역 도착'

    elif MSG == '99':
        msg = '운행중'

    else:
        msg = '알 수 없음'
    
    return msg

def get_arrival_train_list(CERTIFICATION_KEY, STATION_NAME):
    URL = f'http://swopenAPI.seoul.go.kr/api/subway/{CERTIFICATION_KEY}/json/realtimeStationArrival/0/20/{STATION_NAME}'
    response = requests.get(URL)
    json_data = response.json()
    train_list = json_data.get('realtimeArrivalList')

    return train_list

def get_current_train_info(TRAIN_LIST, UPDNLINE = '하행'):
    result_list = list()
    for train in TRAIN_LIST:
        if (train.get('subwayId') == '1001') & (train.get('updnLine') == UPDNLINE):
            Train_num = train.get('btrainNo')
            Destination = get_destination(train.get('bstatnNm'))
            Current_Location_num = get_current_location(train.get('arvlMsg2'), train.get('barvlDt'), train.get('statnId'))
            Current_Location_stn = train.get('arvlMsg3')
            local_express_fx = lambda x : x if x == '급행' else '일반'
            local_express = local_express_fx(train.get('btrainSttus'))
            train_status = convert_status_code_to_str(train.get('arvlCd'))

            if Current_Location_num < 25:
                result_list.append([Train_num,
                                Destination,
                                local_express,
                                Current_Location_num,
                                Current_Location_stn,
                                train_status
                                ])
            
    # if len(result_list) == 0:
    #     result_list = '도착예정정보없음'

    return result_list

def getCTI(CERTIFICATION_KEY, STATION_NAME, UPDNLINE = '하행'):
    train_list = get_arrival_train_list(CERTIFICATION_KEY, STATION_NAME)
    
    try:
        return get_current_train_info(train_list, UPDNLINE)

    except:
        return '입력 정보를 다시 확인하십시오.'

if __name__ == '__main__':

    train_list = getCTI(CERTIFICATION_KEY, '종각', '하행')
    print(train_list)
    
    