import psycopg2

# Connect to the PostgreSQL server
conn = psycopg2.connect(
    host="localhost",
    database="postgres",
    user="postgres",
    password="1111"
)

# Create a new database named "mydatabase"
cur = conn.cursor()
cur.execute("CREATE DATABASE esakor;")
cur.close()

# Connect to the new database
conn.close()
conn = psycopg2.connect(
    host="localhost",
    database="esakor",
    user="postgres",
    password="1111"
)

# Create a district table in the new database
cur = conn.cursor()
cur.execute("""
    DROP TABLE IF EXISTS `district`;
CREATE TABLE `district`  (
  `aDzongkhag` tinyint(3) UNSIGNED NOT NULL,
  `aDescr` varchar(21) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `aDzDescrOld` varchar(21) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `aDzDescr` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `aPopulation` int(7) NULL DEFAULT NULL,
  `created` datetime(0) NULL DEFAULT NULL,
  `modified` datetime(0) NULL DEFAULT NULL,
  PRIMARY KEY (`aDzongkhag`) USING BTREE,
  UNIQUE INDEX `DISTRICT01`(`aDescr`) USING BTREE,
  UNIQUE INDEX `DISTRICT02`(`aDzDescrOld`) USING BTREE
);
""")
cur.close()

# Create a block in the new database
cur = conn.cursor()
cur.execute("""
    DROP TABLE IF EXISTS `block`;
CREATE TABLE `block`  (
  `bGewog` tinyint(3) UNSIGNED NOT NULL,
  `bDzongkhag` tinyint(3) UNSIGNED NOT NULL,
  `bDescr` varchar(20) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL,
  `bDzdescrOld` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `bDzDescr` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `bDungkhag` tinyint(3) UNSIGNED NULL DEFAULT NULL,
  `bSort` char(1) CHARACTER SET latin1 COLLATE latin1_swedish_ci NULL DEFAULT NULL,
  `created` datetime(0) NULL DEFAULT NULL,
  `modified` datetime(0) NULL DEFAULT NULL,
  PRIMARY KEY (`bGewog`) USING BTREE,
  UNIQUE INDEX `BLOCK02`(`bGewog`) USING BTREE,
  INDEX `BLOCK01`(`bDzongkhag`) USING BTREE,
  CONSTRAINT `block_ibfk_1` FOREIGN KEY (`bDzongkhag`) REFERENCES `district` (`aDzongkhag`) ON DELETE NO ACTION ON UPDATE NO ACTION
);
""")
cur.close()

# Create a thram in the new database
cur = conn.cursor()
cur.execute("""
    DROP TABLE IF EXISTS `thram`;
CREATE TABLE `thram`  (
  `cGewog` tinyint(3) UNSIGNED NOT NULL,
  `cThram` smallint(6) NOT NULL,
  `cVillage` varchar(30) CHARACTER SET latin1 COLLATE latin1_swedish_ci NULL DEFAULT '',
  `cDzVillage` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `cChiwog` tinyint(3) UNSIGNED NULL DEFAULT NULL,
  `cOwnId` char(11) CHARACTER SET latin1 COLLATE latin1_swedish_ci NULL DEFAULT NULL,
  `cOwnName` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `cDzOwnName` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `cOwntype` char(2) CHARACTER SET latin1 COLLATE latin1_swedish_ci NULL DEFAULT NULL,
  `cAddOwners` tinyint(1) NOT NULL DEFAULT 0,
  `cRemark` longtext CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `cDzRemark` longtext CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `cStatus` tinyint(3) UNSIGNED NOT NULL DEFAULT 0,
  `cPhotoPath` varchar(200) CHARACTER SET latin1 COLLATE latin1_swedish_ci NULL DEFAULT NULL,
  `cDeprecated` tinyint(1) NOT NULL DEFAULT 0,
  `cSMID` int(11) NULL DEFAULT NULL,
  `cTMID` int(11) NULL DEFAULT NULL,
  `cContactNo` int(8) NULL DEFAULT NULL,
  `cOwnerQualification` smallint(5) NULL DEFAULT NULL,
  `author` int(11) NULL DEFAULT NULL,
  `created` datetime(0) NULL DEFAULT NULL,
  `modified` datetime(0) NULL DEFAULT NULL,
  PRIMARY KEY (`cGewog`, `cThram`) USING BTREE,
  INDEX `IX_Owner`(`cOwnName`) USING BTREE,
  INDEX `IX_CID`(`cOwnId`) USING BTREE
);
""")
cur.close()

# Create a owntype in the new database
cur = conn.cursor()
cur.execute("""
 DROP TABLE IF EXISTS `owntype`;
CREATE TABLE `owntype`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `OTCode` char(2) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL,
  `OTDescr` varchar(50) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL,
  `OTDzDescr` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `OTIndividual` tinyint(4) NULL DEFAULT NULL COMMENT '0-individual, 1-agency',
  `created` datetime(0) NULL DEFAULT NULL,
  `modified` datetime(0) NULL DEFAULT NULL,
  PRIMARY KEY (`OTCode`, `id`) USING BTREE,
  INDEX `id`(`id`) USING BTREE
);   
""")
cur.close()

