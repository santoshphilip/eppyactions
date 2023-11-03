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




def main():
    iddname = iddfhandle
    idfname = StringIO("  Version,8.7;")
    print(getversion(iddname, idfname))

if __name__ == '__main__':
    main()
