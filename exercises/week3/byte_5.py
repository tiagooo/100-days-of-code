# Bite 5. Parse a list of names


NAMES = ['arnold schwarzenegger', 'alec baldwin', 'bob belderbos',
         'julian sequeira', 'sandra bullock', 'keanu reeves',
         'julbob pybites', 'bob belderbos', 'julian sequeira',
         'al pacino', 'brad pitt', 'matt damon', 'brad pitt']

def dedup_and_title_case_names(names):
#remove duplicates    
    names = list(dict.fromkeys(names))
#capitalize names on list 
    names = [name.title() for name in names]
    return names

def sort_by_surname_desc(names):
    names = dedup_and_title_case_names(names)
#sort names by surname
    sort_names = sorted(names, key=lambda x: x.split(" ")[-1], reverse=True)
    return sort_names

def shortest_first_name(names):
    names = dedup_and_title_case_names(names)
#returns the shortest name on the list
    short_name = 'abcsd'
    for name in names:
        test = name.split(" ")
        for subname in test:
            if len(subname) < len (short_name):
                short_name = subname
    return short_name