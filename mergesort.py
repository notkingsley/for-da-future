def merge(inp1, inp2):
	#cant quite make it not inverted
	outp = list()
	if inp1:
		for i in inp1:
			while len(inp2) and i < inp2[0]:
				outp.append(inp2.pop(0))
			else:
				outp.append(i)
		outp += inp2
	return outp

def merge2(inp1, inp2):
	c1, c2 = 0, 0
	s1 = len(inp1)
	s2 = len(inp2)
	outp = list()

	for k in range(s1 + s2):
		if c1 < s1 and c2 < s2:
			if inp1[c1] <= inp2[c2]:
				outp.append(inp1[c1])
				c1 += 1
			else:
				outp.append(inp2[c2])
				c2 +=1
		elif c1 < s1:
			for q in range(k, s1 + s2):
				outp.append(inp1[c1])
				c1 += 1
			break
		elif c2 < s2:
			for q in range(k, s1 + s2):
				outp.append(inp2[c2])
				c2 += 1
			break
	return outp

def mergesort(inp):
	if len(inp) > 1:
		m = int(len(inp)/2)
		list1 = inp[m:]
		list2 = inp[:m]
		return merge2(mergesort(list1), mergesort(list2))
	return inp

def main():	
	import random
	me = []
	for i in range(100):
		me.append(random.randint(0, 1000))
	#meme = [3, 6, 5, 8, 0, 1, 4, 4, 6, 90, 56, 1, 0]
	print(mergesort(me))

if __name__ == '__main__':
	main()