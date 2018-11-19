def list_animals(animals):
    list_animals = []
    tempo_list = list(animals)
    for i in tempo_list:
        list_animals.append('{0}. {1}\n'.format(tempo_list.index(i)+1, i))
    nimals = ''.join(list_animals)
    return nimals
