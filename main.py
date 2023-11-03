from math import sqrt
from math import acos, sin
from math import pi

def degToPi(d):
    return d * (pi / 180)

class Point:
    def __init__(self, x, y): #Initialise le point
        self.x = x #Coordonnee X
        self.y = y #Coordonnee Y

    def data(self): #Retourne les donnes du point sous forme de liste
        return [self.x, self.y]

    def __str__(self):
        return f"x: {self.x}, y: {self.y}" #Renvoie les coordonnés x, y du point




class Segment:
    def __init__(self, _p1, _p2): #Initalise le segment
        self.p1 = _p1 #Point 1
        self.p2 = _p2 #Point 2

    def pente(self):
        return (self.p2.y - self.p1.y)/(self.p2.x - self.p1.x) #Calcule le coef dir avec la formule : m = (Yb-Ya)/(Xb-Xa)

    def norme(self):
        #la formule de la norme est : N = ((Xb - Xa)**2 + (Yb - Ya)**2)**1/2
        return sqrt(((self.p2.x - self.p1.x)**2) + ((self.p2.y - self.p1.y)**2))

    def __str__(self):
        return f"p1: ({str(self.p1)}), p2: ({str(self.p2)})" #Renvoie-les coordonnes correspondentes à chaque point du seg




class Figure:
    def __init__(self, listeSeg): #Initialise la figure
        self.listeSeg = listeSeg            #Tous les segs de la figure
        self.nbAretes = len(self.listeSeg) #Nombres des arretes de la figure

    def sommets(self): #Pour trouver la liste de points de la figure
        listeSom = [] #var pour stocker les points
        for seg in self.listeSeg: #Ajoutons tous les points/extremites des segments
            listeSom.append(seg.p1.data())
            listeSom.append(seg.p2.data())

        for a in enumerate(listeSom):
            for b in enumerate(listeSom):
                if a[1] == b[1] and not a[0] == b[0]: #Verifions que nous n'avons pas de doubles
                    listeSom.pop(a[0]) #faisons un pop() de l'element qui est double
        return listeSom #Retournons le resultat

    def perimetre(self): #Calculons le perimetre
        #Un perimetre est la somme des normes de toutes les aretes qui le forme.
        #Nous avons deja une fonction qui calcule la norme d'un seg dans la Classe Segment
        p = 0 #Le perimetre
        for seg in self.listeSeg:
            p += seg.norme()
        return p

    def estQuadrilatere(self):
        if self.nbAretes == 4:
            return True
        return False

    def estParallelograme(self): #POUR REGARDER SI LA FIGURE EST UN PARALLELOGRAMME FAITES QUE LA LISTE DE SEGMENTS EST DANS
        # L'ORDRE AVEC LES POINTS A B C D POUR LES SEGMENTS DANS LA LISTE RESPECTIVEMENT : AB-BC-CD-DA OU ALORS
        #Regarder si la figure possede 4 arretes
        if self.estQuadrilatere():
            #Regarder si AB // DC et AD // BC
            if self.listeSeg[0].norme() == self.listeSeg[2].norme() and self.listeSeg[1].norme() == self.listeSeg[3].norme():
                return True
            return False


    def estRectangle(self):
        #Pour savoir si ce parallelograme est un rectangle.
        #Il faut et il suffit que le Rectangle avec AB // CD et DA // BC (AVEC LE RECTANGLE SOUS ORDRE AB-BC-CD-DA)
        #que A(y) = B(y) et A(x) = D(x) aussi que C(x) = B(x) et C(y) = D(y)
        if self.estParallelograme():
            A = self.sommets()[0]
            B = self.sommets()[1]
            C = self.sommets()[2]
            D = self.sommets()[3]

            if A[1] == B[1] and A[0] == D[0] and C[0] == B[0] and C[1] == D[1]:
                return True
            return False
        return False


    def estCarre(self):
        #Pour savoir si cette figure est carré il faut que tous les
        if self.estRectangle():
            a = True
            for seg in self.listeSeg:
                if a:
                    if seg.norme() == self.listeSeg[0].norme():
                        a = True
                    else:
                        return False
            return True
        return False
    def estTriangle(self):
        #Regarder si la figure possede 3 arretes
        if self.nbAretes == 3:
            return True
        return False

    def Aire(self):
        #Voir si c'est un triangle
        a = self.listeSeg[0].norme()
        b = self.listeSeg[1].norme()
        c = self.listeSeg[2].norme()
        if self.estTriangle():
            #Utilise la formule de heron
            #S = (p(p-a)(p-b)(p-c))**1/2 avec p = (a+b+c)/2

            #Pour rendre le calcul plus simple :

            p = (a+b+c)/2


            print(f"a:{a}, b:{b}, c:{c}, p:{p}\n")
            print(f"{p}({p-a})({p-b})({p-c})")
            return round(sqrt(abs(p*(p-a)*(p-b)*(p-c))), 3)
        if self.estCarre():
            return a*a
        if self.estRectangle():
            return a*b
        if self.estParallelograme():
            A = self.sommets()[0]
            B = self.sommets()[1]
            D = self.sommets()[3]
            return (B[0] - A[0]) * (D[1] - A[1])
        if self.estQuadrilatere():
            a = self.listeSeg[3].norme()
            b = self.listeSeg[0].norme()
            c = self.listeSeg[1].norme()
            d = self.listeSeg[2].norme()
            A = self.sommets()[0]
            B = self.sommets()[1]
            C = self.sommets()[2]
            D = self.sommets()[3]
            print(f"Norme : a : {a}, b : {b}, c : {c}, d : {d}")
            return 0.5*a*d*sin(acos(degToPi((((A[0]-D[0])*(C[0]-D[0]))+(A[1]-D[1])*(C[1]-D[1]))/a*d))) + 0.5*c*b*sin(acos(degToPi((((A[0]-B[0])*(C[0]-B[0]))+(A[1]-B[1])*(C[1]-B[1]))/b*c)))

    def __str__(self): #str(Figure)
        value = f"nbAretes : {self.nbAretes}\n" #Ici montrons les nombres de segments avant des affiches
        value += f"Perimetre : {self.perimetre()}\n"
        for seg in range(len(self.listeSeg)): #Prennons les segments de notre Figure
            value += f"posSeg : {seg + 1}, {str(self.listeSeg[seg])}\n" #Ajoutons à notre resultat la position du segment en termes de liste de la figure et
                                                                         #ajoutons donc les donnes du seg : str(seg)
        return value

p1 = Point(0, 0)
p2 = Point(1, 3)
p3 = Point(2.5, 2)
p4 = Point(3, 0)

seg1 = Segment(p1, p2)
seg2 = Segment(p2, p3)
seg3 = Segment(p3, p4)
seg4 = Segment(p4, p1)

fig = Figure([seg1, seg2, seg3, seg4]) #seg4
print(fig.Aire())

