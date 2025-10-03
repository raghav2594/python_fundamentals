#Overloading Methods are not possible in python.
def print_multiplication_table(table=5,start=1,end=10):  #default values added in python to simplyfy the overloading method in java
    for i in range(start,end+1):
        print(f"{table} X {i} = {table*i}")  #this is the format printing

print_multiplication_table(6,1,5)

print_multiplication_table(7,1,10)
