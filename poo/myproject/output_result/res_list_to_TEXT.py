def list_to_TEXT(TRAIN_LIST):
    # [['0665', '신창', '일반', 1, '세마', '전역 진입'],[]]
    TRAIN_LIST = sorted(TRAIN_LIST, key=lambda x: x[3])

    Text_LIST = []

    
    for TRAIN in TRAIN_LIST:
        # print(TRAIN[0], TRAIN[1], TRAIN[2], TRAIN[3], TRAIN[4], TRAIN[5])
        if TRAIN[0][0] == '1':
            TRAIN[2] = '급행'

        if TRAIN[3] >= 2:

            if TRAIN[5] == '운행중':
                # print(TRAIN[0], TRAIN[1], TRAIN[2], TRAIN[3], TRAIN[4], TRAIN[5])
                # print(f'{TRAIN[1]}행 {TRAIN[2]}열차 현재 {TRAIN[3]}개 역 전인 {TRAIN[4]}역에서 출발했습니다.')
                Text_LIST += [f'{TRAIN[1]}행 {TRAIN[2]}열차 현재 {TRAIN[3]}개 역 전인 {TRAIN[4]}역에서 출발했습니다.']
            
            else:
                # print(TRAIN[0], TRAIN[1], TRAIN[2], TRAIN[3], TRAIN[4], TRAIN[5])
                # print(f'{TRAIN[1]}행 {TRAIN[2]}열차 현재 {TRAIN[3]}개 역 전인 {TRAIN[4]}역 {TRAIN[5]}중입니다.')
                Text_LIST += [f'{TRAIN[1]}행 {TRAIN[2]}열차 현재 {TRAIN[3]}개 역 전인 {TRAIN[4]}역 {TRAIN[5]}중입니다.']

        if TRAIN[3] == 1:
            # print(TRAIN[0], TRAIN[1], TRAIN[2], TRAIN[3], TRAIN[4], TRAIN[5])
            # print(f'{TRAIN[1]}행 {TRAIN[2]}열차 현재 {TRAIN[5]}중입니다.')
            Text_LIST += [f'{TRAIN[1]}행 {TRAIN[2]}열차 현재 {TRAIN[5]}중입니다.']

        if TRAIN[3] == 0:
            # 당역 도착 관련
            # print(TRAIN[0], TRAIN[1], TRAIN[2], TRAIN[3], TRAIN[4], TRAIN[5])
            if TRAIN[5] == '운행중':
                pass

            else:
                # print(f'{TRAIN[1]}행 {TRAIN[2]}열차 현재 {TRAIN[5]}중입니다.')
                Text_LIST += [f'{TRAIN[1]}행 {TRAIN[2]}열차 현재 {TRAIN[5]}중입니다.']

    return Text_LIST

    

        

if __name__ == '__main__':
    list_to_TEXT([['0665', '신창', '일반', 1, '세마', '전역 진입'], 
                  ['1937', '천안', '급행', 17, '가산디지털단지', '운행중'], 
                  ['0667', '신창', '일반', 4, '수원', '운행중'], 
                  ['1939', '신창', '일반', 23, '노량진', '운행중']])