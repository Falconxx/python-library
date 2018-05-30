#!/usr/bin/env python

import calc_pack
import dirlist

print('APLIKACJA KORZYSTA Z PAKIETÓW calc_pack ORAZ listdir')

print('\nObliczamy ile płytek 10x20 potrzeba, aby wyłożyć powierzchnię 120x340:')
print(calc_pack.hmcalc.tiles(120,340,10,20))

print('\nListujemy analizę obecnego katalogu (linki symboliczne, linki wskazujące na pliki)')
print(dirlist.dirlist.lll())
