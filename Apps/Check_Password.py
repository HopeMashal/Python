def checkPassword(password):
  if len(password)>=8 and len(password)<20:
    s1="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    s2="abcdefghijklmnopqrstuvwxyz"
    s3="0123456789"
    s4="@#$%!"
    hasUpper=False
    hasLower=False
    hasNumber=False
    hasSymbol=False
    for i in password:
      if i in s1:
        hasUpper = True
      elif i in s2:
        hasLower = True
      elif i in s3:
        hasNumber = True
      elif i in s4:
        hasSymbol = True
    if (hasUpper and hasLower and hasNumber and hasSymbol):
      print("The password is valid!!")

    elif(not hasUpper and hasLower and hasNumber and hasSymbol):
      print("The password is valid!! Please add upper case")
    elif(not hasUpper and not hasLower and hasNumber and hasSymbol):
      print("The password is valid!! Please add upper case and lower case")
    elif(not hasUpper and hasLower and not hasNumber and hasSymbol):
      print("The password is valid!! Please add upper case and number")
    elif(not hasUpper and hasLower and hasNumber and not hasSymbol):
      print("The password is valid!! Please add upper case and symbol")
    elif(not hasUpper and not hasLower and not hasNumber and hasSymbol):
      print("The password is valid!! Please add upper case and lower case and number")
    elif(not hasUpper and not hasLower and hasNumber and not hasSymbol):
      print("The password is valid!! Please add upper case and lower case and symbol")
    elif(not hasUpper and hasLower and not hasNumber and not hasSymbol):
      print("The password is valid!! Please add upper case and number and symbol")

    elif( hasUpper and not hasLower and hasNumber and hasSymbol):
      print("The password is valid!! Please add lower case")
    elif( hasUpper and not hasLower and not hasNumber and hasSymbol):
      print("The password is valid!! Please add lower case and number")
    elif( hasUpper and not hasLower and hasNumber and not hasSymbol):
      print("The password is valid!! Please add lower case and symbol")
    elif( hasUpper and not hasLower and not hasNumber and not hasSymbol):
      print("The password is valid!! Please add lower case and number and symbol")

    elif( hasUpper and hasLower and not hasNumber and hasSymbol):
      print("The password is valid!! Please add number and number")
    elif( hasUpper and hasLower and not hasNumber and not hasSymbol):
      print("The password is valid!! Please add number and symbol")

    elif( hasUpper and hasLower and hasNumber and not hasSymbol):
      print("The password is valid!! Please add symbol")
  else:
    print("The password is invalid!! Password must be at least 8, and less than 20")

checkPassword("dsadFSDA")