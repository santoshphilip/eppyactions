"""pytest for getversion"""

import importlib
import pytest
from io import StringIO
import eppy
import eppy.modeleditor
import eppyactions.eppyread as eppyread
import eppyactions.iddv800 as iddv800
iddfhandle = StringIO(iddv800.iddtxt)

@pytest.mark.parametrize(
    "iddname, idfname, expected",
    [
    (iddfhandle, StringIO("  Version,23.2.0;"), "23.2.0"), # iddname, idfname, expected
    ]
)
def test_getversion(iddname, idfname, expected):
    """pytest for getversion"""
    importlib.reload(eppy.modeleditor)
    result = eppyread.getversion(iddname, idfname)
    assert result == expected


@pytest.mark.parametrize(
    "iddname, idfname, expected",
    [
    (iddfhandle, StringIO("  Version,23.2.0;"), "23.2.0"), # iddname, idfname, expected
    (iddfhandle, StringIO("  Version,8.3.0;"), "8.3.0"), # iddname, idfname, expected
    ]
)
def test_getversion_1(iddname, idfname, expected):
    """pytest for getversion_1"""
    importlib.reload(eppy.modeleditor)
    result = eppyread.getversion_1(iddname, idfname)
    assert result == expected
