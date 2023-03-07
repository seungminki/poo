import get_current_train_info as CTI
import res_list_to_TEXT as resText
from dotenv import load_dotenv
import os

load_dotenv()
train_key = os.environ['TRAIN_KEY']

def output_keyvlaue(st, di):
    
    
    response = CTI.getCTI(train_key, st, di)
    # Text_LIST = resText.list_to_TEXT(response)

    return response
    
    

if __name__ == '__main__':
    print(output_keyvlaue('금천구청', '하행'))