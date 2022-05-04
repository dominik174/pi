numbers = [2,3,5,4]

print('napisi brojeve')
brojevi = input()

brojevi_arr = []
for x in brojevi:
    brojevi_arr.append(int(x))
    
is_equal = numbers == brojevi_arr
print('dali je jednako')
print(is_equal)