r, c, N = map(int, input().split())
hutan = [list(map(int, input().split())) for _ in range(r)]
gerakan = str(input())

pak_dengklek = [0, 0]
emas = hutan[0][0]
salah = False

for i in gerakan:
  if i == 'L':
    if pak_dengklek[1] - 1 < 0:
      salah = True
      break
    pak_dengklek[1] -= 1
    emas += hutan[pak_dengklek[0]][pak_dengklek[1]] - 2

  elif i == 'R':
    if pak_dengklek[1] + 1 >= c:
      salah = True
      break
    pak_dengklek[1] += 1
    emas += hutan[pak_dengklek[0]][pak_dengklek[1]] + 3

  elif i == 'D':
    if pak_dengklek[0] + 1 >= r:
      salah = True
      break
    pak_dengklek[0] += 1
    emas += hutan[pak_dengklek[0]][pak_dengklek[1]] - 2

  elif i == 'U':
    if pak_dengklek[0] - 1 < 0:
      salah = True
      break
    pak_dengklek[0] -= 1
    emas += hutan[pak_dengklek[0]][pak_dengklek[1]] + 3

print(emas)
if salah:
  print("gerakanmu salah bung!")


r, c, N = map(int, input().split())
hutan = [list(map(int, input().split())) for _ in range(r)]
gerakan = input().strip()

pak_dengklek = [0, 0]
emas = hutan[0][0]
salah = False

# Dictionary to map movements to their respective changes in coordinates and gold adjustments
moves = {
  'L': (0, -1, -2),
  'R': (0, 1, 3),
  'D': (1, 0, -2),
  'U': (-1, 0, 3)
}

for i in gerakan:
  if i in moves:
    dx, dy, gold_adjust = moves[i]
    new_x, new_y = pak_dengklek[0] + dx, pak_dengklek[1] + dy
    
    if 0 <= new_x < r and 0 <= new_y < c:
      pak_dengklek[0], pak_dengklek[1] = new_x, new_y
      emas += hutan[new_x][new_y] + gold_adjust
    else:
      salah = True
      break

print(emas)
if salah:
  print("gerakanmu salah bung!")