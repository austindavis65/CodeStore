Recursive evaluator
===================

In this step you will implement the full evaluator that handles
recursive expressions. It builds naturally from the version in the
previous step:

    def eval(exp: *expression) -> int:
        set up stack frame

        tag = exp.tag
        if tag == 1:        # literal case
            # use the memory layout of a literal variant
            result = exp.n

        elif tag == 2:      # plus case
            # use the memory layout of a plus variant
            left_ptr = exp.left
            left_val = eval(left_ptr)
            right_ptr = exp.right
            right_val = eval(right_ptr)
            result = left_val + right_val
            
        elif tag == 3:      # minus case
            # use the memory layout of a minus variant
            left_ptr = exp.left
            left_val = eval(left_ptr)
            right_ptr = exp.right
            right_val = eval(right_ptr)
            result = left_val - right_val

        elif tag == 4:      # negation case
            # use the memory layout of a negation variant
            child_ptr = exp.child
            child_val = eval(child_ptr)
            result = -child_val

        else:
            result = -1

        clean up stack frame
        return result

This uses *structural recursion*, which is a recursive function
whose structure mimics that of the recursive data it operates on.

You do not need to do anything special to make recursion work: as
long as you are using the stack correctly a recursive call is like
any other function call. One key to using recursion correctly is to
be clear on what the function does: given a pointer to an expression
it returns and integer that is the result of evaluating that
expression. Make sure that when you call `eval` you give it a
pointer to an expression, and then trust that it will return with an
integer after evaluating that expression.
