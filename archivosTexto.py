'''
f = open('alumnos.txt','r')
nombres = f.read()
print(nombres)

nombres2 = f.read()
print(nombres2)
f.close()

for items in nombres2:
    print(items,end='')
'''

alumno = {'Matricula':12345,'Nombre':'Mario','Apellidos':'Lopez','correo':'mlopez@umanimundial.edu.mx'}
f = open('alumnos.txt','a')
for nom  in alumno:
    f.write('\n'+ nom + ":" + str(alumno[nom]))

f.close()

