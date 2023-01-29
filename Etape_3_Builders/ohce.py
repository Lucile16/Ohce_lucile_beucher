import dummy_langue_periode as dummy_langue_periode
import constantes_salutation as salutation
import constantes_au_revoir as au_revoir

class Ohce:

    def miroir(self,mot, langue,periode):
        miroir = mot[::-1]
        bien_dit_langue = self.langue_palindrome(langue)
        bonjour_langue_choisie = self.bonjour_langue_periode(langue,periode)
        au_revoir_langue_choisie = self.au_revoir_langue_choisie(langue,periode)

        if mot == miroir:
            return miroir + bien_dit_langue
        return bonjour_langue_choisie + "\n " + miroir + "\n " + au_revoir_langue_choisie
    
    def langue_palindrome(self,langue):
        langue_actuelle = langue.lower()
        if langue_actuelle == "francais":
            return "\n Bien dit"
        else :
            return "\n Well said"
    
    def bonjour_langue_periode(self,langue,periode):
        langue_actuelle = langue.lower()
        periode_actuelle = periode.lower()
        if langue_actuelle == "francais":
            match periode_actuelle:
                case "matin":
                    return salutation.francais.MATIN
                case "apres_midi":
                    return salutation.francais.APRES_MIDI
                case "soiree":
                    return salutation.francais.SOIREE
                case "nuit":
                    return salutation.francais.NUIT
        if langue_actuelle == "anglais":
            match periode_actuelle:
                case "matin":
                    return salutation.anglais.MATIN
                case "apres_midi":
                    return salutation.anglais.APRES_MIDI
                case "soiree":
                    return salutation.anglais.SOIREE
                case "nuit":
                    return salutation.anglais.NUIT

        return dummy_langue_periode.dummy_au_revoir_langue_periode(langue,periode)
        

    def au_revoir_langue_choisie(self,langue,periode):
        langue_actuelle = langue.lower()
        periode_actuelle = periode.lower()

        if langue_actuelle == "anglais":
            match periode_actuelle:
                case "matin":
                    return au_revoir.anglais.MATIN
                case "apres_midi":
                    return au_revoir.anglais.APRES_MIDI
                case "soiree":
                    return au_revoir.anglais.SOIREE
                case "nuit":
                    return au_revoir.anglais.NUIT
        
        if langue_actuelle == "francais":
            match periode_actuelle:
                case "matin":
                    return au_revoir.francais.MATIN
                case "apres_midi":
                    return au_revoir.francais.APRES_MIDI
                case "soiree":
                    return au_revoir.francais.SOIREE
                case "nuit":
                    return au_revoir.francais.NUIT
        return dummy_langue_periode.dummy_au_revoir_langue_periode(langue,periode)