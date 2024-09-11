import os
from time import time
import re
import sys
sys.path.append('..')
parentroot='oop-master'

def file_parser():
    starttime=time()
    allfiles=[]  #μεταβλητη τυπου λιστα (κενη που τη γεμιζω με τα αρχεια μεσω της os.walk)
    try:
        for path,_,file in os.walk(top=parentroot, topdown=True):  #χωρις το os.walk δεν θα μπορουσα να μπω στους υποφακελους του oop-master
            allfiles+= [path+'/'+ l for l in file if l.endswith('.cpp') or l.endswith('.c') or l.endswith('.hpp') or l.endswith('.h')]
    except:
        print('Can not open folder oop-master')
        return list([])
    print('Elapsed Time for file opening: '+str(time()-starttime)+' sec')
    print('=='*30)
    return allfiles

print(file_parser())


files=file_parser()

#Ερωτημα 1 - Πληθος αρχειων c,cpp,h,hpp
def files_by_category():
    counter={'cpp':0,'hpp':0, 'c':0, 'h':0}
    starttime=time()
    print('Start time for 1 is: ' +str(starttime) + ' sec')
    for x in files:
        if x.endswith('.cpp'):
            counter['cpp']+=1
        elif x.endswith('.hpp'):
            counter['hpp']+=1
        elif x.endswith('.c'):
            counter['c']+=1
        else:
            counter['h']+=1
    for key in counter:
        print(f'{key}--> {counter[key]}')
    endtime=time()
    print('Elapsed Time for finding the files: '+str(endtime-starttime)+ ' sec')

    

#Ερωτημα 2 - Πληθος γραμμων χωρις κενες
def codelines():
    starttime=time()
    print('\nStart time for 2 is: ' +str(starttime) + ' sec')
    linecounter=0
    for i in files:
        with open(i,'r',encoding="ISO-8859-1",errors='ignore') as f:
            for j in f:
                if len(j.strip())!=0:
                    linecounter+=1
    print('Lines of code: '+str(linecounter))
    print('Elapsed Time for finding all lines of code: '+str(time()-starttime)+ ' sec')



#Ερώτημα 3 - Πλήθος συμβόλων
def Symbols_Letters_Digits():
    parser={'characters':0, 'digits':0, 'symbols':0}
    patternC=re.compile('[A-Za-z]')
    patternD=re.compile('\d')
    if len(files)==0:
        print('No input data!! Please check your file data!')
        return
    starttime=time()
    print('\nStart time for 3 is: ' +str(starttime) + ' sec')

    for x in files:
        with open(x,'r',encoding='utf-8',errors='ignore') as f:
            for k in f:
                chars=len(patternC.findall(k))
                digits=len(patternD.findall(k))
                parser['characters']+=chars
                parser['digits']+=digits
                parser['symbols']+=len(k)-(chars+digits)
    endtime=time()
    for x in parser:
        print(f'{x}-->{parser[x]}')
    
    print(f'Elapsed Time for symbols:{endtime-starttime} sec')




#Ερώτημα 4 - Πλήθος if με ==

print('\t\t Files found:'+str(len(files)))

def equality_statements():
    starttime=time()
    print('\nStart time for 4 is: ' +str(starttime) + ' sec')
    counter=0
    fls=[]
    pattern=re.compile('\s*if\s*\(\s*.+\s*==\s*.+\)|^if\s*\(.+==.+\)|.*if\s*\(\s*\w+\s*\)')
    for x in files:
        with open(x, "r", encoding="utf-8", errors="ignore") as f:
            for k in f:
                fls+=pattern.findall(k)
    id=1
    for k in fls:
        k=k.replace(' ','').replace('\t','')
        id+=1
    endtime=time()
    print('Elapsed Time for if statements: '+str(endtime-starttime)+ ' sec')
    return len(fls)



