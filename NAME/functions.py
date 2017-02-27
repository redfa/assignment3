'''
Created on Feb 27, 2017

@author: Peng Xu
'''
from pprint import pprint
'''create intial list''' 
def listcreate(size):
    a2d =[[False]*size for _ in range(size)]
    return a2d
    
#pprint(listcreate(10))
def turnon(list,x1,x2,y1,y2):
    '''turnon funciton'''
    x1=max(x1,0)
    x2=min(len(list)-1,x2)
    y2=min(len(list)-1,y2)
    for m in range(y1,y2+1):
        for n in range(x1,x2+1):
            if list[m][n]==False:
                list[m][n]=True
    return list
#pprint(turnon(listcreate(10),0,0,1,1))
def turnoff(list,x1,x2,y1,y2):
    '''turnoff funciton'''
    x1=max(x1,0)
    x2=min(len(list)-1,x2)
    y2=min(len(list)-1,y2)
    for m in range(y1,y2+1):
        for n in range(x1,x2+1):
            if list[m][n]==True:
                list[m][n]=False
    return list   

def switch(list,x1,x2,y1,y2):
    '''switch function'''
    x1=max(x1,0)
    x2=min(len(list)-1,x2)
    y2=min(len(list)-1,y2)
    for m in range(y1,y2+1):
        for n in range(x1,x2+1):
            if list[m][n]==True:
                list[m][n]=False
            else:
                list[m][n]=True
    return list   
pprint(switch(listcreate(10),1,5,1,1))    
    
        
    