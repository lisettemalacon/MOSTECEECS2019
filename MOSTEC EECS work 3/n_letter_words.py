def n_letter_words(original, n):
  """Return a list containing only those from the original list with n or more characters.  
  """
  new_list = []
  for word in original:
      if len(word) >= n:
        new_list.append(word)
  return new_list

original=["Lisp","Fortran","Cobol","C","C++","C#","BASIC","Logo","Pascal","Java","JavaScript","SQL","Python","R"]
long_names = n_letter_words(original, 5)
print("The words at least 5 letters long as " + str(long_names))
