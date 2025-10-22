# Input list with duplicates
numbers = [4,2,7,4,2,4,9,7,9,9]

# a) Remove duplicates using set comprehension
unique_numbers = {x for x in numbers}
print("Unique numbers:", unique_numbers)

# b) Frequency dictionary using dictionary comprehension
freq_dict = {x: numbers.count(x) for x in unique_numbers}
print("Frequency dictionary:", freq_dict)

# c) Sort numbers by descending frequency using lambda
sorted_by_freq = sorted(freq_dict.keys(), key=lambda x: freq_dict[x], reverse=True)
print("Numbers sorted by descending frequency:", sorted_by_freq)
