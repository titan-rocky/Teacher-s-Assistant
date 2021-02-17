-- MySQL dump 10.13  Distrib 8.0.21, for Win64 (x86_64)
--
-- Host: localhost    Database: jeff_db
-- ------------------------------------------------------
-- Server version	5.7.31-log

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `attendence`
--

DROP TABLE IF EXISTS `attendence`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `attendence` (
  `studentname` varchar(32) DEFAULT NULL,
  `admn_no` char(6) NOT NULL,
  `7_12_2020` varchar(1) DEFAULT NULL,
  `8_12_2020` varchar(1) DEFAULT NULL,
  `10_12_2020` varchar(1) DEFAULT NULL,
  `11_12_2020` varchar(1) DEFAULT NULL,
  `12_12_2020` varchar(1) DEFAULT NULL,
  `23_12_2020` varchar(1) DEFAULT NULL,
  `24_12_2020` varchar(1) DEFAULT NULL,
  `28_12_2020` varchar(1) DEFAULT NULL,
  `29_12_2020` varchar(1) DEFAULT NULL,
  `30_12_2020` varchar(1) DEFAULT NULL,
  `31_12_2020` varchar(1) DEFAULT NULL,
  `13_12_2020` varchar(1) DEFAULT NULL,
  PRIMARY KEY (`admn_no`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `attendence`
--

LOCK TABLES `attendence` WRITE;
/*!40000 ALTER TABLE `attendence` DISABLE KEYS */;
INSERT INTO `attendence` VALUES ('name1','sabc1','0','0','0','0','1','0','0','0','0','0','1','1'),('name10','sabc10','0','0','0','0','0','0','0','1','1','1','1','0'),('name11','sabc11','0','0','0','0','1','1','0','0','1','0','1','1'),('name12','sabc12','0','0','0','0','0','0','0','0','0','1','0','1'),('name2','sabc2','0','0','0','0','0','0','1','1','0','0','0','0'),('name3','sabc3','0','0','0','0','0','0','0','0','0','0','0','0'),('name4','sabc4','0','0','0','0','0','1','1','1','1','0','1','0'),('name5','sabc5','0','0','0','0','1','0','1','1','0','1','0','1'),('name6','sabc6','0','0','0','0','0','1','0','0','0','0','0','1'),('name7','sabc7','0','0','0','0','1','1','1','0','0','0','0','0'),('name8','sabc8','0','0','0','0','0','0','0','0','0','0','0','1'),('name9','sabc9','0','0','0','0','0','1','0','1','0','0','1','0');
/*!40000 ALTER TABLE `attendence` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-02-17 11:19:01
