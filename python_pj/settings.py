import logging

# MySQL
HOST = 'localhost'
DB = 'python-pj'
USER = 'root'
PASSWORD = 'root'

# Path
RESOURCE_PATH = './resources/data/'
DDL_PATH = './resources/ddl/'
OUTPUT_PATH = './python-pj/'

# FileName
WPP_TOTAL_POPULATION_BY_SEX = 'WPP2019_TotalPopulationBySex.zip'
WEO_GDP = 'WEOApr2021all.zip'
WTO_IMPORTS = 'WtoDataCSV_imports.zip'
WTO_EXPORTS = 'WtoDataCSV_exports.zip'
SDG_LABOUR_INCOME = 'SDG_1041_NOC_RT_A.zip'

# Execution Setting
LOG_PATH  = None
LOG_LEVEL = logging.DEBUG

# DDL
# WPP_TotalPopulationBySex
ddl_wpp_total_population_by_sex = open(DDL_PATH + 'WPP_TotalPopulationBySex.sql', 'r')
CREATE_WPP_TOTAL_POPULATION_BY_SEX = ddl_wpp_total_population_by_sex.read()
ddl_wpp_total_population_by_sex.close()
TRUNCATE_WPP_TOTAL_POPULATION_BY_SEX = 'TRUNCATE TABLE wpp2019_totalpopulationbysex'
INSERT_WPP_TOTAL_POPULATION_BY_SEX = 'INSERT INTO wpp2019_totalpopulationbysex VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'

# SDG_LabourIncome
ddl_sdg_labour_income = open(DDL_PATH + 'SDG_LabourIncome.sql', 'r')
CREATE_SDG_LABOUR_INCOME = ddl_sdg_labour_income.read()
ddl_sdg_labour_income.close()
TRUNCATE_SDG_LABOUR_INCOME = 'TRUNCATE TABLE sdg_labourincome'
INSERT_SDG_LABOUR_INCOME = 'INSERT INTO sdg_labourincome VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'

# WtoData_Imports
ddl_wto_imports = open(DDL_PATH + 'WtoData_Imports.sql', 'r')
CREATE_WTO_IMPORTS = ddl_wto_imports.read()
ddl_wto_imports.close()
TRUNCATE_WTO_IMPORTS = 'TRUNCATE TABLE wtodata_import'
INSERT_WTO_IMPORTS = 'INSERT INTO wtodata_import VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'

# WtoData_Exports
ddl_wto_exports = open(DDL_PATH + 'WtoData_Exports.sql', 'r')
CREATE_WTO_EXPORTS = ddl_wto_exports.read()
ddl_wto_exports.close()
TRUNCATE_WTO_EXPORTS = 'TRUNCATE TABLE wtodata_export'
INSERT_WTO_EXPORTS = 'INSERT INTO wtodata_export VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'

# WEO_GDP
ddl_weo_gdp = open(DDL_PATH + 'WEO_GDP.sql', 'r')
CREATE_WEO_GDP = ddl_weo_gdp.read()
ddl_weo_gdp.close()
TRUNCATE_WEO_GDP = 'TRUNCATE TABLE weo_gdp'
INSERT_WEO_GDP = 'INSERT INTO weo_gdp VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'

# WEO_GDP_NORMALIZED
ddl_weo_gdp_norm = open(DDL_PATH + 'WEO_GDP_norm.sql', 'r')
CREATE_WEO_GDP_NORM = ddl_weo_gdp_norm.read()
ddl_weo_gdp_norm.close()
TRUNCATE_WEO_GDP_NORM = 'TRUNCATE TABLE weo_gdp_norm'
INSERT_WEO_GDP_NORM = 'INSERT INTO weo_gdp_norm VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'

# Country View
ddl_countries_view = open(DDL_PATH + 'CountriesView.sql', 'r')
CREATE_COUNTRY_VIEW = ddl_countries_view.read()
ddl_countries_view.close()
SELECT_COUNTRY_VIEW = 'SELECT * FROM countries'

# Analysis Data View
ddl_analysis_data_view = open(DDL_PATH + 'AnalysisDataView.sql', 'r')
CREATE_ANALYSIS_DATA_VIEW = ddl_analysis_data_view.read()
ddl_analysis_data_view.close()
SELECT_ANALYSIS_DATA = 'SELECT * FROM analysis_data'