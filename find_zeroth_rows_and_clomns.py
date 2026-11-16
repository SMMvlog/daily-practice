b =[
    ['0', '1', '1', '1', '0', '1', '0'],
    ['0', '0', '0', '0', '0', '0', '0'],
    ['0', '0', '1', '1', '0', '1', '0'],
    ['0', '1', '1', '1', '0', '1', '0'],
    ['0', '1', '1', '1', '0', '1', '0']
]
def get_result(b):
  rows = []
  columns = []
  for i in range(len(b[0])):
    for j in range(len(b)):
      if b[j][i] !='0':
        break
    else:
      columns.append(i)
  for i in range(len(b)):
    for j in range(len(b[0])):
      if b[i][j] !='0':
        break
    else:
      rows.append(i)
  return rows, columns
print(get_result(b))