import math

# The function print_cuboid_area() takes 3 parameters(length, width, and height)
# Then it compute and print the area of a cuboid
def print_cuboid_area(length, width, height):
     area = (2 * ((length * height) + (length * width) + (height * width)))
     print('The area is ' + str(area))


# The function print_triangle_area() takes 2 parameters(height and base)
# Then it compute and print the area of a triangle
def print_triangle_area(height, base):
     area = float( (height * base)/2)
     print('The area is ' + str(area))


# pad_spaces_string() takes two argument: a string and number of the spaces(spaces)
# The funtion pad the string on the left with the given number of space
# characters and print the result
def pad_spaces_string(string ,num_of_space):
    print((" " * num_of_space) + string)


# This funtion takes a year (an integer), month (an integer 1-12) and day (an integer 1-30)
# It computes and prints the approximate number of seconds that have passed between that day
# and the due date of the assignment
def compute_seconds(year, month, day):
    DUE_DATE_YEAR = 2023
    DUE_DATE_MONTH = 2
    DUE_DATE_DAY = 19

    SECS_IN_DAY = (60 ** 2) * 24;

    # calculate the number of days between the two dates
    due_date_days = 365 * DUE_DATE_YEAR + DUE_DATE_MONTH * 30 + DUE_DATE_DAY
    given_date_days = 365 * year + month * 30 + day
    days_difference = due_date_days - given_date_days

    passed_seconds = str(days_difference * SECS_IN_DAY)
    print('The approximate number of seconds that have passed between two dates is ' + passed_seconds)



# This function accepts 4 parameters, for the two (x, y) coordinates
# It compute and print the Euclidean distance between the two coordinates
def print_euclidean_distance(x1, y1, x2, y2):
    compute1 = (x2 - x1)** 2
    compute2 = (y2 - y1)** 2
    distance =  str(math.sqrt(compute1 + compute2))
    print('The Euclidean distance between the two point is '+ distance)




print('Computing the area of a cuboid.')
length = float(input('Length? ')) # Get the the input form the user
width = float(input('Width? '))
height = float(input('Height? '))
print_cuboid_area(length, width, height) # call the funtion print_cuboid_area() to print results


print('\n')
print('Computing the area of a triangle.')
height = 23
base = 30
print('height: ' + str(height))
print('base: ' + str(base))
print_triangle_area(height, base) # calling the funtion print_triangle_area()


print('\n')
print('Add the given number of spaces (n) before the string and print results.')
string = "Python is fun!"
num_of_space = 5
print(string)
print(num_of_space)
pad_spaces_string(string ,num_of_space) # calling the funtion pad_spaces_string()


print('\n')
print('Computing number of seconds that have passed between given date and the due date of the assignment.')
print('Given Date: September 06, 2022')
print('Due Date: February 19, 2023')
compute_seconds(2022, 9, 6)  # calling the funtion compute_seconds()


print('\n')
print('Computing the Euclidean distance between the two coordinates (x,y).')
print('Point 1: (2, 5)')
print('Point 2: (3, 8)')
print_euclidean_distance(2, 5, 3, 8) # calling the funtion print_euclidean_distance()

