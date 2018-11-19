def double_char(s):
    s_list = list(s)
    list_string = []
    for i in s_list:
        list_string.append(''.join(i+i))
    string = ''.join(list_string)
    return string
