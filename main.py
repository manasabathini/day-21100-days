print("Math Game!")

print("Name your multiples: ")

number_fact = int(input("Enter your number: "))
print()

counter = 0
for i in range(1,11):
  correct_answer = i * number_fact
  print(i, "X", number_fact)
  ans = int(input(">"))
  if ans == correct_answer:
    print("Great work!") 
    counter += 1
  else: 
    print("not right!", correct_answer)

if counter == 10:
  print("Awesome score! 🥳")
else:
  print("you got", counter, "out of 10 correct.")
