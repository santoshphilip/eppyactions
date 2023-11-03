"""pytest for getversion"""

import pytest
from io import StringIO
import eppyactions.eppyread as eppyread
import eppyactions.iddv800 as iddv800
iddfhandle = StringIO(iddv800.iddtxt)

@pytest.mark.parametrize(
    "iddname, idfname, expected",
    [
    (iddfhandle, StringIO("  Version,8.7;"), "8.7"), # iddname, idfname, expected
    ]
)
def test_getversion(iddname, idfname, expected):
    """pytest for getversion"""
    result = eppyread.getversion(iddname, idfname)
    assert result == expected
