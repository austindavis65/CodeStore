                .global array_max
                .text

# int array_max(int *array, int count)
array_max:

		#a0: array
		#a1: count
		#a3: max
		#a4: i
		
		li	a4, 1 
		ld	a3, (a0)
.start:		bge	a4, a1, .end
		slli	t2, a4, 3
		add	t2, a0, t2
		addi	a4, a4, 1
		ld	t1, (t2)
		bgt	a3, t1, .start 
		mv	a3, t1
		j	.start

.end:		mv	a0, a3
		ret
