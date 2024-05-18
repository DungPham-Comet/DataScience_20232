from hacom import hacom
from laptopword_vp import laptopworld_vp
from laptopword_gm import laptopworld_gm
from final import final
class Preprocessing:
    def hacom_preprocessing(files):
        hacom(files)

    def ltw_vp_preprocessing(file):
        laptopworld_vp(file)

    def ltw_gm_preprocessing(file):
        laptopworld_gm(file)

    def preprocessing(files):
        hacom_files = []
        for file in files:
            if file == 'hacom_vp.json':
                hacom_files.append(file)
            elif file == 'hacom_gm.json':
                hacom_files.append(file)
            elif file == 'laptopworld_vp.json':
                laptopworld_vp(file)
            elif file == 'laptopworld_gaming.json':
                laptopworld_gm(file)

        if len(hacom_files) == 2:
            hacom(hacom_files)
            
        final()


def main():
    Preprocessing.preprocessing(['hacom_vp.json', 'hacom_gm.json' ,'laptopworld_vp.json', 'laptopworld_gaming.json'])

if __name__ == '__main__':
    main()