'''
Erguei As Mãos
Padre Marcelo Rossi
___________________

Erguei as mãos e dai glória a Deus
Erguei as mãos e dai glória a Deus
Erguei as mãos
E cantai como os filhos do Senhor

Os animaizinhos subiram de dois em dois
Os animaizinhos subiram de dois em dois
O elefante
E os passarinhos, como os filhos do Senhor

(Para não!)
Os animaizinhos subiram de dois em dois
Os animaizinhos subiram de dois em dois
A minhoquinha
E os pinguins, como os filhos do Senhor

Os animaizinhos subiram de dois em dois
Os animaizinhos subiram de dois em dois
O canguru
E o sapinho, como os filhos do Senhor

Deus disse a Noé: Constrói uma arca
Deus disse a Noé: Constrói uma arca
Que seja feita
De madeira para os filhos do Senhor

Por isso...!
Erguei as mãos e dai glória a Deus
Erguei as mãos e dai glória a Deus
Erguei as mãos
E cantai como os filhos do Senhor

Erguei as mãos e dai glória a Deus
Erguei as mãos e dai glória a Deus
Erguei as mãos
E cantai como os filhos do Senhor (de novo!)

Erguei as mãos e dai glória a Deus
Erguei as mãos e dai glória a Deus
Erguei as mãos
E cantai como os filhos do Senhor

E atenção agora, porque

O senhor tem muitos filhos
Muitos filhos ele tem
Eu sou um deles, você também
Louvemos ao senhor

Braço direito

O senhor tem muitos filhos
Muitos filhos ele tem
Eu sou um deles, você também
Louvemos ao senhor

Braço direito, braço esquerdo

O senhor tem muitos filhos
Muitos filhos ele tem (Até que eu tô em forma)
Eu sou um deles, você também
Louvemos ao senhor

Braço direito, braço esquerdo
Perna direita

O senhor tem muitos filhos
Muitos filhos ele tem
Eu sou um deles, você também
Louvemos ao senhor

Braço direito, braço esquerdo
Perna direita, perna esquerda

O senhor tem muitos filhos (muitos filhos)
Muitos filhos ele tem
Eu sou um deles, você também (Que saudade dessa música)
Louvemos ao senhor

Braço direito, braço esquerdo
Perna direita, perna esquerda
Balança a cabeça

O senhor tem muitos filhos
Muitos filhos ele tem
Eu sou um deles, você também
Louvemos ao senhor

Braço direito, braço esquerdo
Perna direita, perna esquerda
Balança a cabeça, dá uma voltinha

O senhor tem muitos filhos
Muitos filhos ele tem (Bonita cruz)
Eu sou um deles, você também
Louvemos ao senhor

Braço direito, braço esquerdo
Perna direita, perna esquerda
Balança a cabeça, dá uma voltinha
Dá um pulinho

O senhor tem muitos filhos (Para não)
Muitos filhos ele tem
Eu sou um deles, você também
Louvemos ao senhor

Braço direito, braço esquerdo
Perna direita, perna esquerda
Balança a cabeça, dá uma voltinha
Dá um pulinho e abraça o irmão
'''


def chorus():

    print("Erguei as mãos e dai glória a Deus")
    print("Erguei as mãos e dai glória a Deus")
    print("Erguei as mãos")
    print("E cantai como os filhos do Senhor\n")


def verse(fst_animal, snd_animal):

    (fst_prefix, fst_animal_name) = fst_animal
    (snd_prefix, snd_animal_name) = snd_animal

    print("Os animaizinhos subiram de dois em dois")
    print("Os animaizinhos subiram de dois em dois")
    print(f"{fst_prefix} {fst_animal_name}")
    print(f"E {snd_prefix} {snd_animal_name}, como os filhos do Senhor\n")


def first_half_half():

    print("Deus disse a Noé: Constrói uma arca")
    print("Deus disse a Noé: Constrói uma arca")
    print("Que seja feita")
    print("De madeira para os filhos do Senhor\n")


def half_division():

    print("E atenção agora, porque\n")


def chorus2():

    print("O senhor tem muitos filhos")
    print("Muitos filhos ele tem")
    print("Eu sou um deles, você também")
    print("Louvemos ao senhor\n")


animals = [
    [
        ("O", "elefante"),
        ("os", "passarinhos")
    ],
    [
        ("A", "minhoquinha"),
        ("os", "pinguins")
    ],
    [
        ("O", "canguru"),
        ("o", "sapinho")
    ]
]

movements = [
    "Braço direito", "braço esquerdo",
    "Perna direita", "perna esquerda",
    "Balança a cabeça", "dá uma voltinha",
    "Dá um pulinho", "abraça o irmão"
]


def original_song():
    # 1st half:

    chorus()

    for pair in animals:
        fst_animal = pair[0]
        snd_animal = pair[1]
        verse(fst_animal, snd_animal)

    first_half_half()

    for i in range(3):
        chorus()
    
    half_division() ##########

    # 2nd half:

    for i in range(len(movements)):
        chorus2()
        for j in range(0, i + 1, 1):
            if j % 2 == 0 and j != i:
                print(movements[j], end=", ")
            else:
                print(movements[j])
        print()

    return


original_song()