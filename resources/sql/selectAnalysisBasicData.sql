WITH 
	Population   AS (SELECT Location as Country, Time as Year, PopMale, PopFemale, PopTotal, PopDensity from WPP2019_TotalPopulationBySex WHERE Variant='Medium'),
	LabourIncome AS (SELECT ref_area_label as Country, time as Year, obs_value as LabourIncome from SDG_LabourIncome),
	Import       AS (SELECT ReportingEconomy as Country, Year, Value as Import from WtoData_Import WHERE ProductSectorCode='TO'),
	Export       AS (SELECT ReportingEconomy as Country, Year, Value as Export from WtoData_Export WHERE ProductSectorCode='TO'),
	NGDP_RPCH    AS (SELECT Country, year as Year, GDP as NGDP_RPCH    from WEO_GDP_norm where WEOSubjectCode='NGDP_RPCH'),
	NGDPD        AS (SELECT Country, year as Year, GDP as NGDPD        from WEO_GDP_norm where WEOSubjectCode='NGDPD'),
	PPPGDP       AS (SELECT Country, year as Year, GDP as PPPGDP       from WEO_GDP_norm where WEOSubjectCode='PPPGDP'),
	NGDP_D       AS (SELECT Country, year as Year, GDP as NGDP_D       from WEO_GDP_norm where WEOSubjectCode='NGDP_D'),
	NGDPRPPPPC   AS (SELECT Country, year as Year, GDP as NGDPRPPPPC   from WEO_GDP_norm where WEOSubjectCode='NGDPRPPPPC'),
	NGDPDPC      AS (SELECT Country, year as Year, GDP as NGDPDPC      from WEO_GDP_norm where WEOSubjectCode='NGDPDPC'),
	PPPPC        AS (SELECT Country, year as Year, GDP as PPPPC        from WEO_GDP_norm where WEOSubjectCode='PPPPC'),
	PPPSH        AS (SELECT Country, year as Year, GDP as PPPSH        from WEO_GDP_norm where WEOSubjectCode='PPPSH'),
	PPPEX        AS (SELECT Country, year as Year, GDP as PPPEX        from WEO_GDP_norm where WEOSubjectCode='PPPEX'),	
	NGSD_NGDP    AS (SELECT Country, year as Year, GDP as NGSD_NGDP    from WEO_GDP_norm where WEOSubjectCode='NGSD_NGDP'),
	BCA          AS (SELECT Country, year as Year, GDP as BCA          from WEO_GDP_norm where WEOSubjectCode='BCA'),
	BCA_NGDPD    AS (SELECT Country, year as Year, GDP as BCA_NGDPD    from WEO_GDP_norm where WEOSubjectCode='BCA_NGDPD'),
	PCPI         AS (SELECT Country, year as Year, GDP as PCPI         from WEO_GDP_norm where WEOSubjectCode='PCPI'),
	PCPIPCH      AS (SELECT Country, year as Year, GDP as PCPIPCH      from WEO_GDP_norm where WEOSubjectCode='PCPIPCH'),
	PCPIE        AS (SELECT Country, year as Year, GDP as PCPIE        from WEO_GDP_norm where WEOSubjectCode='PCPIE'),
	PCPIEPCH     AS (SELECT Country, year as Year, GDP as PCPIEPCH     from WEO_GDP_norm where WEOSubjectCode='PCPIEPCH'),
	NGAP_NPGDP   AS (SELECT Country, year as Year, GDP as NGAP_NPGDP   from WEO_GDP_norm where WEOSubjectCode='NGAP_NPGDP'),
	GGR_NGDP     AS (SELECT Country, year as Year, GDP as GGR_NGDP     from WEO_GDP_norm where WEOSubjectCode='GGR_NGDP'),
	GGX_NGDP     AS (SELECT Country, year as Year, GDP as GGX_NGDP     from WEO_GDP_norm where WEOSubjectCode='GGX_NGDP'),
	GGXCNL_NGDP  AS (SELECT Country, year as Year, GDP as GGXCNL_NGDP  from WEO_GDP_norm where WEOSubjectCode='GGXCNL_NGDP'),
	GGXONLB_NGDP AS (SELECT Country, year as Year, GDP as GGXONLB_NGDP from WEO_GDP_norm where WEOSubjectCode='GGXONLB_NGDP'),
	GGXWDG_NGDP  AS (SELECT Country, year as Year, GDP as GGXWDG_NGDP  from WEO_GDP_norm where WEOSubjectCode='GGXWDG_NGDP'),
	GGSB_NPGDP   AS (SELECT Country, year as Year, GDP as GGSB_NPGDP   from WEO_GDP_norm where WEOSubjectCode='GGSB_NPGDP'),
	GGXWDN_NGDP  AS (SELECT Country, year as Year, GDP as GGXWDN_NGDP  from WEO_GDP_norm where WEOSubjectCode='GGXWDN_NGDP')
