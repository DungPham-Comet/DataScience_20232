from hacom import hacom
from laptopword_vp import laptopworld_vp
from laptopword_gm import laptopworld_gm
from final import final
import os
class Preprocessing:
    def hacom_preprocessing(files):
        hacom(files)

    def ltw_vp_preprocessing(file):
        laptopworld_vp(file)

    def ltw_gm_preprocessing(file):
        laptopworld_gm(file)

    def preprocessing(files):
        hacom([files[0], files[1]])
        laptopworld_gm(files[2])
        laptopworld_vp(files[3])
        final()

def get_files_preprocess():
    # Get the directory of the current script
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Construct the relative path to the 'database/latest_files' directory
    directory = os.path.join(script_dir, '../database/latest_files')

    # Get the absolute path to the directory
    directory = os.path.abspath(directory)

    files = os.listdir(directory)
    files = [os.path.join(directory, file) for file in files]
    return files

def main():
    files = get_files_preprocess()
    Preprocessing.preprocessing(files)

if __name__ == '__main__':
    main()