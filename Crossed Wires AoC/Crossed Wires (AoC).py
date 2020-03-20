def path_finder(wire):
    '''
    This function finds the wires' path from the given commands
    and returns it in (x, y) format
    '''
    x, y = 0, 0
    path = [(0, 0)]
    for j in wire:
        direction = j[0]
        distance = int(j[1:])
        if direction == 'U':
            y += distance
        elif direction == 'D':
            y -= distance
        elif direction == 'R':
            x += distance
        elif direction == 'L':
            x -= distance
        else:
            print("Wrong direction!")
        path.append((x, y))
    
    return path

def closest_intersection(path_1, path_2):
    '''
    This function finds the closest intersection point and it's manhattan distance 
    '''
    inter = 0
    
    for i in range(len(path_1)-1):
        # here i'm comparing the current point with the point after it to see if the x value is staying the same
        # if it's staying the same this means that the line is moving in the y direction
        if path_1[i][0] == path_1[i+1][0]:
            res1 = 1
        # this code sees if the y value is staying the same
        # if the y value is staying the same this means that the line is moving in the x direction
        else:
            res1 = 0
        for j in range(len(path_2)-1):
            # here I'm doing the same as the previous one but this time on the second wire
            if path_2[j][0] == path_2[j+1][0]:
                res2 = 1
            else:
                res2 = 0
            # To see whether the two lines intersect they shouldn't be parrallel so I'm ignoring the lines with the same axis staying the same
            if res1 == res2:
                continue
            else:
                if (path_1[i] and path_2[j]) != (0, 0):
                    if res1:
                        # this compares the fixed value from the first line with the moving value from the second line 
                        if min(path_2[j][0], path_2[j+1][0]) <= path_1[i][0] <= max(path_2[j][0], path_2[j+1][0]) and min(path_1[i][1], path_1[i+1][1]) <= path_2[j][1] <= max(path_1[i][1], path_1[i+1][1]):
                            # this calculates the distance from the nearest intersection to the start point
                            if inter == 0 or sum((abs(path_1[i][0]), abs(path_2[j][1]))) < inter:
                                inter = sum((abs(path_1[i][0]), abs(path_2[j][1])))
                    # this is the same as above but this works if the first lines' y value is fixed   
                    else:
                        if min(path_2[j][1], path_2[j+1][1]) <= path_1[i][1] <= max(path_2[j][1], path_2[j+1][1]) and min(path_1[i][0], path_1[i+1][0]) <= path_2[j][0] <= max(path_1[i][0], path_1[i+1][0]):
                            if inter == 0 or sum((abs(path_2[j][0]), abs(path_1[i][1]))) < inter:
                                inter = sum((abs(path_2[j][0]), abs(path_1[i][1])))
  
                                                            
    return inter 


wires_file = open('Crossed Wires.txt', 'r')
wire_1 = wires_file.readline().split(',')
wire_2 = wires_file.readline().split(',')

print(closest_intersection(path_finder(wire_1), path_finder(wire_2)))

wires_file.close()

