import random, math
from math import sqrt
from collections import Counter


__all__ = [
    "square", "cube", "sqrt_n", "rule_three", "sigma", "graph",
    "find_t", "increase", "decrease", "resume",
    "moyenne", "pond", "troncature", "geometric",
    "mediane", "mode", "variance", "ecart_type",
    "ecart_abs_moy", "minmax", "etendu", "coef_var",
    "quantile", "iqr", "list_quantiles",
    "z_score", "skewness", "kurtosis",
    "covar", "correl",
    "cumul_sum", "freq_abs", "freq_rel"
]

#Carré
def square(x) :
    return x * x
#Cube
def cube(x) :
    return x * x * x
#Racine n-ième
def sqrt_n(x,n) :
    return x ** (1/n)
#Règle de 3
def rule_three(a, b, c):
    x = a*b/c
    return x
# Sigma 
def sigma(a, b, f): # utiliser lambda pour f
    s = 0
    for i in range(a, b+1):
        s += f(i)
    return s
# print(sigma(1,5,lambda i : square(i) + cube(i)))


# TAUX
def find_t(Vf, Vi) : # Trouver le taux %
    t = (Vf - Vi) / Vi * 100
    print("taux : ", t,"%")
    return t
def increase(t, Vi) : # Augmenter de t%
    Vf = Vi + (Vi * t/100)
    print(Vf)
    return Vf
def decrease(t, Vi) : # Diminuer de t%
    Vf = Vi - (Vi * t/100)
    return Vf



def resume(n):
    verify_list(n)

    return([
        str(moyenne(n)),
        str(troncature(n, 1)),
        str(geometric(n)),
        str(mediane(n)),
        str(mode(n)),

        str(variance(n)),
        str(ecart_type(n)),
        str(ecart_abs_moy(n)),
        str(etendu(n)),
        str(coef_var(n)),

        str(quantile(n, 0.01)),   # centile
        str(iqr(n, 0.01)),
        str(quantile(n, 0.1)),    # décile
        str(iqr(n, 0.1)),
        str(quantile(n, 0.2)),    # quintile
        str(iqr(n, 0.2)),
        str(quantile(n, 0.25)),   # quartile
        str(iqr(n, 0.25)),

        str(z_score(n, random.randint(0, len(n)-1))),
        str(round(skewness(n), 2)),
        str(round(kurtosis(n), 2)),
    ])
   



def print_resume(n) :
    verify_list(n)
    print("\n")

    print("Effectif :", n)
    print("Effectif rangé : ", sorted(n))
    print("nombre d'éléments : ", len(n))
    print("somme : ", sum(n))
    print("produit : ", math.prod(n))
    print("\n")

    print("Mesures de tendance centrale \n")

    moyenne(n, True)
    troncature(n, 1, True)
    geometric(n, True)
    mediane(n)
    mode(n, True)
    print("\n")

    print("Mesures de dispersion \n")

    variance(n, "p", True)
    ecart_type(n)
    ecart_abs_moy(n, True)
    minmax(n, True)
    etendu(n)
    coef_var(n)
    print("\n")

    print("Mesures de position \n")

    quantile(n, 0.01, True) # centile
    iqr(n, 0.01, True)
    print(list_quantiles(n, 100))
    print("\n")
    quantile(n, 0.1, True) # décile 
    iqr(n, 0.1, True)
    print(list_quantiles(n, 10))
    print("\n")
    quantile(n, 0.2, True) # quintile
    iqr(n, 0.2, True)
    print(list_quantiles(n, 20))
    print("\n")
    quantile(n, 0.25, True) # quartile
    iqr(n, 0.25, True)
    print(list_quantiles(n, 25))
    print("\n")

    print("Mesures standardisées \n")
    z_score(n, int(random.randint(0, len(n)-1)))
    print("\n")

    print("Forme de la distribution \n")
    skewness(n, True, "p")
    kurtosis(n, True, "p")
    print("\n")

    print("Autres \n")
    cumul_sum(n, True)
    freq_abs(n, True)
    freq_rel(n, True)
    print("\n")
    




# Mesure d'effectif
def verify_list(n) :
    if not isinstance(n, list) :
        raise TypeError("le paramètre indiquée doit etre une liste")
    if len(n) == 0 :
        raise TypeError("la liste est vide")
    
#Moyenne
def moyenne(n=[], show=False) :
    verify_list(n)

    m = sum(n)/len(n)
    if show == True :
        print("moyenne : ", round(m))
    return round(m)

#Moyenne pondérée
def pond(n, coef=[1], show=False) :
    verify_list(n)
    verify_list(coef)

    mp = sum(n * c for n,c in zip(n, coef)) / sum(coef)
    if show==True:
        print("moyenne pondérée : ", round(mp))
    return round(mp)

