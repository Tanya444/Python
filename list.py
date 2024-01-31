#list[] just like vector in c++ -creation,0 indexing,slicing
#it can contain multiple datatypes-int,string ,object,etc-, is mutable
list=['red','yellow','green','blue']
print(list)
print(list[-1])  #last item
print(len(list))
#append() to add at end of list 
list.append("orange")
#insert(position,value)
list.insert(3,0)
print("adding at some index",list)
list.extend(["tanya","arya"])
print("adding multiple values at end", list )
list.reverse()
print("after reversing",list)
#to remove elements- list.remove() -first occurence of searched, list.pop(index)

#slicing
l=['a','b','c','d','e']

print(l[:2])     #start se excluding index 2
print(l[2:])
print(l[1:3])    #index 3 exclude
print(l[1::2])   #index 1 se fir alternate
print(l[:-1])    #start se excluding last element
print(l[-4:-1])  # -4 till last excluding -1
print(l[::-1])   #reverse list

#list comprehension
oddsquare=[x**2 for x in range(1,10) if x%2==1]
print(oddsquare)