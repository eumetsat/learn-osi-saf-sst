#! /usr/bin/env python
# -*- coding: utf-8 -*-

'''fonctions relatives a matplotlib'''

import sys
import os
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcol

#-----------------------------------------------------------------------------
def make_colormap_spk(fname):
    '''
    fabrique une colormap matplotlib a partir d'un fichier "spk"
    au format des palettes ferret (0-100)

    entree : le nom du fichier de la table couleur
    sortie : la colormap matplotlib
             ou None si erreur
    '''
    try:
        # lecture du fichier spk
        lines = open(fname, 'r').readlines()
        # enleve retours chariot et lignes de commentaires
        lines = [x[:-1] for x in lines ]
        lines = [x for x in lines if not '!' in x]
        lines = [x for x in lines if not 'RGB' in x]
        lines = [x for x in lines if x!='']

        # recupere les valeurs (x,r,v,b) entre 0 et 1.
        val = []
        for line in lines:
             val.append([float(x)/100. for x in line.split()])

        # construit un dictionnaire pour LinearSegmentedColormap
        segments= {'red': [], 'green': [], 'blue': []}
        for l in range(len(val)):
             for i,rvb in enumerate(['red','green','blue']):
                segments[rvb].append( (val[l][0], val[l][i+1] ,val[l][i+1]) )

        # fait la colormap
        name = os.path.splitext(fname)[0]
        colormap = mcol.LinearSegmentedColormap(name, segments)
        return colormap

    except:
        print('err')
        return None

#-----------------------------------------------------------------------------
def make_colormap_fix(fname):
    '''
    fabrique une colormap matplotlib pour comptes entiers et dynamique fixe
    a partir d'un fichier type palette ferret (0-100) ou en comptes RVB

    entree : le nom du fichier de table couleur
    sorties: la colormap matplotlib
             le compte minimum de la table couleur (vaut 0)
             le compte maximum de la table couleur
             ou (None,None,None) si erreur
    '''
    try:
        # lecture du fichier de table couleur
        lines = open(fname, 'r').readlines()
        # enleve retours chariot et lignes de commentaires
        lines = [x[:-1] for x in lines ]
        lines = [x for x in lines if not '!' in x]
        lines = [x for x in lines if not 'RGB' in x]
        lines = [x for x in lines if x!='']

        # recupere les valeurs (x,r,v,b) entre 0 et 1.
        val = []
        txt = ' '.join(lines)
        values = np.array(txt.split(), dtype=float)
        if (values.max() > 100.)  :
            # le fichier est en comptes RVB
            f = 255.
            f0= len(lines)-1
            for line in lines:
                v = [float(x) for x in line.split()]
                val.append([v[0]/f0, v[1]/f, v[2]/f, v[3]/f])
        else:
            # le fichier est en (0-100)
            for line in lines:
                val.append([float(x)/100. for x in line.split()])

        # construit un dictionnaire pour LinearSegmentedColormap
        segments= {'red': [], 'green': [], 'blue': []}
        for l in range(len(val)):
             for i,rvb in enumerate(['red','green','blue']):
                segments[rvb].append( (val[l][0], val[l][i+1] ,val[l][i+1]) )

        # fait la colormap
        name = os.path.splitext(fname)[0]
        colormap = mcol.LinearSegmentedColormap(name, segments)
        return (colormap,0,len(val)-1)

    except:
        print('err')
        return (None,None,None)
#-----------------------------------------------------------------------------
