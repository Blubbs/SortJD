import os
import shutil

mypath = "D:\Download\JDownloader\\"

def get_filepaths(directory):
    """
    This function will generate the file names in a directory
    tree by walking the tree either top-down or bottom-up. For each
    directory in the tree rooted at directory top (including top itself),
    it yields a 3-tuple (dirpath, dirnames, filenames).
    """
    file_paths = []  # List which will store all of the full filepaths.

    # Walk the tree.
    for root, dirs, files in os.walk(directory):
        for filename in files:
            # Join the two strings in order to form the full filepath.
            filepath = os.path.join(root, filename)
            file_paths.append(filepath)

    return file_paths

def move_file(files, destination):
    """
    Move files to a new directory.
    """
    for i in files:
        shutil.move(i, destination + os.path.basename(i))

def delete_folder(directory):
    """
    Delete all empty folders in the directory.
    """
    for root, dirs, files in os.walk(directory):
        for i in dirs:
            try:
                os.rmdir(root + i)
            except OSError:
                pass


full_file_paths = get_filepaths(mypath)

#for  i in full_file_paths:
#    print i

move_file(full_file_paths, mypath)

delete_folder(mypath)
