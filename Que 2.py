from collections import MutableMapping
def aflatten(d, parent_key ='', sep ='.'): 
    items = [] 
    for k, v in d.items(): 
        new_key = parent_key + sep + k if parent_key else k 
  
        if isinstance(v, MutableMapping): 
            items.extend(aflatten(v, new_key, sep = sep).items()) 
        else: 
            items.append((new_key, v)) 
    return dict(items)
a = eval(input())
print(str(aflatten(a)))
