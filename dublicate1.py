my_name ="MISSISSIPPI"
dict={}
for item in my_name:
    if item in dict:
        dict[item]+=1
    else:
        dict[item]=1
print(dict)