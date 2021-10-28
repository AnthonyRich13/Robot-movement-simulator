#!/usr/bin/python
import sympy
import math
import numpy as np

class cd:
 @classmethod
 def cInversaGeneral(self):
  print "Introduzca las longitudes del robot"
  a1 = input("a1 = ")
  a2 = input("a2 = ")
  print ("Ingrese la informacion pedida")
  x = input("x = ")
  y = input("y = ")
  z = input("z = ")
  o1 = input("Ingrese el punto de orientacion Nx = ")
  o2 = input("Ingrese el punto de orientacion Ny = ")
 
  c11 = x**2
  c12 = y**2
  c13 = a1**2
  c14 = a2**2
  c15 = 2*a1*a2
  c2 = (c11 + c12 - c13 - c14)/c15
  s2 = math.sqrt(1 - c2**2)
  s2n = -math.sqrt(1 - c2**2)
  Theta2p = math.degrees(math.acos(c2))
  Theta2n = -math.degrees(math.acos(c2))
  s1 = (a2*s2*x + (a1 +a2*c2)*y)/((a2*s2)**2 + (a1 + a2*c2)**2)
  c1 = ((a1 +a2*c2)*x - a2*s2*y)/((a2*s2)**2 + (a1 + a2*c2)**2)
  Theta1p = math.degrees(math.atan2(a2*s2*x + (a1 + a2*c2)*y,(a1 +a2*c2)*x - a2*s2*y))
  Theta1n = math.degrees(math.atan2(a2*s2n*x + (a1 + a2*c2)*y,(a1 +a2*c2)*x - a2*s2n*y))
  d3= -z
  Theta41 = Theta1p + Theta2n - math.degrees(math.atan2(o2,o1))
  Theta42 = Theta1p + Theta2p - math.degrees(math.atan2(o2,o1))
  Theta43 = Theta1n + Theta2n - math.degrees(math.atan2(o2,o1))
  Theta44 = Theta1n + Theta2p - math.degrees(math.atan2(o2,o1))                 
    
  if Theta2p == Theta2n and Theta1n == Theta1p:
   print("Parametros posibles = (%s, %s, %s, %s)" % (Theta1p,Theta2p, d3, Theta42))
  elif Theta2p != Theta2n and Theta1n != Theta1p:
   print("Parametros posibles = (%s, %s, %s, %s) , (%s, %s, %s, %s), (%s, %s, %s, %s) , (%s, %s, %s, %s), (%s, %s, %s, %s) , (%s, %s, %s, %s), (%s, %s, %s, %s) , (%s, %s, %s, %s) , (%s, %s, %s, %s) , (%s, %s, %s, %s), (%s, %s, %s, %s) , (%s, %s, %s, %s),(%s, %s, %s, %s) , (%s, %s, %s, %s), (%s, %s, %s, %s) , (%s, %s, %s, %s)" % (Theta1p,Theta2p, d3, Theta41,Theta1p,Theta2n, d3, Theta41,Theta1n,Theta2n, d3, Theta41,Theta1n,Theta2p, d3, Theta41,Theta1p,Theta2p, d3, Theta42,Theta1p,Theta2n, d3, Theta42,Theta1n,Theta2n, d3, Theta42,Theta1n,Theta2p, d3, Theta42, Theta1p,Theta2p, d3, Theta43,Theta1p,Theta2n, d3, Theta43,Theta1n,Theta2n, d3, Theta43,Theta1n,Theta2p, d3, Theta43,Theta1p,Theta2p, d3, Theta44,Theta1p,Theta2n, d3, Theta44,Theta1n,Theta2n, d3, Theta44,Theta1n,Theta2p, d3, Theta44))
  elif Theta2p != Theta2n and Theta1n == Theta1p:
   print("Parametros posibles = (%s, %s, %s, %s) , (%s, %s, %s, %s)" % (Theta1p,Theta2p, d3, Theta41,Theta1p,Theta2n, d3, Theta42))
  elif Theta2p == Theta2n and Theta1n != Theta1p:
   print("Parametros posibles = (%s, %s, %s, %s) , (%s, %s, %s, %s)" % (Theta1p,Theta2p, d3, Theta4p,Theta1n,Theta2p, d3, Theta4p))  
  
def main():
 cd.cInversaGeneral()
 
if __name__ == "__main__":
    main()