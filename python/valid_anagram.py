'''
Given two strings s and t,
return TRUE if is an anagram of s,
and FALSE otherwise.
'''

def anagram(org, shuf):
    if len(org) != len(shuf): return False      # sino son cadenas el mismo tamaño adios

    ctr_org, ctr_shu = {}, {}                   # hashmap como contador para cada cadena

    for s, t in zip(org, shuf):                 # Iteramos sobre los valores de los parametros
        ctr_org[s] = 1 + ctr_org.get(s, 0)      # Se agrega el item a cada hashmap como llave, y
        ctr_shu[t] = 1 + ctr_shu.get(t, 0)      # se le suma 1 sino existe el item se inicializa

    return ctr_org == ctr_shu


if __name__ == '__main__':
    words = [
        ('anagram', 'nagaram'),  # true
        ('anagram', 'anagaram'), # false
        ('rat', 'car'),          # false
    ]
    for s, t in words:
        print(anagram(s, t))
