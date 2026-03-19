                .global thermostat

                .text
thermostat:
                # your code goes here

		li	t0, 68
		li	t1, 75
		bgt	a0, t1, 1f
		blt	a0, t0, 2f
		li	a0, 0
		ret
		
1:		li	a0, -1
		ret

2:		li	a0, 1
		ret
