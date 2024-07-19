number = 23
values=[21,46,97,32,54,9]
def find_value(list,number):
    for i in range(len(list)):
        if list[i] == number:
            print("it was found at position " + str(i+1))
            return
    print("not found")       

find_value(values,number)

values.append(23)

find_value(values,number)