import os
import re
import sys
from time import time
sys.path.append('..') #για το προηγουμενο path
import file_walk as fw

files=fw.file_parser() #βρισκει τα αρχεια


def Symbols_Letters_Digits():
    parser={'characters':0, 'digits':0, 'symbols':0}
    patternC=re.compile('[A-Za-z]')
    patternD=re.compile('\d')
    if len(files)==0:
        print('No input data!! Please check your file data!')
        return
    starttime=time()
    print('Start time for 3 is: ' +str(starttime) + ' sec')

    for x in files:
        with open(x,'r',encoding='utf-8',errors='ignore') as f:
            for k in f:
                #actualsd=k.replace(' ','').replace('\n','')  # k->string που αποθ την καθε γραμμη
                chars=len(patternC.findall(k))
                digits=len(patternD.findall(k))
                parser['characters']+=chars
                parser['digits']+=digits
                parser['symbols']+=len(k)-(chars+digits)
    endtime=time()
    for x in parser:
        print(f'{x}-->{parser[x]}')
    print('=='*30)
    print(f'Elapsed Time for symbols:{endtime-starttime} sec')



Symbols_Letters_Digits()       