class Rectangle:
  
  def __init__(self, width, height):
    #print(" __init__(self, width, height)")
    self.width = width
    self.height = height
    
  def set_width(self, width):
    #print("set_width(self, width)")
    self.width = width

  def set_height(self, height):
    #print("set_height(self, height)")
    self.height = height

  def get_area(self):
    #print("get_area(self)")
    return self.width * self.height

  def get_perimeter(self):
    #print("get_perimeter(self)")
    return ((2 * self.width) + (2 * self.height))

  def get_diagonal(self):
    #print("get_diagonal(self)")
    return ((self.width ** 2 + self.height ** 2) ** 0.5)

  def get_picture(self):
    print("get_picture(self)")
    if self.width <= 50 and self.height <= 50:
      print("self.width:", self.width, "self.height:", self.height)
      picture_lines = ""
      for i in range(self.height):
        picture_lines += ('*'*self.width) + '\n'
      return picture_lines
    return "Too big for picture."

  def get_amount_inside(self, other_shape):
    #print("get_amount_inside(self, other_shape)")
    amount = 0
    remaining_width = self.width
    remaining_height = self.height
    while remaining_width >= other_shape.width and remaining_height >= other_shape.height:
      amount += 1
      remaining_width -= other_shape.width

      # If we're done with our row, then reset the x-axis and move down the y-axis
      if remaining_width < other_shape.width:
        remaining_width = self.width
        remaining_height -= other_shape.height
    return amount

  def __str__(self):
    #print("__str__(self)")
    return "Rectangle(width=" + str(self.width) + ", height=" + str(self.height) + ")"

class Square(Rectangle):
  
  def __init__(self, side):
    #print("__init__(self, side)")
    self.width = side
    self.height = side

  def set_side(self, side):
    #print("set_side(self, side)")
    self.width = side
    self.height = side

  def set_width(self, width):
    #print("set_width(self, width)")
    self.set_side(width)

  def set_height(self, height):
    #print("set_height(self, height)")
    self.set_side(height)

  def __str__(self):
    #print("__str__(self)")
    return "Square(side=" + str(self.width) + ")"
