import unittest
import parameterized as parameterized
from ohce import Ohce

#Automatique, palindrome, anglais, soir. OK
#Automatique, non-palindrome, français, matin. OK
#Saisie libre du client, langue et moment actuels du système.


class OhceTest(unittest.TestCase):
    # Test "salutation" (palindrome, anglais, soir)
    @parameterized.parameterized.expand([
        ("anglais","soiree","sos", "sos\n Well said")
        ])
    def test_miroir_langue_periode_bonjour(self,langue,periode_journee,mot,attendu):
        # ETANT DONNE une langue ET une période de la journée
        ohce = Ohce()

        # QUAND on saisit une chaine de caractère
        resultat = ohce.miroir(mot,langue,periode_journee)

        # ALORS "salutation" est retournée avant tout dans la langue choisie
        self.assertIn(attendu,resultat)

    # Test "au revoir" (non-palindrome, français, matin)
    @parameterized.parameterized.expand([
        ("francais","matin","test", "Au revoir")
        ])
    def test_miroir_langue_periode_au_revoir(self,langue,periode_journee,mot,attendu):
        # ETANT DONNE une langue ET une période de la journée
        ohce = Ohce()

        # QUAND on saisit une chaine de caractère
        resultat = ohce.miroir(mot,langue,periode_journee)

        # ALORS "au revoir" est retourné après tout dans la langue choisie
        self.assertIn(attendu,resultat)

    # Test "au revoir" (saisie libre, langue et moment actuels du système)
    mot = input('Entrez un mot :\n')
    miroir = mot[::-1]
    if mot == miroir:
        attendu = mot + "\n Bien dit"
    else:
        attendu = "Bon après-midi"
    @parameterized.parameterized.expand([
        ("francais","apres_midi",mot,attendu)
        ])
    def test_miroir_langue_periode_au_revoir_system(self,langue,periode_journee,mot,attendu):
        # ETANT DONNE une langue ET une période de la journée du système
        ohce = Ohce()

        # QUAND on saisit une chaine de caractère
        resultat = ohce.miroir_system(mot,langue,periode_journee)

        # ALORS "au revoir" est retourné après tout dans la langue choisie et en fonction de l'heure du système
        self.assertIn(attendu,resultat)

if __name__ == '__main__':
    unittest.main()