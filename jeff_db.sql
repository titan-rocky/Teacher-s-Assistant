CREATE DATABASE  IF NOT EXISTS `jeff_db` /*!40100 DEFAULT CHARACTER SET latin1 */;
USE `jeff_db`;
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
  `17_2_2021` varchar(1) DEFAULT NULL,
  `15_2_2021` varchar(1) DEFAULT NULL,
  `12_2_2021` varchar(1) DEFAULT NULL,
  `3_2_2021` varchar(1) DEFAULT NULL,
  `1_2_2021` varchar(1) DEFAULT NULL,
  PRIMARY KEY (`admn_no`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `attendence`
--

LOCK TABLES `attendence` WRITE;
/*!40000 ALTER TABLE `attendence` DISABLE KEYS */;
INSERT INTO `attendence` VALUES ('name1','sabc1','0','0','0','0','1','0','0','0','0','0','1','1','0','0','0',NULL,'0'),('name10','sabc10','0','0','0','0','0','0','0','1','1','1','1','0','0','0','0',NULL,'0'),('name11','sabc11','0','0','0','0','1','1','0','0','1','0','1','1','0','0','0',NULL,'0'),('name12','sabc12','0','0','0','0','0','0','0','0','0','1','0','1','0','0','0',NULL,'0'),('name2','sabc2','0','0','0','0','0','0','1','1','0','0','0','0','0','0','0',NULL,'0'),('name3','sabc3','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',NULL,'0'),('name4','sabc4','0','0','0','0','0','1','1','1','1','0','1','0','0','0','0',NULL,'0'),('name5','sabc5','0','0','0','0','1','0','1','1','0','1','0','1','0','0','0',NULL,'0'),('name6','sabc6','0','0','0','0','0','1','0','0','0','0','0','1','0','0','0',NULL,'0'),('name7','sabc7','0','0','0','0','1','1','1','0','0','0','0','0','0','0','0',NULL,'0'),('name8','sabc8','0','0','0','0','0','0','0','0','0','0','0','1','0','0','0',NULL,'0'),('name9','sabc9','0','0','0','0','0','1','0','1','0','0','1','0','0','0','0',NULL,'0');
/*!40000 ALTER TABLE `attendence` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `student_details`
--

DROP TABLE IF EXISTS `student_details`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `student_details` (
  `studentname` varchar(32) DEFAULT NULL,
  `admn_no` char(6) NOT NULL,
  `Father_Name` varchar(32) DEFAULT NULL,
  `gender` varchar(15) DEFAULT NULL,
  `contact_no` varchar(15) DEFAULT NULL,
  `address` varchar(100) DEFAULT NULL,
  `blood_group` varchar(3) DEFAULT NULL,
  `disciplinary_records` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `student_details`
--

LOCK TABLES `student_details` WRITE;
/*!40000 ALTER TABLE `student_details` DISABLE KEYS */;
INSERT INTO `student_details` VALUES ('name1','sabc1','Father1','Male','9375565477','16, Benetic Street , Agra-223007','AB+',NULL),('name10','sabc10',NULL,NULL,NULL,NULL,NULL,NULL),('name11','sabc11',NULL,NULL,NULL,NULL,NULL,NULL),('name12','sabc12',NULL,NULL,NULL,NULL,NULL,NULL),('name2','sabc2','Father2','Male','9043022616','21/20,Gandhi Street, Agra-223010','AB+',NULL),('name3','sabc3','Father3','Female','9999999999','31,B block,Dalk Apartments,Agra-223010','O+','1 Yellow Card'),('name4','sabc4',NULL,NULL,NULL,'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA','AB-','2 Yellow Cards , 1 Red Card'),('name5','sabc5',NULL,NULL,NULL,NULL,NULL,NULL),('name6','sabc6',NULL,NULL,NULL,NULL,NULL,NULL),('name7','sabc7',NULL,NULL,NULL,NULL,NULL,NULL),('name8','sabc8',NULL,NULL,NULL,NULL,NULL,NULL),('name9','sabc9',NULL,NULL,NULL,NULL,NULL,NULL);
/*!40000 ALTER TABLE `student_details` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `timet`
--

DROP TABLE IF EXISTS `timet`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `timet` (
  `Day_Period` varchar(32) DEFAULT NULL,
  `Period1` varchar(6) DEFAULT NULL,
  `Period2` varchar(6) DEFAULT NULL,
  `Period3` varchar(6) DEFAULT NULL,
  `Break1` varchar(4) DEFAULT NULL,
  `Period4` varchar(6) DEFAULT NULL,
  `Period5` varchar(6) DEFAULT NULL,
  `LunchB` varchar(4) DEFAULT NULL,
  `Period6` varchar(6) DEFAULT NULL,
  `Period7` varchar(6) DEFAULT NULL,
  `Break2` varchar(4) DEFAULT NULL,
  `Period8` varchar(6) DEFAULT NULL,
  `Period9` varchar(6) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `timet`
--

LOCK TABLES `timet` WRITE;
/*!40000 ALTER TABLE `timet` DISABLE KEYS */;
INSERT INTO `timet` VALUES ('Monday','XII-B',NULL,'XII-F','','XI-E',NULL,'','XI-G','XII-B','','XII-F',NULL),('Tuesday',NULL,NULL,'XII-F','','XII-B',NULL,'',NULL,'XII-F','','XII-F',NULL),('Wednesday','XII-B',NULL,'XI-E','','XI-G',NULL,'',NULL,'XII-B','','XII-F','XI-G'),('Thursday',NULL,'XII-F','XI-E','','XI-E','XI-G','',NULL,NULL,'','XII-B',NULL),('Friday',NULL,'XII-B',NULL,'',NULL,'XI-E','','XII-B',NULL,'',NULL,'XII-F');
/*!40000 ALTER TABLE `timet` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-02-21 12:44:26
