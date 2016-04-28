import sys

def main(limit):
	pow = []
	val = []
	for num in range(2, limit):
		# For every iteration, reset all values of
		# pow to 0
		for i in range(0,limit):
			pow.append(0)
			val.append(0)

		ten = 1
		for x in range(1, limit):
			val[x] = ten
			for j in range(0, limit):
				if pow[j]:
					if not pow[(j+ten)%num] and pow[j] != x:
						pow[(j+ten)%num] = x

			if not pow[ten]:
				pow[ten] = x
			ten = (10 * ten) % num
			#sys.stdout.write("ten=%d\tval[%d]=%d\n" % (ten,x, val[x]))
			#if pow[0]:
			#	break;

		count = 0
		#for i in range(0,num+1):
		#	sys.stdout.write("pow[%d]=%d\tval[%d]=%d\n" % (i, pow[i], i, val[i]))

		x = num

		sys.stdout.write("%d\tdivides\t" % x)

		if pow[0]:
			while x:
				count = count - 1
				while count > pow[x % num] - 1:
					sys.stdout.write('0')
					count = count - 1
				count = pow[x % num] - 1
				sys.stdout.write('1')
				x = ( num + x - val[pow[x%num]] ) % num
			while count > 0:
				sys.stdout.write('0')
				count = count - 1
		else:
			print "Cant"
		print ""

if __name__ == "__main__":
	input = int(sys.argv[1])
	main(input)

