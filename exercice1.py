def fizzBuzz(n):
    if n % 3 == 0 and n % 5 == 0:
        resultat = 'fizzBuzz'
        return print(resultat)
    elif n % 3 == 0:
        resultat= 'fizz'
        return print(resultat)
    elif n % 5 == 0:
        resultat = 'Buzz'
        return print(resultat)
    else:
        resultat = n
        return print(n)

if __name__ == "__main__":
    a = int(input("Entrez un nombre : "))
    (fizzBuzz(a))





