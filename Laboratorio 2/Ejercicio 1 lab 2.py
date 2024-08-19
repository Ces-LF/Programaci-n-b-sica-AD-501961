def max_in_list(numbers):
    max=numbers[0]
    for n in numbers:
        if n>max:
            max=n
    return max
list=[1,9,500,300,0.5,10500,200000000000]
print(max_in_list(list))
