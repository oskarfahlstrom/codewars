from collections import deque

MOD = 10**9 + 7 

def digitwise_addition(n, k):
    digits = deque([0] * 10)
    for digit in str(n):
        digits[int(digit)] += 1
    for _ in range(k):
        digits.rotate()
        digits[1] += digits[0]
            
    return sum(digits) % MOD

if __name__ == "__main__":
    assert digitwise_addition(257538455, 16) == 33