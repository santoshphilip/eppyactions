"""read an IDF file"""

import eppy

from io import StringIO
try:
    import iddv800
except ModuleNotFoundError as e:
    import eppyactions.iddv800 as iddv800
iddfhandle = StringIO(iddv800.iddtxt)
from eppy import modeleditor
from eppy.modeleditor import IDF


def getversion(iddname, idfname):
    """return the version number of the idf file"""
    IDF.setiddname(iddname)
    idf = IDF(idfname)
    version = idf.idfobjects['version'][0]
    versionnumber = version.Version_Identifier
    return versionnumber

def getversion_1(iddname, idfname):
    """return the version number of the idf file
    uses eppy.idfopen
    needs E+ installed"""
    idf = eppy.openidf(idfname)
    version = idf.idfobjects['version'][0]
    versionnumber = version.Version_Identifier
    return versionnumber



def main():
    iddname = iddfhandle
    idfname = StringIO("  Version,9.2.0;")
    print(getversion(iddname, idfname))

if __name__ == '__main__':
    main()
