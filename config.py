import os

FPS = 30
FRAME = [320, 160]

base_path = os.getcwd()
output_file_dir = 'video/'
output_file_name = 'capturedVideo.avi'
DIR_PATH = os.path.join(base_path, output_file_dir)

if os.path.exists(DIR_PATH):
    temp_file_path = os.path.join(DIR_PATH, output_file_name)
    if os.path.exists(temp_file_path):
        os.remove(temp_file_path)
    PATH = temp_file_path
else:
    os.mkdir(DIR_PATH)
    temp_file_path = os.path.join(DIR_PATH, output_file_name)
    if os.path.exists(temp_file_path):
        os.remove(temp_file_path)
    PATH = temp_file_path




