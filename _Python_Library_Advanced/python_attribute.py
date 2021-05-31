
class myclass():
    def __init__(self):
        self.a = 'A'
    def print(self):
        print('this is method')

if __name__ == "__main__":

    # case 1. 일반적인 속성접근자를 사용한 접근 방법
    t = myclass()
    print(t.a)

    # case 2. getattr() 함수를 이용해 접근
    print(getattr(t, 'a')) # 멤버변수
    getattr(t,'print')() # 멤버함수

    # case 3. hasattr
    print(hasattr(t, 'a')) # 멤버변수 존재 여부
    print(hasattr(t, 'print')) # 멤버함수 존재여부

    # case 4. setattr
    setattr(t, 'a', 5) # 멤버 변수 설정
    print(t.a)