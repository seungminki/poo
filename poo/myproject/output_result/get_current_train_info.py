import requests
import re

def get_current_location(MSG):
    if ('[' in MSG) & ('(' in MSG):
        num = re.search('(?=\[).+(?=\])', MSG).group().lstrip('[')
        
    elif '전역' in MSG:
        num = '1'
        
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
            Current_Location_num = get_current_location(train.get('arvlMsg2'))
            Current_Location_stn = train.get('arvlMsg3')

            if Train_num[0] == '1':
                local_express = '급행'

            else:
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
            
        result_list = sorted(result_list, key=lambda x: x[3])
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

    train_list = get_arrival_train_list('', '가산디지털단지')
    
    try:
        print(get_current_train_info(train_list, '하행'))

    except:
        print('입력 정보를 다시 확인하십시오.')
    
    