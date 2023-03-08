def text_precessing(a_result):
    KOR_DIC = dict()

    from pathlib import Path

    tb_path = f"{Path.cwd()}/processing/processing_rule.table"
    
    with open(tb_path, 'r', encoding='UTF8') as tb:
        lines = tb.readlines()

        for line in lines[1:]:
            
            line = line.strip(' \n')
            
            line_list = line.split('|')
            KOR_DIC[line_list[0]] = line_list[1]

    insert_list = list(a_result)

    for key in KOR_DIC:
        
        v = a_result.find(key)

        if v == -1:
            pass

        else:
            insert_list[v : v + len(KOR_DIC[key])] = KOR_DIC[key]
            
    answer = ('').join(insert_list)

    return answer

def str_indexing(result_str):
    for i in range(len(result_str)):
        if result_str[i] == '역':
            station = result_str[:i]
        if result_str[i] == "행":
            direction = result_str[i-1:i+1]
        
    return station, direction

