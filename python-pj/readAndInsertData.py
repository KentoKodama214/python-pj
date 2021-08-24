#! /usr/bin/env python

# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

import pandas as pd
import sys
import settings
import re
import csv
import zipfile
import pymysql.cursors

__author__ = "kodamakento"
argvs = sys.argv
argc = len(argvs)
    
try:
    conn = pymysql.connect(host=settings.HOST,
                    user=settings.USER,
                    db=settings.DB,
                    charset='utf8',
                    cursorclass=pymysql.cursors.DictCursor)
    
    # WPP Total Population
    df = pd.read_csv(settings.RESOURCE_PATH + settings.WPP_TOTAL_POPULATION_BY_SEX, delimiter=',', quoting = csv.QUOTE_ALL, compression='zip', memory_map=True)
    df.fillna({'PopMale':df['PopTotal']/2, 'PopFemale':df['PopTotal']/2, 'PopDensity':0}, inplace=True)

    # SDG Labour Income
    df2 = pd.read_csv(settings.RESOURCE_PATH + settings.SDG_LABOUR_INCOME, delimiter=',', quoting = csv.QUOTE_ALL, compression='zip', memory_map=True)
    df2.fillna({'obs_status':'', 'obs_status.label':''}, inplace=True)

    # WTO Imports
    with zipfile.ZipFile(settings.RESOURCE_PATH + settings.WTO_IMPORTS, 'r') as zip: 
        csvfile = zip.open(zip.namelist()[0], 'r')
        df3 = pd.read_csv(csvfile, encoding_errors='ignore', delimiter=',', memory_map=True)
        df3['Reporting Economy ISO3A Code'].fillna('', inplace=True)
        df3['Partner Economy ISO3A Code'].fillna('', inplace=True)
        df3['Value Flag Code'].fillna('', inplace=True)
        df3['Value Flag'].fillna('', inplace=True)
        df3['Text Value'].fillna('', inplace=True)
        df3['Value'].fillna('', inplace=True)
    
    # WTO Exports
    with zipfile.ZipFile(settings.RESOURCE_PATH + settings.WTO_EXPORTS, 'r') as zip: 
        csvfile = zip.open(zip.namelist()[0], 'r')
        df4 = pd.read_csv(csvfile, encoding_errors='ignore', delimiter=',', memory_map=True)
        df4['Reporting Economy ISO3A Code'].fillna('', inplace=True)
        df4['Partner Economy ISO3A Code'].fillna('', inplace=True)
        df4['Value Flag Code'].fillna('', inplace=True)
        df4['Value Flag'].fillna('', inplace=True)
        df4['Text Value'].fillna('', inplace=True)
        df4['Value'].fillna('', inplace=True)

    # WEO GDP
    df5 = pd.read_csv(settings.RESOURCE_PATH + settings.WEO_GDP, delimiter='\t', encoding_errors='ignore', quoting = csv.QUOTE_ALL, compression='zip', memory_map=True)
    df5.drop('Estimates Start After', axis=1, inplace=True)
    df5.dropna(thresh=2, inplace=True)
    df5['Subject Notes'].fillna('', inplace=True)
    df5['Scale'].fillna('', inplace=True)
    df5['Country/Series-specific Notes'].fillna('', inplace=True)
    df5_gdp_year_column_list = [s for s in df5.columns.values.tolist() if re.match('[0-9]{4}', s)]
    df5_parameter_column_list = [s for s in df5.columns.values.tolist() if s not in df5_gdp_year_column_list]
    
    cols = df5_parameter_column_list + ['Year', 'GDP']
    df5_norm = pd.DataFrame(data=[], index=None, columns=cols, dtype=None, copy=False)
    
    for column in df5_gdp_year_column_list:
        df5[column].fillna('0', inplace=True)
        df5[column] = df5[column].str.replace(',', '')
        df5[column] = df5[column].str.replace('--', '0')
        df5_norm = df5_norm.append(df5[df5_parameter_column_list].assign(Year=column).assign(GDP=df5[column]))

    with conn.cursor() as cursor:
        cursor.execute("SHOW TABLES FROM `" + settings.DB + "`;")
        tables = cursor.fetchall()
        table_list = []
        for table in tables:
            table_list.append(table['Tables_in_' + settings.DB])
        
        # WPP Total Population
        if("WPP2019_TotalPopulationBySex" in table_list):
            cursor.execute(settings.TRUNCATE_WPP_TOTAL_POPULATION_BY_SEX)
        else:
            cursor.execute(settings.CREATE_WPP_TOTAL_POPULATION_BY_SEX)
        cursor.executemany(settings.INSERT_WPP_TOTAL_POPULATION_BY_SEX, df.values.tolist())
    
        # SDG Labour Income
        if("SDG_LabourIncome" in table_list):
            cursor.execute(settings.TRUNCATE_SDG_LABOUR_INCOME)
        else:
            cursor.execute(settings.CREATE_SDG_LABOUR_INCOME)
        cursor.executemany(settings.INSERT_SDG_LABOUR_INCOME, df2.values.tolist())
        
        # WTO Imports
        if("WtoData_Import" in table_list):
            cursor.execute(settings.TRUNCATE_WTO_IMPORTS)
        else:
            cursor.execute(settings.CREATE_WTO_IMPORTS)
        cursor.executemany(settings.INSERT_WTO_IMPORTS, df3.values.tolist())
        
        # WTO Exports
        if("WtoData_Export" in table_list):
            cursor.execute(settings.TRUNCATE_WTO_EXPORTS)
        else:
            cursor.execute(settings.CREATE_WTO_EXPORTS)
        cursor.executemany(settings.INSERT_WTO_EXPORTS, df4.values.tolist())
        
        # WEO GDP
        if("WEO_GDP" in table_list):
            cursor.execute(settings.TRUNCATE_WEO_GDP)
        else:
            cursor.execute(settings.CREATE_WEO_GDP)
        cursor.executemany(settings.INSERT_WEO_GDP, df5.values.tolist())
        
        # WEO GDP Normalization
        if("WEO_GDP_norm" in table_list):
            cursor.execute(settings.TRUNCATE_WEO_GDP_NORM)
        else:
            cursor.execute(settings.CREATE_WEO_GDP_NORM)
        cursor.executemany(settings.INSERT_WEO_GDP_NORM, df5_norm[df5_norm['GDP']!='0'].values.tolist())
        
        # countries view
        if("countries" in table_list):
            cursor.execute("DROP VIEW countries;")    
        cursor.execute(settings.CREATE_COUNTRY_VIEW)
        
        # analysis data view
        if("analysis_data" in table_list):
            cursor.execute("DROP VIEW analysis_data;")    
        cursor.execute(settings.CREATE_ANALYSIS_DATA_VIEW)
        
        conn.commit()
finally:
    conn.close()