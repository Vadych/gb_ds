# для получения информации вида: 
# (<remote_addr>, <request_datetime>, <request_type>, 
# <requested_resource>, <response_code>, <response_size>), 
# 
# например:
# raw = '188.138.60.101 - - [17/May/2015:08:05:49 +0000] "GET
# /downloads/product_2 HTTP/1.1" 304 0 "-" "Debian APT-HTTP/1.3 (0.9.7.9)"'
#
# parsed_raw = ('188.138.60.101', '17/May/2015:08:05:49 +0000', 'GET',
# '/downloads/product_2', '304', '0')


import re
pattern = re.compile(r'((?:[0-9a-f]{,4}[\.:]){3,7}[0-9a-f]{,4})'
                    r'.*\[(\d{1,2}/[A-Z][a-z]+/\d{4}(?::\d\d){3} \+\d{4})'
                    r'.*"([A-Z]+) '
                    r'((?:/[a-z]+)+)'
                    r'.*" (\d+) (\d+)'
)

with open('nginx_logs.txt') as f:
    for line in f:
        res = pattern.findall(line)
        if not res:
            raise TypeError (line)
        print (res[0])


    
