# MySQL
host = 'localhost'
db = 'python-pj'
user = 'root'
password = 'root'

# Path
resource_path = './resources/data/'
ddl_path = './resources/ddl/'

# FileName
wpp_total_population_by_sex = 'WPP2019_TotalPopulationBySex.zip'
weo_gdp = 'WEOApr2021all.zip'
wto_imports = 'WtoDataCSV_imports.zip'
wto_exports = 'WtoDataCSV_exports.zip'
sdg_labour_income = 'SDG_1041_NOC_RT_A.zip'

# DDL
# WPP_TotalPopulationBySex
ddl_wpp_total_population_by_sex = open(ddl_path + 'WPP_TotalPopulationBySex.sql', 'r')
create_wpp_total_population_by_sex = ddl_wpp_total_population_by_sex.read()
ddl_wpp_total_population_by_sex.close()
truncate_wpp_total_population_by_sex = 'TRUNCATE TABLE wpp2019_totalpopulationbysex'
insert_wpp_total_population_by_sex = 'INSERT INTO wpp2019_totalpopulationbysex VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'

# SDG_LabourIncome
ddl_sdg_labourincome = open(ddl_path + 'SDG_LabourIncome.sql', 'r')
create_sdg_labourincome = ddl_sdg_labourincome.read()
ddl_sdg_labourincome.close()
truncate_sdg_labourincome = 'TRUNCATE TABLE sdg_labourincome'
insert_sdg_labourincome = 'INSERT INTO sdg_labourincome VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'

# WtoData_Imports
ddl_wto_imports = open(ddl_path + 'WtoData_Imports.sql', 'r')
create_wto_imports = ddl_wto_imports.read()
ddl_wto_imports.close()
truncate_wto_imports = 'TRUNCATE TABLE wtodata_import'
insert_wto_imports = 'INSERT INTO wtodata_import VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'

# WtoData_Exports
ddl_wto_exports = open(ddl_path + 'WtoData_Exports.sql', 'r')
create_wto_exports = ddl_wto_exports.read()
ddl_wto_exports.close()
truncate_wto_exports = 'TRUNCATE TABLE wtodata_export'
insert_wto_exports = 'INSERT INTO wtodata_export VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'

# WEO_GDP
ddl_weo_gdp = open(ddl_path + 'WEO_GDP.sql', 'r')
create_weo_gdp = ddl_weo_gdp.read()
ddl_weo_gdp.close()
truncate_weo_gdp = 'TRUNCATE TABLE weo_gdp'
insert_weo_gdp = 'INSERT INTO weo_gdp VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'

# WEO_GDP_NORMALIZED
ddl_weo_gdp_norm = open(ddl_path + 'WEO_GDP_norm.sql', 'r')
create_weo_gdp_norm = ddl_weo_gdp_norm.read()
ddl_weo_gdp_norm.close()
truncate_weo_gdp_norm = 'TRUNCATE TABLE weo_gdp_norm'
insert_weo_gdp_norm = 'INSERT INTO weo_gdp_norm VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'

# Country View
ddl_countries_view = open(ddl_path + 'CountriesView.sql', 'r')
create_country_view = ddl_countries_view.read()
ddl_countries_view.close()

# Analysis Data View
ddl_analysis_data_view = open(ddl_path + 'AnalysisDataView.sql', 'r')
create_analysis_data_view = ddl_analysis_data_view.read()
ddl_analysis_data_view.close()
select_analysis_data = 'SELECT * FROM analysis_data'