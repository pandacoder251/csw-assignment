#list
a_list = [1, 2, 3, 4, 5]
print("a_list:", a_list)
b_list = a_list
print("b_list:", b_list)
a_list.append(5)
a_list.append(6)
print("After appending elements to a_list:" , a_list)
print("b_list remains unchanged:" , b_list)
b_list = a_list[:]

#deepcopy
import copy
c_list = copy.deepcopy(a_list)
a_list.append(7)
print("After appending 7 to a_list:" , a_list)
print("b_list remains unchanged:" , b_list)

#list-slicing
list1 = [10, 20, 30, 40, 50]
print("Original list:", list1)
print(list1[1:4])
print(list1[:3])
print(list1[2:])
print(list1[::2])
print(list1[4:1:-1])

#list-methods
a_list = ['A' , 'B' , 'C' , 'D' , 'E']
for i in a_list:
    print(i, end=' ')
    print(max(a_list))
    print(min(a_list))
    print(a_list.count('C'))
    print(a_list.index('D'))
    print(sorted(a_list))
    print(list(reversed(a_list)))
    print(a_list.extend(['F' , 'G']))
    print(a_list.clear())
    print(a_list.remove('D'))
    print(a_list.pop())
    print(a_list.insert(2 , 'Z'))
    print("length of a_list:", len(a_list))
for i , value in enumerate(a_list):
    print("Index:", i, "Value:", value)
    print(a_list , start = 5)


