list1=['a','b','taco']
list2=['taco','hamburguesa','1']
superposicion=[]
for n1 in list1:
    for n2 in list2:
        if n1==n2 in list1 and list2: 
            superposicion.appen(n1)
        else:
            n2=n2+1
    n1=n1+1
print(superposicion)