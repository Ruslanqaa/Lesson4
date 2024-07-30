immutable_var = tuple([1, 2, 3, True, 'String'])
print(immutable_var)
#immutable_var[0] = 30 При попытке заменить первый элемент, программа указывает на ошибку
mutable_list = [1, 2, 3, 4, 5]
mutable_list[1] = "картошка"
mutable_list.append(False)
print(mutable_list)

