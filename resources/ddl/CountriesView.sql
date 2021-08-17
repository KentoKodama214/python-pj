CREATE VIEW Countries AS 
WITH
	LabourIncome_Countries AS (SELECT distinct ref_area as LabourIncome_ISO, ref_area_label as Country from SDG_LabourIncome),
	WEO_GDP_Countries AS (SELECT distinct ISO, Country from WEO_GDP_norm),
	Population_Countries AS (SELECT distinct LocID, Location as Country from WPP2019_TotalPopulationBySex),
	WTO_Import_Countries AS (SELECT distinct ReportingEconomyCode as ImportCountryCode, ReportingEconomyISO3ACode as ImportCountryISO, ReportingEconomy as Country from WtoData_Import),
	WTO_Export_Countries AS (SELECT distinct ReportingEconomyCode as ExportCountryCode, ReportingEconomyISO3ACode as ExportCountryISO, ReportingEconomy as Country from WtoData_Export)
SELECT * from Population_Countries
	LEFT OUTER JOIN LabourIncome_Countries USING(Country)
	LEFT OUTER JOIN WEO_GDP_Countries USING(Country)
	LEFT OUTER JOIN WTO_Import_Countries USING(Country)
	LEFT OUTER JOIN WTO_Export_Countries USING(Country)
ORDER BY LocID;