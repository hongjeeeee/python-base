tuple_1 = ("I", "love", "Python")
tuple_2 = (30, 60, 100, 3000)
print(tuple_1[1])
print(tuple_2[2])

tuple_1 = ("I", "love", "Python", 10)
tuple_2 = (30, 60, 100, 3000)
end = tuple_2[3]
tuple_1[3] = end

list_1 = ("I", "love", "Python", 10)
list_2 = (30, 60, 100, 3000)
end = list_2[3]
list_1[3] = end
print(list_1)