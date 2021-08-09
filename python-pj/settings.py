# MySQL
host = 'localhost'
user = 'root'
# db = 'triplan'
db = 'python-pj'
password = 'root'

# Path
resource_path = './resources/data/'
sql_path = './resources/sql/'

# FileName
wpp_total_population_by_sex = 'WPP2019_TotalPopulationBySex.zip'
weo_gdp = 'WEOApr2021all.zip'
wto_imports = 'WtoDataCSV_imports.zip'
wto_exports = 'WtoDataCSV_exports.zip'
sdg_labour_income = 'SDG_1041_NOC_RT_A.zip'

# SQL
delete_wpp_total_population_by_sex = 'DELETE FROM wpp2019_totalpopulationbysex'
insert_wpp_total_population_by_sex = 'INSERT INTO wpp2019_totalpopulationbysex VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
delete_weo_gdp = 'DELETE FROM weo_gdp'
insert_weo_gdp = 'INSERT INTO weo_gdp VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
delete_wto_imports = 'DELETE FROM wtodata_import'
insert_wto_imports = 'INSERT INTO wtodata_import VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
delete_wto_exports = 'DELETE FROM wtodata_export'
insert_wto_exports = 'INSERT INTO wtodata_export VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
delete_sdg_labourincome = 'DELETE FROM sdg_labourincome'
insert_sdg_labourincome = 'INSERT INTO sdg_labourincome VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
delete_weo_gdp_norm = 'DELETE FROM weo_gdp_norm'
insert_weo_gdp_norm = 'INSERT INTO weo_gdp_norm VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'

f = open(sql_path + 'selectAnalysisBasicData.sql', 'r')
select_analysis_basic_data = f.read()
f.close()