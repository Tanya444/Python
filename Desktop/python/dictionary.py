#Values in a dictionary can be of any data type and can be duplicated, whereas keys can’t be repeated and must be immutable. 
#keys and values can be any mix of datatypes
d={1:"geek",2:"prateek", "name": {"tanya" : "arya"}}  #nested dictionary
print(d["name"]["tanya"])
print(d)

dd=dict([(2,"geek"), (1,"prateek")])
print(dd)
del(dd[2])
print(dd)