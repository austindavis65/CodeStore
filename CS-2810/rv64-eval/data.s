                .global n1, n2, n3, n4, n5
                .global e1, e2, e3, e4, e5
                .global print_exp
                .data

                .balign 8
n1:             .8byte  1, 0, 0xdeadbeefdecafbad
n2:             .8byte  1, 17, 0xdeadbeefdecafbad
n3:             .8byte  1, -91, 0xdeadbeefdecafbad
n4:             .8byte  1, 12345, 0xdeadbeefdecafbad
n5:             .8byte  1, -98765, 0xdeadbeefdecafbad

                # expressions
                # (5 + 7)
n6:             .8byte  1, 5, 0xdeadbeefdecafbad
n7:             .8byte  1, 7, 0xdeadbeefdecafbad
e1:             .8byte  2, n6, n7

                # (9 - 3)
n8:             .8byte  1, 9, 0xdeadbeefdecafbad
n9:             .8byte  1, 3, 0xdeadbeefdecafbad
e2:             .8byte  3, n8, n9

                # ((5 + 7) - (9 - 3))
e3:             .8byte  3, e1, e2

                # -4
n10:            .8byte  1, 4, 0xdeadbeefdecafbad
e4:             .8byte  4, n10, 0xdeadbeefdecafbad

                # -((5 + 7) - (9 - 3))
e5:             .8byte  4, e3, 0xdeadbeefdecafbad
e_end:

s_left:         .asciz  "("
s_right:        .asciz  ")"
s_plus:         .asciz " + "
s_minus:        .asciz " - "
s_neg:          .asciz "-"
s_err:          .asciz "<ERROR>"
newline:        .asciz "\n"

                .text
print_exp:
                addi    sp, sp, -16
                sd      ra, 8(sp)
                sd      s0, 0(sp)

                mv      s0, a0

                # get the tag
                ld      t0, (s0)
                li      t1, 1
                bne     t0, t1, 1f

                # int literal case
                ld      a0, 8(s0)
                call    print_int
                j       5f

1:              li      t1, 2
                bne     t0, t1, 2f

                # plus
                la      a0, s_left
                call    print_string
                ld      a0, 8(s0)
                call    print_exp
                la      a0, s_plus
                call    print_string
                ld      a0, 16(s0)
                call    print_exp
                la      a0, s_right
                call    print_string
                j       5f

2:              li      t1, 3
                bne     t0, t1, 3f

                # minus
                la      a0, s_left
                call    print_string
                ld      a0, 8(s0)
                call    print_exp
                la      a0, s_minus
                call    print_string
                ld      a0, 16(s0)
                call    print_exp
                la      a0, s_right
                call    print_string
                j       5f

3:              li      t1, 4
                bne     t0, t1, 4f

                # neg
                la      a0, s_neg
                call    print_string
                ld      a0, 8(s0)
                call    print_exp
                j       5f

4:              la      a0, s_err
                call    print_string

5:              ld      ra, 8(sp)
                ld      s0, 0(sp)
                addi    sp, sp, 16
                ret
