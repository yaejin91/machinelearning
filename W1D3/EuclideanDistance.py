def euclidean_distance(pt1, pt2):
    distance = 0
    sqdiffSum = 0
    for dimension in range(len(pt1)):
        diff = pt1[dimension] - pt2[dimension]
    sqdiff = diff ** 2

    sqdiffSum += sqdiff
    distance = sqdiffSum ** 0.5
    return distance

p1 = [1, 2]
p2 = [4, 0]
p3 = [5,4,3]
p4 = [1,7,9]

print(euclidean_distance(p1, p2))
print(euclidean_distance(p3,p4))
