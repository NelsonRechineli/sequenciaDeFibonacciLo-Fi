n = int(input("Digite um Número para a Série de Números de Fibonacci:     "))

def fib(n):    # escreve serie de fibonaci até n
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()
fib(n)