#Ερώτημα 5 - Πλήθος for με > 12 χαρακτήρες
def over_12_characters():
    starttime=time()
    print('\nStart time for 5 is: ' +str(starttime) + ' sec')
    found=0
    print('Files with for loops: '+str(len(files)))
    pattern=re.compile('\s*for\s*\(\s*.*\s*;\s*.*\s*;\s*.*\s*\)|\s*for\s*\(\s*.+[:]\s*.+\s*\)')
    for x in files:
        with open(x,'r',encoding='ISO-8859-1') as f:
           for k in f:
               for l in pattern.findall(k):
                   current=l[int(l.find('('))+1:len(l)-1]
                   if len(current.replace(' ',''))>=12:
                         found+=1
                   
    print(f'Number of for loops with over 12 characters: {found}')
    endtime=time()
    print(f'Elapsed Time for for loops is: {endtime-starttime} sec')




#Ερώτημα 6 -  Κοινά ονόματα μεταβλητών
def commonVars():
    common=0
    starttime=time()
    commonvars=dict({})
    unacceptable=re.compile('((const|static|static\s+const)\s+int\s+\w+\s*[=]\s*\w+\s*[;])')
    pattern=re.compile('\s*int\s+\w+[;]') #int a;  int   b; 
    patternA=re.compile('\s*int\s+\w+([,]\w+)+[;]') #int a,b,h,j,i,....;
    patternB=re.compile('\s*int\s+\w+([=]\w+)+[;]') #int a=2;
    patternC=re.compile('\s*int\s+\w+\s*[=]\s*\w+\s*([,]\s*\w+\s*[=]\s*\w+\s*)+[;]') #int a=1,b=3;
    for x in files:
        with open(x,'r',encoding='utf8',errors='ignore') as f:
            lines=f.readlines()
            for k in lines:
                word=k
                if word.startswith('//') or word.startswith('#'):
                    continue

                for l in unacceptable.finditer(k):
                    word=k[0:l.start()]+k[l.end():]


                for n1 in pattern.findall(word):
                   if len(n1)==0: continue
                   word=n1.replace(';','').strip()
                   spdat=re.split('\s',word)
                   if spdat[1] in commonvars:
                       commonvars[spdat[1]]+=1
                       common+=1
                   else:
                       commonvars.update({spdat[1]:1})

                for n2 in [l[0] for l in patternA.findall(word)]:
                    word=n2.replace(';',' ').strip()
                    data2=re.split('[,\s]',word)
                    for j in data2:
                        if j.strip()=='int': 
                            continue
                        if j.strip() in commonvars:
                           commonvars[j.strip()]+=1
                           common+=1
                        else:
                           commonvars.update({j.strip():1}) 

                for n3 in [l[0] for l in patternB.findall(word)]:
                    word=n3.strip().replace(';','')
                    data3=[x for x in re.split('[\s=]',word) if x.strip()!=';' and re.search('^\s+$',x)==None]
                    counter=0
                    for j in data3:
                       counter+=1
                       if len(data3)==int(counter):
                            continue
                       if j.strip()=='int':
                           continue
                       if j.strip() in commonvars:
                           commonvars[j.strip()]+=1
                           common+=1
                       else:
                           commonvars.update({j.strip():1})

                for n4 in [l[0] for l in patternC.findall(k)]:
                    word=n4.strip().replace(';','')
                    
                    data4=[x.replace(' ','') for x in word.split(',')]
                    for j in data4:
                        checkstr=word.split('=')[0]
                        if checkstr in commonvars:
                            commonvars[checkstr]+=1
                            common+=1
                        else:
                            commonvars.update({checkstr:1})
                
    tops=sorted(commonvars.items(),key=lambda elem:elem[1])
    print('Common Variables are:')
    for i in range(len(tops)-1,len(tops)-4,-1):
        print(f'{tops[i][0]}-->{tops[i][1]}') 
    print(f'\nNumber of variables\' appearance is: {common}')
    endtime=time()
    print(f'Elapsed Time for common vars is: {endtime-starttime} sec')



#Main κομματι
files_by_category()
print('=='*30)

codelines()
print('=='*30)

Symbols_Letters_Digits() 
print('=='*30)

equals=equality_statements()
print('If Statements containing equality')
print('=='*20)
print('Number of Statements:'+str(equals))
print('=='*30)

over_12_characters()
print('=='*30)

commonVars()
print('=='*40)

print('\t\t FINISH!!!')