x = [1, 2, 3]
y = [5, 1, 3]

#y = x
m1 = 1
b1 = 0

#y = 0.5x + 1
m2 = 0.5
b2 = 1

y_predicted1 = [xval*m1 for xval in x]
y_predicted2 = [xval*m2+b2 for xval in x]

total_loss1 = 0
subsq = 0

ydiff = [yi - ypi for yi,ypi in zip(y,y_predicted1)]

for sub in ydiff:
  subsq = sub*sub
  total_loss1 += subsq
print(total_loss1)

total_loss2 = 0
ydiff2 = [yi - yp2i for yi, yp2i in zip(y, y_predicted2)]

subsq = 0

for sub in ydiff2:
  subsq = sub*sub
  total_loss2 += subsq

print(total_loss1)
print(total_loss2)

better_fit = 2