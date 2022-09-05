
def maximo(a, b):
    return max(a,b)

def longitud(l):
    return len(l)

def palindromo(s):
    for i in range(len(s)//2):
        print(s[i], s[len(s)-1-i])
        if s[i] != s[len(s)-1-i]:
            return False
    return True

def multiplica(i, c):
    return i*c

if __name__ == '__main__':
    print(maximo(12, 1))
    print(longitud('Hola mundo'))
    print(multiplica(5, 's'))
    print(palindromo('anitalagordalagartonanotragaladrogalatina'))
