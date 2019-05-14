def URLify(in_string, in_string_length):
  return in_string[:in_string_length].replace(" ", "%20")

print(URLify("the cat", 6))