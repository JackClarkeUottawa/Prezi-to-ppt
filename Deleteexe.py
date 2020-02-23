import os
def DELETE_ALLadsaf():
    directory = os.fsencode(os.getcwd())
    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        if (filename.endswith('.png') or filename.endswith('.pdf')):
            if os.path.exists(filename):
                os.remove(filename)
            else:
                print('Error Path DOES NOT EXIST')
            continue
        else:
            continue