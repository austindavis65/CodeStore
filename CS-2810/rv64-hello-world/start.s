                .global _start
                .equ    sys_exit, 93

                .data
msg_calling:    .asciz  "Calling hw with no input\n"
msg_got:        .asciz  "  hw returned =========> "
msg_newline:    .asciz  "\n"

                .text
_start:
                .option push
                .option norelax
                la      gp, __global_pointer$
                .option pop

                la      a0, msg_calling
                call    print_string
                la      a0, msg_got
                call    print_string
                call    hw
                call    print_int
                la      a0, msg_newline
                call    print_string

                li      a0, 0
                li      a7, sys_exit
                ecall
