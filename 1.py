import os
import shutil

current_dir = os.getcwd()
diretory = ['Python files','Image files','Excel files','Ppt file','Pdf files','Executable files','Jar file','msi files','zip files','iso files','Other files','Audio files','Video files']
for i in diretory:
    try:
        os.mkdir(os.path.join(current_dir, i))
    except FileExistsError:
        pass
    except:
        print('got an error in creating a folder')
for f in os.listdir(current_dir):
    filename, file_ext = os.path.splitext(f)

    try:
        if not file_ext:
            pass

        elif file_ext in ('.py'):
            shutil.move(
                os.path.join(current_dir, f'{filename}{file_ext}'),
                os.path.join(current_dir, 'Python files', f'{filename}{file_ext}'))
        elif file_ext in ('.jpg', '.png', '.gif'):
            shutil.move(
                os.path.join(current_dir, f'{filename}{file_ext}'),
                os.path.join(current_dir, 'Image files', f'{filename}{file_ext}'))
        elif file_ext in ('.xls', '.xlsx', '.xltx', '.xlsm'):
            shutil.move(
                os.path.join(current_dir, f'{filename}{file_ext}'),
                os.path.join(current_dir, 'Excel files', f'{filename}{file_ext}'))
        elif file_ext in ('.ppt', '.pptx'):
            shutil.move(
                os.path.join(current_dir, f'{filename}{file_ext}'),
                os.path.join(current_dir, 'Ppt file', f'{filename}{file_ext}'))
        elif file_ext in ('.pdf'):
            shutil.move(
                os.path.join(current_dir, f'{filename}{file_ext}'),
                os.path.join(current_dir, 'Pdf files', f'{filename}{file_ext}'))
        elif file_ext in ('.exe'):
            shutil.move(
                os.path.join(current_dir, f'{filename}{file_ext}'),
                os.path.join(current_dir, 'Executable files', f'{filename}{file_ext}'))
        elif file_ext in ('.jar'):
            shutil.move(
                os.path.join(current_dir, f'{filename}{file_ext}'),
                os.path.join(current_dir, 'Jar file', f'{filename}{file_ext}'))
        elif file_ext in ('.msi'):
            shutil.move(
                os.path.join(current_dir, f'{filename}{file_ext}'),
                os.path.join(current_dir, 'msi files', f'{filename}{file_ext}'))
        elif file_ext in ('.zip','.rar'):
            shutil.move(
                os.path.join(current_dir, f'{filename}{file_ext}'),
                os.path.join(current_dir, 'zip files', f'{filename}{file_ext}'))
        elif file_ext in ('.iso'):
            shutil.move(
                os.path.join(current_dir, f'{filename}{file_ext}'),
                os.path.join(current_dir, 'iso files', f'{filename}{file_ext}'))
        elif file_ext in ('.mkv','.mp4','.avi','.webm','.mov'):
            shutil.move(
                os.path.join(current_dir, f'{filename}{file_ext}'),
                os.path.join(current_dir, 'Video files', f'{filename}{file_ext}'))
        elif file_ext in ('.mp3','.wav'):
            shutil.move(
                os.path.join(current_dir, f'{filename}{file_ext}'),
                os.path.join(current_dir, 'Audio files', f'{filename}{file_ext}'))
                
        else:
            shutil.move(
                os.path.join(current_dir, f'{filename}{file_ext}'),
                os.path.join(current_dir, 'Other files', f'{filename}{file_ext}'))                        

    except (FileNotFoundError, PermissionError)        :
        pass
    