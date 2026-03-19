                .global _start
                .equ    sys_exit, 93

                .data
                .balign 8
msg_prefix:     .asciz  "finding smallest element of list out of "
msg_end:        .asciz  " elements\n"
msg_result:     .asciz  "    found element ===> "
newline:        .asciz  "\n"
string_end:

                .balign 8
lst:            .8byte  -803, 518, -706, 415, -455, -688, -64, 978, 599, 923
                .8byte  880, -76, -125, -688, 974, -16, -368, -28, -274, -273
                .equ    lst_len, 20
lst_end:


                .text
_start:
                .option push
                .option norelax
                la      gp, __global_pointer$
                .option pop

                # while start < end
                la      s0, lst
                la      s1, lst_end
1:              bge     s0, s1, 2f
                la      a0, msg_prefix
                call    print_string
                la      a0, lst
                sub     a0, s0, a0
                srli    a0, a0, 3
                call    print_int
                la      a0, msg_end
                call    print_string
                la      a0, msg_result
                call    print_string
                mv      a0, s0
                mv      a1, s1
                call    find_smallest
                ld      a0, (a0)
                call    print_int
                la      a0, newline
                call    print_string
                addi    s0, s0, 8
                j       1b
2:              li      a0, 0
                li      a7, sys_exit
                ecall
