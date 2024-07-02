import turtle

# Base class for all shapes
class Shape:
    def __init__(self, name):
        # Initialize the shape with a name
        self.name = name
    
    def draw(self, turtle_obj):
        # Method to draw the shape, to be implemented by subclasses
        raise NotImplementedError("You should implement this method in subclasses")

# Circle class inheriting from Shape
class Circle(Shape):
    def __init__(self, radius):
        # Initialize the Circle with a radius
        super().__init__("Circle")
        self.radius = radius
    
    def draw(self, turtle_obj):
        # Use the turtle object to draw a circle
        turtle_obj.circle(self.radius)

# Rectangle class inheriting from Shape
class Rectangle(Shape):
    def __init__(self, width, height):
        # Initialize the Rectangle with width and height
        super().__init__("Rectangle")
        self.width = width
        self.height = height
    
    def draw(self, turtle_obj):
        # Use the turtle object to draw a rectangle
        for _ in range(2):
            turtle_obj.forward(self.width)
            turtle_obj.left(90)
            turtle_obj.forward(self.height)
            turtle_obj.left(90)

# Triangle class inheriting from Shape
class Triangle(Shape):
    def __init__(self, side_length):
        # Initialize the Triangle with a side length
        super().__init__("Triangle")
        self.side_length = side_length
    
    def draw(self, turtle_obj):
        # Use the turtle object to draw an equilateral triangle
        for _ in range(3):
            turtle_obj.forward(self.side_length)
            turtle_obj.left(120)

# Function to test drawing shapes
def test_shapes():
    # Set up the turtle graphics window
    screen = turtle.Screen()
    screen.setup(width=800, height=600)
    turtle_obj = turtle.Turtle()
    
    # List of shapes to draw
    shapes = [
        Circle(radius=50),
        Rectangle(width=100, height=50),
        Triangle(side_length=100)
    ]
    
    # Draw each shape in the list
    for shape in shapes:
        shape.draw(turtle_obj)
        turtle_obj.penup()  # Lift the pen to move without drawing
        turtle_obj.forward(150)  # Move the turtle to the right
        turtle_obj.pendown()  # Lower the pen to resume drawing
    
    # Keep the window open until it is closed by the user
    screen.mainloop()

# Call the test_shapes function to draw the shapes
test_shapes()
