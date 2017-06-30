# Excercise 2.2
x = "Tesla"
y = "Buick"
z = "Ferrari"
w = "Ford"
t = "Lamborghini"
p = "Masertati"
sumatoria=[]
sumatoria2=[]

Carros =(x,y,z,w,t,p)
count = 0
count2 =0
for i in range(6) :
    for char in Carros[i]:
        if char in 'aeiou':
            count+=1
        if char in 'a':
            count2+=1
        if char in 'e':
            count2+=2
        if char in 'i':
            count2+=3
        if char in 'o':
            count2+=4
        if char in 'u':
            count2+=5
    sumatoria.append(count)
    count=0
    sumatoria2.append(count2)
    count2=0
    print (Carros[i],"tiene :",sumatoria[i], "vocales")
    if sumatoria2[i]%2 ==0:
        print("Buy it")
    elif sumatoria2[i]%3 ==0:
        print("Sell it")


    
 
