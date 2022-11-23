print("Transfert de chaleur par rayonnement")
print("La tempérture à la surface")
Sig=input("Entrez la valeur de sigma: ")
d=input("Entrez le diamétre  de cylindrique: ")
h=input("Entrez la longueur  de cylindrique: ")
Q=input("Entrez le flux: ")
Lamb=input("Entrez la longueur  d'onde: ")
Lamb2=input("Entrez la longueur  d'onde 2: ")
try:
    Sig=float(Sig)
    d=float(d)
    Q=float(Q)
    Lamb=float(Lamb)
    h = float(h)
    Lamb2 = float(Lamb2)
    Ep=1
    Pi=3.14
    cst=2898
    T= (Q/(Ep*h*d*Pi*Sig*Lamb))
    Lamb = cst / T
    T2 = cst / Lamb2
    Q1 = Ep * Sig * d * h * Pi * (T ** 4)
    print("La température est", T)
    print("La longueur maximal est", Lamb)
    print("La température", T2)
    print("La puissance dégagé est", Q1)
except:
    print("erreur")
