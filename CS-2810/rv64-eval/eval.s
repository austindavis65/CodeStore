                .text
                .global eval

# eval(*exp) -> int
eval:
    	addi sp, sp, -32  
    	sd  ra, 0(sp)     
    	sd  s0, 8(sp)
	sd  s1, 16(sp)    
	sd  s2, 24(sp)    

    	ld  t0, 0(a0)
	mv  s0, a0
    	li  t1, 1      
    	beq t0, t1, .literalcase

    	li  t1, 2     
    	beq t0, t1, .pluscase

    	li  t1, 3     
    	beq t0, t1, .minuscase

    	li  t1, 4     
    	beq t0, t1, .negatecase

    	li  a0, -1
    	j .return

.literalcase:
    
    	ld  a0, 8(s0)
    	j .return

.pluscase:
    	ld  a0, 8(s0)  
	call eval
    	mv  s1, a0     
    	ld  a0, 16(s0) 
    	call eval
	mv  s2, a0      
    	add a0, s1, s2
    	j .return

.minuscase:
    	ld  a0, 8(s0) 
    	call eval      
    	mv  s1, a0   
    	ld  a0, 16(s0) 
    	call eval
	mv  s2, a0    
    	sub a0, s1, s2
    	j .return

.negatecase:
   
    	ld  a0, 8(s0) 
    	call eval      
    	neg a0, a0
    	j .return

.return:
	ld  s1, 16(sp)    
	ld  s2, 24(sp)    
    	ld  s0, 8(sp)    
    	ld  ra, 0(sp)    
    	addi sp, sp, 32  
    	ret         
