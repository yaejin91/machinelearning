def manhattan_distance(pt1, pt2):
    distance = 0
    for dimension in range(len(pt1)):
        distance += abs(pt1[dimension] - pt2[dimension])
    return distance

p1 = [1,2]
p2 = [4,0]
p3 = [5,4,3]
p4 = [1,7,9]

print(manhattan_distance(p1,p2))
print(manhattan_distance(p3,p4))