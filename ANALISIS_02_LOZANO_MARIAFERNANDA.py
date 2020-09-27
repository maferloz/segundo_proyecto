#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 16:28:11 2020

@author: mariafernandalozanocancino
"""
#NOTA IMPORTANTE: Si la base de datos y este archivo (código) no se encuentran en la misma ruta o carpeta,
#no se podrá visualizar la información adecuadamente

#se importan las librerías que se usarán para la realización del código
import pandas as pd
from collections import Counter

#se importa la base de datos de Synergy Logistics
datos_syn = pd.read_csv("synergy_logistics_database.csv")

#aquí se está separando los datos de importaciones y de exportaciones para manejarlos por separado
exportaciones = datos_syn[datos_syn['direction'] == 'Exports']
importaciones = datos_syn[datos_syn['direction'] == 'Imports']


"""
OPCIÓN 1
"""

print('PRIMER ANÁLISIS \n')

#posteriormente se juntan los países de origen y destino, para analizar su incidencia
lista_export = list(exportaciones['origin'] + ' ' + exportaciones['destination'])
lista_import = list(importaciones['origin'] + ' ' + importaciones['destination'])

#se utiliza una de las librerías para analizar cuantas veces se llevó a cabo la ruta y se sacan las mejores 10
contador_export = Counter(lista_export)
print('Las rutas de exportación más concurridas son:', contador_export.most_common(10), '\n')

contador_import = Counter(lista_import)
print('Las rutas de importación más concurridas son:', contador_import.most_common(10), '\n')

#a continuación se calcula el valor monetario total para ambos casos
mejores_export = []
for index, row in exportaciones.iterrows():
    if 'South Korea' in row['origin'] and 'Vietnam' in row['destination']:
        mejores_export.append(row['total_value'])
    elif 'Netherlands' in row['origin'] and 'Belgium' in row['destination']:
        mejores_export.append(row['total_value'])
    elif 'USA' in row['origin'] and 'Netherlands' in row['destination']:
        mejores_export.append(row['total_value'])
    elif 'China' in row['origin'] and 'Mexico' in row['destination']:
        mejores_export.append(row['total_value'])
    elif 'Japan' in row['origin'] and 'Brazil' in row['destination']:
        mejores_export.append(row['total_value'])
    elif 'Germany' in row['origin'] and 'France' in row['destination']:
        mejores_export.append(row['total_value'])
    elif 'South Korea' in row['origin'] and 'Japan' in row['destination']:
        mejores_export.append(row['total_value'])
    elif 'Australia' in row['origin'] and 'Singapore' in row['destination']:
        mejores_export.append(row['total_value'])
    elif 'Canada' in row['origin'] and 'Mexico' in row['destination']:
        mejores_export.append(row['total_value'])
    elif 'China' in row['origin'] and 'Spain' in row['destination']:
        mejores_export.append(row['total_value'])
print('El valor total de las exportaciones es:', sum(mejores_export), '\n')

mejores_import = []
for index, row in importaciones.iterrows():
    if 'Singapore' in row['origin'] and 'Thailand' in row['destination']:
        mejores_export.append(row['total_value'])
    elif 'Germany' in row['origin'] and 'China' in row['destination']:
        mejores_export.append(row['total_value'])
    elif 'China' in row['origin'] and 'Japan' in row['destination']:
        mejores_export.append(row['total_value'])
    elif 'Japan' in row['origin'] and 'Mexico' in row['destination']:
        mejores_export.append(row['total_value'])
    elif 'China' in row['origin'] and 'Thailand' in row['destination']:
        mejores_export.append(row['total_value'])
    elif 'Malaysia' in row['origin'] and 'Thailand' in row['destination']:
        mejores_export.append(row['total_value'])
    elif 'Spain Korea' in row['origin'] and 'Germany' in row['destination']:
        mejores_export.append(row['total_value'])
    elif 'Mexico' in row['origin'] and 'Usa' in row['destination']:
        mejores_export.append(row['total_value'])
    elif 'China' in row['origin'] and 'United Arab Emirates' in row['destination']:
        mejores_export.append(row['total_value'])
    elif 'Brazil' in row['origin'] and 'China' in row['destination']:
        mejores_export.append(row['total_value'])
print('El valor total de las importaciones es:', sum(mejores_export), '\n')


"""
OPCION 2
"""
print('SEGUNDO ANÁLISIS \n')

#empezamos por filtrar los medios de transporte según exportaciones, importaciones y el total
lista_transporte_export = list(exportaciones['transport_mode'])
lista_transporte_import = list(importaciones['transport_mode'])
lista_transporte_total = list(datos_syn['transport_mode'])

#una vez mas definimos los contadores para cada tipo
contador_transporte_export = Counter(lista_transporte_export)
contador_transporte_import = Counter(lista_transporte_import)
contador_transporte_total = Counter(lista_transporte_total)


print('Los tres medios de transporte más utilizados en exportaciones son (medio, veces):', contador_transporte_export.most_common(3), '\n')
print('Los tres medios de transporte más utilizados en importaciones son (medio, veces):', contador_transporte_import.most_common(3), '\n')
print('Los tres medios de transporte más utilizados en total son (medio, veces):', contador_transporte_total.most_common(3), '\n')

#después se usa una sentencia if para calcular el valor de cada medio en cada importaciones, exportaciones y en total

#para las exportaciones
values_transporte_export = []
for index, row in exportaciones.iterrows():
    if 'Sea' in row['transport_mode']:
        values_transporte_export.append(row['total_value'])
    elif 'Rail' in row['transport_mode']:
        values_transporte_export.append(row['total_value'])
    elif 'Road' in row['transport_mode']:
        values_transporte_export.append(row['total_value'])
print('El valor total de los tres medios de transporte más utilizado en las exportaciones es de:', sum(values_transporte_export), '\n')

values_sea_export = []
for index, row in exportaciones.iterrows():
    if 'Sea' in row['transport_mode']:
        values_sea_export.append(row['total_value'])
print('El valor total de las exportaciones por mar es de:', sum(values_sea_export))

values_rail_export = []
for index, row in exportaciones.iterrows():
    if 'Rail' in row['transport_mode']:
        values_rail_export.append(row['total_value'])
print('El valor total de las exportaciones por tren es de:', sum(values_rail_export))

values_road_export = []
for index, row in exportaciones.iterrows():
    if 'Road' in row['transport_mode']:
        values_road_export.append(row['total_value'])
print('El valor total de las exportaciones por carretera es de:', sum(values_road_export))

values_air_export = []
for index, row in exportaciones.iterrows():
    if 'Air' in row['transport_mode']:
        values_air_export.append(row['total_value'])
print('El valor total de las exportaciones por aire es de:', sum(values_air_export), '\n')

#importaciones
values_transporte_import = []
for index, row in importaciones.iterrows():
    if 'Sea' in row['transport_mode']:
        values_transporte_import.append(row['total_value'])
    elif 'Rail' in row['transport_mode']:
        values_transporte_import.append(row['total_value'])
    elif 'Road' in row['transport_mode']:
        values_transporte_import.append(row['total_value'])
print('El valor total de los tres medios de transporte más utilizado en las importaciones es de:',sum(values_transporte_import), '\n')

values_sea_import = []
for index, row in importaciones.iterrows():
    if 'Sea' in row['transport_mode']:
        values_sea_import.append(row['total_value'])
print('El valor total de las importaciones por mar es de:', sum(values_sea_import))

values_rail_import = []
for index, row in importaciones.iterrows():
    if 'Rail' in row['transport_mode']:
        values_rail_import.append(row['total_value'])
print('El valor total de las importaciones por tren es de:', sum(values_rail_import))

values_road_import = []
for index, row in importaciones.iterrows():
    if 'Road' in row['transport_mode']:
        values_road_import.append(row['total_value'])
print('El valor total de las importaciones por carretera es de:', sum(values_road_import))

values_air_import = []
for index, row in importaciones.iterrows():
    if 'Air' in row['transport_mode']:
        values_air_import.append(row['total_value'])
print('El valor total de las importaciones por aire es de:', sum(values_air_import), '\n')

"""
OPCIÓN 3
"""

print('TERCER ANÁLISIS \n')

#se crearon dos nuevos data frames para observar solamente los datos de los valores totales de cada país para exportaciones e importaciones
valores_export = pd.concat([exportaciones['origin'], exportaciones['total_value']], axis=1, keys=['origen export', 'total_value'])
valores_import = pd.concat([importaciones['origin'], importaciones['total_value']], axis=1, keys=['origen import', 'total_value'])


#para saber el valor total para exportaciones e importaciones se usa el commando len y así podremos sacar los porcentajes
sum(valores_export['total_value'])
sum(valores_import['total_value'])

#a continuación se usa el commando count para saber cuántas veces aparece cada país y así poder comparar si existe correlación entre ser país que mas genera valor así como que más se repite
#con los valores obtenidos se construyó una tabla para mejor visualización
#primero se mostrará para las exportaciones
valores_export['origen export'].value_counts()

#ahora con el uso de un for loop y usando los commandos if y elif, damos la orden que se sume el valor y se junte en una nueva lista el valor total para cada país
china_filtrados_export = []
usa_filtrados_export = []
gmy_filtrados_export = []
jpn_filtrados_export = []
sk_filtrados_export = []
frn_filtrados_export = []
uk_filtrados_export = []
aus_filtrados_export = []
nth_filtrados_export = []
mex_filtrados_export = []
rus_filtrados_export = []
can_filtrados_export = []
ind_filtrados_export = []
ita_filtrados_export = []
ast_filtrados_export = []
brz_filtrados_export = []
spn_filtrados_export = []
sgp_filtrados_export = []
swz_filtrados_export = []
bel_filtrados_export = []

for index, row in valores_export.iterrows():
    if 'China' in row['origen export']:
        china_filtrados_export.append(row['total_value'])
    elif 'USA' in row['origen export']:
        usa_filtrados_export.append(row['total_value'])
    elif 'Germany' in row['origen export']:
        gmy_filtrados_export.append(row['total_value'])
    elif 'Japan' in row['origen export']:
        jpn_filtrados_export.append(row['total_value'])
    elif 'South Korea' in row['origen export']:
        sk_filtrados_export.append(row['total_value'])
    elif 'France' in row['origen export']:
        frn_filtrados_export.append(row['total_value'])
    elif 'United Kingdom' in row['origen export']:
        uk_filtrados_export.append(row['total_value'])
    elif 'Australia' in row['origen export']:
        aus_filtrados_export.append(row['total_value'])
    elif 'Netherlands' in row['origen export']:
        nth_filtrados_export.append(row['total_value'])
    elif 'Mexico' in row['origen export']:
        mex_filtrados_export.append(row['total_value'])
    elif 'Russia' in row['origen export']:
        rus_filtrados_export.append(row['total_value'])
    elif 'Canada' in row['origen export']:
        can_filtrados_export.append(row['total_value'])
    elif 'India' in row['origen export']:
        ind_filtrados_export.append(row['total_value'])
    elif 'Italy' in row['origen export']:
        ita_filtrados_export.append(row['total_value'])
    elif 'Austria' in row['origen export']:
        ast_filtrados_export.append(row['total_value'])
    elif 'Brazil' in row['origen export']:
        brz_filtrados_export.append(row['total_value'])
    elif 'Spain' in row['origen export']:
        spn_filtrados_export.append(row['total_value'])
    elif 'Singapore' in row['origen export']:
        sgp_filtrados_export.append(row['total_value'])
    elif 'Switzerland' in row['origen export']:
        swz_filtrados_export.append(row['total_value'])
    elif 'Belgium' in row['origen export']:
        bel_filtrados_export.append(row['total_value'])
        
print(sum(china_filtrados_export),'', sum(usa_filtrados_export),'', sum(gmy_filtrados_export),'', sum(jpn_filtrados_export),'', sum(sk_filtrados_export),'', sum(frn_filtrados_export),'', sum(uk_filtrados_export),'', sum(aus_filtrados_export),'', sum(nth_filtrados_export),'', sum(mex_filtrados_export),'', sum(rus_filtrados_export),'', sum(can_filtrados_export),'', sum(ind_filtrados_export),'', sum(ita_filtrados_export),'', sum(ast_filtrados_export),'', sum(brz_filtrados_export),'', sum(spn_filtrados_export),'', sum(sgp_filtrados_export),'', sum(swz_filtrados_export),'', sum(bel_filtrados_export), '\n') 

#ahora para importaciones se repite el proceso anterior
valores_import['origen import'].value_counts()

china_filtrados_import = []
jpn_filtrados_import = []
usa_filtrados_import = []
gmy_filtrados_import = []
mex_filtrados_import = []
sgp_filtrados_import = []
mal_filtrados_import = []
spn_filtrados_import = []
frn_filtrados_import = []
sk_filtrados_import = []
brz_filtrados_import = []
aus_filtrados_import = []
ita_filtrados_import = []
uk_filtrados_import = []
can_filtrados_import = []
rus_filtrados_import = []
uae_filtrados_import = []
vie_filtrados_import = []

for index, row in valores_import.iterrows():
    if 'China' in row['origen import']:
        china_filtrados_import.append(row['total_value'])
    elif 'Japan' in row['origen import']:
        jpn_filtrados_import.append(row['total_value'])
    elif 'USA' in row['origen import']:
        usa_filtrados_import.append(row['total_value'])
    elif 'Germany' in row['origen import']:
        gmy_filtrados_import.append(row['total_value'])
    elif 'Mexico' in row['origen import']:
        mex_filtrados_import.append(row['total_value'])
    elif 'Singapore' in row['origen import']:
        sgp_filtrados_import.append(row['total_value'])
    elif 'Malaysia' in row['origen import']:
        mal_filtrados_import.append(row['total_value'])
    elif 'Spain' in row['origen import']:
        spn_filtrados_import.append(row['total_value'])
    elif 'France' in row['origen import']:
        frn_filtrados_import.append(row['total_value'])
    elif 'South Korea' in row['origen import']:
        sk_filtrados_import.append(row['total_value'])
    elif 'Brazil' in row['origen import']:
        brz_filtrados_import.append(row['total_value'])
    elif 'Australia' in row['origen import']:
        aus_filtrados_import.append(row['total_value'])
    elif 'Italy' in row['origen import']:
        ita_filtrados_import.append(row['total_value'])
    elif 'United Kingdom' in row['origen import']:
        uk_filtrados_import.append(row['total_value'])
    elif 'Canada' in row['origen import']:
        can_filtrados_import.append(row['total_value'])
    elif 'Russia' in row['origen import']:
        rus_filtrados_import.append(row['total_value'])
    elif 'United Arab Emirates' in row['origen import']:
        uae_filtrados_import.append(row['total_value'])
    elif 'Vietnam' in row['origen import']:
        vie_filtrados_import.append(row['total_value'])
    
print(sum(china_filtrados_import),'', sum(jpn_filtrados_import),'', sum(usa_filtrados_import),'', sum(gmy_filtrados_import),'', sum(mex_filtrados_import),'', sum(sgp_filtrados_import),'', sum(mal_filtrados_import),'', sum(spn_filtrados_import),'', sum(frn_filtrados_import),'', sum(sk_filtrados_import),'', sum(brz_filtrados_import),'', sum(aus_filtrados_import),'', sum(ita_filtrados_import),'', sum(uk_filtrados_import),'', sum(can_filtrados_import),'', sum(rus_filtrados_import),'', sum(uae_filtrados_import),'', sum(vie_filtrados_import), '\n')

#con esto se contruyen ambas tablas y se sacan los porcentajes para cada país




