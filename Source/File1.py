tuple_1 = ("Jack", "Max", "Harry")
tuple_2 = [(len(tuple_1[0]), tuple_1[0]),(len(tuple_1[1]), tuple_1[1]),(len(tuple_1[2]),tuple_1[2])]

tuple_3 = max(sorted(tuple_2))


print(tuple_1)
print(tuple_2)
print(tuple_3)