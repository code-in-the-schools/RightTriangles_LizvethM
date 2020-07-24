#UserInput
char= input("Enter a character: ")
num = int(input("Enter a numer: "))
#triangle 1text
for i in range(1, num+1):
  text=""
  for j in range (i):
    text+= char

  print(text)

print()

for i in range (len(char)):
  for j in range (int(num)):
    print(char*num)
    num= num- 1

  print()

#working on third triangle
#for i in range(0,num):
  for j in range(0,char):
    print(