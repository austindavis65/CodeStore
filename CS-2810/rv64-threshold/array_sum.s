                .global array_sum
                .text

# int array_sum(int *array, int count, int threshold)
array_sum:

		#a0: array
		#a1: count
		#a2: threshold
		#a3: sum
		#a4: i
		
		li	a4, 0
1:		bge	a4, a1, 2f
		slli	t2, a4, 3
		add	t2, a0, t2
		addi	a4, a4, 1
		ld	t1, (t2)
		blt	t1, a2, 1b
		add	a3, a3, t1
		j	1b

2:		mv	a0, a3
		ret
