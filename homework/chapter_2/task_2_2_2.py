def summation(A):
  sum = 0
  m = 0
  for i in range(len(A)):
    if A[i] < 0:
      A[i] = abs(A[i]) * 2
    m = max(A)
  for i in range(len(A)):
    A[i] = A[i] / m
  for i in range(len(A)):
    sum += A[i]
  return(sum)
