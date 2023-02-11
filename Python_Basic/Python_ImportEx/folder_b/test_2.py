'''
case 1. test_2.py (자식) 에서 folder_a (부모) 의 a1.py 참조
- 자식 폴더에서 부모폴더의 절대경로를 참조 path에 추가
- 필요 path를 환경변수에 등록
'''
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from folder_a import a1

def test1():
    a1.method_a1()
    print('test1')
    print('절대 경로 추가된 것 확인 : ' + sys.path[-1])

'''
case 2. test_2.py에서 d1.py 모듈 참조
'''
import d1 

def test2():
    d1.method_d1()
    print('test2')



if __name__ == "__main__":
    test1()
    test2()