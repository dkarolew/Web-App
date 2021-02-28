-- MySQL dump 10.13  Distrib 8.0.22, for Win64 (x86_64)
--
-- Host: test.ci2uiudwrhbr.eu-central-1.rds.amazonaws.com    Database: test
-- ------------------------------------------------------
-- Server version	8.0.20

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
SET @MYSQLDUMP_TEMP_LOG_BIN = @@SESSION.SQL_LOG_BIN;
SET @@SESSION.SQL_LOG_BIN= 0;

--
-- GTID state at the beginning of the backup 
--

SET @@GLOBAL.GTID_PURGED=/*!80000 '+'*/ '';

--
-- Table structure for table `tabela_testowa`
--

DROP TABLE IF EXISTS `tabela_testowa`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tabela_testowa` (
  `czas` datetime DEFAULT NULL,
  `temperatura` int DEFAULT NULL,
  `parametr` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tabela_testowa`
--

LOCK TABLES `tabela_testowa` WRITE;
/*!40000 ALTER TABLE `tabela_testowa` DISABLE KEYS */;
INSERT INTO `tabela_testowa` VALUES ('2020-10-22 20:20:01',100,10),('2020-10-22 20:20:02',100,20),('2020-10-22 20:20:03',110,10),('2020-10-22 20:20:04',115,30),('2020-10-22 20:20:05',130,30),('2020-10-22 20:20:06',130,40),('2020-10-22 20:20:07',145,60),('2020-10-22 20:20:08',105,70),('2020-10-22 20:20:09',90,30),('2020-10-22 20:20:10',70,30),('2020-10-22 20:20:11',95,20),('2020-10-22 20:20:12',90,20),('2020-10-22 21:35:45',145,5),('2020-10-23 07:59:06',145,5);
/*!40000 ALTER TABLE `tabela_testowa` ENABLE KEYS */;
UNLOCK TABLES;
SET @@SESSION.SQL_LOG_BIN = @MYSQLDUMP_TEMP_LOG_BIN;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-10-27 13:58:24
