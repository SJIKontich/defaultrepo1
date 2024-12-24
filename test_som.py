from som import *

def test_emptysom():
    assert som([]) == 0

def test_singlesom():
    assert som([1]) == 1

def test_doublesom():
    assert som([1,2]) == 3

def test_triplesom():
    assert som([1,2,9]) == 3