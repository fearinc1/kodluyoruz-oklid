import math

points = [(2, 3), (5, 8)]

def euclideanDistance(point1, point2):    
    if len(point1) != len(point2):
        raise ValueError("Points must have the same dimensionality.")
    
    squared_sum = sum((p1 - p2) ** 2 for p1, p2 in zip(point1, point2))
    return math.sqrt(squared_sum)

distances = []

for x in range(len(points)):
    if len(points) <= x + 1:
        break
    
    distances.append(euclideanDistance(points[x], points[x + 1]))

print(min(distances))