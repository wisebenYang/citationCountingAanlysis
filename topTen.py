#coding=utf-8
from __future__ import division 
import numpy as np

fnCA = ['ICCV', 'AAAI', 'NIPS', 'CVPR', 'ACL', 'IJCAI', 'ICML']
fnCB = ['COLT','UAI','PPSN','KR','ICRA','ICCBR','ICAPS','EMNLP','ECCV','ECAI','COLING','AAMAS']
fnCC = ['ACCV','AISTATS','BMVC','CoNLL','FGR','GECCO','ICANN','ICB','ICDAR','ICONIP','ICPR','ICTAI','IJCNN','IROS','KSEM','NAACL','PRICAI']
fnJA = ['AI','IJCV','JMLR','PAMI']
fnJB = ['IJAR','AAMAS','TNNLS','TFS','TEC','TCYB','TASLP','TAC','NN','NECO','ML','MIT','JAR','DKE','CVIU']
fnJC = ['AIM','Alife','APIN','CSL','DSS','EAAI','ES','ESWA','FSS','IDA','IJNS','IJIS','IJON','IJPRAI','IVC','KBS','MVA','NC','NPL','PAA','PRL','SOCO','tNCA']

def writeFile(filename,Txtstr):
    fr = open(filename,'a+')
    fr.write(Txtstr)
    fr.close()

def readFile(fileneme):
    word = []
    file=open(fileneme)
    while 1:
        line = file.readline().replace('\n','')
        if not line:
            break
        try:
            word.append(np.log(int(line.split('\t')[1])+1))
        except:
            pass
    return word

def getJour():
    for fn in fnJA:
        CW1 = []
        for i in range(2007,2017):
            try:
                filename = 'data/counts/journalA/'+fn+'/'+str(i)
                CW1.append( np.mean( readFile(filename) )/(2017-i) )
            except:
                continue
        print fn,'\t',np.sum(CW1)/(len(CW1))
    
    for fn in fnJB:
        CW2 = []
        for i in range(2007,2017):
            try:
                filename = 'data/counts/journalB/'+fn+'/'+str(i)
                CW2.append( np.mean( readFile(filename))/(2017-i) ) 
            except:
                continue
        print fn,'\t',np.sum(CW2)/(len(CW2))
    
    for fn in fnJC:
        CW3 = []
        for i in range(2007,2017):
            try:
                filename = 'data/counts/journalC/'+fn+'/'+str(i)
                CW3.append( np.mean( readFile(filename) )/(2017-i) )
            except:
                continue
        print fn,'\t',np.sum(CW3)/(len(CW3))
        
def getConf():
    for fn in fnCA:
        CW1 = []
        for i in range(2007,2017):
            try:
                filename = 'data/counts/conferenceA/'+fn+'/'+str(i)
                CW1.append( np.mean( readFile(filename) )/(2017-i) )
            except:
                continue
        print fn,'\t',np.sum(CW1)/(len(CW1))
    
    for fn in fnCB:
        CW2 = []
        for i in range(2007,2017):
            try:
                filename = 'data/counts/conferenceB/'+fn+'/'+str(i)
                CW2.append( np.mean( readFile(filename))/(2017-i) ) 
            except:
                continue
        print fn,'\t',np.sum(CW2)/(len(CW2))
    
    for fn in fnCC:
        CW3 = []
        for i in range(2007,2017):
            try:
                filename = 'data/counts/conferenceC/'+fn+'/'+str(i)
                CW3.append( np.mean( readFile(filename) )/(2017-i) )
            except:
                continue
        print fn,'\t',np.sum(CW3)/(len(CW3))
if __name__ == '__main__':
    getConf()
    getJour()
    
