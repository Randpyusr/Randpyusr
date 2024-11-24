import methods
# import cards inutilisé pour le moment 
"test de la fonction avec pierre attaque caillou"
methods.set_name('kit1', methods.kit_list, 'carcaters')
methods.set_name('kit1', methods.kit_list, 'carcaters')
methods.printing_status(methods.caracters,'pierre')
methods.printing_status(methods.caracters,'caillou')
methods.attack(methods.caracters['pierre'],methods.caracters['caillou'])
methods.printing_status(methods.caracters,'pierre')
methods.printing_status(methods.caracters,'caillou')
# Test de la fonction carcter_change pour changer de personnage actif
methods.set_name('kit1', methods.kit_list)
methods.set_name('kit1', methods.kit_list)
print(methods.currently_selected)
methods.caracter_change()
print(methods.currently_selected)
print(methods.caracters)
# Rien à faire dans le main pour le moment, création des cartes et des fonctions avant
