for i in range(1,10):
    print(i)
print("Done")

for i in range(1,10):
    print(i * i)

for ch in "Hello World":
    print(ch)

for word in "Hello World".split():
    print(word)

# Excercises
# Write a function to sum upto n

def sumUptoN(number):
   sum = 0
   for i in range(1,number+1):
       sum = sum + i
   return sum

print(sumUptoN(5))

#Write a function to printNumberTriangle
def triangleNumber(number):
    for i in range(1,number+1):
        for j in range(1, i+1):
            print(f'{j} ')
        print()

triangleNumber(5)
