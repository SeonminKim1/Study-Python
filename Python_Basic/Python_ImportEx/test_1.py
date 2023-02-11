'''
case 1. test_1.py에서 a_folder의 a1.py 참조
'''
from folder_a import a1
def test1():
    print('test1')
    a1.method_a1()

'''
case 2. test_1.py에서 d1.py 모듈 참조
'''
import d1
def test2():
    print('test2')
    d1.method_d1()

if __name__ == "__main__":
    test1()
    test2()