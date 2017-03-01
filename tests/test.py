from nose.tools import *
from NAME.functions import *
from NAME.main import read_file

def test1():
    filename="http://claritytrec.ucd.ie/~alawlor/comp30670/input_assign3.txt"
    buffer=read_file(filename=filename)
    eq_(len(buffer),9506,"buffer sizes do not match")