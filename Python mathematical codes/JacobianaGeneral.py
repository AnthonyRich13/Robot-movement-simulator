#!/usr/bin/python
import sympy
import math
import numpy as np

class cd:
 @classmethod
 def jacobianaGeneral(self):
 
  print "Introduzca las longitudes del robot"
  a1 = input("a1 = ")
  a2 = input("a2 = ")

  print ("Ingrese los datos que se quieren observar")
  t1 = input("Theta uno = ")
  t2 = input("Theta dos = ")
  d = input("d3 = ")
  t3 = input("Theta cuatro = ")

  Ja = np.array([[-a1*sympy.sin(t1) - a2*(sympy.sin(t1)*sympy.cos(t2) + sympy.cos(t1)*sympy.sin(t2)),-a2*(sympy.sin(t1)*sympy.cos(t2) + sympy.cos(t1)*sympy.sin(t2)), 0, 0],
                 [a1*sympy.cos(t1) + a2*(sympy.cos(t1)*sympy.cos(t2) + sympy.sin(t1)*sympy.sin(t2)),a2*(sympy.cos(t1)*sympy.cos(t2) - sympy.sin(t1)*sympy.sin(t2)), 0, 0],
                 [0,0,-1,0],
                 [0,0,0,0],
                 [0,0,0,0],
                 [1,1,0,-1]])

  print("Matriz Jacobiana =", Ja)

def main():
 cd.jacobianaGeneral()
 
if __name__ == "__main__":
    main()