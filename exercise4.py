math =int(input ("Math: "))
english = int(input ("English: "))
kiswahili = int(input ("Kiswahili: "))
science =int(input ("Science: "))
total = math+english+kiswahili+science
average = total/4

# if math or english or kiswahili or science > 100:
#     print("Invalid Input A")
#
# elif math or english or kiswahili or science < 0:
#     print("Invalid Input B")

if average > 70:
    print("Your score is A")

elif average > 60 < 71:
    print("Your score is B")

elif average > 50 < 61:
    print("Your average is C")

elif average > 40 < 51:
    print("Your score is D")

elif average < 40:
    print("Your score is E")