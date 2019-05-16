def rotate_matrix(matrix, d):
  #contruct new matrix 
  m2 = [[0 for x in range(d)]for y in range(d)]
  l = d-1

  for i in range(len(matrix)):
    for j in range(matrix[i]):
      m2[i][j] = m2[j][i]
  l -= 1
  print(m2)