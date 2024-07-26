numbers = [3,2,9,5,6,1,3,0,4,8]

for o in range(len(numbers)-1):
    print("pass "+ str(o+1))
    swapped = False
    for i in range(len(numbers)-1):
        if numbers[i] > numbers[i+1]:
            temp = numbers[i]
            numbers[i] = numbers[i+1]
            numbers[i+1] = temp
            swapped = True
    print(numbers)
    if swapped == False:
        break