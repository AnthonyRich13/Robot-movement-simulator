#!/usr/bin/python
import sympy
import math
import numpy as np

class cd:
 @classmethod
 def cDirectaGeneral(self):
  print "Introduzca las longitudes del robot"
  a1 = input("a1 = ")
  a2 = input("a2 = ")
  print "Ingrese los datos que se quieren observar"
  t1 = input("Theta uno = ")
  t2 = input("Theta dos = ")
  d = input("d3 = ")
  t3 = input("Theta cuatro = ")

  A1 = np.array([[sympy.cos(t1),-sympy.sin(t1), 0, sympy.cos(t1)*a1],
                 [sympy.sin(t1),sympy.cos(t1),0,sympy.sin(t1)*a1],
                 [0,0,1,0],
                 [0,0,0,1]])
  A2 = np.array([[sympy.cos(t2),sympy.sin(t2), 0, sympy.cos(t2)*a2],
                 [sympy.sin(t2),-sympy.cos(t2),0,sympy.sin(t2)*a2],
                 [0,0,-1,0],
                 [0,0,0,1]])
  A3 = np.array([[1,0,0,0],
                 [0,1,0,0],
                 [0,0,1,d],
                 [0,0,0,1]])
  A4 = np.array([[sympy.cos(t3),-sympy.sin(t3), 0, 0],
                 [sympy.sin(t3),sympy.cos(t3),0,0],
                 [0,0,1,0],
                 [0,0,0,1]])
  A12 = np.dot(A1,A2)
  A123 = np.dot(A12,A3)
  A1234 = np.dot(A123,A4)
  
  print "Primera articulacion =", A1
  print "Segunda articulacion =", A2
  print "Tercera articulacion =", A3
  print "Cuarta articulacion =", A4
  print "Matriz total =", A1234

  
 
  
def main():
 cd.cDirectaGeneral()
 
if __name__ == "__main__":
    main()