#minifier v1.0.0

from minifier import minify
from os import path

def main():
    file = input("Input file path (absolute)")
    minify_file = minify(file)

    print(minify_file)

    with open(minify_file[1], 'w') as file:
        file.write(minify_file[0])

    if path.exists(minify_file[1]):
        print (f"File ---{minify_file[1]} successfully minified.")
    else:
        print (f"File ---{minify_file[1]} Not minified")

    

if __name__ == '__main__':
    main()
