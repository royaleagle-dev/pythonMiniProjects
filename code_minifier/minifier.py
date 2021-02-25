import re
import os


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
    new_file_name = 'min_'+file_name
    new_path = my_file.replace(file_name, new_file_name)
    return [data_string, new_path]

#get current file extension
