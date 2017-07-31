def isPrime(n):
    if 0 <= n <= 2:
        return True
    i = 2
    imax = n ** 0.5
    while i <= imax:
        if n % i == 0:
            return False
        i += 1
    return True


n = int(input())

if isPrime(n):
    print("Yes")
else:
    print("No")