# Create a landtype in the new database
cur = conn.cursor()
cur.execute("""
  DROP TABLE IF EXISTS `landtype`;
CREATE TABLE `landtype`  (
  `fLandtype` tinyint(3) UNSIGNED NOT NULL,
  `fDescr` varchar(22) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL,
  `fTax` decimal(6, 2) NULL DEFAULT NULL,
  `fType` char(1) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL,
  `fSort` tinyint(3) UNSIGNED NOT NULL,
  `fDzDescr` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `fDescrOld` char(22) CHARACTER SET latin1 COLLATE latin1_swedish_ci NULL DEFAULT NULL,
  `fDzDescrOld` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `fGrpForReport` char(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `created` datetime(0) NULL DEFAULT NULL,
  `modified` datetime(0) NULL DEFAULT NULL,
  PRIMARY KEY (`fLandtype`) USING BTREE,
  INDEX `IX_LANDTYPE`(`fDescr`) USING BTREE
);  
""")
cur.close()

# Create a plot in the new database
cur = conn.cursor()
cur.execute("""
   DROP TABLE IF EXISTS `plot`;
CREATE TABLE `plot`  (
  `RecId` int(11) UNSIGNED NOT NULL AUTO_INCREMENT,
  `ePlotId` varchar(10) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `eGewog` tinyint(3) UNSIGNED NOT NULL,
  `eThram` smallint(6) NOT NULL,
  `eSheet` char(9) CHARACTER SET latin1 COLLATE latin1_swedish_ci NULL DEFAULT NULL,
  `ePlot` smallint(6) NULL DEFAULT NULL,
  `ePlotsuff` char(2) CHARACTER SET latin1 COLLATE latin1_swedish_ci NULL DEFAULT '',
  `eLandtype` tinyint(3) UNSIGNED NOT NULL,
  `ePlotName` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `eDzPlotName` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `eBund` smallint(6) NULL DEFAULT NULL,
  `eVillage` varchar(30) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `eDzVillage` varchar(65) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `eRemark` longtext CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `eDzRemark` longtext CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `eTsadroDescr` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL,
  `eSurvDist` char(3) CHARACTER SET latin1 COLLATE latin1_swedish_ci NULL DEFAULT NULL,
  `eToSArea` double(10, 3) UNSIGNED NULL DEFAULT 0,
  `ePlotCat` char(3) CHARACTER SET latin1 COLLATE latin1_swedish_ci NULL DEFAULT NULL,
  `ePlotCatYr` int(11) NULL DEFAULT NULL,
  `ePvtForestry` char(1) CHARACTER SET latin1 COLLATE latin1_swedish_ci NULL DEFAULT NULL,
  `eThazhingBukzhing` char(2) CHARACTER SET latin1 COLLATE latin1_swedish_ci NULL DEFAULT NULL,
  `eSChiwog` smallint(6) NULL DEFAULT NULL,
  `eFitForSwap` char(2) CHARACTER SET latin1 COLLATE latin1_swedish_ci NULL DEFAULT NULL,
  `eLhakhangCat` char(2) CHARACTER SET latin1 COLLATE latin1_swedish_ci NULL DEFAULT NULL,
  `eTotExcessArea` double(10, 3) UNSIGNED NULL DEFAULT NULL,
  `ePlotCatDt` datetime(0) NULL DEFAULT NULL,
  `eKiduDt` date NULL DEFAULT NULL,
  `eSource` tinyint(3) UNSIGNED NULL DEFAULT NULL,
  `eSRem` varchar(500) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `eURSPurpose` varchar(500) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `eLandClass` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `author` int(11) NULL DEFAULT NULL,
  `created` datetime(0) NULL DEFAULT NULL,
  `modified` datetime(0) NULL DEFAULT NULL,
  PRIMARY KEY (`RecId`) USING BTREE,
  UNIQUE INDEX `IX_PotID`(`ePlotId`) USING BTREE,
  INDEX `IX_LType`(`eLandtype`) USING BTREE,
  INDEX `FK_PLOT_THRAM`(`eGewog`, `eThram`) USING BTREE
) 
""")

# Create a vparcel in the new database
cur = conn.cursor()
cur.execute("""
  CREATE OR REPLACE VIEW public.vparcel
 AS
 SELECT district.adescr as district,
 	district.adzongkhag as district_id,
    block.bgewog as subdist_id,
    block.bdescr as sub_district,
    thram.cthram as sheet_id,
    thram.cownid as owner_id,
    thram.cownname as owner_name,
    owntype.otdescr as owner_type,
    thram.cvillage as village_name,
    plot.eplotid as plot_id,
    plot.eplotname as plot_name,
    plot.etosarea as plot_area,
    landtype.fdescr as land_type,
	st_asGeoJSON(parcel_wgs.geom) as geometry
   FROM block
     JOIN thram ON block.bgewog = thram.cgewog
     JOIN plot ON thram.cthram = plot.ethram AND thram.cgewog = plot.egewog
     JOIN parcel_wgs on plot.eplotid= parcel_wgs.plotid
	 JOIN landtype ON plot.elandtype = landtype.flandtype
     JOIN owntype ON thram.cowntype = owntype.otcode
     JOIN district ON district.adzongkhag = block.bdzongkhag;

ALTER TABLE public.vparcel);  
""")
cur.close()

# Commit the changes and close the connection
conn.commit()
conn.close()
