#! /usr/bin/env python

# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

import numpy as np
import pandas as pd
import sys
import settings
import re
import csv
import zipfile
import pymysql.cursors
from sqlalchemy import create_engine

__author__ = "kodamakento"
argvs = sys.argv
argc = len(argvs)
    
try:
    conn = pymysql.connect(host=settings.host,
                    user=settings.user,
                    db=settings.db,
                    charset='utf8',
                    cursorclass=pymysql.cursors.DictCursor)
    
    # WPP Total Population
    df = pd.read_csv(settings.resource_path + settings.wpp_total_population_by_sex, delimiter=',', quoting = csv.QUOTE_ALL, compression='zip', memory_map=True)
    df.fillna({'PopMale':df['PopTotal']/2, 'PopFemale':df['PopTotal']/2, 'PopDensity':0}, inplace=True)

    # SDG Labour Income
    df2 = pd.read_csv(settings.resource_path + settings.sdg_labour_income, delimiter=',', quoting = csv.QUOTE_ALL, compression='zip', memory_map=True)
    df2.fillna({'obs_status':'', 'obs_status.label':''}, inplace=True)

    # WTO Imports
    with zipfile.ZipFile(settings.resource_path + settings.wto_imports, 'r') as zip: 
        csvfile = zip.open(zip.namelist()[0], 'r')
        df3 = pd.read_csv(csvfile, encoding_errors='ignore', delimiter=',', memory_map=True)
        df3['Reporting Economy ISO3A Code'].fillna('', inplace=True)
        df3['Partner Economy ISO3A Code'].fillna('', inplace=True)
        df3['Value Flag Code'].fillna('', inplace=True)
        df3['Value Flag'].fillna('', inplace=True)
        df3['Text Value'].fillna('', inplace=True)
        df3['Value'].fillna('', inplace=True)
    
    # WTO Exports
    with zipfile.ZipFile(settings.resource_path + settings.wto_exports, 'r') as zip: 
        csvfile = zip.open(zip.namelist()[0], 'r')
        df4 = pd.read_csv(csvfile, encoding_errors='ignore', delimiter=',', memory_map=True)
        df4['Reporting Economy ISO3A Code'].fillna('', inplace=True)
        df4['Partner Economy ISO3A Code'].fillna('', inplace=True)
        df4['Value Flag Code'].fillna('', inplace=True)
        df4['Value Flag'].fillna('', inplace=True)
        df4['Text Value'].fillna('', inplace=True)
        df4['Value'].fillna('', inplace=True)

    # WEO GDP
    df5 = pd.read_csv(settings.resource_path + settings.weo_gdp, delimiter='\t', encoding_errors='ignore', quoting = csv.QUOTE_ALL, compression='zip', memory_map=True)
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
        cursor.execute("SHOW TABLES FROM `" + settings.db + "`;")
        tables = cursor.fetchall()
        table_list = []
        for table in tables:
            table_list.append(table['Tables_in_' + settings.db])
        
        # WPP Total Population
        if("WPP2019_TotalPopulationBySex" in table_list):
            cursor.execute(settings.truncate_wpp_total_population_by_sex)
        else:
            cursor.execute(settings.create_wpp_total_population_by_sex)
        cursor.executemany(settings.insert_wpp_total_population_by_sex, df.values.tolist())
    
        # SDG Labour Income
        if("SDG_LabourIncome" in table_list):
            cursor.execute(settings.truncate_sdg_labourincome)
        else:
            cursor.execute(settings.create_sdg_labourincome)
        cursor.executemany(settings.insert_sdg_labourincome, df2.values.tolist())
        
        # WTO Imports
        if("WtoData_Import" in table_list):
            cursor.execute(settings.truncate_wto_imports)
        else:
            cursor.execute(settings.create_wto_imports)
        cursor.executemany(settings.insert_wto_imports, df3.values.tolist())
        
        # WTO Exports
        if("WtoData_Export" in table_list):
            cursor.execute(settings.truncate_wto_exports)
        else:
            cursor.execute(settings.create_wto_exports)
        cursor.executemany(settings.insert_wto_exports, df4.values.tolist())
        
        # WEO GDP
        if("WEO_GDP" in table_list):
            cursor.execute(settings.truncate_weo_gdp)
        else:
            cursor.execute(settings.create_weo_gdp)
        cursor.executemany(settings.insert_weo_gdp, df5.values.tolist())
        
        # WEO GDP Normalization
        if("WEO_GDP_norm" in table_list):
            cursor.execute(settings.truncate_weo_gdp_norm)
        else:
            cursor.execute(settings.create_weo_gdp_norm)
        cursor.executemany(settings.insert_weo_gdp_norm, df5_norm[df5_norm['GDP']!='0'].values.tolist())
        
        # countries view
        if("countries" in table_list):
            cursor.execute("DROP VIEW countries;")    
        cursor.execute(settings.create_country_view)
        
        # analysis data view
        if("analysis_data" in table_list):
            cursor.execute("DROP VIEW analysis_data;")    
        cursor.execute(settings.create_analysis_data_view)
        
        conn.commit()
finally:
    conn.close()