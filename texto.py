texto=["Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec placerat lacus sed lacinia suscipit. Pellentesque pulvinar tempus dui, non facilisis dolor vestibulum et. Suspendisse potenti. Duis in molestie orci, feugiat eleifend nisi. Aliquam consequat tortor id nisl interdum mattis. In hac habitasse platea dictumst. Suspendisse aliquam tincidunt velit. Phasellus pretium fermentum leo id rutrum. Fusce suscipit augue sit amet pulvinar vulputate. Proin pretium mauris vitae purus efficitur auctor. Vestibulum est lorem, varius a tempus non, consequat vel risus. Nam laoreet velit sit amet ipsum tincidunt luctus. Nunc gravida tortor a leo efficitur, et maximus enim pharetra.","Mauris tincidunt commodo lorem a pellentesque. Nam rutrum luctus neque. Maecenas porttitor dolor in sollicitudin ultrices. Aliquam eget blandit massa. Sed bibendum suscipit finibus. Suspendisse potenti. Nullam nec luctus diam, at bibendum dui. Ut vestibulum venenatis finibus. Mauris sed turpis at ante facilisis rhoncus. Phasellus molestie pharetra sagittis. Ut tincidunt, turpis sodales dapibus commodo, quam nisi mollis quam, at maximus quam tortor vitae nibh. Phasellus posuere aliquam erat sed elementum. Pellentesque faucibus, nulla eget hendrerit venenatis, tellus enim posuere dui, eu iaculis nibh ipsum a ligula. Quisque scelerisque odio sit amet libero iaculis rutrum. In hac habitasse platea dictumst."]
count=0
sumatoria=[]
vocales=[]
counta=0
counte=0
counti=0
counto=0
countu=0



for i in range(2):
     for char in texto[i]:
          if char in 'aeiou':
              count+=1   
          if char in 'a':
              counta+=1 
          if char in 'e':
              counte+=1 
          if char in 'i':
              counti+=1 
          if char in 'o':
              counto+=1 
          if char in 'u':
              countu+=1 
     sumatoria.append(count)
     print("Vocales del texto",i+1," :", sumatoria[i],"numero de a :",counta,"numero de e :",counte,"numero de i :",counti,"numero de o :",counto, "numero de u :",countu)
     count=0
     counta=0
     counte=0
     counti=0
     counto=0
     countu=0
     print("todas las vocales de los textos : ", sum(sumatoria))

parrafo1="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec placerat lacus sed lacinia suscipit. Pellentesque pulvinar tempus dui, non facilisis dolor vestibulum et. Suspendisse potenti. Duis in molestie orci, feugiat eleifend nisi. Aliquam consequat tortor id nisl interdum mattis. In hac habitasse platea dictumst. Suspendisse aliquam tincidunt velit. Phasellus pretium fermentum leo id rutrum. Fusce suscipit augue sit amet pulvinar vulputate. Proin pretium mauris vitae purus efficitur auctor. Vestibulum est lorem, varius a tempus non, consequat vel risus. Nam laoreet velit sit amet ipsum tincidunt luctus. Nunc gravida tortor a leo efficitur, et maximus enim pharetra."
parrafo2="Mauris tincidunt commodo lorem a pellentesque. Nam rutrum luctus neque. Maecenas porttitor dolor in sollicitudin ultrices. Aliquam eget blandit massa. Sed bibendum suscipit finibus. Suspendisse potenti. Nullam nec luctus diam, at bibendum dui. Ut vestibulum venenatis finibus. Mauris sed turpis at ante facilisis rhoncus. Phasellus molestie pharetra sagittis. Ut tincidunt, turpis sodales dapibus commodo, quam nisi mollis quam, at maximus quam tortor vitae nibh. Phasellus posuere aliquam erat sed elementum. Pellentesque faucibus, nulla eget hendrerit venenatis, tellus enim posuere dui, eu iaculis nibh ipsum a ligula. Quisque scelerisque odio sit amet libero iaculis rutrum. In hac habitasse platea dictumst."
set1=set(parrafo1.split())
set2=set(parrafo1.split())

union=set1.union(set2)
print("union entre los dos parrafos :",union)
intersection= set1.intersection(set2)
print("inerseccion entre los dos parrafos :",intersection)
difference= set1.difference(set2)
print("diferencia entre los dos parrafos :", difference)




r=parrafo1.lower()
rr=parrafo2.lower()
r=r.replace('.','')
rr=rr.replace('.','')
r=r.replace(',','')
rr=rr.replace(',','')

r=r.split()
rr=rr.split()
count1=0
count2=100
most_u_w=''
less_u_w=''

for i in range(len(r)):
    if count1 < r.count(r[i]):
        count1=r.count(r[i])
        most_u_w=r[i]

print('\n')
print('Most and less repeated words in text')
print('Most used word: ',most_u_w)
print('Times of appearance: ', count1)

for i in range(len(r)):
    if count1 > r.count(r[i]):
        count1=r.count(r[i])
        less_u_w=r[i]
print('Most used word: ',less_u_w)
print('Times of appearance: ', count1)
    

# **Print the most used word on each paragraph
# **Print the least used word on each paragraph
# If only one word is found, just add it to an 
# array and print the lenngth of the array.
