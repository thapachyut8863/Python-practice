#keys and value in python using the dictionary
keys = ["achyut","thapa","kaji"]
values=["python","java","c++"]

data = dict(zip(keys,values))
#adding the key in the dictionary
data['tirsana'] = "nursing"


#deleting the key from the dictionary 
#del is used to delete the key from the dictionary

del data['achyut']
print(data)