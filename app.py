import random

def generate_password(length):
    """
    Génère un mot de passe aléatoire d'une longueur spécifiée.

    Args:
        length (int): La longueur du mot de passe à générer.

    Returns:
        str: Le mot de passe généré.
    """
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()"
    password = ""
    for _ in range(length):
        password += random.choice(characters)
    return password

def main():
    """
    Fonction principale qui demande à l'utilisateur la longueur du mot de passe
    et affiche le mot de passe généré.
    """
    print("Bienvenue dans le générateur de mot de passe !")
    try:
        length = int(input("Entrez la longueur du mot de passe (minimum 8) : "))
        if length < 8:
            print("La longueur doit être d'au moins 8 caractères.")
            return
        password = generate_password(length)
        print(f"Votre mot de passe généré est : {password}")
    except ValueError:
        print("Erreur : veuillez entrer un nombre valide.")

if __name__ == "__main__":
    main()

