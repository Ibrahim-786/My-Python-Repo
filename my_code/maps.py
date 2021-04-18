#demonstrating MAP


var_list = [1,3,54,6,7,88,99]

new_list = list(map(lambda x:x+2, var_list))


print(new_list)


names = [{"name":"ibrahim","age":25},
         {"name":"tabbu","age":23},
         {"name":"sheetal","age":25}]


sec_name = list(map(lambda x:x["name"], names))

print(sec_name)
