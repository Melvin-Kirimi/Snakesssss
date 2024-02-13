class People :
    def james(self):
        print("Can walk")

    def tom(self):
        print("Speaks English")



# kk = People()
# print(kk.james())



class Parrot(People):             #links two classes : parent class and child class
    def conor(self):
        print("Parrot can walk")


yy = Parrot()
print(yy.james())