""" combaining filter and maps """

lit =  list (filter(lambda x:x%2==0, range(1,15)))

print(lit)

lit_1 =  list (map( lambda x:x+1 ,filter(lambda x:x%2==0, range(1,15))))

print(lit_1)
