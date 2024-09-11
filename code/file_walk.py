#Εύρεση αρχείων από φάκελο και υποφακέλους με χρήση os.walk
import os
from time import time
import re
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



#path = μονοπατι που βρισκεται το αρχειο που εξεταζω καθε φορα, η δαιδρομη μεχρι τον φακελο που εξεταζω καθε φορα
# _ = placeholder, παιρνει τη θεση 1 μεταβλητης, οταν δεν μας ενδιαφερει η τιμη της δεν θα την χρησιμοποιησουμε, οι φακελοι που μπορω να παω αν η 3η μετ ειναι φακελος
#εχω 3 μεταβλητες διοτι η os.walk εχει 1 πλειαδα που αποτελειται απο 3 εγγραφες, αν αφηνα μονο το path θα ηταν πλειαδα κ θα επρεπε να ειναι path[0], path[1] κτλ 
# os.walk ειναι 1 λιστα επιστρεφει ενα tuple 


files=file_parser()

#Ερωτημα 1 - Πληθος αρχειων c,cpp,h,hpp
def files_by_category():
    counter={'cpp':0,'hpp':0, 'c':0, 'h':0}
    starttime=time()
    print('Start time for 1 is: ' +str(starttime) + ' sec')
    for x in files:
        #if re.match('.+\.cpp$',x):
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
    print('Start time for 2 is: ' +str(starttime) + ' sec')
    linecounter=0
    for i in files:
        with open(i,'r',encoding="ISO-8859-1",errors='ignore') as f:
            for j in f:
                if len(j.strip())!=0:
                    linecounter+=1
    print('Lines of code: '+str(linecounter))
    print('Elapsed Time for finding all lines of code: '+str(time()-starttime)+ ' sec')








#Main κομματι
files_by_category()
print('=='*30)
codelines()
print('=='*30)