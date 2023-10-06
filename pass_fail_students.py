examscore = int(input("Introduce tu nota del examen (sobre 100): ", ))
classes = int(input("Introduce el numeros de clases que has atendido: ", ))

if (examscore > 100 or classes > 40):
   print("Eso no es posible")

if ((examscore >= 70 and examscore < 100) and (classes >= 32 and classes < 40)):
    print("Has aprobado la asignatura")

else:
    print("Has suspendido la asignatura")
    
