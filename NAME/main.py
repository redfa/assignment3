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
url="http://claritytrec.ucd.ie/~alawlor/comp30670/input_assign3.txt" 
data=urllib.request.urlopen(url).read()
buffer=data.decode('UTF-8')  
content=buffer.splitlines()
#print(content)
'''catch the key number and words'''
size= int(content[0])
list1=[]
for line in content[1:]:
    value=line.split()
    #print(value)
    
    flag=0
    for item in value:
        value=[int(s) for s in item.split(',') if s.isdigit()]
        if value:
            list1.append(value)
        
print(list1)

#print (size)

  
