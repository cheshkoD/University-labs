# Write a script which will take an array of strings and returns an array of strings
#   with the needless directions removed (W<->E or S<->N side by side).

map = [ "NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST" ]
opposites = { "NORTH": "SOUTH", "SOUTH": "NORTH", "EAST": "WEST", "WEST": "EAST" }

def createmap(list):
    new_list = [ ]
    for i in range(0,len(list)):
        if len(new_list) == 0:
            new_list.append(list[i])
        elif new_list[-1] != opposites[list[i]]:
            new_list.append(list[i])
        else:
            new_list.pop()
    return new_list
new_map = createmap(map)
print('Final map is: ', new_map)
