list1=[0,10,3,5]
list2=[10,4,6,2]
i=0
list=[]
while i<len(list1):
    j=0
    while j<len(list2):
        a=list1[i]*list2[j]
        list.append(a)
        print(list[i])
        break
        j+=1
    i+=1