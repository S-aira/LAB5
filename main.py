# main.py

# Importing classes from shapes.py and data_structures.py
from shapes import Rectangle, Circle
from data_structures import DataProcessor

def print_details(shape):
    """
    Print the area and perimeter of a Shape object.
    
    Args:
    - shape: A Shape object.
    """
    print("Area:", shape.area())
    print("Perimeter:", shape.perimeter())

def main():
    # Creating instances of classes
    rectangle = Rectangle(4, 5)
    circle = Circle(3)
    data_processor = DataProcessor()
    
    # Demonstrating polymorphism
    shapes = [rectangle, circle]
    for shape in shapes:
        print("Area:", shape.area())
        print("Perimeter:", shape.perimeter())
        print()

        print(rectangle)
       print(circle)

    # Instantiating objects of Rectangle and Circle
    rectangle = Rectangle(4, 5)
    circle = Circle(3)
    
    # Print details of the Rectangle
    print("Details of Rectangle:")
    print_details(rectangle)
    
    # Print details of the Circle
    print("\nDetails of Circle:")
    print_details(circle)
    
    # Demonstrating abstraction
    data_processor.demonstrate_list_operations()
    data_processor.demonstrate_tuple_operations()
    data_processor.demonstrate_dictionary_operations()
    data_processor.demonstrate_set_operations()
    # Importing DataProcessor class from data_structures.py
    
    # Demonstrate operations on various data structures
    print("Demonstrating operations on lists:")
    data_processor.demonstrate_list_operations()
    
    print("\nDemonstrating operations on tuples:")
    data_processor.demonstrate_tuple_operations()
    
    print("\nDemonstrating operations on dictionaries:")
    data_processor.demonstrate_dictionary_operations()
    
    print("\nDemonstrating operations on sets:")
    data_processor.demonstrate_set_operations()

if _name_ == "_main_":
    main()

