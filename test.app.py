import unittest
from app import generate_password

class TestPasswordGenerator(unittest.TestCase):
    """
    Classe de test pour le générateur de mot de passe.
    """

    def test_generate_password_length(self):
        """
        Tester que le mot de passe a la bonne longueur.
        """
        length = 10
        password = generate_password(length)
        self.assertEqual(len(password), length, f"Le mot de passe doit avoir {length} caractères")
        
    def test_generate_password_characters(self):
        """
        Tester que le mot de passe ne contient que des caractères valides.
        """
        valid_characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()"
        password = generate_password(15)
        for char in password:
            self.assertIn(char, valid_characters, f"Le caractère '{char}' n'est pas valide.")
    
    def test_generate_password_minimum_length(self):
        """
        Tester que la longueur minimale est respectée.
        """
        password = generate_password(8)
        self.assertGreaterEqual(len(password), 8, "La longueur du mot de passe doit être au moins 8.")

if __name__ == "__main__":
    unittest.main()

