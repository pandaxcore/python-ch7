def sanitize(data):
    if '-' in data:
        splitter = '-'
    elif ':' in data:
        splitter = ':'
    else:
        return(data)
    
    (mins, secs) = data.split(splitter)

    return(mins + '.' + secs)

def get_data(file_name):
    with open(file_name) as file:
        data = file.readline()
    return(data.strip().split(','))

james = get_data('james2.txt')

(james_name, james_dob) = james.pop(0), james.pop(0)

clean_james = []

for each_item in james:
    clean_james.append(sanitize(each_item))

print(james_name + ' ' + james_dob + ' best time`s are ' + str(sorted(set(clean_james))[0:3]))