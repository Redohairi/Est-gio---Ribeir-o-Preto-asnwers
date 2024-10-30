def fibonacci_sequence(n):
    fib_sequence = [0, 1]
    
    # Gera a sequência de Fibonacci até o número n
    while True:
        next_value = fib_sequence[-1] + fib_sequence[-2]
        if next_value > n:
            break
        fib_sequence.append(next_value)
    
    return fib_sequence

def main():
    # Lista de números de teste
    test_numbers = [0, 1, 2, 3, 4, 5, 6, 8, 13, 21, 34, 55, 89, 144, 233, 300, 400]
    
    for number in test_numbers:
        # Calcula a sequência de Fibonacci até o número atual
        fib_sequence = fibonacci_sequence(number)

        # Verifica se o número pertence à sequência
        if number in fib_sequence:
            print(f"O número {number} pertence à sequência de Fibonacci.")
        else:
            print(f"O número {number} não pertence à sequência de Fibonacci.")

if __name__ == "__main__":
    main()
