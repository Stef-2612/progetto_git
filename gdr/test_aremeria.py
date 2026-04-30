import pytest
from armeria import equipaggia_artefatto

def guerriero base():
    return {
        "hp": 100,
        "livello": 10,
        "classe": "mago",
        
    }

def test_guerriero_caduto():
    with pytest.raises