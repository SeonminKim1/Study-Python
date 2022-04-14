# 0. 기타
# 파이썬 에디터 종류 PyCharm, IPython notebook, SciTE 에디터
# 주석처리하기 -> """특정부분 주석"""
# 파이썬은 1초에 20만번 연산
print("==== 자료형 연습 ====")
# 1, 자료형
# 복소수 j만 됨.
a = 3 + 5j
print("a.real: ", a.real, "a.imag: ", a.imag)

# 시퀀스 자료형들
# list
arr = [1, 2, 3]
print(arr)

# tuple 튜플은 값이 변경이 안됨.
tuple_ex = {3, 4, 5}
print(tuple_ex)
a, b, c = tuple_ex
print(a, b, c) # 값 분리됨.

print("==== Dictionary 연습 ====")
# dic_data   key:value 로 저장됨. 순서는 딱히 없음.
# 딕셔너리 선언시 빈 중괄호 사용 d = {}
# 순서가 없기 때문에 인덱스로는 접근할수 없고, 키로 접근 할 수 있습니다.
dic_data = {3: 'hi', 4: 'man', 5: 'women', 6: 'fuck you'}
dic_data2 = dict(alice = 50, bob=20, tony=15, suzy=30) #
print('dic_data:', dic_data, 'len: ', len(dic_data))
print('dic_data[3]:', dic_data[3]) # 3이라는 키로 접근
print('dic_data2[alice]:', dic_data2['alice'])
dic_data[7]="add"
print('dic_data추가:', dic_data) # dictionary 추가하는 방법

del dic_data2['tony'] # dict 삭제

# dictionary 읽기 쉽게 표현해주는 pprint 모듈
from pprint import pprint as pp
pp(dic_data)

# key값 print
for val in dic_data:
    print(val, end=', ') # end='' 을 써주면 한줄에 붙여 쓸수 있음.

# value값 print
for val2 in dic_data2.values():
    print(val2, end=', ') # end='' 을 써주면 한줄에 붙여 쓸수 있음.

# key-value값 한번에 print
for val3, val4 in dic_data.items():
    print('key:',val3,', ','value:',val4, end=', ') # end='' 을 써주면 한줄에 붙여 쓸수 있음.

# None null대신 , not
print("==== None 연습 ====")
val = None
print(val)
xy=10
print(not xy) # not = ! 와 같은 것

# 2. if 조건 :
print("==== if문 연습 ====")
listdata = ['a', 'b', 'c']
if 'a' in listdata:
    print('a가 listdata 안에 있습니다')
    print(listdata)
elif listdata == None:
    pass # 아무것도 하지 않음.
else:
    print('안에 없어')

# 3. for문
# for-elif-else문 for문이 모두 잘 실행됬을 때
print("==== For문 연습 ====")
range2 = range(1, 11)  # range 1이상 11미만
range3 = range(start=20, stop=1, step=-2)
for x in range2: # 1~10까지. 11은 포함 x
    if x<=5:
        print("case1:"+str(x), end=' ')
    elif x>5 and x<=9:
        print("case2:"+str(x), end=' ')
    else:
        print("case3:"+str(x), end=' ')

# while
print("==== While문 연습 ====")
x=0
while x<10:
    x=x+1
    if x<3:
        continue
    print(x)
    if x>7:
        break

# ex2
x2=1
total=0
while 1: # 1로도 무한루프 할 수 있음.
    print("x2는", x2 , "," , "total은", total)
    total=total+x2
    x2=x2+1 # python ++ -- 이런거 없음.
    
    if total>=30:
        break

# 4. list형 시퀀스형들 이해하기.
# list 형
# list에서 insert는 비용이 많이 든다. 모든걸 다 옮겨야 하기 때문에
print("==== list문 연습 ====")
listdata = [1, 2, 4, 1, [4, 5, 6]]
listdata5 = [7,2,8] + ['ss', 6, 'si'] # 리스트끼리 + 로 이어붙이기 가능
print('listdata:', listdata)
print('listdata[2]:', listdata[2]) # [4,5,6]
print('listdata[-1]:', listdata[-1])  # - 붙으면 끝에서 부터 몇번째

