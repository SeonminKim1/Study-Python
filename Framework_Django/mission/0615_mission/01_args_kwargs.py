# 가변인자 args
def test_args(a, b, *args):
    print(a, b)
    print(type(args), args) # 전부 Tuple로 묶여서 들어옴.

# 가변 인자 kwargs
def test_kwargs(a,b, **kwargs):
    print(a,b)
    print(type(kwargs), kwargs) # Dictionary {k:v} 형태로 들어옴.
    print(kwargs['case1'])
    print(kwargs['case2'])

test_args(1,3,[1,2,3],(4,5,6), {'a':1,'b':2,'c':3})
test_kwargs(2, 4, case1={'b':'c','a':'b','c':'a'}, case2={'d':'e','e':'f','f':'e'})
