def quicksort(inpl):
	same = 1
	for a in inpl:
		if inpl[0] != a:
			same = 0
	if len(inpl) == 1 or same:
		return inpl
	f = inpl.pop(0)
	l1, l2 = [], []
	for i in inpl:
		if i <= f:
			l1.append(i)
		else:
			l2.append(i)
	l1.append(f)
	return quicksort(l1) + quicksort(l2)

def main():	
	import random
	me = []
	for i in range(1000):
		me.append(random.randint(0, 100))
	#meme = [3, 6, 5, 8, 0, 1, 4, 4, 6, 90, 56, 1, 0]
	print(quicksort(me))
if __name__ == '__main__':
	main()