def filter_words(st):
    st_list = list(st)
    for i in range(1, len(st_list)):
        st_list[0] = st_list[0].upper()
        if st_list[i].isupper() is True:
            st_list[i] = st_list[i].lower()
        else:
            continue
    st = ' '.join(''.join(st_list).split())
    return st
