from print import printed

def test_printed():
    #setup
    x = 10
    #assert that it works
    
    assert printed(x) == "Hello World!"
    
    #tear down

def test_printed2():
    x = 1
    assert printed(x) == "Not hello"


def loop_test(x):
    if x >= 10:
        assert printed(x) == "Hello World!"
    else:
        assert printed(x) == "Not hello"

def test_loop_printed():
    for i in range(12):
        loop_test(i)