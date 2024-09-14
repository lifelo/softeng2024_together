def is_primes(n:int) -> bool:
    if n < 2:
        return False
    for i in range(2,n):
        if n % i == 0:
            return False
        break
    return True


def main():
    primes = []
    for i in range(2,51):
        if is_primes(i):
            primes.append(i)
    print(primes)

    print([i for i in range(2,51)])

if __name__ == "__main__":
    main()