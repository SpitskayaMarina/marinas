try:
    uskoreniye(3,2,4)
exept ZeroDivisionError:
    print('Нельзя делить на 0')
exept ValueError:
    print('все значения должны быть числами')
def rasstoyaniye(uskoreniye):
    def wrapper(v1,v2,t):
        uskoreniye(v1,v2,t)
        s=(v2-v1)*t
        print('s=',s)
    return wrapper
@rasstoyaniye
def uskoreniye(v1,v2,t):
    a=(v1-v2)/t
    print('a=',a)
uskoreniye(3,2,4)
