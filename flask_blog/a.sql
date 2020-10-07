-- MySQL dump 10.13  Distrib 5.7.31, for Win64 (x86_64)
--
-- Host: localhost    Database: flask_blog
-- ------------------------------------------------------
-- Server version	5.7.31-log

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `alembic_version`
--

DROP TABLE IF EXISTS `alembic_version`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `alembic_version` (
  `version_num` varchar(32) NOT NULL,
  PRIMARY KEY (`version_num`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `alembic_version`
--

LOCK TABLES `alembic_version` WRITE;
/*!40000 ALTER TABLE `alembic_version` DISABLE KEYS */;
INSERT INTO `alembic_version` VALUES ('6bb0071829be');
/*!40000 ALTER TABLE `alembic_version` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `article`
--

DROP TABLE IF EXISTS `article`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `article` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(50) NOT NULL,
  `content` text NOT NULL,
  `create_time` datetime DEFAULT NULL,
  `click_num` int(11) DEFAULT NULL,
  `save_num` int(11) DEFAULT NULL,
  `love_num` int(11) DEFAULT NULL,
  `type_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `type_id` (`type_id`),
  KEY `user_id` (`user_id`),
  CONSTRAINT `article_ibfk_1` FOREIGN KEY (`type_id`) REFERENCES `article_type` (`id`),
  CONSTRAINT `article_ibfk_2` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `article`
--

LOCK TABLES `article` WRITE;
/*!40000 ALTER TABLE `article` DISABLE KEYS */;
INSERT INTO `article` VALUES (1,'国庆大事','<p>法大师傅十分1地方的方式JFK就，</p>\r\n<p><strong>打发士大夫十分地方。</strong></p>\r\n<p><em><strong>打发士大夫士大夫</strong></em></p>\r\n<h2>法大师傅十分地方反对法</h2>','2020-10-03 16:36:02',0,0,0,19,1),(2,'python','<p>大夫十分地方fdfdfdfsfsfsdfsdf1/</p>\r\n<p>fdfjkjddkfjdkfjsdf</p>\r\n<p><strong>dfsjfkjsdkdfjdskfjk1jflksdjflkf1j</strong></p>\r\n<p><em><strong>dfsfdsfsdf</strong></em></p>','2020-10-03 16:47:58',0,0,0,20,1),(3,'测试文章','<p>打发打发</p>\r\n<p><strong><img src=\"data:image/jpeg;base64,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\" /></strong></p>','2020-10-04 11:38:02',0,0,68,22,1),(4,'111','<p>饿温热微软单位覅健康减肥离开我的JFKr的福克斯的房价看空进jf</p>','2020-10-04 11:40:29',0,0,2,18,1),(5,'22222','<p>的发生发射点发范德萨发顺丰方法是多少地方法师攻防技术洛夫克拉的饭卡里说的饭卡了</p>','2020-10-04 11:40:29',0,0,0,21,1),(6,'33333','<p>是非法的飒飒该方法司法考试脚本开发代码</p>','2020-10-04 11:40:29',0,0,0,20,1),(7,'444','<p>方式打发时间的飓风看不到你补发了十几个3</p>','2020-10-04 11:40:29',0,0,0,21,1),(8,'111','<p>饿温热微软单位覅健康减肥离开我的JFKr的福克斯的房价看空进jf</p>','2020-10-04 11:40:29',0,0,1,18,1);
/*!40000 ALTER TABLE `article` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `article_type`
--

DROP TABLE IF EXISTS `article_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `article_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `type_name` varchar(30) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=23 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `article_type`
--

LOCK TABLES `article_type` WRITE;
/*!40000 ALTER TABLE `article_type` DISABLE KEYS */;
INSERT INTO `article_type` VALUES (18,'科技'),(19,'热门'),(20,'互联网'),(21,'新闻'),(22,'搞笑');
/*!40000 ALTER TABLE `article_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `comment`
--

DROP TABLE IF EXISTS `comment`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `comment` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `content` varchar(255) DEFAULT NULL,
  `create_time` datetime DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  `article_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `article_id` (`article_id`),
  KEY `user_id` (`user_id`),
  CONSTRAINT `comment_ibfk_1` FOREIGN KEY (`article_id`) REFERENCES `article` (`id`),
  CONSTRAINT `comment_ibfk_2` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=68 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `comment`
--

LOCK TABLES `comment` WRITE;
/*!40000 ALTER TABLE `comment` DISABLE KEYS */;
INSERT INTO `comment` VALUES (1,'这是一条评论','2020-10-03 17:18:59',1,2),(2,'666','2020-10-06 12:06:07',1,4),(3,'666','2020-10-06 12:06:07',1,4),(4,'666','2020-10-06 12:06:07',1,4),(5,'666','2020-10-06 12:06:07',1,4),(6,'666','2020-10-06 12:06:07',1,4),(7,'666','2020-10-06 12:06:07',1,4),(8,'666','2020-10-06 12:06:07',1,4),(9,'777','2020-10-06 12:06:07',1,4),(10,'777','2020-10-06 12:08:05',1,4),(11,'777','2020-10-06 12:08:05',1,4),(12,'777','2020-10-06 12:08:05',1,4),(13,'777','2020-10-06 12:08:05',1,4),(14,'777','2020-10-06 12:08:05',1,4),(15,'777','2020-10-06 12:08:05',1,4),(16,'777','2020-10-06 12:08:05',1,4),(17,'777','2020-10-06 12:08:05',1,4),(18,'666','2020-10-06 12:08:05',1,2),(19,'666','2020-10-06 12:09:25',1,2),(20,'111','2020-10-06 12:11:24',1,2),(21,'666','2020-10-06 12:16:37',1,8),(22,'666','2020-10-06 12:23:08',1,8),(23,'777','2020-10-06 12:24:23',1,8),(24,'888','2020-10-06 12:25:24',1,8),(25,'999','2020-10-06 12:25:24',1,8),(26,'999','2020-10-06 12:25:24',1,8),(27,'999','2020-10-06 12:25:24',1,8),(28,'11','2020-10-06 12:25:24',1,3),(29,'212','2020-10-06 12:25:24',1,3),(30,'212','2020-10-06 12:25:24',1,3),(31,'212','2020-10-06 12:25:24',1,3),(32,'212','2020-10-06 12:25:24',1,3),(33,'212','2020-10-06 12:25:24',1,3),(34,'212','2020-10-06 12:25:24',1,3),(35,'212','2020-10-06 12:25:24',1,3),(36,'212','2020-10-06 12:25:24',1,3),(37,'212','2020-10-06 12:25:24',1,3),(38,'212','2020-10-06 12:25:24',1,3),(39,'212','2020-10-06 12:25:24',1,3),(40,'212','2020-10-06 12:25:24',1,3),(41,'212','2020-10-06 12:25:24',1,3),(42,'212','2020-10-06 12:25:24',1,3),(43,'212','2020-10-06 12:25:24',1,3),(44,'212','2020-10-06 12:25:24',1,3),(45,'212','2020-10-06 12:25:24',1,3),(46,'212','2020-10-06 12:25:24',1,3),(47,'212','2020-10-06 12:25:24',1,3),(48,'212','2020-10-06 12:25:24',1,3),(49,'212','2020-10-06 12:25:24',1,3),(50,'212','2020-10-06 12:25:24',1,3),(51,'212','2020-10-06 12:25:24',1,3),(52,'212','2020-10-06 12:25:24',1,3),(53,'212','2020-10-06 12:25:24',1,3),(54,'212','2020-10-06 12:25:24',1,3),(55,'212','2020-10-06 12:25:24',1,3),(56,'212','2020-10-06 12:25:24',1,3),(57,'212','2020-10-06 12:25:24',1,3),(58,'212','2020-10-06 12:25:24',1,3),(59,'212','2020-10-06 12:25:24',1,3),(60,'212','2020-10-06 12:25:24',1,3),(61,'212','2020-10-06 12:25:24',1,3),(62,'212','2020-10-06 12:25:24',1,3),(63,'212','2020-10-06 12:25:24',1,3),(64,'212','2020-10-06 12:25:24',1,3),(65,'11','2020-10-06 13:27:03',1,3),(66,'666','2020-10-06 13:27:03',2,5),(67,'666','2020-10-06 13:27:03',2,5);
/*!40000 ALTER TABLE `comment` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `goods`
--

DROP TABLE IF EXISTS `goods`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `goods` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(20) NOT NULL,
  `price` float NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `goods`
--

LOCK TABLES `goods` WRITE;
/*!40000 ALTER TABLE `goods` DISABLE KEYS */;
/*!40000 ALTER TABLE `goods` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `photo`
--

DROP TABLE IF EXISTS `photo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `photo` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `photo_name` varchar(255) NOT NULL,
  `create_time` datetime DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `user_id` (`user_id`),
  CONSTRAINT `photo_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `photo`
--

LOCK TABLES `photo` WRITE;
/*!40000 ALTER TABLE `photo` DISABLE KEYS */;
INSERT INTO `photo` VALUES (8,'202010052358321_2_3_9924.PNG','2020-10-05 23:58:03',1),(9,'20201006133537default_icon1687.jpg','2020-10-06 13:27:03',2);
/*!40000 ALTER TABLE `photo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(30) NOT NULL,
  `password` varchar(255) NOT NULL,
  `phone` varchar(11) NOT NULL,
  `register_time` datetime DEFAULT NULL,
  `is_delete` tinyint(1) DEFAULT NULL,
  `icon` varchar(255) DEFAULT 'upload/icon/default_icon.jpg',
  PRIMARY KEY (`id`),
  UNIQUE KEY `phone` (`phone`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES (1,'ggg','pbkdf2:sha256:150000$tWK3UaUj$4b7b27952059ad44db2b5444c54507d0a2d4f4a59c6d9be6d9c26892314ca772','18307858303','2020-10-03 15:41:32',0,'upload/icon/1231AA0D48B45A349C33C958A9F0FA4F53.jpg'),(2,'aaa','pbkdf2:sha256:150000$iGFBTBJ5$3a09356923db5504fb1e25d1b82305a4e4c98ae011c39ca25111c27e3d3057e1','18307858304','2020-10-06 13:27:03',0,'upload/icon/default_icon.jpg');
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user__goods`
--

DROP TABLE IF EXISTS `user__goods`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `user__goods` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `goods_id` int(11) NOT NULL,
  `num` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `goods_id` (`goods_id`),
  KEY `user_id` (`user_id`),
  CONSTRAINT `user__goods_ibfk_1` FOREIGN KEY (`goods_id`) REFERENCES `goods` (`id`),
  CONSTRAINT `user__goods_ibfk_2` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user__goods`
--

LOCK TABLES `user__goods` WRITE;
/*!40000 ALTER TABLE `user__goods` DISABLE KEYS */;
/*!40000 ALTER TABLE `user__goods` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-10-07 13:40:45
