#numbers = [3,2,9,7,5,6,1,3,0,4,8]
numbers = ["hi","hello","hey"]

for i in range(len(numbers)):
    key = numbers[i]
    j = i-1
    while key < numbers[j] and j >= 0:
        numbers[j+1] = numbers[j]
        j = j-1
    numbers[j+1] = key

    print(numbers)