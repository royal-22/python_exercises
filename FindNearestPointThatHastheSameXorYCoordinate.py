def nearestValidPoint(x: int, y: int, points: list) -> int:
    valid_points = []
    res = []
    for point in points: 
        if point[0] == x or point[1] == y:
            valid_points.append(point)
    if not valid_points:
        return -1
    for i in range(len(valid_points)):
        res.append((abs(valid_points[i][0]-x) + abs(valid_points[i][1]-y), points.index(valid_points[i]))) # saves the distances and the index from the points in the original "points" list as a tuple
    print(res)
    res.sort()
    print(res)
    return res[0][1]
print(nearestValidPoint(x = 1, y = 1, points = [[1,1],[1,1]]))

# implementation example 
lis = []
points = [2, 3, 4, 5, 0, 1, 6, 7, 8, 9]
for i in range(10):
    lis.append(((i), points.index(i)))
print(lis)

"""class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        
        if len(points) == 1:
            [x2,y2] = points[0]
            if x == x2 and y == y2:
                return 0
            
        valid_points = {}
        
        for index in range(len(points)):
            [xi, yi] = points[index]
            if xi == x or yi == y:
                valid_points[index] = points[index]

        if len(valid_points) == 0:
            return -1
        
        # index and distance
        min_man = [-1, float('inf')]
        
        for index in valid_points:
            [x2, y2] = valid_points[index]
            manhattan_distance = abs(x - x2) + abs(y - y2)
            point = [index, manhattan_distance]
            if min_man[1] > point[1]:
                min_man = point
        return min_man[0]
        
        
        # Time O(N + N) => O(n)
        # Space O(len(points))
"""
