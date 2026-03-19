        		.global fibonacci
        		.text

fibonacci:
				# write your code here

		li	a1, 1
		li	a2, 1
		li	a3, 2
.start:		add	a4, a1, a2
		mv	a1, a2
		mv	a2, a4
		addi	a3, a3, 1 
		bge	a3, a0, .end
		j	.start


.end:		mv	a0, a2
		ret
		
