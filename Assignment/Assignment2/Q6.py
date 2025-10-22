def process_dict(data):
    def is_prime(n):
        if n < 2: return False
        for i in range(2, int(n**0.5)+1):
            if n % i == 0: return False
        return True

    new_data = {}
    for key, value in data.items():
        if isinstance(value, list):
            new_data[key] = sum([x for x in value if is_prime(x)])
        elif isinstance(value, tuple):
            prod = 1
            for x in value:
                if x % 2 == 1: prod *= x
            new_data[key] = prod
    return new_data

data = {"A":[2,3,4,5,10],"B":(1,2,3,4,5),"C":[7,8,9],"D":(6,7,8)}
print(process_dict(data))
