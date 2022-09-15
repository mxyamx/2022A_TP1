
def decomposer(secondes):

    # TODO: Assigner à la variable "annees" le nombre d'années
    annees = int(secondes/31536000)
    secondes= secondes-31536000*annees
    print(annees, 'années')

    # TODO: Assigner à la variable "semaines" le nombre de semaines restantes
    semaines = int(secondes / 604800)
    secondes = secondes-604800*semaines
    print(semaines, 'semaines')

    # TODO: Assigner à la variable "jours" le nombre de jours restants
    jours = int(secondes / 86400)
    secondes = secondes-86400*jours
    print(jours, 'jours')

    # TODO: Assigner à la variable "heures" le nombre d'heures restantes
    heures = int(secondes / 3600)
    secondes = secondes - 3600*heures
    print(heures, 'heures')

    # TODO: Assigner à la variable "minute" le nombre de minutes restantes
    minutes = int(secondes / 60)
    secondes = secondes - 60*minutes
    print(minutes, 'minutes')

    # TODO: Assigner à la variable "secondes" le nombre de secondes restantes
    secondes = int(secondes)
    reste = secondes
    print(secondes, 'secondes')

    # TODO: Afficher le nombres d'années, semaines, jours, heures, minutes et secondes
    print(annees ,semaines ,jours ,heures ,minutes ,secondes)

    return (annees ,semaines ,jours ,heures ,minutes ,secondes)

if __name__ == '__main__':
    secondes = int(input("Entrer les secondes: "))
    print(decomposer(secondes))
