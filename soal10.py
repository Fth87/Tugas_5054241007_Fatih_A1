# input x1,x2,y1,y2
# gradien dari input
# x & y tengah
# gradien tegak lurus (-1 / gradien1)
# y = mx + b, b = y(tengah) - gradien2 . x(tengah)
# output: 2 titik & hasil persamaan

x1 = int(input('x1 = '))
x2 = int(input('x2 = '))
y1 = int(input('y1 = '))
y2 = int(input('y2 = '))

m1 = (y2 - y1) / (x2 - x1)
xmid = (x1 + x2) / 2
ymid = (y1 + y2) / 2

m2 = -1/m1

b = ymid - m2 * xmid

print(f' xmid : {xmid}, ymid : {ymid}, {b:.2f}') 





