# class Flower:
#   def __init__(self, kind, color):
#    self.kind = kind
#    self.color = color

#   def display_color(self):
#     print(self.color)

#   def display_kind(self):
#      print(self.kind)


# rose_flower = Flower("rose", "red")
# rose_flower.display_color()
# rose_flower.display_kind()

# blue_flower = Flower("tulips" ,"blue")
# print(blue_flower.kind)
# #print(f"{blue_flower.kind}  {blue_flower.color}")


class Virtual_Pet:
  color = "brown"
  legs = 4

  def bark(self):
    print("Bark")

  def display_color(self):
    print(self.color)

  def display_legs(self):
    print(self.legs)

rocky = Virtual_Pet()
rocky.display_color()       
rocky.display_legs()
rocky.bark()
