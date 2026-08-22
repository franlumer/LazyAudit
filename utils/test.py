lista = ["1","2","a","3","4","5"]

left_list, right_list = lista[:2], lista[3:]
left_list.extend("A")
left_list.extend(right_list)


print(left_list)