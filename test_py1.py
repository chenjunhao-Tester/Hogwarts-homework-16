import pytest
import random


list1=[[random.randint(0,9) for i in range(3)]for j in range(3)]
print(list1)

@pytest.mark.parametrize("a,b,c",list1,ids=('test1','test2','test3'))
def test_demo1(a,b,c):
        assert a+b==c
        print('END')
