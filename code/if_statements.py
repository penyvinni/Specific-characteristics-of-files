import sys
sys.path.append('..')
import re
import file_walk as fw
from time import time

files=fw.file_parser()
print('\t\t Files found:'+str(len(files)))

def equality_statements():
    starttime=time()
    print('Start time for 4 is: ' +str(starttime) + ' sec')
    counter=0
    fls=[]
    pattern=re.compile('\s*if\s*\(\s*.+\s*==\s*.+\)|^if\s*\(.+==.+\)|\s*if\s*\(\s*\w+\s*\)')
    #if(1)->1==0 για το 3ο if που πιανει τα boolean
    for x in files:
        with open(x, "r", encoding="utf-8", errors="ignore") as f:
            #counter+=len([m for m in f if(r.match('.*if(.+==.+).*',m))])
            for k in f:
                fls+=pattern.findall(k)
    id=1
    for k in fls:
        k=k.replace(' ','').replace('\t','')
        #print(str(id)+'. '+str(k))
        id+=1
    #print('\n\n')
    print('\t If Statements containing equality')
    print('=='*22)
    print('\t Number of Statements:'+str(len(fls)))
    endtime=time()
    print('Elapsed Time for if statements: '+str(endtime-starttime)+ ' sec')
    
equality_statements()