# reverse쓰는 두가지 방식. list.reverse / reversed(list)
listdata.reverse();
print('listdata.reverse():', listdata)  # list reverse - ((4,5,6),2,1)
print('reversed(listdata):', list(reversed(listdata)))  # list reversed 자료형을 리턴하면 (list)로 감싸서 list로 만듬 - (1,2,[4,5,6))

# 추가 append, insert, 인덱스 (index)
listdata.append(5); # ((4,5,6),2,1,5)
print('listdata.append(5):', listdata)  # list append
listdata.insert(2, 7); # 2번째 인덱스에 7꼽기.
print('listdata.insert(2,7):', listdata)
print('listdata.index(1):', listdata.index(1))  # 1이란 값을 가진 index찾기

# remove, del 지우기
listdata.remove(1); # 1번째 인덱스 지우기.
print('listdata.remove(1):', listdata)
del listdata[3] # 3번째 인덱스 지우기.
print('del listdata[3]:', listdata)
del listdata[1:3] # 1번째 인덱스 ~ 2번째 인덱스까지 지우기
print('del listdata[1:3]', listdata)  # del 범위 지우기 1번째 2번째 지워짐.
print('listdata.count([4,5,6]):', listdata.count([4, 5, 6]))  # listdata안에 값 갯수세기.

# sorted 정렬
listdata2 = [4, 7, 1, 10, 2, 5, 3]
print('\n내림차순 sorted(listdata2):', sorted(listdata2, reverse=True))  # 내림차순 정렬
print('오름차순 sorted(listdata2):', sorted(listdata2))  # 오름차순 정렬
print('sum(listdata2):', sum(listdata2))  # 리스트 합

# shuffle 랜덤 섞기.
from random import shuffle
shuffle(listdata2); # 리스트 랜덤섞기
print('\nshuffle(listdata2):', listdata2)  # list shuffle하기 from random import shuffle

print('리스트와 인덱스를 쌍으로 추출해보기')
print('enumerate(listdata2):', list(enumerate(listdata2)))  # 리스트를 인덱스와 쌍으로 추출하기 # {0,3}, {1,5}, {2,7}, {3,4}, {4,2} ...

print("==== all, any문 연습 ====")
# all , any
listdata3 = [0, 1, 2, 3, 4]
print('listdata3:', listdata3)
print('all(listdata3):', all(listdata3))  # false가 출력됨. 인자로 입력되는 리스트의 모든 요소가 참인지
print('any(listdata3):', any(listdata3))  # true가 출력됨. 인자로 입력되는 리스트중 하나라도 참인지

