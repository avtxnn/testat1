# Aufgabe 2

def get_primenumbers(n):
    primes = []
    for num in range(2, n):
        is_prime = True
        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    return primes


def main():
    num = 7
    print(f"prime numbers in range 0 to {num}: {get_primenumbers(num)}")

    num = 19
    print(f"prime numbers in range 0 to {num}: {get_primenumbers(num)}")

    num = 37
    print(f"prime numbers in range 0 to {num}: {get_primenumbers(num)}")


if __name__ == "__main__":
    main()
    
    #ccec