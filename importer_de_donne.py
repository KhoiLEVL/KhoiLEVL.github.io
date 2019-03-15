# -*- coding: utf-8 -*-
"""
Created on Sat Nov  3 23:24:55 2018

@author: lhkho
"""

import os
import csv
from lxml import etree

#traduire le nom de element de fraçais à anglais
def translateFrancais(a):
    translationTable = str.maketrans("éàèùâêîôûç", "eaeuaeiouc")
    a = a.translate(translationTable)
    return a

#ouvrir fichier csv
with open('ponctualite-mensuelle-transilien.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=";")
    list_element_tmp = next(csv_reader)
#étape de récupérer le nom de élément et transferer ces nom comme des nom des element  
    list_element = []
    for i in list_element_tmp:
        i = translateFrancais(i)
        i = i.replace("\'","_")
        list_element.append(i.replace(" ", "_"))
#créer l'arbre de xml avec le nœud principal "classe" et sa deux élément des services 
    root = etree.Element('classe')
    root_service_RER = etree.Element('service')
    root_service_RER.attrib['nom_service']='RER'
    root.append(root_service_RER)
    root_service_Transilien = etree.Element('service')
    root_service_Transilien.attrib['nom_service']='Transilien'
    root.append(root_service_Transilien)
    tree = etree.ElementTree(root)
    list_ligne_service_RER = []
    list_ligne_service_Transilien = []
#lire chaque ligne du fichier csv et recuperer des valeur
    for row in csv_reader:
    #lire des données dans le cas de service "RER"
        if row[2] == "RER":
            #lire des données dans le cas de deja lire cette Ligne avant 
            if row[0] in list_ligne_service_RER:
                #chercher et acceder à le node du cette Ligne
                b = (".//Ligne[@nom_ligne='" + row[3] +"']")
                a = root_service_RER.find(b)
                #ajouter de element ponctualite_mensuelle dans cet Ligne
                elm_ligne_ponctualite = etree.Element("ponctualite_mensuelle")
                elm_ligne_ponctualite_date = etree.Element(list_element[1])
                elm_ligne_ponctualite_date.text = row[1]
                elm_ligne_ponctualite_taux = etree.Element(list_element[5])
                elm_ligne_ponctualite_taux.text = row[5]
                elm_ligne_ponctualite_nombre = etree.Element(list_element[6])
                elm_ligne_ponctualite_nombre.text = row[6]
                elm_ligne_ponctualite.append(elm_ligne_ponctualite_date)
                elm_ligne_ponctualite.append(elm_ligne_ponctualite_taux)
                elm_ligne_ponctualite.append(elm_ligne_ponctualite_nombre)
                a.append(elm_ligne_ponctualite)
            #Lire des données dans la première fois de lire cette Ligne avant
            else:
                list_ligne_service_RER.append(row[0])
                #créér et ajouter le nouveau Ligne
                elm_ligne = etree.Element(list_element[3])
                elm_ligne.attrib['nom_ligne']=row[3]
                elm_ligne_ID = etree.Element(list_element[0])
                elm_ligne_ID.text = row[0]
                elm_ligne_nom = etree.Element(list_element[4])
                elm_ligne_nom.text = row[4]
                #ajouter de element ponctualite_mensuelle dans cet Ligne
                elm_ligne_ponctualite = etree.Element("ponctualite_mensuelle")
                elm_ligne_ponctualite_date = etree.Element(list_element[1])
                elm_ligne_ponctualite_date.text = row[1]
                elm_ligne_ponctualite_taux = etree.Element(list_element[5])
                elm_ligne_ponctualite_taux.text = row[5]
                elm_ligne_ponctualite_nombre = etree.Element(list_element[6])
                elm_ligne_ponctualite_nombre.text = row[6]
                elm_ligne_ponctualite.append(elm_ligne_ponctualite_date)
                elm_ligne_ponctualite.append(elm_ligne_ponctualite_taux)
                elm_ligne_ponctualite.append(elm_ligne_ponctualite_nombre)
                elm_ligne.append(elm_ligne_ID)
                elm_ligne.append(elm_ligne_nom)
                elm_ligne.append(elm_ligne_ponctualite)
                root_service_RER.append(elm_ligne)
        #lire des données dans le cas de service "RER""Transilien"
        if row[2] == "Transilien":
             #lire des données dans le cas de deja lire cette Ligne avant 
            if row[0] in list_ligne_service_Transilien:
                b = (".//Ligne[@nom_ligne='" + row[3] +"']")
                a = root_service_Transilien.find(b)
                elm_ligne_ponctualite = etree.Element("ponctualite_mensuelle")
                elm_ligne_ponctualite_date = etree.Element(list_element[1])
                elm_ligne_ponctualite_date.text = row[1]
                elm_ligne_ponctualite_taux = etree.Element(list_element[5])
                elm_ligne_ponctualite_taux.text = row[5]
                elm_ligne_ponctualite_nombre = etree.Element(list_element[6])
                elm_ligne_ponctualite_nombre.text = row[6]
                elm_ligne_ponctualite.append(elm_ligne_ponctualite_date)
                elm_ligne_ponctualite.append(elm_ligne_ponctualite_taux)
                elm_ligne_ponctualite.append(elm_ligne_ponctualite_nombre)
                a.append(elm_ligne_ponctualite )     
            #Lire des données dans la première fois de lire cette Ligne 
            else:
                list_ligne_service_Transilien.append(row[0])
                #créér et ajouter le nouveau Ligne
                elm_ligne = etree.Element(list_element[3])
                elm_ligne.attrib['nom_ligne']=row[3]
                elm_ligne_ID = etree.Element(list_element[0])
                elm_ligne_ID.text = row[0]
                elm_ligne_nom = etree.Element(list_element[4])
                elm_ligne_nom.text = row[4]
                #ajouter de element ponctualite_mensuelle dans cet Ligne
                elm_ligne_ponctualite = etree.Element("ponctualite_mensuelle")
                elm_ligne_ponctualite_date = etree.Element(list_element[1])
                elm_ligne_ponctualite_date.text = row[1]
                elm_ligne_ponctualite_taux = etree.Element(list_element[5])
                elm_ligne_ponctualite_taux.text = row[5]
                elm_ligne_ponctualite_nombre = etree.Element(list_element[6])
                elm_ligne_ponctualite_nombre.text = row[6]
                elm_ligne_ponctualite.append(elm_ligne_ponctualite_date)
                elm_ligne_ponctualite.append(elm_ligne_ponctualite_taux)
                elm_ligne_ponctualite.append(elm_ligne_ponctualite_nombre)
                elm_ligne.append(elm_ligne_ID)
                elm_ligne.append(elm_ligne_nom)
                elm_ligne.append(elm_ligne_ponctualite)
                root_service_Transilien.append(elm_ligne)
    #ecrire le fichier de document xml
    tree.write('ponctualite-mensuelle-transilien.xml', pretty_print=True, xml_declaration=True, encoding="utf-8") 
                     
