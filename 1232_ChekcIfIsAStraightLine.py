coor = [[1,-8],[2,-3],[1,2]]
def CheckStraightLine(coordinates)->bool: 
    (x0,y0),(x1,y1)=coordinates[:2]
    for i in range(2,len(coordinates)):
        (x,y)=coordinates[i]
        if (y1-y0)*(x-x1)!=(x1-x0)*(y-y1):return False
    return True

print(CheckStraightLine(coordinates=coor))

"""if (coordinates[i+1][0] - coordinates[i][0] <= 1 and coordinates[i+1][0] - coordinates[i][0] >= -1) and (coordinates[i+1][1] - coordinates[i][1] <= 1 and coordinates[i+1][1] - coordinates[i][1] >= -1)"""