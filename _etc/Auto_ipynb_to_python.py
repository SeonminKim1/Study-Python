# ipynb를 python으로 자동으로 바꾸어주는 프로그램
from subprocess import call
import os

# ipynb파일과 python 파일이 같은 디렉토리에 있다는 가정하에 진행
file_list = os.listdir() # 현재 디렉토리 목록 받아오기.
for i, file in enumerate(file_list):
    if 'ipynb' in file:
        call('jupyter nbconvert --to python '+file) # ipynb 변환
        print(str(i), file, ' is Completed with .py file.')
    else :
        print(str(i), file, ' is Not Ipynb file.')