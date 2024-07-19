#Name: Shaad Patankar
#Email: shaad.patankar73@myhunter.cuny.edu
#Date: Sepetember 7, 2023
#This program creates a cipher!

alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
word = list(input(""))
answer = ""
for letter in word:
    reg_num = alphabet.index(letter)
    if reg_num >= 12:
        answer += alphabet[reg_num - 13]
    else:
        answer += alphabet[reg_num + 13]
print(answer)

