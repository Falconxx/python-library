#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import calc_pack
import dirlist

print('APLIKACJA KORZYSTA Z PAKIETÓW calc_pack ORAZ listdir')

print('\nObliczamy cene przewozu ladunku o wielkości 150mx400m w ciągu min 5 dni max 10 dni:')
print(calc_pack.hmcalc.tiles(120,340,5,10))

print('\nListujemy analizę obecnego katalogu (linki symboliczne, linki wskazujące na pliki)')
print(dirlist.dirlist.lll())
