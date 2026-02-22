abu='soul'
bua=45
uba=True
for i in abu:
	print(i)
for j in range (1,100):
	print(j)
	if j==bua:
		print('The end','\n',j)
		break
for i in range(10):
	print('\n',i)
for i in range(1,10,2):
	print('\n',i)
for i in range(10,1,-2):
	print('\n',i)
#List
#Ordered
#Mutable
flowers=['Lilies','Orchids','Roses','Daisies','Sunflowers']
print(type(flowers))
print(flowers)
print(flowers[2])
print(flowers[0:3])
print(flowers[:4])
print(flowers[: :2])
print(flowers[: :3])
print(flowers[: :-1])
#List
#append(edit)
#insert(ingiza)
#remove(toa sth from a list using the word)
#pop(remove sth from a list using indent)
#sort(kupanga na aspect fulani)
#len(identifies the number of items on your list)
#count(hesabu occurences of a value,hio item imejirudia mara ngapi kwa list) 
flowers.append('Tulips')
print(flowers)
flowers2=["Zaburi","Satura","Ua","Lilies"]
for i in flowers2:
	flowers.append(i)
print(flowers)
flowers.insert(4,'Love')
print(flowers)
flowers.remove("Orchids")
print(flowers)
flowers.pop(6)
print(flowers)
print(len(flowers))
print(flowers.count('Lilies'))
#New list
marks=[10,20,30,40,50,60,70,80,90,100]
print(marks)
chopi=[i for i in marks if i>=90]
print(chopi)
print(type(chopi))
average=[i for i in marks if 50<i<=80]
print(average)
#Tuples
scores=[15,35,55,75,95]
print(type(scores))
print(scores)
John,Alex,Andie,Trevor,Patrick=[15,35,55,75,95]
print(John,Alex,Andie,Trevor,Patrick)
print(type(John))
#Sets-use calibraces
#No duplicates-set lazima ikue na unique words
#Unordered(hii haina indent,like haianzi from 0,1 etc)
Days_of_the_week={'Monday','Tuesday','Wednesday','Thursday','Friday','Saturday',}
print(type(Days_of_the_week))
print(Days_of_the_week)
Days_of_the_week.add('Sunday')
print(Days_of_the_week)
#Dictionary-uses calibraces,but has key and value
Students={'Name':'John',
                   'Age':45,
                   'Marital status':'Married'}
print(Students)