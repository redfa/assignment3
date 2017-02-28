'''
Created on Feb 26, 2017

@author: Peng Xu
'''
import urllib.request
'''import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--input', help='input help')
args = parser.parse_args()

url = args.input'''
# read the url 
url=" http://claritytrec.ucd.ie/~alawlor/comp30670/input_assign3_c.txt" 
data=urllib.request.urlopen(url).read()
buffer=data.decode('UTF-8')  
content=buffer.splitlines()
#print(content)
'''catch the key number and words'''
size= int(content[0])
list1=[]
x1=0
x2=0
y1=0
y2=0
for line in content[1:]:
    value=line.split()
    #print(value)
    flag=0

    for item in value:
        list1=[]
        value=[int(s) for s in item.split(',') if s.isdigit() or (s.startswith('-') and s[1:].isdigit())]
        
        if value and flag % 2==0:
            x1=value[0]
            y1=value[1]
            flag=1
        elif value and flag % 2==1:
            x2=value[0]
            y2=value[1]
            flag=0
            #print(x1,x2,y1,y2)
            
        
    ''' create a list include all key number needed'''   
    #x1=list1[i][0]
    #y1=list1[i][1]
    #x2=list1[i+1][0]
    #y2=list1[i+1][1]
    #i+=2
    #print(x1,x2,y1,y2)

#print (size)
