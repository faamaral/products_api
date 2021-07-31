
def verify_data(data):
    arg = ['id', 'name', 'description', 'manufacturer', 'price', 'amount']
    i = []
    for d in data.keys():
        for a in arg:
            if d in a:
                i.append(d)
    return len(i)
