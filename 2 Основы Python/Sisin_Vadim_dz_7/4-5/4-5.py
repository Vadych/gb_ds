from math import log10
import os
import json

# Взята тестовая папка с большим оличеством файлов, что бы их не тащить в гит
# в рабочем варианте заменить следующую строку на 
# SEARCH_DIR = os.getcwd()
SEARCH_DIR = '/Users/vadim/Library/Mobile Documents/iCloud~md~obsidian/Documents/Knowledge'

res_dict = {}
for root, dirs, files in os.walk(SEARCH_DIR):
    for file in files:
        ext_file = file.split('.')[-1].lower()
        file_path = os.path.join(root, file)
        size_file = os.path.getsize(file_path)
        #print(size_file)
        if size_file:
            key = 10 ** (int(log10(size_file)) +1)
        else:
            key = 0
        if not key in res_dict:
            res_dict[key] = [0, set()]
        res_dict[key][0] += 1
        res_dict[key][1].add(ext_file)

for idx, val in res_dict.items():
    res_dict[idx] = val[0], list(sorted(val[1]))
summary_file_name = os.path.split(SEARCH_DIR)[-1] + '_summary.json'

with open(summary_file_name, 'w', encoding='utf-8') as f:
    json.dump(res_dict, f, sort_keys=True)
    
    

