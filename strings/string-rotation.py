import string

def rotation(string1, string2):
  #checking the length of the strings
  if len(string1) != len(string2):
    return False
  string1 = string1.lower()
  string2 = string2.lower()

  #create dictionaries for comparison
  dict_1 = dict.fromkeys(list(string.ascii_lowercase), 0)
  dict_2 = dict.fromkeys(list(string.ascii_lowercase), 0)

  #run throught the loop till characters are rotated
  for i in range(len(string1)):
    dict_1[string1[i]] += 1
    dict_2[string1[i]] += 1
  return dict_1 == dict_2