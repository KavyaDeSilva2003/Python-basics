num_one = 5
num_two = 2

greater_than = num_one > num_two # True or False 
print("greater than :", greater_than)

less_than = num_one < num_two
print("less than :", less_than)

and_operator = (num_one > num_two) and (num_one < num_two)
print("and operator :", and_operator)

or_operator = (num_one > num_two) or (num_one < num_two)
print("or operator :", or_operator)

not_operator = not(greater_than)
print("not operator :", not_operator)

"""
A	B	A XOR B
0	0	0
0	1	1
1	0	1
1	1	0
"""
xor_operator = greater_than ^ less_than
print("xor operator :", xor_operator)