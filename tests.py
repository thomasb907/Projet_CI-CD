import subprocess
import pytest

def test_program_builds():
    """Vérifie que le programme s'exécute sans erreur."""
    try:
        # Lancer le script principal
        subprocess.run(["python", "main.py"], check=True)
    except subprocess.CalledProcessError:
        pytest.fail("Le programme n'a pas pu être exécuté correctement.")

