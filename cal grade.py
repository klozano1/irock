#exam scores
arturo= [90, 100, 50, 70]
artemio=[70, 65, 100, 80]
juan=[90, 90, 100, 80]
rene=[50, 60, 70, 80]
pedro=[100, 50, 100, 90]
alan = [50,40,70,80]
estudiantes=["arturo","artemio","juan","rene","pedro","alan"]
e1= sum(arturo)/len(arturo)
e2= sum(artemio)/len(artemio)
e3= sum(juan)/len(juan)
e4= sum(rene)/len(rene)
e5= sum(pedro)/len(pedro)
e6= sum(alan)/len(alan)
grade=[e1,e2,e3,e4,e5,e6]
print(grade)
for i in range(6):
    if grade[i]>=95.00: #excentado:
        print("Name     " ,"Score      ","Message    " )
        print( estudiantes[i],("      ") ,grade[i] ,("      ") , "Excentado" )
    elif grade[i]<95.00 and grade[i]>=85.00: # aprobado
        print("Name     " ,"Score      ","Message    " )
        print(  estudiantes[i],("      ") ,grade[i] ,("      ") , "Aprobado" )
    elif grade[i]>=70.00 and grade[i]<85.00: #promedio
        print("Name     " ,"Score      ","Message    " )
        print(  estudiantes[i],("  ") ,grade[i] ,("  ") , "¨Promedio" )   
    elif grade[i]<70.00: # reprobado
        print ("Name     " ,"Score      ","Message    " )
        print (  estudiantes[i],("      ") ,grade[i] ,("      ") , "Reprobado" )

print(estudiantes[2] , grade[grade.index(max(grade))])
print(estudiantes[5] ,grade[grade.index(min(grade))])
