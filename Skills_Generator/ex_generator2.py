def test1():
    print('print 1')
    yield 1
    print('print 2')
    yield 2

def test2():
    for i in range(10):
        yield i * 2

if __name__ == "__main__":	
    # case 1
    gen1 = test1()
    print(type(gen1)) # class 'generator'
    print('=== ', next(gen1))
    print('=== ', next(gen1))
    print()

    # case 2
    gen2 = test2()
    print(type(gen2)) # class 'generator'
    for _ in range(10+1):
        print(next(gen2), end = ' ') # stop iteration 에러 발생
