def print_squares_of_numbers_upto(n):
    for i in range(1,n+1):
        print(i*i)


def print_squares_of_even_numbers_upto(n):
    for i in range(2,n+1,2):
        print(i*i)

def print_numbers_in_reverse(n):
    for i in range(n,0,-1):
        print(i)

# print_squares_of_numbers_upto(10)
# print_squares_of_even_numbers_upto(10)
# print_numbers_in_reverse(10)


#Returning values from method
def sum_of_two_values(n1,n2):
    sum = n1 + n2
    return sum  # if return key word is not used by default it returns as None class

print(f"Sum value is : {sum_of_two_values(1,2)}")
