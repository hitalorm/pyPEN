'''
set_in.py         
Subrotina para configurar os parâmetros de entrada
da simualção

                Autor: Hitalo Rodrigues Mendes
                (hitalo.rm@gmail.com)
                
                Data: 2021/09/21
'''
import re
import math
import shutil

def open_ini(filename):
    file = open(filename, 'r')
    buffer = file.read()
    file.close()
    return buffer
    
def set_config(buffer,time,update):
    time_string ='\n '+str("{0:.1e}".format(time))+'             NUMBER OF HISTORIES (1.0e15 MAX)'
    buffer = re.sub('\n (.*?)NUMBER OF HISTORIES \(1.0e15 MAX\)',time_string,buffer)
    update_string = '\n '+str("{0:.1f}".format(update))+'             UPDATE INTERVAL'
    buffer = re.sub('\n (.*?)UPDATE INTERVAL', update_string, buffer)
    return buffer


def set_particle_type(buffer, kpar):
    string = ' ' + str(kpar)+'                               PARTICLE TYPE'
    buffer = re.sub(' (.*?)                               PARTICLE TYPE',string,buffer)
    return buffer
 
def set_particle_position(buffer,new_z):
    new_coordinates = '0.0  0.0  -'+str("{0:.1f}".format(new_z))+'                COORDINATES (cm) OF BOX CENTER'
    buffer = re.sub('0.0  0.0  -(.*?)                COORDINATES \(cm\) OF BOX CENTER',new_coordinates,buffer)
    return buffer

def set_particle_angle(buffer, new_z, radius_x):
    #radius = 5.641895835
    angle_x = math.atan(radius_x/new_z)
    angle_x = angle_x*180/math.pi
    angle_x = round(angle_x,2)


    new_angle = ' 0.0 ' + str("{0:.2f}".format(angle_x))+'                     DIRECTION POLAR'
    buffer = re.sub(' 0.0 (.*?)                     DIRECTION POLAR',new_angle,buffer)
    return buffer

def set_particle_energy(buffer, energy):
    string = ' '+str("{0:.3e}".format(energy))+'      1.0                   Spectrum table'
    buffer = re.sub('(.*?)      1.0                   Spectrum table', string,buffer)

    string = ' '+str("{0:.3e}".format(energy))+'      -1                    Enter a negative'
    buffer = re.sub('(.*?)      -1                    Enter a negative', string,buffer)

    return buffer

def set_geometry(buffer, name_geo):
    string ='\n '+name_geo
    buffer = re.sub('\n (.*?).geo', string,buffer)
    return buffer

def set_material(buffer, material):
    string = '\n  1   mat/'+material+'.mat'
    buffer = re.sub('\n  1   (.*?).mat', string, buffer)
    return buffer


def write_file(buffer, filename):
    file = open(filename, 'w')
    file.write(buffer)
    file.close()

def set_seed(buffer, seed1, seed2):
    string = '\n ' + str(seed1)+ '  ' + str(seed2) + '              INITIAL RANDOM SEEDS'
    buffer = re.sub('\n (.*?)INITIAL RANDOM SEEDS', string, buffer)
    return buffer


def set_tally_SDD(buffer,thick):
    bins = thick/0.1-2
    string = ' 0.0  '+str("{0:.1f}".format(thick))+'   '+str(int(bins))+'                   ZMIN'
    buffer = re.sub(' 0.0  (.*?)   (.*?)                   ZMIN',string,buffer)
    return buffer

def set_in(filename, hist, update, new_z, energy, material, radius_x, name_geo, kpar, thick):
    buffer = open_ini(filename)
    buffer = set_config(buffer, hist, update)
    buffer = set_particle_type(buffer,kpar)
    buffer = set_particle_energy(buffer,energy)
    buffer = set_particle_position(buffer, new_z)
    buffer = set_particle_angle(buffer, new_z,radius_x)
    buffer = set_geometry(buffer, name_geo)
    buffer = set_material(buffer, material)
    buffer = set_tally_SDD(buffer, thick)
    write_file(buffer, filename)
