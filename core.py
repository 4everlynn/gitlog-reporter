# load file
import os.path as path

import os

import re
from dateutil.parser import parse
import datetime


# get all log files in target path
def search_file(pathname, filename):
    matched_file = []
    for root, dirs, files in os.walk(pathname):
        for file in files:
            if re.match(filename, file):
                file_name = os.path.abspath(os.path.join(root, file))
                matched_file.append(file_name)
    return matched_file


# get log files in current path
logs = search_file('.', 'log-\d+.rep')
author = ''

if len(logs) == 0:
    print('there are no log files in git repos :(')
    exit(1)

if path.exists('reporter.meta'):
    log = open('reporter.meta')
    author = log.readlines()[0]
    log.close()
else:
    author = input('Enter author -> ')
    _save = input('Do you want to save author name [y/n] ')
    if _save == 'y':
        f = open("reporter.meta", 'wb')
        f.write(bytes(author, encoding="utf8"))
        f.close()

gen_type = input('Enter generate type(day | week) -> ')
data = []
for log_path in logs:
    log = open(log_path)
    lines = log.readlines()
    log.close()
    for line in lines:
        if 'Merge remote-tracking branch' in line or 'Merge branch' in line:
            continue
        if author.lower() in line.lower():
            dataOfLine = line.split('[sep]')
            time = parse(dataOfLine[2])
            if gen_type == 'day':
                offset_time = datetime.date.today() + datetime.timedelta(days=-1)
                if time.day == offset_time.day and time.month == offset_time.month:
                    module = dataOfLine[1].split('://')
                    message = ''
                    if len(module) == 2:
                        message = module[1]
                        module = module[0]
                    else:
                        module = ''
                        message = dataOfLine[1]
                    data.append({
                        'name': dataOfLine[0],
                        'message': message,
                        'module': module,
                        'time': time
                    })
            if gen_type == 'week':
                now = datetime.datetime.now()
                week = now.weekday()
                _from = (now - datetime.timedelta(days=week - 7 * 0))
                _to = (now + datetime.timedelta(days=6 - week + 7 * 0))
                module = dataOfLine[1].split('://')
                message = ''
                if len(module) == 2:
                    message = module[1]
                    module = module[0]
                else:
                    module = ''
                    message = dataOfLine[1]
                if _from.timestamp() <= time.timestamp() <= _to.timestamp():
                    data.append({
                        'name': dataOfLine[0],
                        'module': module,
                        'message': message,
                        'time': time
                    })


def group(group_key, data_set):
    result = {'': []}
    for item in data_set:
        if group_key in item.keys():
            if item[group_key] not in result.keys():
                result[item[group_key]] = []
            result[item[group_key]].append(item)
        else:
            result[''].append(item)

    return result


index = [chr(i) for i in range(ord("a"), ord("z") + 1)]

target = group('module', data)
out_num = 1
for key in target:
    if key != '':
        if len(target[key]) > 1:
            print(str(out_num) + '、' + str(key))
        inner_num = 0
        for log in target[key]:
            if len(target[key]) > 1:
                print('\t' + index[inner_num] + '、' + log['message'])
                inner_num += 1
            else:
                print(str(out_num) + '、' + str(key) + ',' + log['message'])
        out_num += 1
    else:
        for log in target[key]:
            print(str(out_num) + '、' + log['message'])
            out_num += 1
