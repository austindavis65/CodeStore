from cisc108 import assert_equal
def letters_up_to_char(long_word, char):
    new = ''
    x=True
    for letter in long_word:
        if letter != char:
            new += letter
        else:
            return new
#assert_equal(letters_up_to_char('coderoxthesox',"x"),'codero')
