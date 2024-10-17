#!/usr/bin/python3
def minOperations(n):
    if n <= 1:
        return 0
    
    operations = 0
    divisor = 2
    
    # Loop to factorize n by trying divisors starting from 2
    while n > 1:
        # While the current divisor divides n
        while n % divisor == 0:
            # Add the divisor to operations
            operations += divisor
            # Reduce n by dividing it by the current divisor
            n //= divisor
        # Move to the next divisor
        divisor += 1
    
    return operations
