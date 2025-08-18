intial_key = 1
intial_key_value = 3
value = intial_key_value


dct = {}
inputs = 13
for i in range(inputs):
    dct[intial_key +i] = value
    value -=1
    if value == 0:
        new_key_value = intial_key_value * 2
        intial_key_value = new_key_value
        value = intial_key_value
    
print(dct[4])
    