def fibonacci_sequence(limit):
    fib_seq = [0, 1]  # Inicia a sequência com 0 e 1
    while fib_seq[-1] < limit:
        next_value = fib_seq[-1] + fib_seq[-2]
        fib_seq.append(next_value)
    return fib_seq

def is_fibonacci_number(num):
    fib_seq = fibonacci_sequence(num)
    if num in fib_seq:
        return f"{fib_seq}\nO número {num} pertence à sequência de Fibonacci."
    else:
        return f"{fib_seq}\nO número {num} não pertence à sequência de Fibonacci."

# Exemplo de uso:
numero = int(input("Informe um número: "))
print(is_fibonacci_number(numero))

