
import numpy as np
A = np.array([5, 10, 15, 20])
B = np.array([1, 2, 3, 4])
print("A :", A)
print("B :", B)
addition = A + B
multiplication = A * B        
puissances = A ** 2   
print("A + B =", addition)
print("A * B =", multiplication)
print("A ** 2 =", puissances)
C = np.array([1, 2, 3])        
D = np.array([[10], [20], [30]]) 
print("\nBroadcasting C + D :\n", C + D)
E = np.array([1, 2, 3], dtype=int)
F = np.array([0.5, 1.5, 2.5], dtype=float)
print("\nE + F =", E + F)       
print("dtype du résultat :", (E + F).dtype)
angles = np.linspace(0, np.pi, 5) 
sinus = np.sin(angles)
logarithmes = np.log(angles[1:]) 
print("Angles :", angles)
print("sin(angles) :", sinus)
print("log(angles[1:]) :", logarithmes)
print("exp(A)   :", np.exp(A))   
print("sqrt(B)  :", np.sqrt(B))   
print("abs([-1, -2, 3]) :", np.abs([-1, -2, 3]))  
print("round([1.2, 2.7, 3.5]) :", np.round([1.2, 2.7, 3.5]))
masque = A > 10
print("Masque A > 10 :", masque)
valeurs_filtrées = A[masque]
print("Valeurs de A > 10 :", valeurs_filtrées)
masque_composé = (A > 10) & (A < 20)
print("Masque (A > 10) & (A < 20) :", masque_composé) 
print("Valeurs filtrées :", A[masque_composé])
addition_scalaire = A + 5
print("A + 5 =", addition_scalaire) 
M = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])
vecteur_ligne = np.array([10, 20, 30])
resultat = M + vecteur_ligne
print("M + vecteur_ligne :\n", resultat)
vecteur_colonne = np.array([[10],
                            [20],
                            [30]])
resultat_colonne = M + vecteur_colonne
print("M + vecteur_colonne :\n", resultat_colonne)
C = (A * 2) + np.sin(A) - np.mean(A)
print("Opération composite sur A :", C)
log_A = np.log(A)
masque_log = log_A > 2
print("log(A) > 2 :", log_A[masque_log])
print("Shape de A :", A.shape)
print("Shape de C :", C.shape)