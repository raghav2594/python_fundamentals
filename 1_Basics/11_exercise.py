#Exercise-1: How to tell whether the given character is vowel or not?
vowel_string= 'aeiouAEIOU'
char = "w"
print(f"Given vowel {char} is vowel: {char in vowel_string}")
print("----------------")


#Exercise-2: I want to print all the alphabets from A to Z
import string
print(string.ascii_uppercase)
print("----------------")

#Exercise-3: How to tell whether the given character is cpnsonent?
#Any alphabets which are not a vowel
vowel_string= 'aeiouAEIOU'
#char = "1"
char = "w"
print(f"Given Character {char} is conconent: {char not in vowel_string and char.isalpha()}")
print("----------------")

#Exercise-4:"This is a great thing" -  this sentence should be printed in separate line
sentence = "This is a great thing"
#print(sentence.split(" "))
for sen in sentence.split():
    print(sen)

for i in range(1,10):
    print("A" * i)