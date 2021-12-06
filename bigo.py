# exemplo de bigo(n) = my_array cresce linear conforme elementos são passados
def find_sum(my_array):
	sum = 0
	for item in my_array:
		sum += item
	return sum

print(find_sum([1, 2, 3]))