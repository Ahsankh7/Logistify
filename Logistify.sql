-- MySQL dump 10.13  Distrib 8.0.23, for Win64 (x86_64)
--
-- Host: localhost    Database: logistify
-- ------------------------------------------------------
-- Server version	8.0.23

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `consumers`
--

DROP TABLE IF EXISTS `consumers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `consumers` (
  `ConsumerID` bigint DEFAULT NULL,
  `UserName` text,
  `Password` text,
  `Name` text,
  `MobileNumber` bigint DEFAULT NULL,
  `Age` bigint DEFAULT NULL,
  `DateOfBirth` text,
  `Address` text,
  `City` text,
  `State` text,
  `PinCode` bigint DEFAULT NULL,
  `TotalOrders` bigint DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `consumers`
--

LOCK TABLES `consumers` WRITE;
/*!40000 ALTER TABLE `consumers` DISABLE KEYS */;
INSERT INTO `consumers` VALUES (1,'ak1','ahsan','Ahsan Khan ',1230000000,17,'02-12-2003','902, King\'s Road, C-Scheme','Jaipur','Rajasthan',302003,17),(2,'as2','armaan','Armaan Saeed',1250000000,18,'24-05-2002','54, Saeed House, Raja Park','Udaipur','Rajasthan',507003,18),(3,'sa3','shivam','Shivam Agarwal',2080000000,25,'13-03-1995','124, Janta Colony, Nirman Nagar','Bhatinda','Punjab',804002,19),(4,'ss4','shreya','Shreya Sharma',3020000000,22,'18-08-2000','305, Queen\'s Road, Juhu','Mumbai','Maharashtra',400802,16),(5,'ps5','pihu','Pihu Singh',8999000000,40,'31-01-1980','708, Vaishali, Thane','Mumbai','Maharashtra',400889,20),(6,'na6','neha','Neha Abraham',9800000000,35,'07-09-1985','354, Naya Mahal, New Gate','Delhi','Delhi',708001,5),(7,'bs7','bhavesh','Bhavesh Solanki',7867646600,18,'01-02-2003','96, Pratap Nagar, Sita Pura','Bilaspur','Chattisgarh',905550,5),(8,'dg8','deepak','Deepak Gupta',7864654640,55,'14-10-1965','9821, Gupta House, Bapu Nagar','Hyderabad','Andhra Pradesh',604444,9),(9,'sk9','salman','Salman Khan',7687646500,56,'25-12-1964','8786, Antalia, M.I. Road','Mumbai','Maharashtra',475550,7),(10,'rk10','ranbir','Ranbir Kapoor',5666000000,35,'27-04-1985','6788, Kapoor Mansion, Karol Bagh','Kolkata','West Bengal',205678,6);
/*!40000 ALTER TABLE `consumers` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `orderdetails`
--

DROP TABLE IF EXISTS `orderdetails`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `orderdetails` (
  `OrderID` bigint DEFAULT NULL,
  `ProductName` text,
  `SellerID` bigint DEFAULT NULL,
  `Qty` bigint DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `orderdetails`
--

LOCK TABLES `orderdetails` WRITE;
/*!40000 ALTER TABLE `orderdetails` DISABLE KEYS */;
INSERT INTO `orderdetails` VALUES (1,'Samsung Galaxy S20 Ultra',105,1),(2,'Oneplus Band',106,1),(3,'Antique Brass Showpiece',101,1),(4,'Oneplus Y Series TV',103,1),(5,'Apollo Office Chair ',110,1),(6,'India Gate Basmati Rice',109,1),(7,'Nivea Men Body Deodorizer',107,1),(8,'Wipro Smart LED Bulb',102,2),(9,'Steering Wheel Knob',108,1),(10,'Milton Thermosteel Flask',104,1);
/*!40000 ALTER TABLE `orderdetails` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `orders`
--

DROP TABLE IF EXISTS `orders`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `orders` (
  `OrderID` bigint DEFAULT NULL,
  `ConsumerID` bigint DEFAULT NULL,
  `OrderingDate` text,
  `OrderType` text,
  `OrderAmount` text,
  `PaymentType` text,
  `Status` text,
  `DeliveryDate` text,
  `DeliveryLocation` text
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `orders`
--

LOCK TABLES `orders` WRITE;
/*!40000 ALTER TABLE `orders` DISABLE KEYS */;
INSERT INTO `orders` VALUES (1,1,'07-01-2021','Mobile','16,999','Cash On Delivery','Yet To Be Delivered','10-01-2021','902, King\'s Road, C-Scheme'),(2,2,'09-01-2021','Wearable Technology','2,499','Cash On Delivery','Delivered','11-01-2021','54, Saeed House, Raja Park'),(3,3,'09-01-2021','Home & Décor','12,999','Credit Card','Yet To Be Delivered','12-01-2021','124, Janta Colony, Nirman Nagar'),(4,4,'11-01-2021','Appliances','5,999','Debit Card','Yet To Be Delivered','13-01-2021','305, Queen\'s Road, Juhu'),(5,5,'12-01-2021','Furniture','17,999','Debit Card','Delivered','15-01-2021','708, Vaishali, Thane'),(6,6,'14-01-2021','Cooking Essential','449','Cash On Delivery','Delivered','16-01-2021','354, Naya Mahal, New Gate'),(7,7,'15-01-2021','Personal Care','259','Cash On Delivery','Delivered','17-01-2021','96, Pratap Nagar, Sita Pura'),(8,8,'18-01-2021','Indoor Lighting','789','Credit Card','Yet To Be Delivered','20-01-2021','9821, Gupta House, Bapu Nagar'),(9,9,'20-01-2021','Vehicle Part','4,559','Debit Card','Yet To Be Delivered','23-01-2021','8786, Antalia, M.I. Road'),(10,10,'22-01-2021','Kitchen & Dining','999','Cash On Delivery','Delivered','24-01-2021','6788, Kapoor Mansion, Karol Bagh');
/*!40000 ALTER TABLE `orders` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ordertransit`
--

