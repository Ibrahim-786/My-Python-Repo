import random




def unapck_dictionaries(**arg):
    """unpack dictionaries """
    print(arg)

   
dic={"one":1,"two":2,"three":3}


unapck_dictionaries(**dic)


def unapcking_list(new_li):
    """ hello this list unapcking function """
    #normal comment
    
    print(new_li)



x= [1,2,3,4]
unapcking_list(x)


"""lambda function   """
sqr = lambda num : num*num

print(sqr(2))

print(sqr.__name__)

print(unapcking_list.__doc__)

print(print.__doc__)

print(random.randint.__doc__)


""" demonstrating  print function """

print([1,2,3,4],(1,2,3,4),{"one":1,"two":2,"three":3},{1,2,5,7},flush = True)


print([1,2,3,4],(1,2,3,4),{"one":1,"two":2,"three":3},{1,2,5,7},sep="    ", end = "                    " )

print(type([1,2,3,4]),type((1,2,3,4)),type({"one":1,"two":2,"three":3}),type({1,2,5,7}))


