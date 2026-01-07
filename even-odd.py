
#def cal_sum(a, b):
   # sum = a + b
    #print( sum)
   # return sum


#cal_sum(3, 5)
#cal_sum(9, 5)



#cities = ("New York", "Los Angeles", "Chicago", "Houston", "Phoenix")
#departments = ["HR", "Finance", "IT", "Marketing", "Sales"]

#def print_len(list):
   # print(len(list))


    #print_len(cities)
    #print_len(departments)


def check_even_odd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"

while True:
    number = int(input("Enter a number (0 to quit): "))
    if number == 0:
        print("Exiting...")
        break
    result = check_even_odd(number)
    print("The number is", result)

