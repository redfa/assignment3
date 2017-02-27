'''
Created on Feb 26, 2017

@author: Peng Xu
'''
import urllib.request
''''import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--input', help='input help')
args = parser.parse_args()

url = args.input'''
# read the url 
url="http://claritytrec.ucd.ie/~alawlor/comp30670/input_assign3.txt" 
data=urllib.request.urlopen(url).read()  
buffer=data.decode('UTF-8')  
print(buffer)

  