DROP TABLE IF EXISTS `ordertransit`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ordertransit` (
  `TransitID` bigint DEFAULT NULL,
  `OrderID` bigint DEFAULT NULL,
  `Location` text,
  `DateReceivedOn` text,
  `DateDeliveredOn` text
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ordertransit`
--

LOCK TABLES `ordertransit` WRITE;
/*!40000 ALTER TABLE `ordertransit` DISABLE KEYS */;
INSERT INTO `ordertransit` VALUES (1,1,'Jaipur, Rajasthan','08-01-2021','10-01-2021'),(2,2,'Udaipur, Rajasthan','10-01-2021','11-01-2021'),(3,3,'Bhatinda, Punjab','10-01-2021','12-01-2021'),(4,4,'Mumbai, Maharashtra','12-01-2021','13-01-2021'),(5,5,'Mumbai, Maharashtra','13-01-2021','15-01-2021'),(6,6,'Delhi','15-01-2021','16-01-2021'),(7,7,'Bilaspur, Chattisgarh','16-01-2021','17-01-2021'),(8,8,'Hyderabad, Andhra Pradesh','19-01-2021','20-01-2021'),(9,9,'Mumbai, Maharashtra','21-01-2021','23-01-2021'),(10,10,'Kolkata, West Bengal','23-01-2021','24-01-2021');
/*!40000 ALTER TABLE `ordertransit` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sales`
--

DROP TABLE IF EXISTS `sales`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `sales` (
  `SellerID` bigint DEFAULT NULL,
  `UserName` text,
  `Password` text,
  `January` bigint DEFAULT NULL,
  `February` bigint DEFAULT NULL,
  `March` bigint DEFAULT NULL,
  `April` bigint DEFAULT NULL,
  `May` bigint DEFAULT NULL,
  `June` bigint DEFAULT NULL,
  `July` bigint DEFAULT NULL,
  `August` bigint DEFAULT NULL,
  `September` bigint DEFAULT NULL,
  `October` bigint DEFAULT NULL,
  `November` bigint DEFAULT NULL,
  `December` bigint DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sales`
--

LOCK TABLES `sales` WRITE;
/*!40000 ALTER TABLE `sales` DISABLE KEYS */;
INSERT INTO `sales` VALUES (1,'ci1','cloudtail',24,17,36,17,28,32,15,21,24,17,19,15),(2,'tt2','tech',21,17,18,19,20,45,17,13,27,32,24,30),(3,'ss3','shanti',15,27,36,22,34,16,25,26,37,29,41,23),(4,'bi4','bata',28,21,12,35,46,40,38,27,15,45,37,25),(5,'kb5','khan',21,42,16,42,25,19,16,16,19,37,14,19),(6,'ls6','longitude',36,39,45,43,24,37,38,34,34,15,26,37),(7,'ac7','arora',41,54,24,24,15,34,28,16,35,43,34,16),(8,'rg8','retail',29,21,37,36,34,16,29,37,16,33,24,34),(9,'us9','uread',38,32,19,16,16,30,26,19,17,31,19,35),(10,'ai10','adidas',19,32,20,37,37,40,16,25,19,22,37,46);
/*!40000 ALTER TABLE `sales` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sellers`
--

DROP TABLE IF EXISTS `sellers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `sellers` (
  `SellerID` bigint DEFAULT NULL,
  `UserName` text,
  `Password` text,
  `SellerName` text,
  `MobileNumber` bigint DEFAULT NULL,
  `Address` text,
  `Ratings` double DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sellers`
--

LOCK TABLES `sellers` WRITE;
/*!40000 ALTER TABLE `sellers` DISABLE KEYS */;
INSERT INTO `sellers` VALUES (1,'ci1','cloudtail','CloudTail India',8897840000,'54, M.I Road, Jaipur, Rajasthan',4.1),(2,'tt2','tech','Tech Trade',7866650000,'11, Jawahar Road, Karol Bagh, Delhi',4.2),(3,'ss3','shanti','Shanti Sons',8784654000,'889, Samar Street, Jaipur, Rajasthan',4.3),(4,'bi4','bata','Bata Inc.',9788788465,'124, A.B. Circle, Clif Road, Mumbai',4.8),(5,'kb5','khan','Khan Brothers',7897864654,'54, X.Y Road, Kanpur, Uttar Pradesh',4.9),(6,'ls6','longitude','Longitude Sales',6876865468,'771, Highway 47, Riwadi, Rajasthan',3.9),(7,'ac7','arora','Arora & Co.',5465435634,'996, Tech Street, Pune, Maharashtra',3.5),(8,'rg8','retail','Retail Grapple',8789764678,'878, Mahmud Plaza, Bengaluru',2.9),(9,'us9','uread','uRead-Store',6876876546,'123, Zakir Street, Delhi',3.2),(10,'ai10','adidas','Adidas India',8768768768,'323, Ghazi Mall, City Road, Madhya Pradesh',3.6);
/*!40000 ALTER TABLE `sellers` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-02-13 19:06:33
