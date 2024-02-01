#  {} unordered (we cant access items using indexes), no duplicates allowed, mutable
# set can store a mixture of string, integer, boolean, etc datatypes.
#Only instances of immutable types can be added to a Python set. so we cant add mutable objects-list,dictionary,set inside set
#other datatypes like string,int ,float can be stored in set bcoz it does not support item asignment.
s={"linux","cmake","vim","vscode","gitbash"}
print(type(s))
s.add("github")
print(s)
#s[1]="colab"   #TypeError: 'set' object does not support item assignment
s.add(True)
#internal working of set is based on hash table.
#union function or | operator -duplicates get removed.
#s1={[1,2,3],"tanya","python"}    #TypeError: unhashable type: 'list'
s1={True,"tanya","arya"}
s2={"hi",False,"tanya"}
s3=s1.union(s2)
print(s3)

#intersection function through intersection() or & operator
s4=s1 & s2
print(s4)

#difference between 2 sets
set1=set()
set2=set()
for i in range(5):
    set1.add(i)
print("set1-",set1)
for j in range(3,9):
    set2.add(j)
print("set2-",set2)
set3=set1-set2
set4=set2-set1
print("set1-set2",set3)
print("set2-set1",set4)
#to clear whole set inplace
s.clear()

ss1=set()
ss2=set()
for i in range(3):
    ss1.add(i)
for j in range(5):
    ss2.add(j)
print(ss1<=ss2)   #checks if ss1 is subset of ss2.
print(ss1<ss2)    #checks if ss1 is proper subset of ss2.
print(ss1>=ss2)   #checks if ss1 is superset of ss2