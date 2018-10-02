def hamming_distance(pt1,pt2):
    distance = 0
    for i in range(len(pt1)):
        print(pt1[i])
        print(pt2[i])
        if pt1[i] != pt2[i]:
            distance += 1
    return distance

p1 = [1,2]
p2 = [4,0]
p3 = [5,4,3]
p4 = [1,7,9]

print(hamming_distance(p1,p2))
print(hamming_distance(p3,p4))