                .global count_jumps
                .text

# int count_jumps(int *array, int size)
count_jumps:

    li t4, 1            
    li t5, 0           

1:  lw t3, 0(a0)      
    add t5, t5, t3   
    bge t5, a1, 2f     

    addi t4, t4, 1    
    add a0, a0, t5    
    j 1b               

2:  mv a0, t4         
    ret               
