
#getting numbers counts and sums
sum = 0
count = 0
number = int(input("Enter a number: "))

#so that i can count number of entry points and add each entry point to each other
while number != -1:
    sum += number
    count += 1
    number = int(input("Enter a number: ")) 
#incase 0 is entered and not give unaccuate average when doing to calcualtion
if count == 0:
    print("No numbers entered.")
#calculating average
else:
    average = sum / count
    print("Average:", average)