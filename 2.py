def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def primes_till_n(n):
    primes = []
    for i in range(2, n + 1):
        if is_prime(i):
            primes.append(i)
    return primes

def first_n_primes(n):
    primes = []
    num = 2
    while len(primes) < n:
        if is_prime(num):
            primes.append(num)
        num += 1
    return primes

def main():
    try:
        n = int(input("Enter a number n: "))

        # a. Check if n is prime
        if is_prime(n):
            print(f"{n} is a prime number.")
        else:
            print(f"{n} is not a prime number.")

        # b. Generate all prime numbers till n
        print(f"Prime numbers up to {n}:")
        print(primes_till_n(n))

        # c. Generate first n prime numbers
        print(f"First {n} prime numbers:")
        print(first_n_primes(n))

    except ValueError:
        print("Please enter a valid integer.")

if __name__ == "__main__":
    main()
