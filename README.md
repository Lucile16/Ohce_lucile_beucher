# Ohce_lucile_beucher

**Pour vérifier chacune des étapes suivantes, il faut se placer dans le dossier correspondant (Etape_1... ou Etape_2... ou Etape_3... ou Etape_4...) dans le terminal et lancer la commande "py -m ohce_test". Chaque étape a été réalisée avec la méthode TDD (Test Driven Development).**

### <ins>Etape 1 :</ins>
- QUAND on saisit une chaîne ALORS celle-ci est renvoyée en miroir
- QUAND on saisit un palindrome ALORS celui-ci est renvoyé ET « Bien dit » est envoyé ensuite
- QUAND on saisit une chaîne ALORS « Bonjour » est envoyé avant toute réponse
- QUAND on saisit une chaîne ALORS « Au revoir » est envoyé en dernier

---

### <ins>Etape 2 :</ins>
ETANT DONNE un utilisateur parlant une langue
- QUAND on saisit un palindrome ALORS celui-ci est renvoyé ET « Bien dit » est envoyé dans cette langue ensuite

ETANT DONNE un utilisateur parlant une langue
- QUAND on saisit une chaîne ALORS « Bonjour » est envoyé dans cette langue avant tout

ETANT DONNE un utilisateur parlant une langue
- QUAND on saisit une chaîne ALORS « Au revoir » est envoyé dans cette langue en dernier

---

### <ins>Etape 3 :</ins>
ETANT DONNE un utilisateur parlant une langue ET que la période de la journée est « période »
- QUAND on saisit une chaîne ALORS « salutation » de cette langue à cette période est envoyé avant tout

ETANT DONNE un utilisateur parlant une langue ET que la période de la journée est « période »
- QUAND on saisit une chaîne ALORS « Au revoir » dans cette langue à cette période est envoyé en dernier

---

### <ins>Etape 4 :</ins>
TESTS DE RECETTE
- Automatique, palindrome, anglais, soir
- Automatique, non-palindrome, français, matin
- Saisie libre du client, langue et moment actuels du système

