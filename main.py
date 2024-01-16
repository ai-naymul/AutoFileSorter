import os 
import shutil as sh 


FOLDER_PATH = 'E:/Downloads'




def organize_folders(FOLDER_PATH):
    file_list = os.listdir(FOLDER_PATH)
    # file_list = [file for file in os.listdir(FOLDER_PATH) if os.path.isfile(os.path.join(FOLDER_PATH, file))]
    for file in file_list:
        _, file_extension = os.path.splitext(file)
        file_extension = file_extension[1:]

        if file_extension == 'exe':
            new_folder = os.path.join(FOLDER_PATH, 'Applications')
        elif file_extension == 'jpg' or file_extension == 'png' or file_extension == 'jpeg' or file_extension == 'jfif':
            new_folder = os.path.join(FOLDER_PATH, 'Images')
        elif file_extension == 'pdf':
            new_folder = os.path.join(FOLDER_PATH, 'PDF Files')
        elif file_extension == 'torrent':
            new_folder = os.path.join(FOLDER_PATH, 'Torrent Download File')

        
        # create a new folder if it doesn't exist
        if not os.path.exists(new_folder):
            os.makedirs(new_folder)

        # get the current file path
        current_file = os.path.join(FOLDER_PATH, file)

        # get the new file path
        new_file = os.path.join(new_folder, file)

        # move the file
        sh.move(current_file, new_file)


organize_folders(FOLDER_PATH=FOLDER_PATH)