from nose.tools import *
from NAME.functions import *


'''def test1():
    filename="http://claritytrec.ucd.ie/~alawlor/comp30670/input_assign.txt"
    buffer=read_file(filename)
    eq_(len(buffer),9506,"buffer sizes do not match")'''
    
def test2():
    list=listcreate(10)
    eq_(len(list),10,"list size do not match")
    
def test3():
    list=listcreate(10)
    a=turnon(list,0,9,0,9)
    list2=a2d =[[True]*10 for _ in range(10)]
    eq_(a,list2,"turn on result do not match")
def test4():
    list=listcreate(10)
    a=turnoff(list,0,9,0,9)
    eq_(a,list,"turn off result do not match")
def test5():
    list=listcreate(10)
    a=switch(list,0,9,0,9)
    list2=a2d =[[True]*10 for _ in range(10)]
    eq_(a,list2,"switch result do not match")
def test6():
    list=listcreate(10)
    a=turnon(list,0,9,0,9)
    b=countlight(a)
    eq_(b,100,"count result do not match")
    