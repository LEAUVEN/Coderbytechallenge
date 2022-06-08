----- ----- ----- ----- ----- ----- ----- ----- PROBLEM ----- ----- ----- ----- ----- ----- ----- -----

 Have the function RomanNumeralReduction(str) read str which will be a string of roman numerals in decreasing order. 
 The numerals being used are: I for 1, V for 5, X for 10, L for 50, C for 100, D for 500 and M for 1000. 
 Your program should return the same number given by str using a smaller set of roman numerals. 
 For example: if str is "LLLXXXVVVV" this is 200, so your program should return CC because this is the shortest way to write 200 
 using the roman numeral system given above. If a string is given in its shortest form, just return that same string.


----- ----- ----- ----- ----- ----- ----- ----- My Answer ----- ----- ----- ----- ----- ----- ----- -----


def RomanNumeralReduction(strParam):
  a=strParam.count("I")
  b=strParam.count("V")
  c=strParam.count("X")
  d=strParam.count("L")
  e=strParam.count("C")
  f=strParam.count("D")
  g=strParam.count("M")
  total=(a*1)+(b*5)+(c*10)+(d*50)+(e*100)+(f*500)+(g*1000)
  aa=total//1000
  ab=(total-aa*1000)//500
  ac=((total-aa*1000)-ab*500)//100
  ad=(((total-aa*1000)-ab*500)-ac*100)//50
  ae=((((total-aa*1000)-ab*500)-ac*100)-ad*50)//10
  af=(((((total-aa*1000)-ab*500)-ac*100)-ad*50)-ae*10)//5
  ag=((((((total-aa*1000)-ab*500)-ac*100)-ad*50)-ae*10)-af*5)//1
  return(aa*'M'+ab*'D'+ac*'C'+ad*'L'+ae*'X'+af*"V"+ag*'I')
  
print(RomanNumeralReduction(input()))