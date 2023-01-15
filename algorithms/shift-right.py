def password_generator(user):
  password = ""
  len_username = len(user)

  for num in range(0,len_username):
    password += user[num - 1]
    
  return password
