#!/usr/bin/env python
# -*- coding: utf-8 -*-
def majuscule(bonjour):
    resultat = ''
    for lettre in mot:
        # TODO completer la fonction ici
        
        resultat += lettre
    return mot


if __name__ == '__main__':
    mots = [
        'riz',
        'cours',
        'voiture',
        'oiseau',
        'bonjour',
        'églantier',
        'arbre'
    ]
    for i in range(len(mots)):
        mots[i] = majuscule(mots[i])

    print(majuscule('bonjour'))
