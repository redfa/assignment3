'''
Created on Feb 26, 2017

@author: Peng Xu
'''
import urllib.request
from functions import turnoff,turnon,switch,listcreate,countlight
import re
def read_file(filename="input"):
    if filename.startswith('http'):
        return urllib.request.urlopen(filename).read().decode('UTF-8') 
    else:
        return open(filename).read()
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--input', help='input help')
args = parser.parse_args()

filename = args.input
# read the url 
#url=" http://claritytrec.ucd.ie/~alawlor/comp30670/input_assign3.txt" 
#data=urllib.request.urlopen(url).read()
#buffer=data.decode('UTF-8')  
buffer=read_file(filename=filename)
content=buffer.splitlines()
#print(content)
'''catch the key number and words'''
size= int(content[0])
list1=listcreate(size)
x1=0
x2=0
y1=0
y2=0

for line in content[1:]:
    value=line.split()
    #print(line)
    #print(value)
    number=re.findall("[-+]?\d+[\.]?\d*[eE]?[-+]?\d*", line)
    #print(re.findall("[-+]?\d+[\.]?\d*[eE]?[-+]?\d*", line))

    '''get the key number from file and assigned them to x1, x2, y1, y2'''    
    x1=int(number[0])
    y1=int(number[1])
    x2=int(number[2])
    y2=int(number[3])    
    '''get the key word of command and exctue the right funcion'''
            #print(value,x1,x2,y1,y2)
    if value[0]=='turn' and value[1]=='on':
        turnon(list1,x1,x2,y1,y2)
    elif value[0]=='turn' and value[1]=='off':
        turnoff(list1,x1,x2,y1,y2)
    elif value[0]=='switch':
        switch(list1,x1,x2,y1,y2)
    else:
        continue       

result=countlight(list1)
list2=[filename,result]
print(list2)
            
                
            
        

