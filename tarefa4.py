def a(n):
    j = 1
    for i in range(1,n):
        j+=2

    return j

print("Resultado da A: ",a(5))

def b(n):
    j = 2
    for i in range(1,n):
        j*=2

    return j

print("Resultado da B: ",b(7))

def c(n):
    j = 0
    for i in range(n):
       j=i**2
    return j

print("Resultado da C: ", c(9))

def d(n):
    return 4*(n*n)

print("Resultado da D: ", d(5))

def e(n):
    a, b = 1, 1
    for _ in range(2, n):
        a, b = b, a + b
    return b

print("Resultado da E: ", e(7))

# A F eu não encontrei um padrão, ou não entendi.
