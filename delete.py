import os 
import shutil
import time

def main ():
    deletedFiles = 0
    deletedFolders = 0

    path  = '/PATH_TO_DELETE'
    days  = 30
    seconds  = time.time()-(days*24*60*60)
    if os.path.exists():
        for root_folders, files, folders in os.walk(path):
            if seconds>= get_file_or_folder_age(root_folders):
                remove_folder(root_folders)
                deletedFolders += 1
                break

            else:
                for folder in folders :
                    folder_path = os.path.join(root_folders,folder)
                    if seconds>= get_file_or_folder_age(folder_path):
                        remove_folder(folder_path)
                        deletedFolders += 1
                for file in files :
                    file_path = os.path.join(root_folders,file)
                    if seconds>= get_file_or_folder_age(file_path):
                        remove_file(file_path)
                        deletedFiles += 1  :
    else:
       print(f'{}')                      
      

                     
                               


