from os import path
from CtrlFacultad import ManejadorFacultad


if __name__ == "__main__":
    
    facultades = ManejadorFacultad(path.dirname(__file__)+"/Facultades.csv")
    
    """for facultad in facultades.getFacultades():
        
        print("*****" + facultad.getNbre())
        print(facultad.getCarreras())
    """
    facultades.Menu()