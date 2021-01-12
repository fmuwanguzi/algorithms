one = [0, 1, 4, 5, 8] 
two =[0, 2, 7, 9, 4]

def intersection(one, two ):
    three = [value for value in one if value in set(two)]
    return three

print(intersection(one,two))

#solution 2
def intersection2(one, two):
    three = []
    for i in one:
        for j in two:
            if i == j:
                three.append(i)
    return three

print(intersection2(one, two))


##solution three and best for time complexity

def intersection3( one, two):
   set1=set(one)
   set2=set(two)
   
   return list(set1 & set2)
                
            
print(intersection3(one, two))