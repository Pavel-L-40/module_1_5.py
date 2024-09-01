immutable_var = 1, 'b', True # создаем кортеж
print(immutable_var)
print(type(immutable_var))

# immutable_var[0] = cat
# кортеж - неизменяемая послеовательность, любая попытка изменения его элементов приведет к ошибке
# NameError: name 'cat' is not defined

mutable_list = [1, 2, 3, 4, 5] # создаем список
print(type(mutable_list))
print(mutable_list)

test = 1, 2, 3, [4, 5]
print(type(test))
test[3][1] = 2
print(test)