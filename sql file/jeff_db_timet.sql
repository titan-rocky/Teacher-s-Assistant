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

-- Dump completed on 2021-02-17 11:19:00
