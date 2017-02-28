'''
Created on Feb 26, 2017

@author: Peng Xu
'''
import urllib.request
from functions import turnoff,turnon,switch,listcreate,countlight
'''import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--input', help='input help')
args = parser.parse_args()

url = args.input'''
# read the url 
url=" http://claritytrec.ucd.ie/~alawlor/comp30670/input_assign3_b.txt" 
data=urllib.request.urlopen(url).read()
buffer=data.decode('UTF-8')  
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
    #print(value)
    flag=0

    for item in value:
        number=[int(s) for s in item.split(',') if s.isdigit() or (s.startswith('-') and s[1:].isdigit())]
        '''get the key number from file and assigned them to x1, x2, y1, y2'''        
        if number and flag % 2==0:
            x1=number[0]
            y1=number[1]
            flag=1
        elif number and flag % 2==1:
            x2=number[0]
            y2=number[1]
            flag=0
            '''get the key word of command and exctue the right funcion'''
            #print(value,x1,x2,y1,y2)
            if value[0]=='turn' and value[1]=='on':
                turnon(list1,x1,x2,y1,y2)
            elif value[0]=='turn' and value[1]=='off':
                turnoff(list1,x1,x2,y1,y2)
            elif value[0]=='switch':
                switch(list1,x1,x2,y1,y2)
            

result=countlight(list1)

print(result)
            
                
            
        

