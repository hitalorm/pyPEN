'''
create_geo.py    
Subrotina para alterar o arquivo de geometria


                Autor: Hitalo Rodrigues Mendes
                (hitalo.rm@gmail.com)
                
                Data: 2021/09/21
'''
import re


def create_geometry_file(filename,thick):
    file = open(filename)
    lines = file.readlines()
    file.close()
    geo_number = thick
    lines[9] = lines[9].replace(lines[9][10:13], str(float(thick)))
    file = open('run/cylinder.geo','w')
    for line in lines:
        file.write(line)
    file.close()