#Moyenne troncaturée
def troncature(n=[], k=1, show=False): # moyenne des valeurs sans les extremes
    verify_list(n)

    # Trier la liste
    sort = sorted(n) # liste triée
    nb = len(sort) # nbr élément liste triée

    # Retirer k valeurs au début et k à la fin
    trimmed = sort[k:nb-k] #sort[de K à nb-K]

    # Calculer la moyenne des valeurs restantes
    trim_m = moyenne(trimmed)
    if show == True :
        print("moyenne tronquée :", round(trim_m))
    return round(trim_m)

#Moyenne geometrique
def geometric(n=[], show=False) : # moyenne de la racine n du produit de l'effectif
    verify_list(n)

    x = math.prod(n)
    gm = sqrt_n(x, len(n))
    
    if show == True:
        print("moyenne géométrique : ", round(gm))
    return round(gm)

#Médiane
def mediane(list) : # milieu de l'effectif
    verify_list(list)

    sort = sorted(list)
    n = len(sort)

    match n % 2 :
        case 1 :
            med = sort[n // 2]
        case 0 : 
            a = sort[n//2-1]
            b = sort[n//2]
            med = (a+b)/2
    return round(med)
        
# Mode
def mode(n=[], show=False): # valeur la plus fréquente de l'effectif
    verify_list(n)

    # Compter chaque valeur
    freq = Counter(n)
    
    # Trouver la valeur avec la fréquence la plus élevée
    max_freq = max(freq.values())
    modes = [val for val, nb in freq.items() if nb == max_freq]

    # Si plusieurs modes possibles
    if len(modes) == 1:
        if show == True:
            print("mode :", modes[0])
    else:
        if show == True:
            print("plusieurs modes :", modes)
    return round(int(modes[0]))



#Variance
def variance(n=[], mode="p", show=False) : # moyenne de la somme des carrés des écarts à la moyenne de chaque nombre de l'effectif
    verify_list(n)  

    x_ = moyenne(n)
    if mode != "e" : #population
        var = sum(square(xi - x_) for xi in n) / len(n) # somme des carrés
    else : # échantillon
        var = sum(square(xi - x_) for xi in n) / len(n) - 1

    if show == True :
        print("variance : ", round(var))
    return round(var)

    
#Ecart Type
def ecart_type(n, show=False, mode="p") : # racine carré de la variance
    verify_list(n)

    if mode != "e" : # population
        ecrtype = sqrt(variance(n, "p"))
    else : # échantillon
        ecrtype = sqrt(variance(n, "e"))

    if show :
        print("écart-type : ", round(ecrtype))
    return round(ecrtype)
    
# Ecart absolu moyen
def ecart_abs_moy(n=[], show=False) : # moyenne des ecarts absolus à la moyenne de chaque nombre
    verify_list(n)

    m = moyenne(n) 
    ecarts = [abs(x-m) for x in n] # écart absolu entre chaque x de n et la moyenne m de n
    ecr_m_abs = moyenne(ecarts) # moyenne des ecarts absolus
    if show :
        print("Ecart absolu moyen : ", round(ecr_m_abs))
    return round(ecr_m_abs)

#Minimum, Maximum
def minmax(n=[], show=False) :
    verify_list(n) 

    sort = sorted(n)
    min = sort[0]
    max = sort[-1]
    if show == True :
        print("minimum et maximum : ", min, "<=>", max)
    return min,max

#Etendue
def etendu(n=[]) : # écart entre le min et le max de l'effectif
    verify_list(n)

    min_max = minmax(n)
    e = min_max[-1] - min_max[0]
    return round(e)

# Coefficient de variation
def coef_var(n) :
    verify_list(n)

    a = ecart_type(n)
    x = moyenne(n)

    cv = a/x

    return round(cv)



# Quantile 
def quantile(n, p, show=False) : # p = le quantile choisi
    verify_list(n)
    if not (0 <= p <= 1):
        raise ValueError("p doit être compris entre 0 et 1")

    sort = sorted(n)
    pos = p * (len(n)+1)


    if pos < 1: 
        q = sort[0]
    # Cas où pos >= len(n) → prendre la dernière valeur
    elif pos >= len(sort):
        q = sort[-1]
    else :
        #Interpolation
        lower_index = int(pos) - 1  # position entière inférieure
        fraction = pos - int(pos)    # partie fractionnaire
        q = sort[lower_index] + fraction * (sort[lower_index+1] - sort[lower_index])

    if show:
        match p:
            case 0.01:
                qua = "centile"
            case 0.1:
                qua = "décile"
            case 0.2:
                qua = "quintile"
            case 0.25:
                qua = "quartile"
            case _:
                qua = "quantile"
        print(f"{qua} 1 : {round(q)}")
    return round(q)

# Inter quantile range
def iqr(n, p, show=False) : # quantile soustrait par un quantile plus grand
    if not (0 <= p <= 1):
        raise ValueError("p doit être compris entre 0 et 1")
    Qa = p
    Qz = 1 - Qa
    Qt = 1 + (Qz/Qa) * (Qa+Qz)
    IQR = quantile(n, Qz) - quantile(n, Qa)
    match Qt : 
        case 100 :
            qua = "centile"
        case 10 :
            qua = "décile"
        case 5 : 
            qua = "quintile"
        case 4 : 
            qua = "quartile"
    if Qt != 100 and Qt != 10 and Qt != 5 and Qt != 4 :
        qua = "quantile"
    if show :
        print(f"Ecart inter{qua} entre : Q{Qa*100}({round(quantile(n, Qa))}) - Q{Qz*100}({round(quantile(n, Qz))}) ==> {round(IQR)}")
    return round(IQR)

def list_quantiles(n,K) :
    verify_list(n)
    return [round(quantile(n, k/K)) for k in range(1, K)]




#Score Z, index d'un élément de n
def z_score(n, x, show=False, mode="p") : # Nombre soustrait par la moyenne / divisé par l'écart-type
    verify_list(n) 

    x_ = moyenne(n)
    if mode != "e" :
        a = ecart_type(n, False, "p")
    else : 
        a = ecart_type(n, False, "e")
    
    z = (x - x_)/a
    if show :
        print(f"Score Z de {x} : {z}")
    return z



# Asymétrie (skewness)
def skewness(n, show=False, mode="p") : # Moyenne de la somme du cube du score Z de chaque nombre
    verify_list(n)

    N = len(n)

    if mode != "e" : # population
        skew = (1/N) * (sigma(0, N-1, lambda i : cube(z_score(n, n[i]))))
    else : # échantillon
        skew = (N/((N-1)*(N-2)))*(sigma(0, N-1, lambda i : cube(z_score(n, n[i], False, "e"))))

    if show :
            print("Skewness : ", round(skew))
    return skew

# Aplatissement (kurtosis)
def kurtosis(n, show=False, mode="p") : # Moyenne de la somme(soustrait par 3) des score Z puissance 4 de chaque nombre
    verify_list(n)

    N=len(n)

    if mode != "e" : # population 
        kurt = (1/N) * sigma(0, N-1, lambda i : z_score(n, n[i], False, "p")**4)-3
    else : # échantillon 
        kurt = (N*(N+1))/((N-1)*(N-2)*(N-3)) * sigma(0, N-1, lambda i : z_score(n, n[i], False, "e")**4) - (3*square(N-1))/((N-2)*(N-3))

    if show : 
        print("Kurtosis : ", round(kurt))
    return kurt




# Covariance
def covar(x, y,show=False, mode="p") : # moyenne de la somme de tous les écarts à la moyenne de X et de tous les écarts de Y
    verify_list(x)
    verify_list(y)

    if len(x) != len(y) :
        raise TypeError(f"X{len(x)} et Y{len(y)} sont de longueurs différentes ")
    else :
        N = len(x)
        x_,y_ = moyenne(x), moyenne(y)
        ecart_x = [i-x_ for i in x]
        ecart_y = [i-y_ for i in y]

        if mode != "e" : # population 
            Cov = 1/N * sigma(0, N-1, lambda i : ecart_x[i] * ecart_y[i])
        else :           # echantillon 
            Cov = 1/N-1 * sigma(0, N-1, lambda i : ecart_x[i] * ecart_y[i])

        if show :
            print(f"Covariance entre {x} et {y} : {round(Cov)}" )
    return Cov

# Corrélation
def correl(x,y, show=False, mode="p") : # Covariance de X et Y divisée / par le produit des ecarts-type de X et Y
    verify_list(x)
    verify_list(y)

    if len(x) != len(y) :
        raise TypeError(f"X{len(x)} et Y{len(y)} sont de longueurs différentes")
    else :
        if mode != "e" :
            Corel = covar(x,y)/ecart_type(x)*ecart_type(y)
        else : 
            Corel = covar(x,y, False, "e")/ecart_type(x, False, "e")*ecart_type(y, False, "e")
        
        if show : 
            print(f"Corrélation entre {x} et {y} : {round(Corel)}")
    
    return Corel



# Somme cummulée 
def cumul_sum(n, show=False) : 
    verify_list(n)

    c = [] # S1,S2,S3,S4
    total = 0

    for x in n :
        total += x
        c.append(total)
    
    if show :
        print(f"Somme cumulée : {c}")
    return c

# Fréquence absolue
def freq_abs(n, show=False) : 
    verify_list(n)
    f = Counter(n)

    if show : 
        for key in f :
            f[key] =  round(f[key], 2)
        print(f"Fréquences absolues : {dict(f)}")
    return f


# Fréquence relative
def freq_rel(n, show=False) : 
    verify_list(n)

    N = len(n)
    f = Counter(n)

    for x in f :
        f[x] /= N
    if show : 
        for key in f :
            f[key] =  round(f[key], 2)
        print(f"Fréquences relatives : {dict(f)}")
    return f