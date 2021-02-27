import re
import os


def minify_file_name(file_name):
    pattern = re.compile(r'([a-zA-Z]+)([.]{1})([a-zA-Z]{2,10})')
    items = re.findall(pattern, file_name)
    new_file_name = items[0][0]+'_min'+items[0][1]+items[0][2]
    return new_file_name


#print (minify_file_name('olaoluwa.css'))
    


def minify(my_file):
    patterns = {'spaces': r'\s'}
    data_string = ''
    with open(my_file, 'r') as file:
        data = file.readlines()
        lines_length = len(data)
        for i in range(0, lines_length):
            new_data = re.sub(patterns['spaces'], '', data[i])
            data_string += new_data
    file_name = os.path.basename(my_file)
    new_file_name = minify_file_name(file_name)
    new_path = my_file.replace(file_name, new_file_name)
    return [data_string, new_path]

#get current file extension
