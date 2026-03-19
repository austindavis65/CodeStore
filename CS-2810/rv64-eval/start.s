                .global _start
                .equ    sys_exit, 93
                .text

_start:
                .option push
                .option norelax
                la      gp, __global_pointer$
                .option pop

                la      a0, n1
                call    do
                la      a0, n2
                call    do
                la      a0, n3
                call    do
                la      a0, n4
                call    do
                la      a0, n5
                call    do
                la      a0, e1
                call    do
                la      a0, e2
                call    do
                la      a0, e3
                call    do
                la      a0, e4
                call    do
                la      a0, e5
                call    do

                li      a0, 0
                li      a7, sys_exit
                ecall

do:
                addi    sp, sp, -16
                sd      ra, 8(sp)
                sd      s0, 0(sp)

                mv      s0, a0

                la      a0, msg_start
                call    print_string
                mv      a0, s0
                call    print_exp
                la      a0, newline
                call    print_string
                mv      a0, s0
                call    eval
                mv      s0, a0
                la      a0, msg_result
                call    print_string
                mv      a0, s0
                call    print_int
                la      a0, newline
                call    print_string

                ld      ra, 8(sp)
                ld      s0, 0(sp)
                addi    sp, sp, 16
                ret

                .data
msg_start:      .asciz  "Evaluating expression: "
msg_result:     .asciz  "      got back result: "
newline:        .asciz  "\n"
msg_end:
