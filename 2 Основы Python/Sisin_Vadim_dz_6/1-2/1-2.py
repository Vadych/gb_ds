# Не используя библиотеки для парсинга, распарсить 
# (получить определённые данные) файл логов web-сервера
# nginx_logs.txt 
# — получить список кортежей вида: 
#     (<remote_addr>, <request_type>, <requested_resource>).
#     Например:  
# [
# ...
# ('141.138.90.60', 'GET', '/downloads/product_2'), 
# ('141.138.90.60', 'GET', '/downloads/product_2'), 
# ('173.255.199.22', 'GET', '/downloads/product_2'), ...
# ]
# 2. *(вместо 1) Найти IP адрес спамера и количество отправленных им 
# запросов по данным файла логов из предыдущего задания.
# Примечание: спамер — это клиент, отправивший больше всех запросов; 
# код должен работать даже с файлами, размер которых превышает 
# объем ОЗУ компьютера.

def parse_str(str):
    ip = str[:str.find(' ')]
    req_start = str.find('"') + 1
    req_end = str.find('"', req_start)
    req_type, req_addr, _ = str[req_start : req_end].split()
    return ip, req_type, req_addr

res_list = []
count_request = {}
spamer_ip = ''
spamer_count = 0
with open ('nginx_logs.txt', 'r') as f:
    for line in f:
        if line:
            ip, quest_type, quest_addr = parse_str (line)
            res_list.append((ip, quest_type, quest_addr))
            count_request[ip] = count_request.setdefault(ip, 0) + 1
            if count_request[ip] > spamer_count:
                spamer_count = count_request[ip]
                spamer_ip = ip
        
        
print (res_list[:10])
print (f'Спамер отправил {spamer_count} запросов c IP {spamer_ip}')