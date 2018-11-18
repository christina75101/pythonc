def double_char(s):
    ''' doubles every sign in the string '''
    new_string  = ''
    for i in str(s):
        new_string += 2*i
    return new_string
