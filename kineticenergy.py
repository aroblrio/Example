mass = input("Introduce el valor de la masa: ", );
mass = float(mass);
velocity = input("Introduce el valor de la velocidad: ", );
velocity = float(velocity);
kinetic = 0.5 * mass * (velocity**2);
print(kinetic);