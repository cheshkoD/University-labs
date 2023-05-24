# Write a Python-script.
# There is a bus moving in the city, and it takes and drop some people in each bus stop.
# You are provided with a list (or array) of integer arrays (or tuples).
#   Each integer array has two items which represent number of people get into bus (The first item)
#       and number of people get off the bus (The second item) in a bus stop.
# Your task is to return number of people who are still in the bus after the last bus station (after the last array).
#   Even though it is the last bus stop, the bus is not empty and some people are still in the bus,
#       and they are probably sleeping there :D
#   Example:
#       number([[10,0],[3,5],[5,8]]) # Result is 5
#       number([[3,0],[9,1],[4,10],[12,2],[6,1],[7,10]]) # Result is 17
#       number([[3,0],[9,1],[4,8],[12,2],[6,1],[7,8]]) # Result is 21



#1
bus_array_1 = [(10,0), (3,5), (5,8)]
passengers_left_1 = sum([entered - left for entered, left in bus_array_1])
#2
bus_array_2 = ([[3,0],[9,1],[4,10],[12,2],[6,1],[7,10]])
passengers_left_2 = sum([entered - left for entered, left in bus_array_2])
#3
bus_array_3 = [[3,0],[9,1],[4,8],[12,2],[6,1],[7,8]]
passengers_left_3 = sum([entered - left for entered, left in bus_array_3])

print('Passengers left in 1st array: ',passengers_left_1)
print('Passengers left in 2nd array: ',passengers_left_2)
print('Passengers left in 3rd array: ',passengers_left_3)
