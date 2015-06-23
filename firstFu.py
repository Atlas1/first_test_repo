
def foo (name, surname, job):
    s = ' '
    return name + s + surname + ':' + s + job

'''print foo('Mr', 'Andrea', 'Job')'''

def power(a, b):
    return a**b

def fwrite(file, L):
    channel = open(file, 'w')
    for i in L:
        channel.write(i + '\n')
    channel.close()

'''fwrite( 'intro',  ['Hi', 'my name...', ' and I am a farmer'])'''

def fib(n):
series up to n
    a, b, f = 0, 1, 0
    print a
    print b
    while b <= n :
        f = a + b
        '''...'''
        
