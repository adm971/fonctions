import matplotlib.pyplot as plt, random as rdm, numpy as np
from matplotlib.ticker import MultipleLocator
from stats import minmax, square


# FONCTION AFFINE

class Mkaffine() :
    def __init__(self, points=(-10,10,21), rnge=[-5,5], step=1, color="red", a=100, b=100) :
            # DEF POINTS
            self.x = np.linspace(points[0], points[1], points[2]) # les points x 
            if a != 100 :
                self.a = a
            else :
                self.a = rdm.randint(rnge[0], rnge[1])
                
            if b != 100 :
                self.b = b
            else :
                self.b = rdm.randint(rnge[0], rnge[1])
            self.y = [self.a*xi + self.b for xi in self.x] # y = ax + b

            # DEF TYPES
            if self.b == 0 :
                self.type = "linéaire"
            elif self.a == 0 :
                self.type = "constante"
            else : 
                self.type = "affine"

            self.step = step
            self.color = color
            self.range = rnge
    
    # AFFICHER GRAPHIQUE
    def show(self) :
            # TRACER
            self.fig, axes = plt.subplots()
            print(hasattr(self.fig.canvas, "mpl_connect"))

            # GRAPHIQUE
            axes.plot(self.x, self.y) # DROITE
            axes.grid() # GRILLE
            axes.set_xlim(minmax(self.range)) # LIMITE X
            axes.set_ylim(minmax(self.range)) # LIMITE Y
            axes.scatter(0, 0, color=self.color) # POINT ORIGINE

            # AFFICHAGE AXES
            axes.spines['left'].set_position('zero') # Y AU CENTRE
            axes.spines['right'].set_color('none')
            axes.spines['bottom'].set_position('zero') # X AU CENTRE
            axes.spines['top'].set_color('none') 

            # STEPS
            axes.xaxis.set_major_locator(MultipleLocator(self.step)) # 1 à 1
            axes.yaxis.set_major_locator(MultipleLocator(self.step)) # 1 à 1

            # FERMETURE
            self.closed = False 
            self.fig.canvas.mpl_connect('close_event', self._on_close)

            # INFO
            print(self.a, self.b)
            result = f"f(x)={str(self.a)}x{str(self.b)} : {self.type}"
            print(result)
            plt.show() 
            return result
    
    def _on_close(self, event) :
        self.closed = True
        print("figure fermée")



# FONCTION QUADRATIQUE
# f(x) = ax² + bx +
# f(x) = a(x - alpha)² + beta
# si a>0 => minimum en alpha = beta 
# si a<0 => maximum en alpha = beta
# f admet un min ou un max pour alpha = -b/2a
class Mkquadra() : # f(x) = ax² + bx + c==> 5x² + 2x + 1
    def __init__(self, points=(-10, 10, 21), rnge=[-5, 5], step=1, color="red", a=100, b=100, c=100):
        self.color = color 
        self.step = step
        self.type = "quadratique"
        self.range = rnge

        # DEF POINTS
        self.x = np.linspace(points[0], points[1], 1000) # les points x 

        # def a 
        self.a = a if a != 100 else rdm.randint(rnge[0], rnge[1])
        if self.a == 0 : 
            self.a = 2
        # def b
        self.b = b if b != 100 else rdm.randint(rnge[0], rnge[1])
        # def c
        self.c = c if c != 100 else rdm.randint(rnge[0], rnge[1])
        
        # forme canonique f(x) = a(x - alpha)² + beta
        self.y = [self.a*square(xi) + self.b*xi + self.c for xi in self.x] # f(x) = ax² + bx + c


    def show(self):
        # TRACER
        self.fig, self.axes = plt.subplots()
        print(hasattr(self.fig.canvas, "mpl_connect"))

        # GRAPHIQUE
        self.axes.plot(self.x, self.y) # DROITE
        self.axes.grid() # GRILLE
        self.axes.set_xlim(minmax(self.range)) # LIMITE X
        self.axes.set_ylim(minmax(self.range)) # LIMITE Y
        self.axes.scatter(0, 0, color=self.color) # POINT ORIGINE

        # AFFICHAGE AXES
        self.axes.spines['left'].set_position('zero') # Y AU CENTRE
        self.axes.spines['right'].set_color('none')
        self.axes.spines['bottom'].set_position('zero') # X AU CENTRE
        self.axes.spines['top'].set_color('none') 

         # AJOUT DU TEXTE
        # x_pos et y_pos sont les coordonnées pour placer le texte
        result = f"f(x) = {self.a}x² + {self.b}x + {self.c}"

        # STEPS
        self.axes.xaxis.set_major_locator(MultipleLocator(self.step)) # 1 à 1
        self.axes.yaxis.set_major_locator(MultipleLocator(self.step)) # 1 à 1

        # FERMETURE
        self.closed = False 
        self.fig.canvas.mpl_connect('close_event', self._on_close)

        print(self.a, self.b, self.c)
        print(f"f(x)={self.a}x²+{self.b}x+{self.c}")

        self.canon(self.a, self.b, self.c)
        plt.show()


    def _on_close(self, event) :
        self.closed = True
        print("figure fermée")

    def canon(self, a, b, c) : 
        # a * square(x-alpha) + beta
        alpha = -b / (2*a)
        #f(x) = ax² + bx + c
        #f(alpha) = a x alpha² + b x alpha + c
        beta = a*square(alpha) + b*alpha + c 
        canon = f"{a}(x - {alpha})² + {beta}"
        print(canon)
        return canon 


