# -*- coding: utf-8 -*- print("януари")
# read_json.py
# like:
# https://pkk.rosreestr.ru/api/features/1?text=50:31:0010101:*&limit=41&skip=0
#
#

import json
import os
import sys


def my_f001(dir_fullpath):
    if dir_fullpath:
        dir_path = r'T:\#tmp\070_ppk5\2\27_11_2018_15ВР_1633\Приложение ' \
                   r'1\1'
    else:
        dir_path = dir_fullpath

    print('KK\ttotal\tloaded\tfullpath')
    for f_path in os.listdir(dir_path):
        # f_path = r'T:\#tmp\070_ppk5\2\27_11_2018_15ВР_1633\Приложение ' \
        #          r'1\1\1@text=50%3A31%3A0032201%3A%2A&limit=40&skip=0'
        f_fullpath = os.path.join(dir_path, f_path)
        if r'@text=' in f_path.lower():
            print(get_ku_id(f_path), sep='', end='\t')
            # print('+',f_fullpath)
            my_json = my_load_json(f_fullpath)
            # print(my_json)
            if my_json['total_relation'] == 'eq':
                print('+', sep='', end='\t')
            else:
                print('?', sep='', end='\t')
            print(
                my_json['total'],
                len(my_json['features']),
                sep='\t', end='\t',
            )
            print('"' + f_fullpath + '"',
                  sep='\t', end='\n'
                  )
        # else:
            # print('-', -1, -1, sep='\t', end='\t')
            # pass
        pass


def get_ku_id(fname: str) -> str:
    m = fname.index(r'@text=')
    n = 0
    if m > 0:
        m += len('@text=')
        n = fname.index(r'%3A%2A&', m + 1)
        if n > 0:
            return fname[m:n].replace(r'%3A', ':')

    return ''


def my_load_json(fpath='', encoding='ascii'):
    with open(fpath, "rt", encoding=encoding) as f:
        data = json.load(f)

    # print(data)
    return data


if __name__ == "__main__":
    dir_path = sys.argv[1]
    my_f001(dir_path)
