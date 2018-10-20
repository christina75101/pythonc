def areYouPlayingBanjo(name):
    name_list = list(name)
    if name_list[0] is "r" or name_list[0] is "R":
        return "{} plays banjo".format(''.join(name_list))
    else:
        return "{} does not play banjo".format(''.join(name_list))

