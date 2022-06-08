----- ----- ----- ----- ----- ----- ----- ----- PROBLEM ----- ----- ----- ----- ----- ----- ----- -----


Have the function Palindrome(str) take the str parameter being passed and return the string true if the parameter is a palindrome, 
(the string is the same forward as it is backward) otherwise return the string false. 
For example: "racecar" is also "racecar" backwards. Punctuation and numbers will not be part of the string.


----- ----- ----- ----- ----- ----- ----- ----- My Answer ----- ----- ----- ----- ----- ----- ----- -----

def Palindrome(strParam):
  d=strParam.replace(" ","")
  if d[::-1]==d:
    return "true"
  else:
    return "false"

print(Palindrome(input()))