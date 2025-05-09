import numpy as np

# Chapitre 1, exercice 14
# Mauvais code
'''
x = 0.0;
while (x != 1.0):
    x = x + 0.1;
    break; # Donne une boucle sans le break
print(x)
'''

# Bon code
'''
x = 0.0;
e = 0.001;
while (x - 1.0) < e :
    for i in range(10) :
        x += 0.1;
print(x)
'''
# Chapitre 1, exercice 19
# Algo 1
'''
def f_1(x):
    if x == 0 :
        return 1;
    else :
        return (np.exp(x) - 1) / x

# Algo 2
def f_2(x) :
    y = np.exp(x);
    if y == 1 :
        return 1;
    else :
        return (y - 1) / np.log(y); # Changement de x pour log(y)

x_values = [1e-1, 1e-5, 1e-8, 1e-12, 1e-16, 0.0]

print("   x\t\tAlgo1\t\t\tAlgo2")
for x in x_values:
    f1 = f_1(x)
    f2 = f_2(x)
    print(f"{x:.1e}\t{f1:.16f}\t{f2:.16f}")
'''
