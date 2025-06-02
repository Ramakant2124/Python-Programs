#creating set in python
set1={10,20,30,40,50}
print(set1)

#Using Add Method
set1.add(60)
print(set1)

#Using Copy Method
set2=set1.copy()
print(set2)


#Using Pop Method
set1.pop()
print(set1)


#Using Remove Method
set1.remove(30)
print(set1)


#Using Update Method
set3={45,25,63}
set1.update(set3)
print(set1)

#Using Union Method
print(set2)
print(set1.union(set2))
print(set1|set2)    # '|'(pipe Operator) Can be use as Union ss

#Using Intersection Method
set4={10,2,3}
print(set1.intersection(set4))
print(set1&set4)    #'&'(And Operator) Can be use as Intersection

#Using Difference Method
print(set1.difference(set2))
print(set2.difference(set1))
print(set1-set2)    #'-' (Minus Operator) Can be use as Difference
