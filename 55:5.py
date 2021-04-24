#example // something@something.something
mail="spano.spano@gmail.com"

def mailCheck():
  global mail
  t=()
  dotCount=0
  atCount=0
  check=True
  for char in mail:
    if char==".":
      dotCount+=1
    if char=="@":
      atCount+=1
    if dotCount==1 and atCount==1:
      check=True
    else:
      check=False
  return check
      
print(mailCheck())
