#demonstrate filter
""" a simplest way to use python filters   """

no = [1,2,3,4,5,6,7]

e= list(filter(lambda x:x%2==0,no))


print(e)

o= list(filter(lambda x:x%2!=0,no))

print(o)
