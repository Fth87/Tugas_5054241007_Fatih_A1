#menghitung input jam dan menit
t = list(map(float, input().split()))

#convert time
t = t[0] + t[1]/60

#menghitung temperatur
T = (((4*t**2)/t+2)-20)

print(f'{T:.2f}')

