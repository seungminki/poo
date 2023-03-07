import get_current_train_info as CTI
import res_list_to_TEXT as resText
from dotenv import load_dotenv
import os

load_dotenv()
train_key = os.environ.get('train_key')

def output_keyvlaue(st, di):
    try:
        response = CTI.getCTI(train_key, st, di)
        # Text_LIST = resText.list_to_TEXT(response)
        print(response)

        return response
    
    except:
        print('오류 발생')