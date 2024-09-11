import file_walk as fw
from time import time
import os
import re
import sys
sys.path.append('..')

files = fw.file_parser()


def over_12_characters():
    starttime = time()
    print('Start time for 5 is: ' + str(starttime) + ' sec')
    found = 0
    print('Files with for loops: '+str(len(files)))
    pattern = re.compile('\s*for\s*\(\s*\w*\s*[;]\s*\w*\s*[;]\s*\w*\s*\)|\s*for\s*\(\s*\w+\s*[:]\s*\w+\s*\)')
    # το 2ο for ειναι για τα range for
    for x in files:
        with open(x, 'r', encoding='ISO-8859-1') as f:
            for k in f:
                for l in  pattern.findall(k):
                    print(l)
                    current = l[int(l.find('('))+1:len(l)-1]
                    if len(current.replace(' ', '')) >= 12:
                        print(current)
                        found += 1
                    print('')
    print(f'Number of for loops with over 12 characters: {found}')
    endtime = time()
    print(f'Elapsed Time for for loops is: {endtime-starttime} sec')


over_12_characters()


#for l in list([u[0] for u in pattern.findall(k)]):