# 시퀀스 자료형 슬라이싱
print("==== 슬라이싱 연습 ====")
strdata="Time is Money"
print('strdata[:]:', strdata[:]) # Time is Money
print('strdata[5:]:', strdata[5:]) # is Money
print('strdata[:9]:', strdata[:9]) # Time is M
print('strdata[::2]:', strdata[::2]) # 홀수번째 슬라이싱하기 0번째부터(아무것도없으니까앞에) 2는 step이란개념 처음부터 끝까지 2씩 (1,3,5,7,9)
print('strdata[1::2]:', strdata[1::2]) # 짝수번째 슬라이싱하기 첫번쨰부터(맨앞에1) :: 다끝나고 step항목 2칸씩
print('strdata[:4]*3:', strdata[:4]*3)
print('strdata[-1]:', strdata[-1])  # 뒤에서 첫번째
print('strdata[3:7]:', strdata[3:7])  # 3번째부터 6번째 글짜
print('strdata[::-1]:', strdata[::-1])  # 문자열 거꾸로 출력하기 , 뒤에서부터 차례대로
# :: 은 ::다 끝나고, step항목 따로 생각 -1, 2
# 5. 사전 데이터형 이해하기 - 사전은 시퀀스형 아니다.
# list 2개를 dict로 zip함수
print("==== zip함수 연습 ====")
solar1 = ['태양', '수성', '금성', '지구', '화성', '목성', '토성', '천왕성', '해왕성']
solar2 = ['Sun', 'Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
solardict = dict(zip(solar1,solar2)) # 리스트 두개를 zip으로 합치기 dictionary형으로 만들기.
print('dict(zip(solar1, solar2)) -> solardict:', solardict)
print('solardict.items():', solardict.items())  # 사전에서 item 단위로 추출하기

print("==== enumerate함수 연습 ====")
# enumerate : 열거하다. 주로 for문에서 많이 씀.
print('enumerate를 이용해 인덱스와 쌍으로 출력하기')
for i, name in enumerate(solar1):  # i에 1,2,3 ~  이렇게 담기고, name에 태양, 수성, 금성 ~ 이렇게 담김.
    print("index: {}, name: {}".format(i, name))

# 키 or 값(value)에 대해서 정렬하기.
print("==== 딕셔너리 key, value에 대해 정렬하기 연습 ====")
print("f1 선언 or lambda 작성필요")
def f1(x): # key에 대해서 정렬.
    return x[0]
# 사전 Key별로, Value별로 오름차순 내림차순
print('key로 정렬:', sorted(solardict.items(), key=f1, reverse = True))  # key에 대해서 정렬하기
print('value로 정렬:', sorted(solardict.items(), key=(lambda x:x[1]))) # value에 대해서 정렬하기

# 6. import, 모듈, 패키지
""" 이미 만들어져 있고 안정성이 검증된 함수들을 파이썬 파일에 묶어놓은 걸 모듈이라고 함.
# 외부모듈에 있는 함수들을 활용시 이런 모듈들을 import 해야함.
# 추가로 내가 만든 파일을 my.py로 저장한다음에 import my 하면 내가 만들어논 함수들 사용 가능.
# 파이썬 모듈을 계층적인 디렉터리 형태로 구성한 것을 파이썬 패키지라고 함.
# 모든 경로를 다 표시해서 임포트하면 힘드니까 from ~ import로 임포트하여 사용 가능.
# from 모듈이름 import 함수이름   # from 패키지이름 import 모듈이름
# import 모듈이름                # import 패키지이름.모듈이름
# import 이름이 긴 모듈명 as 별명 # 이름이 긴 모듈에 대하여 간단히 별명을 붙이는 것"""

print("==== time연습 ====")
import time  # time 임포트에 sleep함수
print("1초간 프로그램을 정지합니다")
time.sleep(1)
print("1초가 지나갔습니다")

# 7. 함수 이해하기 def, lambda, map
# 값이 정해지지 않은 키워드 인자 가변인자의 경우
# def func(width, height, *args, **argv)
# args는 내부적으로 tuple처리 되고, argv는 내부적으로 dict 처리가 됨.
# map 은 인자를 바꾸어가며 함수를 반복호출하는 작업
print("==== 함수 이해하기 - def, lambda, map 연습 ====")
def add_num(n1, n2):  # def 함수이름(매개변수,매개변수) : 코드들  return값
    ret = n1 + n2
    return ret
print('add_num(3,4):', add_num(3, 4))

def reverse_method(x, y, z):  # 여러개의 리턴 값 함수.
    return z, y, x
print('reverse_method(1, 2, 3)->', reverse_method(1, 2, 3))

# 8. 수학함수들
# divmod(수1,수2) 몫과 나머지 입력받기.
print("==== 수학함수 이해하기 ====")
a, b = 12, 5
ret1, ret2 = divmod(a, b)
print('몫과 나머지 입력받기 divmod(a,b)사용')
print("a:{}, b:{}, 몫은:{}, 나머지:{}".format(a, b, ret1, ret2))

# abs() 절댓값
print('abs(-3):', abs(-3))

# round 반올림수
print('round(16.554):', round(16.554))  # 소숫점 첫째자리에서 반올림
print('round(1118, -1):', round(1118, -1))  # 1의 자리에서 반올림
print('round(16.554, 2):', round(16.554), 2)  # 소수점 2째자리에서 반올림

# 문자열로 된 식 실행하기 eval
print("eval('2+3')):", eval('2+3'))

# 예제 정수 리스트에서 소수만 걸러내기 (filter)
# filter함수는 특정 조건을 만족하는 값들만 편리하게 추출해주는 함수
# filter(함수, 반복 가능한 자료)
print("==== filter함수 연습 ====")
def getPrime(x):
    for i in range(2, x - 1):
        if x % i == 0: # 2부터 x-1 까지중 나누어 떨어지면 그 숫자는 소수 x
            break
    else: # 모든 if에 대해서 아닐 때. if i == x-1 와 같은 말
        return x
listdata4 = [6, 13, 51, 11113, 11119]
print('filter(getPrime, listdata4):', list(filter(getPrime, listdata4)))


# 이름없는 한줄짜리 함수 만들기 lambda
print("==== lambda 함수 - 이름없는 한줄 짜리 함수 ====")
add = lambda x, y: x + y  # lambda 인자, 인자 , .. : 실행코드
print('add = lambda x, y : x+y -> ', add(1, 3))  # 이름없는 한줄짜리 함수 만들기 (lambda)

# 인자를 바꾸어 함수를 반복 호출하여 결과값 얻기 map
# map(함수, list형태 = iterable형태)
fn = lambda x: x * x # 한줄짜리 lambda 함수 생성
# list형으로 꼭 묶어주어야 함.
print(list(map(fn, range(5)))) # map(f, args) => 모든요소를 f에 넣어서 map형식으로 반환

# 11. 문자열 활용하기
print("==== 문자열 활용 연습 ====")
print("a in apple", 'a' in 'apple')
txt1, txt2, txt3 = "A", "135P", " c b a "
text = "aefckhgsjdn fucking"
num1 = 100
print('txt1:{}, txt2:{}, txt3{}'.format(txt1,txt2,txt3))
print('txt1.isalpha():', txt1.isalpha())  # 문장이 알파벳인지 확인
print('txt1.issuper():', txt1.isupper())  # 문장이 대문자인지
print('txt1.islower():', txt1.islower())  # 문장이 소문자인지
print('txt2.isdigit():', txt2.isdigit())  # 문장이 숫자인지 확인
print('txt2.isalnum():', txt2.isalnum())  # 문장이 알파벳 또는 숫자인지 검사
print('txt3.lstrip():', txt3.lstrip())  # 왼쪽 공백 없애기
print('txt3.rstrip():', txt3.rstrip())  # 오른쪽 공백 없애기
print('txt3.strip():', txt3.strip())  # 좌우 공백 제거
print("replace:{}".format(txt2.replace('3', '6')))  # replace('문자1','문자2') 모든 문자1을 문자2로 바꿈

print('\ntext:',text)
print('text.count(e):' , text.count('e'))  # text문자열 안에 있는 e의 갯수 구하기
print('text.find(g):', text.find('g'))  # text문자열에서 알파벳 g찾기
print('text.find(f, 10):', text.find('f', 10))  # text문자열에서 알파벳 f찾는데 10번째 이후부터 찾기.

print("==== sorted, join, split 연습 ====")
# 문자열을 정렬할때 일반적으로 join과 sorted()함수를 같이 연결해서 사용함.
# sorted로 분리하고, join으로 합침.

sorted_txt = sorted(text)  # (1) 문자열 정렬 및 분리됨.
sorted_txt2 = '＊'.join(sorted_txt)  # (2) 정렬된 문자들 특정문자열로 합침 (join) ''는 합칠 때 사이에 넣을것들
print("sorted_txt:{}".format(sorted_txt))
print("정렬한 알파벳들 *넣고 합치기. '*'.join", sorted_txt2)

# 문자열을 특정 문자(열)로 분리하기(split)
url = 'http://www.naver.com/news/today=20160831'
log = 'name:홍길동 age:17 sex:남자 nation:조선'
print('url:', url)
print("url.split('/'): ", url.split('/'))

print('log:', log)
print('log split 2단 분리(공백, : )')
print("log.split(): ", log.split()) # 공백기준으로 나누기
data = log.split()
print(data, type(data))
for i, str in enumerate(data):
    d1, d2 = str.split(':')
    print(i,'번째 값:', d1, d2)

# 12. 클래스 이해하기
# self 는 이 클래스의 인스턴스 객체를 가르키는 참조자
print("==== 클래스 생성, 소멸 연습 ====")
class MyClass:
    var = "안녕하세요"
    def sayHello(self):
        print(self.var)  # "안녕하세요"가 출력됨

    def __init__(self):  # 생성자 def __init__(self, *args)
        print('MyClass 인스턴스 객체가 생성되었습니다')
    def __del__(self):  # 소멸자 def __init__(self, *args)
        print("MyClass 인스턴스 객체가 메모리에서 제거됩니다")

obj = MyClass()  # MyClass 인스턴스 객체 생성 ->
print('obj.var:', obj.var)  # 안녕하세요 출력 (클래스 멤버변수를 통한)
print('obj.sayHello()')
obj.sayHello() # 안녕하세요 출력 (클래스 메소드를 통한)
del obj  # MyClass 인스턴스 객체가 메모리에서 제거됩니다

print("==== 클래스 상속연습 ====")
# 상속
class Add:
    def add(self, n1, n2):
        return n1 + n2
class Multiply:
    def multiply(self, n1, n2):
        return n1 * n2
class Calculator(Add, Multiply):  # 다중상속 class 자식클래스(부모클래스)
    def __init__(self):
        print('상속 예제 클래스 생성완료')
    def sub(self, n1, n2):
        return n1 - n2
obj4 = Calculator() # 생성자 출력
print('obj4.add(1,2)', obj4.add(1, 2))  # 3이 출력됨
print('obj4.multiply(3,4)', obj4.multiply(3, 4))  # 12이 출력됨.
print('obj4.sub(1,2)', obj4.sub(1, 2))  # -1이 출력됨

# 14. 파이썬 기타 모듈
print("==== 파이썬 기타 모듈 연습 ====")
import sys
# sys모듈은 파이썬 인터프리터가 제공하는 변수들과 함수들을 직접 제어할 수 있게 해주는 모듈.
# sys.path // 파이썬 모듈들이 저장되어 있는 위치.이걸 통해이위치에 있는 파이썬 모듈을은 경로에 상관없이 어디에서나 불러 올 수 있음.
import os
print('# os모듈은 환경 변수나 디렉터리, 파일등의 OS 자원을 제어할 수 있게 해주는 모듈')
print('os.environ # 현재 시스템의 환경 변수값들 딕셔너리 형태로 리턴')
print("os.environ['PATH'] # PATH 형태로 받기.")
print('os.chdir("C:\Windows") # 디렉터리 위치 변경하기')
print('os.getcwd() # 디렉터리 위치 리턴받기')
print('os.system("dir") # 시스템 명령어 호출하기')

# time 모듈
import time

time.time() # 1970년 1월 1일 0시 0분 0초를 기준으로 초단위 리턴
time.localtime(time.time()) # 연도, 달, 월, 시, 분, 초의 형태로 바꿔줌.
time.struct_time(tm_year=2013, tm_mon=5, tm_mday=21, tm_hour=16, tm_min=48, tm_sec=42, tm_wday=1, tm_yday=141, tm_isdst=0)
time.asctime(time.localtime(time.time())) # 반환된 튜플 형태의 값을 인수로 받아서 날짜와 시간을 알아보기 쉬운 형태로 리턴
time.cime() # 현재시간만 리턴 asctime은 시간 조작가능.
time.sleep(3) # 3초 재우기

# calendar모듈
import calendar
print('#calendar 모듈')
print('calendar.calendar(2015) # 그 해의 전체달력보기.')
print('calendar.prmonth(2015, 12) # 12월 보기.')
print('calendar.weekday(2015, 12, 31) # 요일 리턴.월요일0 일요일6')
print('calendar.monthrange(2015, 12) # 입력받은 달의 1일이 무슨 요일인지와 그 달이 며칠까지 있는지를 튜플형태로 리턴')

import random
print('#random 모듈')
print('random.random() # 0.0과 1.0 사이의 실수중에서 난수값을 리턴.')
print('random.randint(1, 10) # 1과 10 사이의 정수중에서 난수값 리턴.')

# 웹 브라우져 모듈
import webbrowser
print('# webbrowser 모듈')
print('webbrowser.open("http://google.com") # 자신의 시스템에서 사용하는 기본 웹 브라우저가 자동으로 실행되게 하는 모듈')

# 피클모듈
import pickle
print('# pickle 모듈')
print('pickle은 객체의 형태 변형시키지 않고 그대로 유지하면서 파일에 저장하고 불러올 수 있게 하는 모듈.(막상 열어보면 이상하지만, 대화형 인터프리터나 에디터로 읽어보면 그 모습 그대로 읽힘을 알 수 있음.)')

print('Scipy - 과학기술계산', 'scikit-learning - 머신러닝용')
print('웹 - Flask , Django', '크롤링 - Beautiful Soap')
print('Folium - 지리적데이터시각화, Bokeh - 웹브라우저상시각화, matplotlib - 세련된플롯그래프')
print('Cython 2개 방법 - 파이썬 c/c++ 라이브러리 감싸기, 파이썬 코드를 c컴파일하여 최적화')