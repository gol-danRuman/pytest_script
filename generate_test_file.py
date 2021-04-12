""" Script to create -test.py file for every python module inside a folder 

    Run command:
    python [script] [arg1]
    
    example: python generate_test_file.py eai/
    [script] - file name of script
    [arg1] - directory name

"""

import os
import sys


#Constants
init_file = '__init__'
python_extension = '.py'
test_file_extension = '-test.py'
python_extension_compiled = '.pyc'
dummy_test = '''

def test_dummy():
    pass
'''

def validate_argument():
    ''' Validate the first argument that is directory name which is provided while running script from terminal

        :return Absolute path of directory name
        :rtype: str
    '''
    try:
        directory_name=sys.argv[1]
        if os.path.exists(directory_name):
            return (os.path.abspath(directory_name))
        else :
            raise FileNotFoundError
    except (FileNotFoundError, IndexError):
        print('Please pass directory_name ')


def initialize_file_create(path):
    if(os.path.isdir(path)):
        if not (os.path.isfile(os.path.join(path, '__init__.py'))):
            with open( os.path.join(path , '__init__.py'), 'w+') as fp:
                pass



def generate_test_python_file_in_directory(root_folder): 
    ''' Generates test file for each python file

        :param root_folder Path of the folder to generate test file for python module
        :type root_folder: str
    '''   
    for path, subdirs, files in os.walk(root_folder):
        initialize_file_create(os.path.join(path))
        for name in files:
            if not init_file in name and not python_extension_compiled in name  and python_extension in name and not test_file_extension in name and not test_file_exist(os.path.join(path, name)):
                    print('Test file not found for ', os.path.join(path, name))
                    create_test_file(os.path.join(path, name))

def test_file_exist(file_name):
    ''' Check if the file exist or not

        :param file_name File Path which needs to be checked
        :type file_name: str

        :return File exist or not in given path
        :rtype : boolean
    '''
    if os.path.exists(file_name.replace(python_extension, '')+ test_file_extension):
        return True
    return False

def create_test_file(file_name):
    ''' Creates a test file for the file_name provided

        :param file_name Path of file which need test file
        :type file_name: str
    '''
    path_split_list = file_name.split('/')
    f = open(file_name.replace(python_extension, '')+ test_file_extension, "w+")
    f.write('from ')
    try:
        path_split_list = file_name.split('/')
        root_index = path_split_list.index(sys.argv[1].replace('/',''))
        for value in path_split_list[root_index:] :            
            if root_index < (len(path_split_list) - 1):
                if root_index != (len(path_split_list) - 2):
                    f.write(value+'.')
                else:
                    f.write(value)
            else:
                f.write(' import '+ value.replace(python_extension, '  # noqa: F401,E501'))
            root_index+=1

        f.write("\n")
    except IndexError:
        print('Index error while parsing absolute path of file')

    f.write(dummy_test)
    f.close()


def remove(): 
    ''' Removes test file for each python file

        :param root_folder Path of the folder to generate test file for python module
        :type root_folder: str
    '''   
    for path, subdirs, files in os.walk(validate_argument()):
        for name in files:
            if '-test.py' in name:
                    print('Test file found for ', os.path.join(path, name))
                    os.remove(os.path.join(path, name))


if __name__ == "__main__":
    try:
        root_folder = validate_argument()
        generate_test_python_file_in_directory(root_folder)
    except Exception as e:
        print(e)
