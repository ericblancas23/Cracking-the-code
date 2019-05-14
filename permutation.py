def permutation(s1, s2):
  n1 = len(s1)
  n2 = len(s2)

  #check to see if n1 and n2 are the same
  if (n1 != n2):
    return False
  
  #sort the strings
  a = sorted(s1)
  s1 = " ".join(a)
  b = sorted(s2)
  s2 = " ".join(b)

  for i in range(0, n1, 1):
    if (s1[i] != s2[i]):
      return False
  return True



print(permutation("abc", "cna"))