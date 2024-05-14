from hacom import hacom
from laptopword_vp import laptopworld_vp
from laptopword_gm import laptopworld_gm
from final import final
class Preprocessing:
    def hacom_preprocessing(file):
        hacom(file)

    def ltw_vp_preprocessing(file):
        laptopworld_vp(file)

    def ltw_gm_preprocessing(file):
        laptopworld_gm(file)

    def preprocessing(files):
        for file in files:
            if file == 'hacom.json':
                hacom(file)
            elif file == 'laptopworld_vp.json':
                laptopworld_vp(file)
            elif file == 'laptopworld_gaming.json':
                laptopworld_gm(file)
            
        final()


def main():
    Preprocessing.preprocessing(['hacom.json', 'laptopworld_vp.json', 'laptopworld_gaming.json'])

if __name__ == '__main__':
    main()