import math

def classify_numbers(numbers):
    result = {
        "Prime": [],
        "Composite": [],
        "PerfectSquares": [],
        "PerfectCubes": []
    }
    
    def is_prime(n):
        if n < 2: return False
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0: return False
        return True
    
    for num in numbers:
        # Prime or Composite
        if is_prime(num):
            result["Prime"].append(num)
        elif num > 1:
            result["Composite"].append(num)
        
        # Perfect square
        if int(num**0.5) ** 2 == num:
            result["PerfectSquares"].append(num)
        
        # Perfect cube
        if round(num ** (1/3)) ** 3 == num:
            result["PerfectCubes"].append(num)
    
    return result


numbers = [2,4,8,9,27,28]
print(classify_numbers(numbers))