SELECT 
	Population.*, 
	LabourIncome.LabourIncome,
	Import.Import,
	Export.Export,
	NGDP_RPCH.NGDP_RPCH,
	NGDPD.NGDPD,
	PPPGDP.PPPGDP,
	NGDP_D.NGDP_D,
	NGDPRPPPPC.NGDPRPPPPC,
	NGDPDPC.NGDPDPC,
	PPPPC.PPPPC,
	PPPSH.PPPSH,
	PPPEX.PPPEX,
	NGSD_NGDP.NGSD_NGDP,
	BCA.BCA,
	BCA_NGDPD.BCA_NGDPD,
	PCPI.PCPI,
	PCPIPCH.PCPIPCH,
	PCPIE.PCPIE,
	PCPIEPCH.PCPIEPCH,
	NGAP_NPGDP.NGAP_NPGDP,
	GGR_NGDP.GGR_NGDP,
	GGX_NGDP.GGX_NGDP,
	GGXCNL_NGDP.GGXCNL_NGDP,
	GGXONLB_NGDP.GGXONLB_NGDP,
	GGXWDG_NGDP.GGXWDG_NGDP,
	GGSB_NPGDP.GGSB_NPGDP,
	GGXWDN_NGDP.GGXWDN_NGDP
FROM Population
	LEFT OUTER JOIN LabourIncome USING(Country, Year)
	LEFT OUTER JOIN Import       USING(Country, Year)
	LEFT OUTER JOIN Export       USING(Country, Year)
	LEFT OUTER JOIN NGDP_RPCH    USING(Country, Year)
	LEFT OUTER JOIN NGDPD        USING(Country, Year)
	LEFT OUTER JOIN PPPGDP       USING(Country, Year)
	LEFT OUTER JOIN NGDP_D       USING(Country, Year)
	LEFT OUTER JOIN NGDPRPPPPC   USING(Country, Year)
	LEFT OUTER JOIN NGDPDPC      USING(Country, Year)
	LEFT OUTER JOIN PPPPC        USING(Country, Year)
	LEFT OUTER JOIN PPPSH        USING(Country, Year)
	LEFT OUTER JOIN PPPEX        USING(Country, Year)	
	LEFT OUTER JOIN NGSD_NGDP    USING(Country, Year)
	LEFT OUTER JOIN BCA          USING(Country, Year)
	LEFT OUTER JOIN BCA_NGDPD    USING(Country, Year)
	LEFT OUTER JOIN PCPI         USING(Country, Year)
	LEFT OUTER JOIN PCPIPCH      USING(Country, Year)
	LEFT OUTER JOIN PCPIE        USING(Country, Year)
	LEFT OUTER JOIN PCPIEPCH     USING(Country, Year)
	LEFT OUTER JOIN NGAP_NPGDP   USING(Country, Year)
	LEFT OUTER JOIN GGR_NGDP     USING(Country, Year)
	LEFT OUTER JOIN GGX_NGDP     USING(Country, Year)
	LEFT OUTER JOIN GGXCNL_NGDP  USING(Country, Year)
	LEFT OUTER JOIN GGXONLB_NGDP USING(Country, Year)
	LEFT OUTER JOIN GGXWDG_NGDP  USING(Country, Year)
	LEFT OUTER JOIN GGSB_NPGDP   USING(Country, Year)
	LEFT OUTER JOIN GGXWDN_NGDP  USING(Country, Year)
ORDER BY Population.Country asc, Population.Year asc;
