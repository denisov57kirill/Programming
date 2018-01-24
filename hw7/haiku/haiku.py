import random
def noun_pr():
    with open("noun_pr.txt", encoding="utf-8") as f:
        nouns_pr = f.read()
        splited_nouns_pr= nouns_pr.split()
    return random.choice(splited_nouns_pr)


def narech():
    with open("narech.txt", encoding="utf-8") as f:
        narechs = f.read()
        splited_narechs= narechs.split()
    return random.choice(splited_narechs)

def noun_nom():
    with open("noun_nom.txt", encoding="utf-8") as f:
        nouns_nom = f.read()
        splited_nouns_nom= nouns_nom.split()
    return random.choice(splited_nouns_nom)
def predlog():
    with open("predlog.txt", encoding="utf-8") as f:
        predlogs = f.read()
        splited_predlogs= predlogs.split()
    return random.choice(splited_predlogs)
def verb():
    with open("verb.txt", encoding="utf-8") as f:
        verbs = f.read()
        splited_verbs= verbs.split()
    return random.choice(splited_verbs)
def pril2():
    with open("pril2.txt", encoding="utf-8") as f:
        prils2 = f.read()
        splited_prils2= prils2.split()
    return random.choice(splited_prils2)
def pril3():
    with open("pril3.txt", encoding="utf-8") as f:
        prils3 = f.read()
        splited_prils3= prils3.split()
    return random.choice(splited_prils3)


def verse1():
    return predlog() + ' ' + pril2() + ' ' + noun_pr() 

def verse2():
    return noun_nom() + ' ' + verb() + ' ' + narech()+'.'

def verse3():
    return pril3() + ' ' + noun_nom() + '.'

print(verse1())
print(verse2())
print(verse3())

