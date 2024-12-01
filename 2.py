Tuple=(5,10,20)
#Tuple.insert(2,15)
#print(Tuple)

#Tuple is immutable

#Solution is
Tuple1 = Tuple[:2]+(15,)+Tuple[2:]
print(Tuple1)