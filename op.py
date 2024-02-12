# #object-oriented programming
#
# class Fruits:              #The class should start with capital letters
#     def __init__(self):
#         self.name = "apple"
#         self.color = "red"
#
#
# fruits = Fruits()
# fruits.name = "Plum"
# print(fruits.name)


class Fruits :
    def __init__(self, name, color):
        self.name = name
        self.color = color

fruits1 = Fruits('apple', 'red')   #you can also use name= and color= in place of the hints
fruits2 = Fruits("orange", "orange")
print(f"My favourite fruit is {fruits1.name} ")