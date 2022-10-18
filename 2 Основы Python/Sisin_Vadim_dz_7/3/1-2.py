import os

def get_line_param (line):
    if line.find(':') > 0:
        line = line[:-1]
        is_path = True
    else:
        is_path = False
    tmp = line.split('- ')
    return is_path, tmp[-1], len(tmp)

def create_file(name, is_path):
    if is_path:
        try:
            os.mkdir(name)
        except FileExistsError:
            pass
    else:
        f = open(name, 'a')
        f.close()

current_level = 1
last_name = ''
with open('config.yaml', 'r') as f:
    for line in f:
        is_path, name, level = get_line_param(line.strip())
        if current_level == level:
            create_file(name, is_path)
        elif current_level < level:
            os.chdir(last_name)
            create_file(name, is_path)
        else:
            for _ in range(current_level - level):
                os.chdir('..')
            create_file(name, is_path)
        last_name = name
        current_level = level
            