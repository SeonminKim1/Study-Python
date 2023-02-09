# Generator 생성
def ex_func1(nums):
    for i in nums:
        yield i * i

if __name__ =="__main__":
    generator_ex = ex_func1([1,2,3])
    print(next(generator_ex)) # 1
    print(next(generator_ex)) # 4
    print(next(generator_ex)) # 9
    print(next(generator_ex)) # 더 반환할 값이 없으면 StopIteration 발생