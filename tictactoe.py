grille = [
  ["-", "-", "-"],
  ["-", "-", "-"],
  ["-", "-", "-"]
]

user = True # lorsqu'il est vrai, il fait référence à X, sinon O
turns = 0

def afficher_grille(grille):
  for ligne in grille:
    for inser in ligne:
      print(f"{inser} ", end="")
    print()

def quit(entrée_utilisateur):
  if entrée_utilisateur.lower() == "q": 
    print("Merci d'avoir joué..!")
    return True
  else: return False


def check_input(entrée_utilisateur):
    
  # vérifier si c'est un numéro
  
  if not isnum(entrée_utilisateur): return False
  entrée_utilisateur = int(entrée_utilisateur)
  # Entrer un numéro entre 1 et 9
  if not bounds(entrée_utilisateur): return False

  return True

def isnum(entrée_utilisateur):
  if not entrée_utilisateur.isnumeric(): 
    print("Ce n'est pas un numéro valide...!")
    return False
  else: return True

def bounds(entrée_utilisateur):
  if entrée_utilisateur > 9 or entrée_utilisateur < 1: 
    print("Ce nombre n'appartient pas à l'intervalle [1;9]....!")
    return False
  else: return True

def istaken(coordonnées, grille):
  ligne = coordonnées[0]
  col = coordonnées[1]
  if grille[ligne][col] != "-":
    print("Cette case est déjà prise...!")
    return True
  else: return False

def coordinates(entrée_utilisateur):
  ligne = int(entrée_utilisateur / 3)
  col = entrée_utilisateur
  if col > 2: col = int(col % 3)
  return (ligne,col)

def ajouter_a_grille(coordonnées, grille, active_utilisateur):
  ligne = coordonnées[0]
  col = coordonnées[1]
  grille[ligne][col] = active_utilisateur

def utilisateur_en_cours(user):
  if user: return "x"
  else: return "o"



def verifie_ligne(user, grille):
  for ligne in grille:
    complete_ligne = True
    for inser in ligne:
      if inser != user:
        complete_ligne = False
        break
    if complete_ligne: return True
  return False 

def verifie_colonne(user, grille):
  for col in range(3):
    complete_col = True
    for ligne in range(3):
      if grille[ligne][col] != user:
        complete_col = False
        break
    if complete_col: return True
  return False

def verifie_diagonale(user, grille):
    
  #top left to bottom right
  
  if grille[0][0] == user and grille[1][1] == user and grille[2][2] == user: return True
  elif grille[0][2] == user and grille[1][1] == user and grille[2][0] == user: return True
  else: return False

def iswin(user, grille):
  if verifie_ligne(user, grille): return True
  if verifie_colonne(user, grille): return True
  if verifie_diagonale(user, grille): return True
  return False

while turns < 9:
  active_utilisateur = utilisateur_en_cours(user)
  afficher_grille(grille)
  entrée_utilisateur = input("Veuillez saisir une position de 1 à 9 ou saisir \"q\" pour quitter :")
  if quit(entrée_utilisateur): break
  if not check_input(entrée_utilisateur):
    print("Veuillez réessayer..!")
    continue
  entrée_utilisateur = int(entrée_utilisateur) - 1
  coordonnées = coordinates(entrée_utilisateur)
  if istaken(coordonnées, grille):
    print("Veuillez réessayer..!")
    continue
  ajouter_a_grille(coordonnées, grille, active_utilisateur)
  if iswin(active_utilisateur, grille): 
    print(f"{active_utilisateur.upper()} gagné..!")
    break
  
  turns += 1
  if turns == 9: print("Egalité..!")
  user = not user