-- MySQL dump 10.13  Distrib 8.0.12, for Win64 (x86_64)
--
-- Host: localhost    Database: cms_site_db
-- ------------------------------------------------------
-- Server version	8.0.12

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
 SET NAMES utf8mb4 ;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `annoucement_annoucement`
--

DROP TABLE IF EXISTS `annoucement_annoucement`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `annoucement_annoucement` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `receiver` varchar(20) COLLATE utf8_vietnamese_ci NOT NULL,
  `text` longtext COLLATE utf8_vietnamese_ci NOT NULL,
  `sender_id` int(11) NOT NULL,
  `pub_time` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `annoucement_information_sender_id_045c7dc6_fk_users_user_id` (`sender_id`),
  CONSTRAINT `annoucement_information_sender_id_045c7dc6_fk_users_user_id` FOREIGN KEY (`sender_id`) REFERENCES `users_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_vietnamese_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `annoucement_annoucement`
--

LOCK TABLES `annoucement_annoucement` WRITE;
/*!40000 ALTER TABLE `annoucement_annoucement` DISABLE KEYS */;
/*!40000 ALTER TABLE `annoucement_annoucement` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `announcement_announcement`
--

DROP TABLE IF EXISTS `announcement_announcement`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `announcement_announcement` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `receiver` varchar(20) COLLATE utf8_vietnamese_ci NOT NULL,
  `text` longtext COLLATE utf8_vietnamese_ci NOT NULL,
  `pub_time` datetime(6) NOT NULL,
  `sender_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `announcement_annoucement_sender_id_157ee493_fk_users_user_id` (`sender_id`),
  CONSTRAINT `announcement_annoucement_sender_id_157ee493_fk_users_user_id` FOREIGN KEY (`sender_id`) REFERENCES `users_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8 COLLATE=utf8_vietnamese_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `announcement_announcement`
--

LOCK TABLES `announcement_announcement` WRITE;
/*!40000 ALTER TABLE `announcement_announcement` DISABLE KEYS */;
INSERT INTO `announcement_announcement` VALUES (7,'no_thesis_student','请尽快选好导师并且选好论文题目！','2018-11-06 13:21:22.749777',1),(8,'no_thesis_student','请尽快选题！','2018-11-06 22:37:50.916990',1);
/*!40000 ALTER TABLE `announcement_announcement` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) COLLATE utf8_vietnamese_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_vietnamese_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_vietnamese_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) COLLATE utf8_vietnamese_ci NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) COLLATE utf8_vietnamese_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=107 DEFAULT CHARSET=utf8 COLLATE=utf8_vietnamese_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add content type',4,'add_contenttype'),(14,'Can change content type',4,'change_contenttype'),(15,'Can delete content type',4,'delete_contenttype'),(16,'Can view content type',4,'view_contenttype'),(17,'Can add session',5,'add_session'),(18,'Can change session',5,'change_session'),(19,'Can delete session',5,'delete_session'),(20,'Can view session',5,'view_session'),(21,'Can add user',6,'add_user'),(22,'Can change user',6,'change_user'),(23,'Can delete user',6,'delete_user'),(24,'Can view user',6,'view_user'),(25,'Can add student info',7,'add_studentinfo'),(26,'Can change student info',7,'change_studentinfo'),(27,'Can delete student info',7,'delete_studentinfo'),(28,'Can view student info',7,'view_studentinfo'),(29,'Can add teacher info',8,'add_teacherinfo'),(30,'Can change teacher info',8,'change_teacherinfo'),(31,'Can delete teacher info',8,'delete_teacherinfo'),(32,'Can view teacher info',8,'view_teacherinfo'),(33,'Can add student',9,'add_student'),(34,'Can change student',9,'change_student'),(35,'Can delete student',9,'delete_student'),(36,'Can view student',9,'view_student'),(37,'Can add teacher',10,'add_teacher'),(38,'Can change teacher',10,'change_teacher'),(39,'Can delete teacher',10,'delete_teacher'),(40,'Can view teacher',10,'view_teacher'),(41,'Can add tag',11,'add_tag'),(42,'Can change tag',11,'change_tag'),(43,'Can delete tag',11,'delete_tag'),(44,'Can view tag',11,'view_tag'),(45,'Can add thesis',12,'add_thesis'),(46,'Can change thesis',12,'change_thesis'),(47,'Can delete thesis',12,'delete_thesis'),(48,'Can view thesis',12,'view_thesis'),(49,'Can add message',13,'add_message'),(50,'Can change message',13,'change_message'),(51,'Can delete message',13,'delete_message'),(52,'Can view message',13,'view_message'),(53,'Can add collection',14,'add_collection'),(54,'Can change collection',14,'change_collection'),(55,'Can delete collection',14,'delete_collection'),(56,'Can view collection',14,'view_collection'),(57,'Can add Bookmark',15,'add_bookmark'),(58,'Can change Bookmark',15,'change_bookmark'),(59,'Can delete Bookmark',15,'delete_bookmark'),(60,'Can view Bookmark',15,'view_bookmark'),(61,'Can add User Setting',16,'add_usersettings'),(62,'Can change User Setting',16,'change_usersettings'),(63,'Can delete User Setting',16,'delete_usersettings'),(64,'Can view User Setting',16,'view_usersettings'),(65,'Can add User Widget',17,'add_userwidget'),(66,'Can change User Widget',17,'change_userwidget'),(67,'Can delete User Widget',17,'delete_userwidget'),(68,'Can view User Widget',17,'view_userwidget'),(69,'Can add log entry',18,'add_log'),(70,'Can change log entry',18,'change_log'),(71,'Can delete log entry',18,'delete_log'),(72,'Can view log entry',18,'view_log'),(73,'Can add 学生用户表',6,'add_studentuser'),(74,'Can change 学生用户表',6,'change_studentuser'),(75,'Can delete 学生用户表',6,'delete_studentuser'),(76,'Can view 学生用户表',6,'view_studentuser'),(77,'Can add 教师用户表',6,'add_teacheruser'),(78,'Can change 教师用户表',6,'change_teacheruser'),(79,'Can delete 教师用户表',6,'delete_teacheruser'),(80,'Can view 教师用户表',6,'view_teacheruser'),(81,'Can view 学生用户表',19,'view_studentuser'),(82,'Can view 教师用户表',20,'view_teacheruser'),(83,'Can add information',21,'add_information'),(84,'Can change information',21,'change_information'),(85,'Can delete information',21,'delete_information'),(86,'Can view information',21,'view_information'),(87,'Can view annoucement',21,'view_annoucement'),(88,'Can add annoucement',21,'add_annoucement'),(89,'Can change annoucement',21,'change_annoucement'),(90,'Can delete annoucement',21,'delete_annoucement'),(91,'Can add annoucement',22,'add_annoucement'),(92,'Can change annoucement',22,'change_annoucement'),(93,'Can delete annoucement',22,'delete_annoucement'),(94,'Can view annoucement',22,'view_annoucement'),(95,'Can view announcement',22,'view_announcement'),(96,'Can add announcement',22,'add_announcement'),(97,'Can change announcement',22,'change_announcement'),(98,'Can delete announcement',22,'delete_announcement'),(99,'Can add 审题通知表',23,'add_thesisnotice'),(100,'Can change 审题通知表',23,'change_thesisnotice'),(101,'Can delete 审题通知表',23,'delete_thesisnotice'),(102,'Can view 审题通知表',23,'view_thesisnotice'),(103,'Can add 论文题目审核',24,'add_verifythesis'),(104,'Can change 论文题目审核',24,'change_verifythesis'),(105,'Can delete 论文题目审核',24,'delete_verifythesis'),(106,'Can view 论文题目审核',24,'view_verifythesis');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext COLLATE utf8_vietnamese_ci,
  `object_repr` varchar(200) COLLATE utf8_vietnamese_ci NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext COLLATE utf8_vietnamese_ci NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_users_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_users_user_id` FOREIGN KEY (`user_id`) REFERENCES `users_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=148 DEFAULT CHARSET=utf8 COLLATE=utf8_vietnamese_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2018-10-15 15:58:32.443594','2','123456789',3,'',6,1),(2,'2018-10-16 04:42:34.308570','201506401222','张帅桔',2,'[{\"changed\": {\"fields\": [\"teacher\"]}}]',9,1),(3,'2018-10-17 01:41:20.376964','6','<Thesis:图书管理系统>',2,'[{\"changed\": {\"fields\": [\"content\", \"is_choiced\"]}}]',12,1),(4,'2018-10-17 01:41:29.341353','2','<Thesis:网上购物系统>',2,'[{\"changed\": {\"fields\": [\"content\", \"is_choiced\"]}}]',12,1),(5,'2018-10-17 01:49:02.347575','5','<Thesis:飞机大战>',2,'[{\"changed\": {\"fields\": [\"content\", \"is_choiced\"]}}]',12,1),(6,'2018-10-17 01:49:11.042704','2','<Thesis:网上购物系统>',2,'[{\"changed\": {\"fields\": [\"is_choiced\"]}}]',12,1),(7,'2018-10-17 14:58:45.500294','7','201506401224',3,'',6,1),(8,'2018-10-17 14:58:45.618376','6','201506401223',3,'',6,1),(9,'2018-10-17 14:58:45.706440','5','987654321',3,'',6,1),(10,'2018-10-17 14:58:45.818529','4','201506401222',3,'',6,1),(11,'2018-10-17 14:58:45.904580','3','123456789',3,'',6,1),(12,'2018-10-17 14:59:44.087714','201506401224','柳先开',3,'',9,1),(13,'2018-10-17 14:59:44.239819','201506401223','徐军',3,'',9,1),(14,'2018-10-17 14:59:44.317874','201506401222','张帅桔',3,'',9,1),(15,'2018-10-17 14:59:52.329554','987654321','黄云翔',3,'',10,1),(16,'2018-10-17 14:59:52.461645','123456789','覃婷',3,'',10,1),(17,'2018-10-17 15:00:01.209816','7','python',3,'',11,1),(18,'2018-10-17 15:00:01.372933','6','cms',3,'',11,1),(19,'2018-10-17 15:00:01.439979','5','游戏',3,'',11,1),(20,'2018-10-17 15:00:01.611100','4','cms',3,'',11,1),(21,'2018-10-17 15:00:01.718176','3','研究',3,'',11,1),(22,'2018-10-17 15:00:01.784223','2','web',3,'',11,1),(23,'2018-10-17 15:00:08.624060','6','<Thesis:图书管理系统>',3,'',12,1),(24,'2018-10-17 15:00:08.707118','5','<Thesis:飞机大战>',3,'',12,1),(25,'2018-10-17 15:00:08.796181','4','<Thesis:玉林师范学院毕业设计管理系统>',3,'',12,1),(26,'2018-10-17 15:00:08.874237','3','<Thesis:物理大世界>',3,'',12,1),(27,'2018-10-17 15:00:08.928274','2','<Thesis:网上购物系统>',3,'',12,1),(28,'2018-10-17 15:00:17.754515','7','201506401224',3,'',6,1),(29,'2018-10-17 15:00:17.817567','6','201506401223',3,'',6,1),(30,'2018-10-17 15:00:17.890609','5','987654321',3,'',6,1),(31,'2018-10-17 15:00:17.951655','4','201506401222',3,'',6,1),(32,'2018-10-17 15:00:18.039715','3','123456789',3,'',6,1),(33,'2018-10-18 05:41:54.415217','201506401222','张俊桔',2,'[{\"changed\": {\"fields\": [\"thesis\", \"teacher\"]}}]',9,1),(34,'2018-10-18 05:42:30.517741','201506401222','张俊桔',2,'[{\"changed\": {\"fields\": [\"is_choiced_thesis\"]}}]',9,1),(35,'2018-10-18 05:43:09.810518','7','<Thesis:数据挖掘和数据分析>',2,'[{\"changed\": {\"fields\": [\"content\", \"is_choiced\"]}}]',12,1),(36,'2018-10-18 05:56:15.842228','201506401222','张俊桔',2,'[{\"changed\": {\"fields\": [\"is_choiced_thesis\"]}}]',9,1),(37,'2018-10-19 02:41:35.139787','14','cms',3,'',11,1),(38,'2018-10-19 02:41:35.247864','13','数据分析',3,'',11,1),(39,'2018-10-19 02:41:35.343933','12','游戏开发',3,'',11,1),(40,'2018-10-19 02:41:35.432011','11','web开发',3,'',11,1),(41,'2018-10-19 02:41:35.502045','10','web开发',3,'',11,1),(42,'2018-10-19 02:41:35.669162','9','数据分析',3,'',11,1),(43,'2018-10-19 02:41:35.737211','8','python',3,'',11,1),(44,'2018-10-19 07:36:52.442272','24','<Thesis:宇宙的奥秘>',2,'[{\"changed\": {\"fields\": [\"tags\"]}}]',12,1),(45,'2018-10-22 05:28:08.641911','1','Message object (1)',1,'[{\"added\": {}}]',13,1),(46,'2018-10-22 05:28:48.175876','2','Message object (2)',1,'[{\"added\": {}}]',13,1),(47,'2018-10-22 06:05:57.741073','1','老师好，我是张俊桔！',2,'[]',13,1),(48,'2018-10-22 06:07:08.115824','3','老师好！我是计算机学院的一名学生，早已久仰老师大名，不知老师是否愿意指导我完成毕业设计呢？',1,'[{\"added\": {}}]',13,1),(49,'2018-10-22 08:39:12.205239','4','dsa',3,'',13,1),(50,'2018-10-22 08:39:12.338281','5','dsadas',3,'',13,1),(51,'2018-10-22 08:39:12.502398','6','dasdad',3,'',13,1),(52,'2018-10-22 08:39:12.580469','7','dssd',3,'',13,1),(53,'2018-10-22 08:39:12.635492','8','test',3,'',13,1),(54,'2018-10-22 08:39:12.734580','9','testaa',3,'',13,1),(55,'2018-10-22 08:39:12.823630','10','qqqq',3,'',13,1),(56,'2018-10-22 08:39:12.880666','11','dadasddsadas',3,'',13,1),(57,'2018-10-22 08:39:12.935705','12','dsadadsa',3,'',13,1),(58,'2018-10-22 08:39:13.012758','13','zzzzzzzzz',3,'',13,1),(59,'2018-10-23 10:06:02.938098','29','<Thesis:大数据可视化>',2,'[{\"changed\": {\"fields\": [\"is_choiced\"]}}]',12,1),(60,'2018-10-23 15:54:47.699059','25','<Thesis:牛顿第三定律的研究>',2,'[{\"changed\": {\"fields\": [\"tags\"]}}]',12,1),(61,'2018-10-23 15:55:00.496090','27','<Thesis:牛顿第三定律的研究2>',2,'[{\"changed\": {\"fields\": [\"tags\"]}}]',12,1),(62,'2018-10-24 02:00:55.166550','1','Collection object (1)',1,'[{\"added\": {}}]',14,1),(63,'2018-10-24 02:02:53.975533','1','<Collection:张俊桔-<Thesis:python爬虫开发实战>>',2,'[]',14,1),(64,'2018-10-24 02:03:05.331556','3','<Collection:张俊桔-<Thesis:大数据可视化>>',1,'[{\"added\": {}}]',14,1),(65,'2018-10-24 06:02:11.072644','5','何大桂-<Thesis:网上购物系统>',3,'',14,1),(66,'2018-10-24 06:06:16.772343','8','张俊桔-<Thesis:网上购物系统>',3,'',14,1),(67,'2018-10-24 06:06:16.882438','7','张俊桔-<Thesis:网上购物系统>',3,'',14,1),(68,'2018-10-24 07:13:07.542796','4','张俊桔-<Thesis:网上购物系统>',3,'',14,1),(69,'2018-10-24 07:13:07.713926','3','张俊桔-<Thesis:大数据可视化>',3,'',14,1),(70,'2018-10-24 07:13:07.858019','1','张俊桔-<Thesis:python爬虫开发实战>',3,'',14,1),(71,'2018-10-25 14:54:01.279249','1','老师好，我是张俊桔！',3,'',13,1),(72,'2018-10-25 14:54:01.427355','2','张俊桔，你好！',3,'',13,1),(73,'2018-10-25 14:54:01.472399','3','老师好！我是计算机学院的一名学生，早已久仰老师大名，不知老师是否愿意指导我完成毕业设计呢？',3,'',13,1),(74,'2018-10-25 14:54:01.505427','14','何大桂同学，您好',3,'',13,1),(75,'2018-10-25 14:54:01.560447','15','你选题了吗',3,'',13,1),(76,'2018-10-25 14:54:01.605484','16','你选题了吗',3,'',13,1),(77,'2018-10-25 14:54:01.638502','17','你选题了吗',3,'',13,1),(78,'2018-10-25 14:54:01.672540','18','你选题了吗，同学',3,'',13,1),(79,'2018-10-25 14:54:01.704549','19','你选题了吗',3,'',13,1),(80,'2018-10-25 14:54:01.771597','20','dsadads',3,'',13,1),(81,'2018-10-25 14:54:01.816630','21','dsadads',3,'',13,1),(82,'2018-10-25 14:54:01.960731','22','你好',3,'',13,1),(83,'2018-10-25 14:54:02.038787','23','你好吗',3,'',13,1),(84,'2018-10-25 14:54:02.082818','24','哈喽',3,'',13,1),(85,'2018-10-25 14:54:02.127851','25','你好',3,'',13,1),(86,'2018-10-25 14:54:02.171881','26','何足道',3,'',13,1),(87,'2018-10-25 14:54:02.216917','27','你好！',3,'',13,1),(88,'2018-10-25 14:54:02.260951','28','就是打开速度回家',3,'',13,1),(89,'2018-10-25 14:54:02.305977','29','我的历史',3,'',13,1),(90,'2018-10-25 14:54:02.350006','30','我的历史总是',3,'',13,1),(91,'2018-10-25 14:54:02.395040','31','同学，您好！',3,'',13,1),(92,'2018-10-25 14:54:02.438069','32','你你你',3,'',13,1),(93,'2018-10-25 14:54:02.483100','33','你好',3,'',13,1),(94,'2018-10-25 14:54:02.527131','34','123465',3,'',13,1),(95,'2018-10-25 14:54:02.572163','35','123465',3,'',13,1),(96,'2018-10-25 14:54:02.616205','36','200',3,'',13,1),(97,'2018-10-25 14:54:02.661226','37','456',3,'',13,1),(98,'2018-10-25 14:54:02.705258','38','789',3,'',13,1),(99,'2018-10-25 14:54:02.750291','39','789',3,'',13,1),(100,'2018-10-25 14:54:02.794320','40','777',3,'',13,1),(101,'2018-10-25 14:54:02.839369','41','777',3,'',13,1),(102,'2018-10-25 14:54:02.883384','42','444',3,'',13,1),(103,'2018-10-25 14:54:02.928416','43','555',3,'',13,1),(104,'2018-10-25 14:54:02.972463','44','dsadas',3,'',13,1),(105,'2018-10-25 14:54:03.017495','45','dsada',3,'',13,1),(106,'2018-10-25 14:54:03.060509','46','dsadas',3,'',13,1),(107,'2018-10-25 16:08:17.781448','22','游戏',1,'[{\"added\": {}}]',11,1),(108,'2018-10-25 16:08:21.062771','10','<Thesis:飞机大战游戏>',2,'[{\"changed\": {\"fields\": [\"tags\"]}}]',12,1),(109,'2018-10-25 16:08:42.085654','23','web',1,'[{\"added\": {}}]',11,1),(110,'2018-10-25 16:08:45.771248','9','<Thesis:网上订餐系统>',2,'[{\"changed\": {\"fields\": [\"tags\"]}}]',12,1),(111,'2018-10-25 16:08:56.084543','8','<Thesis:网上购物系统>',2,'[{\"changed\": {\"fields\": [\"tags\"]}}]',12,1),(112,'2018-10-26 02:24:48.698523','52','老师您好，很高兴加入你的组！',1,'[{\"added\": {}}]',13,1),(113,'2018-10-26 08:09:51.476601','49','dsa',3,'',13,1),(114,'2018-10-26 08:09:51.598689','48','dsa',3,'',13,1),(115,'2018-10-26 08:09:51.643721','47','dds',3,'',13,1),(116,'2018-10-26 08:10:21.118570','53','梁同学你好！',1,'[{\"added\": {}}]',13,1),(117,'2018-10-26 08:10:46.226341','54','老师你好！',1,'[{\"added\": {}}]',13,1),(118,'2018-10-26 09:01:58.810814','59','你什么时候交开题报告啊！',3,'',13,1),(119,'2018-10-26 09:01:58.912869','58','456798',3,'',13,1),(120,'2018-10-26 09:01:59.057972','57','123456',3,'',13,1),(121,'2018-10-26 09:01:59.235114','56','asdasdadadada',3,'',13,1),(122,'2018-10-26 09:01:59.347176','55','你个傻子',3,'',13,1),(123,'2018-10-26 09:01:59.424231','54','老师你好！',3,'',13,1),(124,'2018-10-26 09:01:59.633392','53','梁同学你好！',3,'',13,1),(125,'2018-10-26 09:01:59.777480','52','老师您好，很高兴加入你的组！',3,'',13,1),(126,'2018-10-26 09:01:59.891562','51','同学你好，你什么时候交开题报告',3,'',13,1),(127,'2018-10-26 09:01:59.979640','50','同学你好，欢迎您选择此题~~',3,'',13,1),(128,'2018-10-26 09:48:44.811571','14','张俊桔-None',3,'',14,1),(129,'2018-10-26 09:49:24.779842','30','<Thesis:python爬虫开发实战>',3,'',12,1),(130,'2018-10-26 09:50:22.284514','9','<Thesis:网上订餐系统>',3,'',12,1),(131,'2018-10-27 04:37:45.373083','74','dadads',3,'',13,1),(132,'2018-10-27 04:37:45.534196','73','dasdasd',3,'',13,1),(133,'2018-10-27 04:37:45.645258','72','dadasd',3,'',13,1),(134,'2018-10-27 04:37:45.733318','71','dasdas',3,'',13,1),(135,'2018-10-27 04:37:45.887427','70','dadadsa',3,'',13,1),(136,'2018-10-27 04:37:45.989500','69','dadasdas',3,'',13,1),(137,'2018-10-27 04:37:46.056548','68','dadasda',3,'',13,1),(138,'2018-10-27 04:37:46.122594','67','dadsa',3,'',13,1),(139,'2018-10-27 04:37:46.189643','66','dadadsa',3,'',13,1),(140,'2018-10-27 04:37:46.266697','65','dsadas',3,'',13,1),(141,'2018-10-27 04:37:46.356777','64','456123456',3,'',13,1),(142,'2018-10-27 04:37:46.422823','63','123456',3,'',13,1),(143,'2018-10-27 04:37:46.489863','62','dadads',3,'',13,1),(144,'2018-10-27 04:37:46.578917','61','dsadas',3,'',13,1),(145,'2018-10-27 04:37:46.644964','60','hhhhh',3,'',13,1),(146,'2018-10-28 04:51:58.346842','456789123','黎簇',2,'[{\"changed\": {\"fields\": [\"rest_number\"]}}]',10,1),(147,'2018-10-28 04:52:11.040589','987654321','王如月',2,'[{\"changed\": {\"fields\": [\"rest_number\"]}}]',10,1);
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) COLLATE utf8_vietnamese_ci NOT NULL,
  `model` varchar(100) COLLATE utf8_vietnamese_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=25 DEFAULT CHARSET=utf8 COLLATE=utf8_vietnamese_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(21,'annoucement','annoucement'),(22,'announcement','announcement'),(3,'auth','group'),(2,'auth','permission'),(4,'contenttypes','contenttype'),(13,'message','message'),(7,'schoolinfo','studentinfo'),(8,'schoolinfo','teacherinfo'),(5,'sessions','session'),(14,'student','collection'),(9,'student','student'),(10,'teacher','teacher'),(11,'thesis','tag'),(12,'thesis','thesis'),(23,'thesis_notice','thesisnotice'),(19,'users','studentuser'),(20,'users','teacheruser'),(6,'users','user'),(24,'verify','verifythesis'),(15,'xadmin','bookmark'),(18,'xadmin','log'),(16,'xadmin','usersettings'),(17,'xadmin','userwidget');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) COLLATE utf8_vietnamese_ci NOT NULL,
  `name` varchar(255) COLLATE utf8_vietnamese_ci NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=82 DEFAULT CHARSET=utf8 COLLATE=utf8_vietnamese_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2018-10-15 15:39:24.120775'),(2,'contenttypes','0002_remove_content_type_name','2018-10-15 15:39:24.978381'),(3,'auth','0001_initial','2018-10-15 15:39:27.722320'),(4,'auth','0002_alter_permission_name_max_length','2018-10-15 15:39:28.266704'),(5,'auth','0003_alter_user_email_max_length','2018-10-15 15:39:28.315741'),(6,'auth','0004_alter_user_username_opts','2018-10-15 15:39:28.358787'),(7,'auth','0005_alter_user_last_login_null','2018-10-15 15:39:28.403819'),(8,'auth','0006_require_contenttypes_0002','2018-10-15 15:39:28.443830'),(9,'auth','0007_alter_validators_add_error_messages','2018-10-15 15:39:28.494866'),(10,'auth','0008_alter_user_username_max_length','2018-10-15 15:39:28.565916'),(11,'auth','0009_alter_user_last_name_max_length','2018-10-15 15:39:28.616972'),(12,'users','0001_initial','2018-10-15 15:39:32.910988'),(13,'admin','0001_initial','2018-10-15 15:39:34.834347'),(14,'admin','0002_logentry_remove_auto_add','2018-10-15 15:39:34.952433'),(15,'admin','0003_logentry_add_action_flag_choices','2018-10-15 15:39:35.017477'),(16,'schoolinfo','0001_initial','2018-10-15 15:39:35.081522'),(17,'sessions','0001_initial','2018-10-15 15:39:35.655928'),(18,'thesis','0001_initial','2018-10-15 15:39:36.229334'),(19,'teacher','0001_initial','2018-10-15 15:39:37.088960'),(20,'student','0001_initial','2018-10-15 15:39:38.132680'),(21,'student','0002_student_teacher','2018-10-15 15:39:38.933264'),(22,'student','0003_student_thesis','2018-10-15 15:39:40.379267'),(23,'student','0004_student_user','2018-10-15 15:39:42.589849'),(24,'teacher','0002_teacher_user','2018-10-15 15:39:44.007851'),(25,'thesis','0002_auto_20181015_2339','2018-10-15 15:39:46.078298'),(26,'student','0005_auto_20181016_2003','2018-10-16 12:04:05.998316'),(27,'teacher','0003_auto_20181016_2003','2018-10-16 12:04:06.128392'),(28,'thesis','0003_auto_20181016_2003','2018-10-16 12:04:06.198459'),(29,'schoolinfo','0002_auto_20181017_2326','2018-10-17 15:27:10.887951'),(30,'schoolinfo','0003_remove_studentinfo_is_register','2018-10-17 15:27:17.324484'),(31,'thesis','0004_auto_20181017_2326','2018-10-17 15:27:17.458578'),(32,'schoolinfo','0004_auto_20181018_1331','2018-10-18 05:31:41.490912'),(33,'student','0006_auto_20181018_1331','2018-10-18 05:31:50.142020'),(34,'thesis','0005_auto_20181019_1040','2018-10-19 02:40:40.013816'),(35,'message','0001_initial','2018-10-20 09:17:50.674956'),(36,'teacher','0004_auto_20181020_1714','2018-10-20 09:17:50.824061'),(37,'message','0002_auto_20181024_0946','2018-10-24 01:46:06.987626'),(38,'student','0007_collection','2018-10-24 01:46:15.515655'),(39,'student','0008_auto_20181024_1405','2018-10-24 06:06:36.143038'),(40,'message','0003_auto_20181026_1730','2018-10-26 09:30:22.700002'),(41,'teacher','0005_teacher_rest_number','2018-10-28 04:40:13.102086'),(42,'teacher','0006_remove_teacher_rest_number','2018-10-28 05:27:49.663493'),(43,'xadmin','0001_initial','2018-10-28 15:12:33.188531'),(44,'xadmin','0002_log','2018-10-28 15:12:35.647288'),(45,'xadmin','0003_auto_20160715_0100','2018-10-28 15:12:36.853141'),(46,'message','0004_auto_20181031_1043','2018-11-03 11:59:31.528189'),(47,'message','0005_auto_20181103_1157','2018-11-03 11:59:33.183363'),(48,'student','0009_auto_20181031_1043','2018-11-03 11:59:37.385340'),(49,'student','0010_auto_20181103_1157','2018-11-03 11:59:37.462411'),(50,'teacher','0007_auto_20181031_1043','2018-11-03 11:59:38.595213'),(51,'thesis','0006_auto_20181031_1043','2018-11-03 11:59:42.004611'),(52,'users','0002_auto_20181103_1157','2018-11-03 11:59:42.056647'),(53,'message','0006_auto_20181103_1408','2018-11-03 14:08:39.204243'),(54,'teacher','0008_auto_20181103_1408','2018-11-03 14:08:40.039832'),(55,'annoucement','0001_initial','2018-11-04 12:19:40.180300'),(56,'users','0003_auto_20181104_1219','2018-11-04 12:19:40.271366'),(57,'annoucement','0002_auto_20181104_1221','2018-11-04 12:21:22.089496'),(58,'annoucement','0003_auto_20181104_1243','2018-11-04 12:44:51.035627'),(59,'annoucement','0004_annoucement_pub_time','2018-11-04 12:44:52.322545'),(60,'announcement','0001_initial','2018-11-04 12:51:09.763944'),(61,'announcement','0002_auto_20181104_1252','2018-11-04 12:52:12.131112'),(62,'thesis_notice','0001_initial','2018-11-05 21:29:33.070331'),(63,'thesis_notice','0002_auto_20181105_2144','2018-11-05 21:44:23.745989'),(64,'thesis','0007_thesis_need_verify','2018-11-05 22:24:17.620348'),(65,'thesis_notice','0003_auto_20181106_1100','2018-11-06 11:00:49.238269'),(66,'thesis','0008_auto_20181106_1108','2018-11-06 11:08:26.397129'),(67,'student','0011_student_read_announcement','2018-11-06 16:35:05.303762'),(68,'student','0012_auto_20181106_1634','2018-11-06 16:35:07.860576'),(69,'teacher','0009_teacher_read_announcement','2018-11-06 16:35:10.060132'),(70,'teacher','0010_auto_20181106_1634','2018-11-06 16:35:11.895433'),(71,'student','0013_auto_20181108_1113','2018-11-08 11:14:05.469046'),(72,'teacher','0011_auto_20181108_1113','2018-11-08 11:14:08.963537'),(73,'thesis','0009_auto_20181108_1113','2018-11-08 11:14:11.703462'),(74,'users','0004_auto_20181108_1113','2018-11-08 11:14:14.023121'),(75,'thesis','0010_remove_thesis_need_verify','2018-11-08 16:33:59.337244'),(76,'verify','0001_initial','2018-11-08 16:34:02.382384'),(77,'verify','0002_verifythesis_teacher','2018-11-08 16:37:23.856131'),(78,'thesis','0011_thesis_need_veryfy','2018-11-08 16:54:28.397941'),(79,'verify','0003_auto_20181108_1654','2018-11-08 16:54:31.507126'),(80,'thesis','0012_auto_20181108_1655','2018-11-08 16:55:34.129491'),(81,'thesis','0013_auto_20181108_1657','2018-11-08 16:57:40.670134');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `django_session` (
  `session_key` varchar(40) COLLATE utf8_vietnamese_ci NOT NULL,
  `session_data` longtext COLLATE utf8_vietnamese_ci NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_vietnamese_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('16906x2vi8nk8vsdpclt2ai2w0riisjl','MzgwNWJjMWE3ZGI4ZjI3NGFjNTk3YWQ4MzQ0NWE3ZWM1MWJiYWEwYjp7Il9hdXRoX3VzZXJfaWQiOiIxNyIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiYzQxOWViZGU2YjJhMzVhMzBmY2ZmNTk4NzdjNzAxNGM1OGVkNzQxYyJ9','2018-11-04 15:54:21.898216'),('1jnddk5d6f4c8wsa14kzdcnvnl87uytp','MzgwNWJjMWE3ZGI4ZjI3NGFjNTk3YWQ4MzQ0NWE3ZWM1MWJiYWEwYjp7Il9hdXRoX3VzZXJfaWQiOiIxNyIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiYzQxOWViZGU2YjJhMzVhMzBmY2ZmNTk4NzdjNzAxNGM1OGVkNzQxYyJ9','2018-11-20 22:55:03.476480'),('1o80ln30cuk14p8qdz41lskjercmg761','ZmVmZjcwYmRkZjk0ZGZmOWE3MmNiYzcyNDdkY2U0NGRhODdhNDc2Yzp7Il9hdXRoX3VzZXJfaWQiOiIxMyIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiYjNkMDQwZTA3YzIwMmI5OTU0OWU2ZTQyYTRlZmZkNzQwNjcwY2YzZSJ9','2018-11-20 22:33:59.386969'),('226il1tt55ambawt136r5fuiwp3l9fc5','ODIxNDRmMjQ5ZWZhMDg1MjhiNDY3ZGM4MTQyZDlmYTk5NjA0OWZjMTp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJiNTEzOTJjN2Q4ZTY4MmUzYzY0YTBiMDY3MzBkMmNjNTNlNWY5NGExIiwiTElTVF9RVUVSWSI6W1sidXNlcnMiLCJ1c2VyIl0sIiJdfQ==','2018-11-11 15:13:05.915679'),('2twjfu0u80lk5p4smloa0hy2c9vdu6y4','MGNkN2NmNWU5MmY4NDhmNjhkOTk1NjEyYmQ4ZjZjNjVlNzg5NzY0Mjp7Il9hdXRoX3VzZXJfaWQiOiIxMyIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiZmI3M2NmMjg5Nzk4ODllMjVlNTYzMTY0ZDY5NzVkMmVlODkxMmNiMCJ9','2018-11-08 03:03:15.949370'),('3p2ondi2rel9p8qp7zpjx6jnmuo7uje1','MGNkN2NmNWU5MmY4NDhmNjhkOTk1NjEyYmQ4ZjZjNjVlNzg5NzY0Mjp7Il9hdXRoX3VzZXJfaWQiOiIxMyIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiZmI3M2NmMjg5Nzk4ODllMjVlNTYzMTY0ZDY5NzVkMmVlODkxMmNiMCJ9','2018-11-08 05:28:53.864698'),('4395mrlnmq9da1ya6rxrvj429u7mdie7','NmExNDMxZjllNGQ5ZWNmZTYwYTY5MWE4ZDFkN2EyOTVmZDg3MDQ2OTp7Il9hdXRoX3VzZXJfaWQiOiI0IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJlNDNjZDY2NDY0OTE5NWZiYTAxNjQ1OTVjYTcwNGExYTkxODViNWFiIn0=','2018-10-31 09:12:07.548981'),('4fqvacvqmhr8f11fik3vqdg3i90qk6ju','ZmVmZjcwYmRkZjk0ZGZmOWE3MmNiYzcyNDdkY2U0NGRhODdhNDc2Yzp7Il9hdXRoX3VzZXJfaWQiOiIxMyIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiYjNkMDQwZTA3YzIwMmI5OTU0OWU2ZTQyYTRlZmZkNzQwNjcwY2YzZSJ9','2018-11-21 10:07:36.140471'),('4zpflbr5johji44w8qw9387gk9yp7n84','ZGU1MWUxMjdkYmU3MjMxZDIyMDMwYTViYjkwMzQ0OWY0OGQxOWYyMzp7Il9hdXRoX3VzZXJfaWQiOiIzIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI5OTcwYzk4MDNmNzA0ZGVkYWZiM2MwMGI1NWVjZDZhNDBjZjBmZTM1In0=','2018-10-30 12:24:43.624252'),('5jp7hpvahtgi1meanxfsqn6g3adx1jcf','YThjNDJmY2JmYjMwMjMwZWJhMjE0ZmRhMDVmM2VhNWYyMTAwYTg4Mjp7Il9hdXRoX3VzZXJfaWQiOiIzMSIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiYzBhMTI5MWVlYzQwNTFlYjM2NmI1MWMzYWViMWU3NzE1ZTY2YjQ4NyJ9','2018-11-23 09:31:46.003290'),('6icqx08th7d55e8ba8qsn1irw0rpztui','YTIwNWU5MjU1ZTlkMjIyMjU2ODk1M2U3NjNjZWFhYWY5NDQ1MDkzODp7Il9hdXRoX3VzZXJfaWQiOiIxMyIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiYzZiODgxMDRhMjQ3YzEzMDlkMzEwOGRmYjNkN2EyOGEwNjk0YzQ3YSJ9','2018-10-31 15:49:19.186987'),('7egdwytnk4od4ve6kavgo1eapo2ia7re','NDFiMTllYzhmMzhiNDY1ZWFmY2NhMmVlYTdiY2ExM2E4OWJjOTg0NTp7fQ==','2018-11-20 13:23:16.086083'),('7ubxkd7jeypb5brl2rndeoxe2z0lbrq9','ZGU1MWUxMjdkYmU3MjMxZDIyMDMwYTViYjkwMzQ0OWY0OGQxOWYyMzp7Il9hdXRoX3VzZXJfaWQiOiIzIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI5OTcwYzk4MDNmNzA0ZGVkYWZiM2MwMGI1NWVjZDZhNDBjZjBmZTM1In0=','2018-10-30 12:55:56.483289'),('7zdi7wvnz2dxxvi6y52rbh1i6x45qq2k','ODc1YzFlZjgwOTkwYTgzNTkwMDk3ZWVlMDQ4NzQ4NjZmOWVhM2M5Mzp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJiNTEzOTJjN2Q4ZTY4MmUzYzY0YTBiMDY3MzBkMmNjNTNlNWY5NGExIiwiTElTVF9RVUVSWSI6W1sidGhlc2lzIiwidGhlc2lzIl0sIiJdfQ==','2018-11-23 21:12:15.569120'),('8go9qk7532x5dexs1a57k8xnox2kd5ow','MTNmYTdiZTFkMjY2NTk3YmI0NDFjYjU0ZGE0NDUxNmQwOGE4ZmI3NDp7Il9hdXRoX3VzZXJfaWQiOiIxNSIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiYmNlZTMyZjQ2YTIyNzFiMzIxOGMxYjEwNDBiYjVhZjM2ZTRhMWU4NyJ9','2018-11-07 05:47:45.464711'),('8o6kood932sm1w5qpfqq7j2q9f12uc81','ZmVmZjcwYmRkZjk0ZGZmOWE3MmNiYzcyNDdkY2U0NGRhODdhNDc2Yzp7Il9hdXRoX3VzZXJfaWQiOiIxMyIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiYjNkMDQwZTA3YzIwMmI5OTU0OWU2ZTQyYTRlZmZkNzQwNjcwY2YzZSJ9','2018-11-22 11:09:10.885037'),('8pak4kqloz5y2kfw9lzk4lqlvhr3w5da','ZmVmZjcwYmRkZjk0ZGZmOWE3MmNiYzcyNDdkY2U0NGRhODdhNDc2Yzp7Il9hdXRoX3VzZXJfaWQiOiIxMyIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiYjNkMDQwZTA3YzIwMmI5OTU0OWU2ZTQyYTRlZmZkNzQwNjcwY2YzZSJ9','2018-11-23 20:41:21.300736'),('99rtm8qu2bh7aumnxmfb4abcd42uxss1','MzgwNWJjMWE3ZGI4ZjI3NGFjNTk3YWQ4MzQ0NWE3ZWM1MWJiYWEwYjp7Il9hdXRoX3VzZXJfaWQiOiIxNyIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiYzQxOWViZGU2YjJhMzVhMzBmY2ZmNTk4NzdjNzAxNGM1OGVkNzQxYyJ9','2018-11-21 22:38:11.638852'),('aciz3xa2oni00qy8sfigjdv8ikbmt372','MzgwNWJjMWE3ZGI4ZjI3NGFjNTk3YWQ4MzQ0NWE3ZWM1MWJiYWEwYjp7Il9hdXRoX3VzZXJfaWQiOiIxNyIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiYzQxOWViZGU2YjJhMzVhMzBmY2ZmNTk4NzdjNzAxNGM1OGVkNzQxYyJ9','2018-11-19 17:19:23.613343'),('b8ps5bupd1v0cmyfav5uvmuo42d1gd5z','MzgwNWJjMWE3ZGI4ZjI3NGFjNTk3YWQ4MzQ0NWE3ZWM1MWJiYWEwYjp7Il9hdXRoX3VzZXJfaWQiOiIxNyIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiYzQxOWViZGU2YjJhMzVhMzBmY2ZmNTk4NzdjNzAxNGM1OGVkNzQxYyJ9','2018-11-23 13:23:54.377385'),('bg8rl6pzqezukv0y67be3uux40nuumai','ZmVmZjcwYmRkZjk0ZGZmOWE3MmNiYzcyNDdkY2U0NGRhODdhNDc2Yzp7Il9hdXRoX3VzZXJfaWQiOiIxMyIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiYjNkMDQwZTA3YzIwMmI5OTU0OWU2ZTQyYTRlZmZkNzQwNjcwY2YzZSJ9','2018-11-19 21:13:04.487977'),('btfzxemk0te94qj75riuwp56jr2rbmhp','NmExNDMxZjllNGQ5ZWNmZTYwYTY5MWE4ZDFkN2EyOTVmZDg3MDQ2OTp7Il9hdXRoX3VzZXJfaWQiOiI0IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJlNDNjZDY2NDY0OTE5NWZiYTAxNjQ1OTVjYTcwNGExYTkxODViNWFiIn0=','2018-10-31 02:39:44.732401'),('dmwib3gjdlr4yl6u63gzkjgzaocd8j8l','MzgwNWJjMWE3ZGI4ZjI3NGFjNTk3YWQ4MzQ0NWE3ZWM1MWJiYWEwYjp7Il9hdXRoX3VzZXJfaWQiOiIxNyIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiYzQxOWViZGU2YjJhMzVhMzBmY2ZmNTk4NzdjNzAxNGM1OGVkNzQxYyJ9','2018-11-03 14:52:16.433064'),('drvq3nm21y4dnbc5q42s8qstgn7h6nbr','MzgwNWJjMWE3ZGI4ZjI3NGFjNTk3YWQ4MzQ0NWE3ZWM1MWJiYWEwYjp7Il9hdXRoX3VzZXJfaWQiOiIxNyIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiYzQxOWViZGU2YjJhMzVhMzBmY2ZmNTk4NzdjNzAxNGM1OGVkNzQxYyJ9','2018-11-07 07:35:18.689864'),('g0lt628c3f7lza8y33wychuie8axwxoi','MzgwNWJjMWE3ZGI4ZjI3NGFjNTk3YWQ4MzQ0NWE3ZWM1MWJiYWEwYjp7Il9hdXRoX3VzZXJfaWQiOiIxNyIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiYzQxOWViZGU2YjJhMzVhMzBmY2ZmNTk4NzdjNzAxNGM1OGVkNzQxYyJ9','2018-11-04 08:05:18.666847'),('hlb8l3dbyc3g4wj3qn1jfale423ueymz','ZmVmZjcwYmRkZjk0ZGZmOWE3MmNiYzcyNDdkY2U0NGRhODdhNDc2Yzp7Il9hdXRoX3VzZXJfaWQiOiIxMyIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiYjNkMDQwZTA3YzIwMmI5OTU0OWU2ZTQyYTRlZmZkNzQwNjcwY2YzZSJ9','2018-11-17 13:55:58.904627'),('jvlcpn4n43bmdt3x3gegplmrj6bxaay8','MGNkN2NmNWU5MmY4NDhmNjhkOTk1NjEyYmQ4ZjZjNjVlNzg5NzY0Mjp7Il9hdXRoX3VzZXJfaWQiOiIxMyIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiZmI3M2NmMjg5Nzk4ODllMjVlNTYzMTY0ZDY5NzVkMmVlODkxMmNiMCJ9','2018-11-09 09:49:54.652954'),('mjbp5dz6gxiha1rwginfmg4ttbq4wp12','ZmVmZjcwYmRkZjk0ZGZmOWE3MmNiYzcyNDdkY2U0NGRhODdhNDc2Yzp7Il9hdXRoX3VzZXJfaWQiOiIxMyIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiYjNkMDQwZTA3YzIwMmI5OTU0OWU2ZTQyYTRlZmZkNzQwNjcwY2YzZSJ9','2018-11-20 13:39:58.418143'),('nhkld5srn9wo3d8zh6zx88axajjvr1k2','MzgwNWJjMWE3ZGI4ZjI3NGFjNTk3YWQ4MzQ0NWE3ZWM1MWJiYWEwYjp7Il9hdXRoX3VzZXJfaWQiOiIxNyIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiYzQxOWViZGU2YjJhMzVhMzBmY2ZmNTk4NzdjNzAxNGM1OGVkNzQxYyJ9','2018-11-04 02:25:11.421772'),('o857rz30zrvb3dy81zt1sl24lmze55gy','MGNkN2NmNWU5MmY4NDhmNjhkOTk1NjEyYmQ4ZjZjNjVlNzg5NzY0Mjp7Il9hdXRoX3VzZXJfaWQiOiIxMyIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiZmI3M2NmMjg5Nzk4ODllMjVlNTYzMTY0ZDY5NzVkMmVlODkxMmNiMCJ9','2018-11-05 09:25:57.008169'),('ozn0842i088z5ttdilua1wq8zksppzlq','ZmVmZjcwYmRkZjk0ZGZmOWE3MmNiYzcyNDdkY2U0NGRhODdhNDc2Yzp7Il9hdXRoX3VzZXJfaWQiOiIxMyIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiYjNkMDQwZTA3YzIwMmI5OTU0OWU2ZTQyYTRlZmZkNzQwNjcwY2YzZSJ9','2018-11-19 23:57:35.038216'),('q2ie4ewdybcsiou55xwyo7mnzgq8cg14','NGJmMWFhMjNhMTBmNzlkNmEwMTM0OTc4NzBhMWI5OTZkMjI3YWE5YTp7Il9hdXRoX3VzZXJfaWQiOiIxNyIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiZGFlNjIwM2E4ZWZmZWMzMWJmMDUzZTNlOTE3NzI1NjQwNjMwZjM4MyJ9','2018-11-01 08:47:50.286969'),('qcaklnj4t371bimrhjuh4ugwxrd8ampw','ZmVmZjcwYmRkZjk0ZGZmOWE3MmNiYzcyNDdkY2U0NGRhODdhNDc2Yzp7Il9hdXRoX3VzZXJfaWQiOiIxMyIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiYjNkMDQwZTA3YzIwMmI5OTU0OWU2ZTQyYTRlZmZkNzQwNjcwY2YzZSJ9','2018-11-21 16:39:02.779362'),('qdbwvojklqtfs6z4kxleu6jrt3iadjvr','ZjFkZTFiNjljODk5OTUxNDI2ZTU2ZTkyYjg2NjhmMzEyMjlhMWRiYjp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJiNTEzOTJjN2Q4ZTY4MmUzYzY0YTBiMDY3MzBkMmNjNTNlNWY5NGExIn0=','2018-10-29 15:59:39.415938'),('qlapkrv9fs47ihld0bk07gwzaacvp1j1','NTFiNmNkN2NmZTcyMWFmMGVlODNjOGQ1NWYxN2JhYmRlZjAwMDJkYTp7Il9hdXRoX3VzZXJfaWQiOiIxNCIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiY2I5OGQ3MGZmMDYxMDhjODg3M2RiZTYxMTgzMWVjYmJkMzYzNjg0MSJ9','2018-11-08 09:37:35.391259'),('qlezz60oprinv51x0ybvipjgkg7tuvsp','ZjgxYTRkMTA0NWI2Y2U3MGNkNjE3YjczYTk4NTcxOTA2MWI3MDQ4Njp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJiNTEzOTJjN2Q4ZTY4MmUzYzY0YTBiMDY3MzBkMmNjNTNlNWY5NGExIiwid2l6YXJkX3hhZG1pbnVzZXJ3aWRnZXRfYWRtaW5fd2l6YXJkX2Zvcm1fcGx1Z2luIjp7InN0ZXAiOiJXaWRnZXRcdTdjN2JcdTU3OGIiLCJzdGVwX2RhdGEiOnt9LCJzdGVwX2ZpbGVzIjp7fSwiZXh0cmFfZGF0YSI6e319LCJMSVNUX1FVRVJZIjpbWyJ4YWRtaW4iLCJ1c2Vyd2lkZ2V0Il0sIiJdfQ==','2018-11-22 23:01:44.987795'),('qoi8551rrlrooouw8lxqfcsjns5kobhr','OWIyYjg5N2IzMzkzZTliZTJlMzg4ZDhiZDA3Y2VhZTdmMGYzZWFiODp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJiNTEzOTJjN2Q4ZTY4MmUzYzY0YTBiMDY3MzBkMmNjNTNlNWY5NGExIiwiTElTVF9RVUVSWSI6W1sidXNlcnMiLCJ1c2VyIl0sIl9xXz0iXSwid2l6YXJkX3hhZG1pbnVzZXJ3aWRnZXRfYWRtaW5fd2l6YXJkX2Zvcm1fcGx1Z2luIjp7InN0ZXAiOiJXaWRnZXRcdTdjN2JcdTU3OGIiLCJzdGVwX2RhdGEiOnt9LCJzdGVwX2ZpbGVzIjp7fSwiZXh0cmFfZGF0YSI6e319fQ==','2018-11-22 22:54:51.252694'),('qtjuv51ep7f46rhyl1wxdmu0wyrigtj0','YThjNDJmY2JmYjMwMjMwZWJhMjE0ZmRhMDVmM2VhNWYyMTAwYTg4Mjp7Il9hdXRoX3VzZXJfaWQiOiIzMSIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiYzBhMTI5MWVlYzQwNTFlYjM2NmI1MWMzYWViMWU3NzE1ZTY2YjQ4NyJ9','2018-11-18 21:42:35.800407'),('rhr29omjkwhasjthklvbyg85z0x1aahh','MzgwNWJjMWE3ZGI4ZjI3NGFjNTk3YWQ4MzQ0NWE3ZWM1MWJiYWEwYjp7Il9hdXRoX3VzZXJfaWQiOiIxNyIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiYzQxOWViZGU2YjJhMzVhMzBmY2ZmNTk4NzdjNzAxNGM1OGVkNzQxYyJ9','2018-11-06 10:07:32.578452'),('s6btvinlbjonyherybciymgw74xc4ekk','NTFiNmNkN2NmZTcyMWFmMGVlODNjOGQ1NWYxN2JhYmRlZjAwMDJkYTp7Il9hdXRoX3VzZXJfaWQiOiIxNCIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiY2I5OGQ3MGZmMDYxMDhjODg3M2RiZTYxMTgzMWVjYmJkMzYzNjg0MSJ9','2018-11-06 09:44:52.585995'),('s95ig6uz4i8mdbedelahjnj04vfuzgan','MzgwNWJjMWE3ZGI4ZjI3NGFjNTk3YWQ4MzQ0NWE3ZWM1MWJiYWEwYjp7Il9hdXRoX3VzZXJfaWQiOiIxNyIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiYzQxOWViZGU2YjJhMzVhMzBmY2ZmNTk4NzdjNzAxNGM1OGVkNzQxYyJ9','2018-11-18 10:31:15.232826'),('t4xjhgoh2wjbq7h4rlutuw3j1fvp3avp','NDFiMTllYzhmMzhiNDY1ZWFmY2NhMmVlYTdiY2ExM2E4OWJjOTg0NTp7fQ==','2018-11-20 13:23:54.728442'),('u5ew52jmy0fohhtyx141ntyn8fs3nl03','MzgwNWJjMWE3ZGI4ZjI3NGFjNTk3YWQ4MzQ0NWE3ZWM1MWJiYWEwYjp7Il9hdXRoX3VzZXJfaWQiOiIxNyIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiYzQxOWViZGU2YjJhMzVhMzBmY2ZmNTk4NzdjNzAxNGM1OGVkNzQxYyJ9','2018-11-17 23:07:45.233433'),('ulmqntv56g2nbgm4czsrq9mhvpgmshjt','NmExNDMxZjllNGQ5ZWNmZTYwYTY5MWE4ZDFkN2EyOTVmZDg3MDQ2OTp7Il9hdXRoX3VzZXJfaWQiOiI0IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJlNDNjZDY2NDY0OTE5NWZiYTAxNjQ1OTVjYTcwNGExYTkxODViNWFiIn0=','2018-10-31 04:35:36.892550'),('uqe152d4nwrh2h4govsl70cqyatptgf7','NDFiMTllYzhmMzhiNDY1ZWFmY2NhMmVlYTdiY2ExM2E4OWJjOTg0NTp7fQ==','2018-10-30 02:04:48.926927'),('uronvql32lz5ywgiufg6puuyum33ryp3','ZmVmZjcwYmRkZjk0ZGZmOWE3MmNiYzcyNDdkY2U0NGRhODdhNDc2Yzp7Il9hdXRoX3VzZXJfaWQiOiIxMyIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiYjNkMDQwZTA3YzIwMmI5OTU0OWU2ZTQyYTRlZmZkNzQwNjcwY2YzZSJ9','2018-11-22 15:34:11.526550'),('v3htqmpkx0bc474tna91n9wsf2r9tjfd','YWIwYzQ3OTY1ZGIxYjQyODZmNDA1Mzc1Y2MxNmNlNmEyMjE1Y2Q4ODp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJiNTEzOTJjN2Q4ZTY4MmUzYzY0YTBiMDY3MzBkMmNjNTNlNWY5NGExIiwiTElTVF9RVUVSWSI6W1siYW5ub3VuY2VtZW50IiwiYW5ub3VuY2VtZW50Il0sIiJdfQ==','2018-11-18 13:14:20.045838'),('y47ul1iau3ht1btsaq5ynoo960lt6wbr','ODgyYjE5NjI4MDI3NzZjNjI4MzFhNThjYmYwYzFjMjNiZTBlNjRjZDp7Il9hdXRoX3VzZXJfaWQiOiIxNiIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiOGEyODdjYzNiYmRlM2IxY2M3MjcyODYzYmUyZGE5ZTRjNGIxZDFhMCJ9','2018-11-08 08:50:23.989949');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `message_message`
--

DROP TABLE IF EXISTS `message_message`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `message_message` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `content` longtext COLLATE utf8_vietnamese_ci NOT NULL,
  `send_time` datetime(6) NOT NULL,
  `is_read` tinyint(1) NOT NULL,
  `receiver_id` int(11) NOT NULL,
  `sender_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `message_message_receiver_id_dc38e7dd` (`receiver_id`),
  KEY `message_message_sender_id_b8690ab2` (`sender_id`),
  CONSTRAINT `message_message_sender_id_b8690ab2_fk_users_user_id` FOREIGN KEY (`sender_id`) REFERENCES `users_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=163 DEFAULT CHARSET=utf8 COLLATE=utf8_vietnamese_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `message_message`
--

LOCK TABLES `message_message` WRITE;
/*!40000 ALTER TABLE `message_message` DISABLE KEYS */;
INSERT INTO `message_message` VALUES (107,'老师好','2018-11-03 14:07:06.347459',1,18,13),(119,'发开题报告的模板给我','2018-11-03 14:09:01.165799',1,18,13),(120,'什么时候交开题报告','2018-11-03 14:09:09.176474',1,18,13),(121,'OK的','2018-11-03 14:09:12.444790',1,18,13),(122,'132456','2018-11-03 15:37:12.966642',1,18,13),(123,'123456','2018-11-03 15:40:50.120480',1,13,18),(124,'HHH','2018-11-03 23:08:26.427597',1,14,17),(125,'HHH','2018-11-03 23:08:35.441984',1,15,17),(126,'你的开题报告交了吗？明天再办公室714集合哦！','2018-11-03 23:23:38.708882',1,14,17),(127,'假设这是一条公告！假设这是一条公告！假设这是一条公告！假设这是一条公告！假设这是一条公告！假设这是一条公告！假设这是一条公告！假设这是一条公告！假设这是一条公告！假设这是一条公告！','2018-11-03 23:24:07.724437',1,14,17),(128,'123465','2018-11-04 00:04:56.920508',1,17,14),(129,'123456','2018-11-04 00:04:59.099052',1,17,14),(130,'132456','2018-11-04 00:05:09.922736',1,17,14),(131,'23456','2018-11-04 00:05:10.801341',1,17,14),(132,'ttttt','2018-11-04 00:05:45.493918',1,17,15),(133,'tt','2018-11-04 00:05:46.033300',1,17,15),(134,'tt','2018-11-04 00:05:46.570681',1,17,15),(135,'t','2018-11-04 00:05:46.902917',1,17,15),(136,'tttt','2018-11-04 00:05:48.381966',1,17,15),(137,'123456','2018-11-04 10:31:31.750976',1,14,17),(138,'aaaaaa','2018-11-04 10:57:04.976736',1,14,17),(139,'这是管理员的信息！','2018-11-04 11:12:16.343056',1,14,1),(154,'123456','2018-11-06 12:30:34.418279',1,14,17),(155,'123465','2018-11-06 12:30:41.074978',0,15,17),(156,'123654','2018-11-06 22:55:16.263540',1,13,17),(157,'123456','2018-11-08 11:51:08.444043',1,17,13),(158,'456','2018-11-08 11:51:22.283848',1,17,13),(159,'建议换个选题！','2018-11-08 16:19:49.107903',1,13,17),(160,'test','2018-11-08 17:00:15.659934',1,13,17),(161,'建议换个选题','2018-11-08 18:00:25.232044',1,13,17),(162,'111\r\n','2018-11-09 09:33:07.303901',1,13,31);
/*!40000 ALTER TABLE `message_message` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `my_cache_table`
--

DROP TABLE IF EXISTS `my_cache_table`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `my_cache_table` (
  `cache_key` varchar(255) COLLATE utf8_vietnamese_ci NOT NULL,
  `value` longtext COLLATE utf8_vietnamese_ci NOT NULL,
  `expires` datetime(6) NOT NULL,
  PRIMARY KEY (`cache_key`),
  KEY `my_cache_table_expires` (`expires`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_vietnamese_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `my_cache_table`
--

LOCK TABLES `my_cache_table` WRITE;
/*!40000 ALTER TABLE `my_cache_table` DISABLE KEYS */;
INSERT INTO `my_cache_table` VALUES (':1:no_r_ancem_count','gARLAi4=','2018-11-08 11:14:11.000000'),(':1:no_r_mesg_count','gARLAC4=','2018-11-08 11:14:11.000000'),(':1:teachers','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','2018-11-09 21:36:44.000000'),(':1:theses','gASV5xYAAAAAAACMFmRqYW5nby5kYi5tb2RlbHMucXVlcnmUjAhRdWVyeVNldJSTlCmBlH2UKIwFbW9kZWyUjA10aGVzaXMubW9kZWxzlIwGVGhlc2lzlJOUjANfZGKUTowGX2hpbnRzlH2UjAVxdWVyeZSMGmRqYW5nby5kYi5tb2RlbHMuc3FsLnF1ZXJ5lIwFUXVlcnmUk5QpgZR9lChoBWgIjA5hbGlhc19yZWZjb3VudJR9lCiMDXRoZXNpc190aGVzaXOUSwKMCnVzZXJzX3VzZXKUSwGMD3RlYWNoZXJfdGVhY2hlcpRLAYwMdGVhY2hlcl9pbmZvlEsBdYwJYWxpYXNfbWFwlIwLY29sbGVjdGlvbnOUjAtPcmRlcmVkRGljdJSTlClSlChoFIwjZGphbmdvLmRiLm1vZGVscy5zcWwuZGF0YXN0cnVjdHVyZXOUjAlCYXNlVGFibGWUk5QpgZR9lCiMCnRhYmxlX25hbWWUaBSMC3RhYmxlX2FsaWFzlGgUdWJoFWgdjARKb2lulJOUKYGUfZQoaCJoFYwMcGFyZW50X2FsaWFzlGgUaCNoFYwJam9pbl90eXBllIwKSU5ORVIgSk9JTpSMCWpvaW5fY29sc5SMDHB1Ymxpc2hlcl9pZJSMAmlklIaUhZSMCmpvaW5fZmllbGSUjBdkamFuZ28uZGIubW9kZWxzLmZpZWxkc5SMC19sb2FkX2ZpZWxklJOUjAZ0aGVzaXOUaAeMCXB1Ymxpc2hlcpSHlFKUjAhudWxsYWJsZZSJjBFmaWx0ZXJlZF9yZWxhdGlvbpROdWJoFmglKYGUfZQoaCJoFmgoaBVoI2gWaCloKmgraC2MB3VzZXJfaWSUhpSFlGgwjCdkamFuZ28uZGIubW9kZWxzLmZpZWxkcy5yZXZlcnNlX3JlbGF0ZWSUjAtPbmVUb09uZVJlbJSTlCmBlH2UKIwFZmllbGSUaDOMB3RlYWNoZXKUjAdUZWFjaGVylIwEdXNlcpSHlFKUaAWMDHVzZXJzLm1vZGVsc5SMBFVzZXKUk5SMDHJlbGF0ZWRfbmFtZZROjBJyZWxhdGVkX3F1ZXJ5X25hbWWUTowQbGltaXRfY2hvaWNlc190b5R9lIwLcGFyZW50X2xpbmuUiYwJb25fZGVsZXRllIwZZGphbmdvLmRiLm1vZGVscy5kZWxldGlvbpSMB0NBU0NBREWUk5SMC3N5bW1ldHJpY2FslImMCG11bHRpcGxllImMCmZpZWxkX25hbWWUaC2MBmhpZGRlbpSJjARuYW1llIwHdGVhY2hlcpR1Ymg4iGg5TnViaBdoJSmBlH2UKGgiaBdoKGgWaCNoF2gpaCpoK4wSdGVhY2hlcmluZm9fcHRyX2lklIwGbnVtYmVylIaUhZRoMGgzaEVoRowPdGVhY2hlcmluZm9fcHRylIeUUpRoOIloOU51YnWMEGV4dGVybmFsX2FsaWFzZXOUj5SMCXRhYmxlX21hcJR9lChoFF2UaBRhaBVdlGgVYWgWXZRoFmFoF12UaBdhdYwMZGVmYXVsdF9jb2xzlIiMEGRlZmF1bHRfb3JkZXJpbmeUiIwRc3RhbmRhcmRfb3JkZXJpbmeUiIwMdXNlZF9hbGlhc2VzlI+UKGgXaBZoFWgUkIwQZmlsdGVyX2lzX3N0aWNreZSJjAhzdWJxdWVyeZSJjAZzZWxlY3SUKYwFd2hlcmWUjBpkamFuZ28uZGIubW9kZWxzLnNxbC53aGVyZZSMCVdoZXJlTm9kZZSTlCmBlH2UKIwIY2hpbGRyZW6UXZQojBhkamFuZ28uZGIubW9kZWxzLmxvb2t1cHOUjAVFeGFjdJSTlCmBlH2UKIwDbGhzlIwcZGphbmdvLmRiLm1vZGVscy5leHByZXNzaW9uc5SMA0NvbJSTlCmBlH2UKIwRX2NvbnN0cnVjdG9yX2FyZ3OUaBRoM2g0aAeMCmlzX2Nob2ljZWSUh5RSlIaUfZSGlIwMb3V0cHV0X2ZpZWxklGiLjAVhbGlhc5RoFIwGdGFyZ2V0lGiLjBJjb250YWluc19hZ2dyZWdhdGWUiXVijANyaHOUiYwUYmlsYXRlcmFsX3RyYW5zZm9ybXOUXZRokol1Ymh/KYGUfZQoaIJohSmBlH2UKGiIaBdoM4wKc2Nob29saW5mb5SMC1RlYWNoZXJJbmZvlIwHY29sbGVnZZSHlFKUhpR9lIaUaI9onmiQaBdokWieaJKJdWJok4wP6K6h566X5py65a2m6ZmilGiUXZRokol1YmWMCWNvbm5lY3RvcpSMA0FORJSMB25lZ2F0ZWSUiWiSiXVijAt3aGVyZV9jbGFzc5RoeIwIZ3JvdXBfYnmUTowIb3JkZXJfYnmUKYwIbG93X21hcmuUSwCMCWhpZ2hfbWFya5ROjAhkaXN0aW5jdJSJjA9kaXN0aW5jdF9maWVsZHOUKYwRc2VsZWN0X2Zvcl91cGRhdGWUiYwYc2VsZWN0X2Zvcl91cGRhdGVfbm93YWl0lImMHXNlbGVjdF9mb3JfdXBkYXRlX3NraXBfbG9ja2VklImMFHNlbGVjdF9mb3JfdXBkYXRlX29mlCmMDnNlbGVjdF9yZWxhdGVklImMCW1heF9kZXB0aJRLBYwNdmFsdWVzX3NlbGVjdJQpjAxfYW5ub3RhdGlvbnOUaBspUpSMFmFubm90YXRpb25fc2VsZWN0X21hc2uUTowYX2Fubm90YXRpb25fc2VsZWN0X2NhY2hllE6MCmNvbWJpbmF0b3KUTowOY29tYmluYXRvcl9hbGyUiYwQY29tYmluZWRfcXVlcmllc5QpjAZfZXh0cmGUTowRZXh0cmFfc2VsZWN0X21hc2uUTowTX2V4dHJhX3NlbGVjdF9jYWNoZZROjAxleHRyYV90YWJsZXOUKYwOZXh0cmFfb3JkZXJfYnmUKYwQZGVmZXJyZWRfbG9hZGluZ5QokZSIhpSME19maWx0ZXJlZF9yZWxhdGlvbnOUfZSMDWV4cGxhaW5fcXVlcnmUiYwOZXhwbGFpbl9mb3JtYXSUTowPZXhwbGFpbl9vcHRpb25zlH2UjA1fbG9va3VwX2pvaW5zlF2UKGgUaBVoFmgXZYwKYmFzZV90YWJsZZRoFHVijA1fcmVzdWx0X2NhY2hllF2UKIwVZGphbmdvLmRiLm1vZGVscy5iYXNllIwObW9kZWxfdW5waWNrbGWUk5RoNGgHhpSFlFKUfZQojAZfc3RhdGWUaM+MCk1vZGVsU3RhdGWUk5QpgZR9lCiMBmFkZGluZ5SJjAJkYpSMB2RlZmF1bHSUdWJoLUsmjAV0aXRsZZSMEumjnuacuuWkp+aImOa4uOaIj5SMB2NvbnRlbnSUjKo8cD7po57mnLrlpKfmiJjmuLjmiI88L3A+DQoNCjxwPumjnuacuuWkp+aImOa4uOaIjzwvcD4NCg0KPHA+6aOe5py65aSn5oiY5ri45oiPPC9wPg0KDQo8cD7po57mnLrlpKfmiJjmuLjmiI88L3A+DQoNCjxwPumjnuacuuWkp+aImOa4uOaIjzwvcD4NCg0KPHA+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gTwvc3Bhbj48L3A+DQoNCjxwPjxzcGFuIHN0eWxlPSJmb250LXNpemU6MjBweCI+cHl0aG9u54is6Jmr5piv6I635Y+W5aSn5pWw5o2u55qE5LiA5Liq6Z2e5bi46auY5pWI5bm25LiU5a6e55So55qE5oqA5pyv77yBPC9zcGFuPjwvcD4NCg0KPHA+PHNwYW4gc3R5bGU9ImZvbnQtc2l6ZToyMHB4Ij5weXRob27niKzomavmmK/ojrflj5blpKfmlbDmja7nmoTkuIDkuKrpnZ7luLjpq5jmlYjlubbkuJTlrp7nlKjnmoTmioDmnK/vvIE8L3NwYW4+PC9wPg0KDQo8cD48c3BhbiBzdHlsZT0iZm9udC1zaXplOjIwcHgiPnB5dGhvbueIrOiZq+aYr+iOt+WPluWkp+aVsOaNrueahOS4gOS4qumdnuW4uOmrmOaViOW5tuS4lOWunueUqOeahOaKgOacr++8gTwvc3Bhbj48L3A+DQoNCjxwPjxzcGFuIHN0eWxlPSJmb250LXNpemU6MjBweCI+cHl0aG9u54is6Jmr5piv6I635Y+W5aSn5pWw5o2u55qE5LiA5Liq6Z2e5bi46auY5pWI5bm25LiU5a6e55So55qE5oqA5pyv77yBPC9zcGFuPjwvcD4NCg0KPHA+PHNwYW4gc3R5bGU9ImZvbnQtc2l6ZToyMHB4Ij5weXRob27niKzomavmmK/ojrflj5blpKfmlbDmja7nmoTkuIDkuKrpnZ7luLjpq5jmlYjlubbkuJTlrp7nlKjnmoTmioDmnK/vvIE8L3NwYW4+PC9wPg0KDQo8cD48c3BhbiBzdHlsZT0iZm9udC1zaXplOjIwcHgiPnB5dGhvbueIrOiZq+aYr+iOt+WPluWkp+aVsOaNrueahOS4gOS4qumdnuW4uOmrmOaViOW5tuS4lOWunueUqOeahOaKgOacr++8gTwvc3Bhbj48L3A+DQoNCjxwPjxzcGFuIHN0eWxlPSJmb250LXNpemU6MjBweCI+cHl0aG9u54is6Jmr5piv6I635Y+W5aSn5pWw5o2u55qE5LiA5Liq6Z2e5bi46auY5pWI5bm25LiU5a6e55So55qE5oqA5pyv77yBPC9zcGFuPjwvcD4NCg0KPHA+Jm5ic3A7PC9wPpRo4mjlQwQH4goTlIWUUpRoLEsRaImJaOmJaOqMBTIuMS4ylHViaNFoNGgHhpSFlFKUfZQoaNZo2CmBlH2UKGjbiWjcaN11YmgtSwho3owS572R5LiK6LSt54mp57O757uflGjgjLU8b2w+DQoJPGxpPuWunueOsOeUqOaIt+eZu+W9leOAgjwvbGk+DQoJPGxpPuWunueOsOeUqOaIt+i0reS5sDwvbGk+DQoJPGxpPuWunueOsOaJgOacieWVhuWTgeeahOS6pOaYkzwvbGk+DQoJPGxpPuWunueOsOeUqOaIt+S4iuS8oOWbvueJhzwvbGk+DQoJPGxpPuS9v+eUqG15c3Fs5pWw5o2u5bqTPC9saT4NCjwvb2w+lGjiaOVDBAfiChKUhZRSlGgsSxJoiYlo6Ylo6owFMi4xLjKUdWJljA5fc3RpY2t5X2ZpbHRlcpSJjApfZm9yX3dyaXRllImMGV9wcmVmZXRjaF9yZWxhdGVkX2xvb2t1cHOUKYwOX3ByZWZldGNoX2RvbmWUiYwWX2tub3duX3JlbGF0ZWRfb2JqZWN0c5R9lIwPX2l0ZXJhYmxlX2NsYXNzlGgAjA1Nb2RlbEl0ZXJhYmxllJOUjAdfZmllbGRzlE5o6owFMi4xLjKUdWIu','2018-11-09 21:28:46.000000');
/*!40000 ALTER TABLE `my_cache_table` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `student_collection`
--

DROP TABLE IF EXISTS `student_collection`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `student_collection` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `object_id` int(10) unsigned NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `student_id` varchar(20) COLLATE utf8_vietnamese_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `student_collection_student_id_object_id_con_04515db5_uniq` (`student_id`,`object_id`,`content_type_id`),
  KEY `student_collection_content_type_id_c91b3155_fk_django_co` (`content_type_id`),
  CONSTRAINT `student_collection_content_type_id_c91b3155_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `student_collection_student_id_6a8d3bac_fk_student_s` FOREIGN KEY (`student_id`) REFERENCES `student_student` (`studentinfo_ptr_id`)
) ENGINE=InnoDB AUTO_INCREMENT=65 DEFAULT CHARSET=utf8 COLLATE=utf8_vietnamese_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `student_collection`
--

LOCK TABLES `student_collection` WRITE;
/*!40000 ALTER TABLE `student_collection` DISABLE KEYS */;
INSERT INTO `student_collection` VALUES (46,30,12,'201506401222'),(49,35,12,'201506401222'),(53,36,12,'201506401222'),(54,37,12,'201506401222'),(55,123456781,10,'201506401222'),(56,123456782,10,'201506401222'),(58,123456783,10,'201506401222'),(48,123456789,10,'201506401222');
/*!40000 ALTER TABLE `student_collection` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `student_info`
--

DROP TABLE IF EXISTS `student_info`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `student_info` (
  `number` varchar(20) COLLATE utf8_vietnamese_ci NOT NULL,
  `name` varchar(10) COLLATE utf8_vietnamese_ci NOT NULL,
  `class_name` varchar(20) COLLATE utf8_vietnamese_ci NOT NULL,
  `college` varchar(30) COLLATE utf8_vietnamese_ci NOT NULL,
  `score` int(11) DEFAULT NULL,
  PRIMARY KEY (`number`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_vietnamese_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `student_info`
--

LOCK TABLES `student_info` WRITE;
/*!40000 ALTER TABLE `student_info` DISABLE KEYS */;
INSERT INTO `student_info` VALUES ('201506401101','黄师','物理152班','物理学院',NULL),('201506401102','林飞','物理152班','物理学院',NULL),('201506401103','柳絮','物理152班','物理学院',NULL),('201506401150','杨欣','商151班','商学院',NULL),('201506401151','廖云芸','商152班','商学院',NULL),('201506401222','张俊桔','计算机152','计算机学院',NULL),('201506401225','梁勋','计算机152班','计算机学院',NULL),('201506401226','何大桂','计算机152','计算机学院',NULL),('201506401227','蓝浩','计算机152','计算机学院',NULL);
/*!40000 ALTER TABLE `student_info` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `student_student`
--

DROP TABLE IF EXISTS `student_student`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `student_student` (
  `studentinfo_ptr_id` varchar(20) COLLATE utf8_vietnamese_ci NOT NULL,
  `introduction` longtext COLLATE utf8_vietnamese_ci,
  `phonenumber` varchar(11) COLLATE utf8_vietnamese_ci DEFAULT NULL,
  `email` varchar(30) COLLATE utf8_vietnamese_ci DEFAULT NULL,
  `is_choiced_thesis` tinyint(1) NOT NULL,
  `teacher_id` varchar(20) COLLATE utf8_vietnamese_ci DEFAULT NULL,
  `thesis_id` int(11) DEFAULT NULL,
  `user_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`studentinfo_ptr_id`),
  UNIQUE KEY `thesis_id` (`thesis_id`),
  UNIQUE KEY `user_id` (`user_id`),
  KEY `student_student_teacher_id_eb50cce2_fk_teacher_t` (`teacher_id`),
  CONSTRAINT `student_student_studentinfo_ptr_id_0ae6a678_fk_student_i` FOREIGN KEY (`studentinfo_ptr_id`) REFERENCES `student_info` (`number`),
  CONSTRAINT `student_student_teacher_id_eb50cce2_fk_teacher_t` FOREIGN KEY (`teacher_id`) REFERENCES `teacher_teacher` (`teacherinfo_ptr_id`),
  CONSTRAINT `student_student_thesis_id_0d69534e_fk_thesis_thesis_id` FOREIGN KEY (`thesis_id`) REFERENCES `thesis_thesis` (`id`),
  CONSTRAINT `student_student_user_id_4f4b35ef_fk_users_user_id` FOREIGN KEY (`user_id`) REFERENCES `users_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_vietnamese_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `student_student`
--

LOCK TABLES `student_student` WRITE;
/*!40000 ALTER TABLE `student_student` DISABLE KEYS */;
INSERT INTO `student_student` VALUES ('201506401101',NULL,'','',0,NULL,NULL,8),('201506401102',NULL,'','',0,NULL,NULL,9),('201506401103',NULL,'','',0,NULL,NULL,10),('201506401150',NULL,'','',0,NULL,NULL,11),('201506401151',NULL,'','',0,NULL,NULL,12),('201506401222','','18877543740','871162592@qq.com',0,'123456781',NULL,13),('201506401225','我很懒，什么都不想说','18877543740','871162592@qq.com',1,'123456789',28,14),('201506401226','','18877543740','871162592@qq.com',1,'123456789',31,15),('201506401227',NULL,'18877543740','871162592@qq.com',0,NULL,NULL,16);
/*!40000 ALTER TABLE `student_student` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `student_student_read_announcement`
--

DROP TABLE IF EXISTS `student_student_read_announcement`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `student_student_read_announcement` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `student_id` varchar(20) COLLATE utf8_vietnamese_ci NOT NULL,
  `announcement_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `student_student_read_ann_student_id_announcement__e0cb31d2_uniq` (`student_id`,`announcement_id`),
  KEY `student_student_read_announcement_id_9f39c0a1_fk_announcem` (`announcement_id`),
  CONSTRAINT `student_student_read_announcement_id_9f39c0a1_fk_announcem` FOREIGN KEY (`announcement_id`) REFERENCES `announcement_announcement` (`id`),
  CONSTRAINT `student_student_read_student_id_06762324_fk_student_s` FOREIGN KEY (`student_id`) REFERENCES `student_student` (`studentinfo_ptr_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8 COLLATE=utf8_vietnamese_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `student_student_read_announcement`
--

LOCK TABLES `student_student_read_announcement` WRITE;
/*!40000 ALTER TABLE `student_student_read_announcement` DISABLE KEYS */;
/*!40000 ALTER TABLE `student_student_read_announcement` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `teacher_info`
--

DROP TABLE IF EXISTS `teacher_info`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `teacher_info` (
  `number` varchar(20) COLLATE utf8_vietnamese_ci NOT NULL,
  `name` varchar(20) COLLATE utf8_vietnamese_ci NOT NULL,
  `college` varchar(30) COLLATE utf8_vietnamese_ci NOT NULL,
  `job_title` varchar(10) COLLATE utf8_vietnamese_ci NOT NULL,
  PRIMARY KEY (`number`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_vietnamese_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `teacher_info`
--

LOCK TABLES `teacher_info` WRITE;
/*!40000 ALTER TABLE `teacher_info` DISABLE KEYS */;
INSERT INTO `teacher_info` VALUES ('123456781','钟盛','计算机学院','教授'),('123456782','柳花明','计算机学院','副教授'),('123456783','王晴','计算机学院','副教授'),('123456789','刘胜才','计算机学院','教授'),('456789123','黎簇','计算机学院','副教授'),('789456123','孔维洺','商学院','副教授'),('987654321','王如月','物理学院','教授');
/*!40000 ALTER TABLE `teacher_info` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `teacher_teacher`
--

DROP TABLE IF EXISTS `teacher_teacher`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `teacher_teacher` (
  `teacherinfo_ptr_id` varchar(20) COLLATE utf8_vietnamese_ci NOT NULL,
  `introduction` longtext COLLATE utf8_vietnamese_ci,
  `phonenumber` varchar(11) COLLATE utf8_vietnamese_ci DEFAULT NULL,
  `email` varchar(30) COLLATE utf8_vietnamese_ci DEFAULT NULL,
  `max_number` int(10) unsigned NOT NULL,
  `user_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`teacherinfo_ptr_id`),
  UNIQUE KEY `user_id` (`user_id`),
  CONSTRAINT `teacher_teacher_teacherinfo_ptr_id_8a06306a_fk_teacher_i` FOREIGN KEY (`teacherinfo_ptr_id`) REFERENCES `teacher_info` (`number`),
  CONSTRAINT `teacher_teacher_user_id_85660d45_fk_users_user_id` FOREIGN KEY (`user_id`) REFERENCES `users_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_vietnamese_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `teacher_teacher`
--

LOCK TABLES `teacher_teacher` WRITE;
/*!40000 ALTER TABLE `teacher_teacher` DISABLE KEYS */;
INSERT INTO `teacher_teacher` VALUES ('123456781','','18877543740',NULL,6,31),('123456782',NULL,NULL,NULL,0,32),('123456783',NULL,NULL,NULL,0,33),('123456789','python 数据挖掘 数据分析','18877543740','',5,17),('456789123','','18877543740',NULL,2,18),('789456123',NULL,'','',0,19),('987654321','物理科学，研究，物理学！','18877543740',NULL,5,20);
/*!40000 ALTER TABLE `teacher_teacher` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `teacher_teacher_read_announcement`
--

DROP TABLE IF EXISTS `teacher_teacher_read_announcement`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `teacher_teacher_read_announcement` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `teacher_id` varchar(20) COLLATE utf8_vietnamese_ci NOT NULL,
  `announcement_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `teacher_teacher_read_ann_teacher_id_announcement__a7fca003_uniq` (`teacher_id`,`announcement_id`),
  KEY `teacher_teacher_read_announcement_id_db843193_fk_announcem` (`announcement_id`),
  CONSTRAINT `teacher_teacher_read_announcement_id_db843193_fk_announcem` FOREIGN KEY (`announcement_id`) REFERENCES `announcement_announcement` (`id`),
  CONSTRAINT `teacher_teacher_read_teacher_id_3ba2e3f5_fk_teacher_t` FOREIGN KEY (`teacher_id`) REFERENCES `teacher_teacher` (`teacherinfo_ptr_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_vietnamese_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `teacher_teacher_read_announcement`
--

LOCK TABLES `teacher_teacher_read_announcement` WRITE;
/*!40000 ALTER TABLE `teacher_teacher_read_announcement` DISABLE KEYS */;
/*!40000 ALTER TABLE `teacher_teacher_read_announcement` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `thesis_tag`
--

DROP TABLE IF EXISTS `thesis_tag`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `thesis_tag` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) COLLATE utf8_vietnamese_ci NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=26 DEFAULT CHARSET=utf8 COLLATE=utf8_vietnamese_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `thesis_tag`
--

LOCK TABLES `thesis_tag` WRITE;
/*!40000 ALTER TABLE `thesis_tag` DISABLE KEYS */;
INSERT INTO `thesis_tag` VALUES (15,'物理学'),(16,'天文学'),(17,'力学'),(18,'大数据'),(19,'python'),(20,'java'),(21,'cms'),(22,'游戏'),(23,'web'),(24,'管理系统');
/*!40000 ALTER TABLE `thesis_tag` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `thesis_thesis`
--

DROP TABLE IF EXISTS `thesis_thesis`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `thesis_thesis` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(255) COLLATE utf8_vietnamese_ci NOT NULL,
  `content` longtext COLLATE utf8_vietnamese_ci NOT NULL,
  `pub_date` date NOT NULL,
  `is_choiced` tinyint(1) NOT NULL,
  `publisher_id` int(11) NOT NULL,
  `need_verify` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `thesis_thesis_title_publisher_id_0f1a39a3_uniq` (`title`,`publisher_id`),
  KEY `thesis_thesis_publisher_id_8ff16cd8_fk_users_user_id` (`publisher_id`),
  CONSTRAINT `thesis_thesis_publisher_id_8ff16cd8_fk_users_user_id` FOREIGN KEY (`publisher_id`) REFERENCES `users_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=80 DEFAULT CHARSET=utf8 COLLATE=utf8_vietnamese_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `thesis_thesis`
--

LOCK TABLES `thesis_thesis` WRITE;
/*!40000 ALTER TABLE `thesis_thesis` DISABLE KEYS */;
INSERT INTO `thesis_thesis` VALUES (8,'网上购物系统','<ol>\r\n	<li>实现用户登录。</li>\r\n	<li>实现用户购买</li>\r\n	<li>实现所有商品的交易</li>\r\n	<li>实现用户上传图片</li>\r\n	<li>使用mysql数据库</li>\r\n</ol>','2018-10-18',0,18,0),(24,'宇宙的奥秘','<h1>宇宙的奥秘</h1>\r\n\r\n<ol>\r\n	<li>宇宙的起源</li>\r\n	<li>宇宙的发展</li>\r\n	<li>宇宙的组成</li>\r\n	<li>你知我也知</li>\r\n	<li>按要求完成</li>\r\n	<li><span style=\"color:#c0392b\">如果未按时完成，完蛋咯！</span></li>\r\n</ol>','2018-10-19',0,20,0),(25,'牛顿第三定律的研究','<h1>牛顿第三定律的研究</h1>\r\n\r\n<ol>\r\n	<li>牛顿第三定律的研究</li>\r\n	<li>牛顿第三定律的研究</li>\r\n	<li>牛顿第三定律的研究</li>\r\n	<li>牛顿第三定律的研究</li>\r\n	<li>牛顿第三定律的研究</li>\r\n	<li>牛顿第三定律的研究</li>\r\n	<li>牛顿第三定律的研究</li>\r\n	<li>牛顿第三定律的研究</li>\r\n	<li>牛顿第三定律的研究</li>\r\n</ol>','2018-10-19',0,20,0),(27,'牛顿第三定律的研究2','<h1>牛顿第三定律的研究</h1>\r\n\r\n<ol>\r\n	<li>牛顿第三定律的研究</li>\r\n	<li>牛顿第三定律的研究</li>\r\n	<li>牛顿第三定律的研究</li>\r\n	<li>牛顿第三定律的研究</li>\r\n	<li>牛顿第三定律的研究</li>\r\n	<li>牛顿第三定律的研究</li>\r\n	<li>牛顿第三定律的研究</li>\r\n	<li>牛顿第三定律的研究</li>\r\n	<li>牛顿第三定律的研究</li>\r\n</ol>','2018-10-19',0,20,0),(28,'大数据分析','<h1>大数据挖掘与分析</h1>\r\n\r\n<p><span style=\"font-size:22px\">大数据是一个非常有用的东西。是未来时代发展的必争之地。</span></p>','2018-10-19',1,17,0),(30,'python爬虫开发实战','<h1>python爬虫开发实战</h1>\r\n\r\n<p><span style=\"font-size:20px\">python爬虫是获取大数据的一个非常高效并且实用的技术！</span></p>\r\n\r\n<p><span style=\"font-size:20px\">python爬虫是获取大数据的一个非常高效并且实用的技术！</span></p>\r\n\r\n<p><span style=\"font-size:20px\">python爬虫是获取大数据的一个非常高效并且实用的技术！</span></p>\r\n\r\n<p><span style=\"font-size:20px\">python爬虫是获取大数据的一个非常高效并且实用的技术！</span></p>\r\n\r\n<p><span style=\"font-size:20px\">python爬虫是获取大数据的一个非常高效并且实用的技术！</span></p>\r\n\r\n<p><span style=\"font-size:20px\">python爬虫是获取大数据的一个非常高效并且实用的技术！</span></p>\r\n\r\n<p><span style=\"font-size:20px\">python爬虫是获取大数据的一个非常高效并且实用的技术！</span></p>\r\n\r\n<p><span style=\"font-size:20px\">python爬虫是获取大数据的一个非常高效并且实用的技术！</span></p>\r\n\r\n<p>&nbsp;</p>','2018-10-19',0,17,0),(31,'网上购物系统','<h1>网上购物系统</h1>\r\n\r\n<ol>\r\n	<li><span style=\"font-size:26px\">网上购物系统</span></li>\r\n	<li><span style=\"font-size:26px\">网上购物系统</span></li>\r\n	<li><span style=\"font-size:26px\">网上购物系统</span></li>\r\n	<li><span style=\"font-size:26px\">网上购物系统</span></li>\r\n</ol>\r\n\r\n<p>&nbsp;</p>\r\n\r\n<p>&nbsp;</p>','2018-10-21',1,17,0),(35,'大数据挖掘','<h1>大数据挖掘</h1>\r\n\r\n<ol>\r\n	<li>\r\n	<h3>大数据挖掘</h3>\r\n	</li>\r\n	<li>大数据挖掘</li>\r\n	<li>大数据挖掘</li>\r\n	<li>大数据挖掘</li>\r\n	<li>大数据挖掘</li>\r\n	<li>大数据挖掘</li>\r\n</ol>','2018-11-03',0,17,0),(36,'基于web的车辆管理系统','<h1>基于web的车辆管理系统</h1>\r\n\r\n<h3>基于web的车辆管理系统</h3>\r\n\r\n<p>基于web的车辆管理系统基于web的车辆管理系统</p>\r\n\r\n<p>基于web的车辆管理系统基于web的车辆管理系统基于web的车辆管理系统</p>\r\n\r\n<p>基于web的车辆管理系统</p>\r\n\r\n<p>基于web的车辆管理系统基于web的车辆管理系统</p>\r\n\r\n<p>基于web的车辆管理系统基于web的车辆管理系统</p>','2018-11-03',1,31,0),(37,'人才招聘网站的设计与实现','<h1>人才招聘网站的设计与实现</h1>\r\n\r\n<h2>人才招聘网站的设计与实现</h2>\r\n\r\n<h2>人才招聘网站的设计与实现</h2>\r\n\r\n<p><span style=\"font-size:22px\">人才招聘网站的设计与实现</span></p>\r\n\r\n<p><span style=\"font-size:22px\">人才招聘网站的设计与实现</span></p>\r\n\r\n<p><span style=\"font-size:22px\">人才招聘网站的设计与实现人才招聘网站的设计与实现</span></p>\r\n\r\n<p><span style=\"font-size:22px\">人才招聘网站的设计与实现</span></p>\r\n\r\n<p><span style=\"font-size:22px\">人才招聘网站的设计与实现</span></p>','2018-11-03',0,31,0),(38,'飞机大战游戏','<p>飞机大战游戏</p>\r\n\r\n<p>飞机大战游戏</p>\r\n\r\n<p>飞机大战游戏</p>\r\n\r\n<p>飞机大战游戏</p>\r\n\r\n<p>飞机大战游戏</p>\r\n\r\n<p>飞机大战游戏</p>','2018-11-04',0,31,0),(40,'飞机大战游戏2','<p>飞机大战游戏</p>\r\n\r\n<p>飞机大战游戏</p>\r\n\r\n<p>飞机大战游戏</p>','2018-11-04',0,31,0),(41,'飞机大战游戏3','<h1>飞机大战游戏</h1>\r\n\r\n<p>飞机大战游戏</p>\r\n\r\n<p>飞机大战游戏</p>\r\n\r\n<p>飞机大战游戏</p>\r\n\r\n<p>飞机大战游戏</p>','2018-11-04',0,31,0);
/*!40000 ALTER TABLE `thesis_thesis` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `thesis_thesis_tags`
--

DROP TABLE IF EXISTS `thesis_thesis_tags`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `thesis_thesis_tags` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `thesis_id` int(11) NOT NULL,
  `tag_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `thesis_thesis_tags_thesis_id_tag_id_2f4e705f_uniq` (`thesis_id`,`tag_id`),
  KEY `thesis_thesis_tags_tag_id_50f63f60_fk_thesis_tag_id` (`tag_id`),
  CONSTRAINT `thesis_thesis_tags_tag_id_50f63f60_fk_thesis_tag_id` FOREIGN KEY (`tag_id`) REFERENCES `thesis_tag` (`id`),
  CONSTRAINT `thesis_thesis_tags_thesis_id_c3045dd8_fk_thesis_thesis_id` FOREIGN KEY (`thesis_id`) REFERENCES `thesis_thesis` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=40 DEFAULT CHARSET=utf8 COLLATE=utf8_vietnamese_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `thesis_thesis_tags`
--

LOCK TABLES `thesis_thesis_tags` WRITE;
/*!40000 ALTER TABLE `thesis_thesis_tags` DISABLE KEYS */;
INSERT INTO `thesis_thesis_tags` VALUES (14,8,23),(1,24,16),(9,25,15),(10,27,15),(3,28,18),(5,30,19),(6,31,19),(7,31,20),(8,31,21),(20,35,18),(21,36,23),(22,36,24),(23,37,23),(24,38,22),(25,40,22),(26,41,22);
/*!40000 ALTER TABLE `thesis_thesis_tags` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users_user`
--

DROP TABLE IF EXISTS `users_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `users_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) COLLATE utf8_vietnamese_ci NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) COLLATE utf8_vietnamese_ci NOT NULL,
  `first_name` varchar(30) COLLATE utf8_vietnamese_ci NOT NULL,
  `last_name` varchar(150) COLLATE utf8_vietnamese_ci NOT NULL,
  `email` varchar(254) COLLATE utf8_vietnamese_ci NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  `person` varchar(10) COLLATE utf8_vietnamese_ci DEFAULT NULL,
  `no_r_ann_count` int(10) unsigned NOT NULL,
  `no_r_message_count` int(10) unsigned NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=34 DEFAULT CHARSET=utf8 COLLATE=utf8_vietnamese_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users_user`
--

LOCK TABLES `users_user` WRITE;
/*!40000 ALTER TABLE `users_user` DISABLE KEYS */;
INSERT INTO `users_user` VALUES (1,'pbkdf2_sha256$120000$2cYZBQaks6ug$LuyvhyqHifxr3/UtsWx8NWIfQaSAUuRHF1IFEoiw8Ac=','2018-11-09 20:49:57.566246',1,'zjj','','','',1,1,'2018-10-15 15:40:58.272388',NULL,0,0),(8,'pbkdf2_sha256$120000$BpMFq7UQwj8P$I3qjsKxUKbpUWuB+CJ2W79a5KhA5cEWyDW2yLL5Yo98=',NULL,0,'201506401101','','','',0,1,'2018-10-17 15:17:29.104653','student',0,0),(9,'pbkdf2_sha256$120000$3a5OvXFEcEr6$x3PNTAqtZUNcS84Jof7n4uIWyIgqQOK1RTIJtzzKt4U=',NULL,0,'201506401102','','','',0,1,'2018-10-17 15:17:29.570967','student',0,0),(10,'pbkdf2_sha256$120000$5L239gc69mxj$9/nU4nMqXkW3c4gWQWCI5yCEJjxWDggEz7gu7mrJ62o=',NULL,0,'201506401103','','','',0,1,'2018-10-17 15:17:30.140368','student',0,0),(11,'pbkdf2_sha256$120000$X6a7PiROHIi4$K+9eSJJcs9gsWZ6cOu4dL8vzSXLCUPqKZdc/rUxY2Ic=',NULL,0,'201506401150','','','',0,1,'2018-10-17 15:17:30.481609','student',0,0),(12,'pbkdf2_sha256$120000$ypBxTA6vrOe5$pYar81aHYAxLbxsNWTdfBybV5WmxpcitgSrf+F6jlg0=',NULL,0,'201506401151','','','',0,1,'2018-10-17 15:17:30.846868','student',0,0),(13,'pbkdf2_sha256$120000$4tcfQ7I5Ox5i$qTzJaQ2Q7zRukcVJa1GA5uHPBjDboNWrjqQzOksBKeU=','2018-11-09 20:41:20.312035',0,'201506401222','','','',0,1,'2018-10-17 15:17:31.171115','student',2,0),(14,'pbkdf2_sha256$120000$mXn65ymzxWb1$FliSab6sLoCUkSyCFKeoJNhr3ZmKtaI5HCt509DpHus=','2018-11-06 12:57:53.629520',0,'201506401225','','','',0,1,'2018-10-17 15:17:31.459319','student',0,0),(15,'pbkdf2_sha256$120000$CF9IywzXtHEq$boApIn+VU/cHveReoH1bumQgKVC3lluIEmQQR9Hm95o=','2018-11-06 12:36:41.929618',0,'201506401226','','','',0,1,'2018-10-17 15:17:31.748506','student',0,0),(16,'pbkdf2_sha256$120000$e5j4SrbsVShy$4QkPW6zuthXy32Pv1M1o+/9HbJfZLuZieccXO7V5CEM=','2018-10-25 08:50:23.942915',0,'201506401227','','','',0,1,'2018-10-17 15:17:32.058725','student',0,0),(17,'pbkdf2_sha256$120000$uBZZZIqQZQ2i$8vnToeFfV/Jviv7I3f6h3xO77tCE8mOxW7pt9lgJZdI=','2018-11-09 13:23:54.268309',0,'123456789','','','',0,1,'2018-10-17 15:20:24.261467','teacher',0,0),(18,'pbkdf2_sha256$120000$47mjzyfhLWxE$fKhPwb0ZvbU1y6F1OIx6uCEPqPNHx0xpInM0wxfUxvg=','2018-11-03 15:09:52.052186',0,'456789123','','','',0,1,'2018-10-17 15:20:24.680764','teacher',0,0),(19,'pbkdf2_sha256$120000$ZEO5KuEiy5eo$PSxOV/kUP3N735trua//WrK/9ZYpVb1FHIewfg0NM74=',NULL,0,'789456123','','','',0,1,'2018-10-17 15:20:25.028007','teacher',0,0),(20,'pbkdf2_sha256$120000$b122dJJRzPnB$EMp0EstDQdoaToHFvFQGbErWaWs1ry/4SSru3JsbuO8=','2018-10-24 01:25:37.481415',0,'987654321','','','',0,1,'2018-10-17 15:20:25.407275','teacher',0,0),(31,'pbkdf2_sha256$120000$MooEzSmtAS9H$yTfL9xAXDog256JQbQq9tXrleGq2F5bh95k0gwQuwnY=','2018-11-09 09:31:45.892211',0,'123456781','','','',0,1,'2018-11-03 13:26:56.413203','teacher',0,0),(32,'pbkdf2_sha256$120000$9Pd45f6mCQgF$UZwWxRx/JEaYqXEmlxDX4ZAJZT08EFAKlPpFtycya8E=',NULL,0,'123456782','','','',0,1,'2018-11-03 13:26:56.729425','teacher',0,0),(33,'pbkdf2_sha256$120000$ygxoMQhv80ps$vH1dcOEwsF/TF6YKR3ajhaPV73VE96Z+VhGjQqXcUB0=',NULL,0,'123456783','','','',0,1,'2018-11-03 13:26:56.974599','teacher',0,0);
/*!40000 ALTER TABLE `users_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users_user_groups`
--

DROP TABLE IF EXISTS `users_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `users_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `users_user_groups_user_id_group_id_b88eab82_uniq` (`user_id`,`group_id`),
  KEY `users_user_groups_group_id_9afc8d0e_fk_auth_group_id` (`group_id`),
  CONSTRAINT `users_user_groups_group_id_9afc8d0e_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `users_user_groups_user_id_5f6f5a90_fk_users_user_id` FOREIGN KEY (`user_id`) REFERENCES `users_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_vietnamese_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users_user_groups`
--

LOCK TABLES `users_user_groups` WRITE;
/*!40000 ALTER TABLE `users_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `users_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users_user_user_permissions`
--

DROP TABLE IF EXISTS `users_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `users_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `users_user_user_permissions_user_id_permission_id_43338c45_uniq` (`user_id`,`permission_id`),
  KEY `users_user_user_perm_permission_id_0b93982e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `users_user_user_perm_permission_id_0b93982e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `users_user_user_permissions_user_id_20aca447_fk_users_user_id` FOREIGN KEY (`user_id`) REFERENCES `users_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_vietnamese_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users_user_user_permissions`
--

LOCK TABLES `users_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `users_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `users_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `xadmin_bookmark`
--

DROP TABLE IF EXISTS `xadmin_bookmark`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `xadmin_bookmark` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(128) COLLATE utf8_vietnamese_ci NOT NULL,
  `url_name` varchar(64) COLLATE utf8_vietnamese_ci NOT NULL,
  `query` varchar(1000) COLLATE utf8_vietnamese_ci NOT NULL,
  `is_share` tinyint(1) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `user_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `xadmin_bookmark_content_type_id_60941679_fk_django_co` (`content_type_id`),
  KEY `xadmin_bookmark_user_id_42d307fc_fk_users_user_id` (`user_id`),
  CONSTRAINT `xadmin_bookmark_content_type_id_60941679_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `xadmin_bookmark_user_id_42d307fc_fk_users_user_id` FOREIGN KEY (`user_id`) REFERENCES `users_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_vietnamese_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `xadmin_bookmark`
--

LOCK TABLES `xadmin_bookmark` WRITE;
/*!40000 ALTER TABLE `xadmin_bookmark` DISABLE KEYS */;
/*!40000 ALTER TABLE `xadmin_bookmark` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `xadmin_log`
--

DROP TABLE IF EXISTS `xadmin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `xadmin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `ip_addr` char(39) COLLATE utf8_vietnamese_ci DEFAULT NULL,
  `object_id` longtext COLLATE utf8_vietnamese_ci,
  `object_repr` varchar(200) COLLATE utf8_vietnamese_ci NOT NULL,
  `action_flag` varchar(32) COLLATE utf8_vietnamese_ci NOT NULL,
  `message` longtext COLLATE utf8_vietnamese_ci NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `xadmin_log_content_type_id_2a6cb852_fk_django_content_type_id` (`content_type_id`),
  KEY `xadmin_log_user_id_bb16a176_fk_users_user_id` (`user_id`),
  CONSTRAINT `xadmin_log_content_type_id_2a6cb852_fk_django_content_type_id` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `xadmin_log_user_id_bb16a176_fk_users_user_id` FOREIGN KEY (`user_id`) REFERENCES `users_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=35 DEFAULT CHARSET=utf8 COLLATE=utf8_vietnamese_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `xadmin_log`
--

LOCK TABLES `xadmin_log` WRITE;
/*!40000 ALTER TABLE `xadmin_log` DISABLE KEYS */;
INSERT INTO `xadmin_log` VALUES (1,'2018-10-31 10:38:43.245419','127.0.0.1',NULL,'','delete','批量删除 4 个 消息',NULL,1),(2,'2018-10-31 10:39:12.438083','127.0.0.1',NULL,'','delete','批量删除 6 个 消息',NULL,1),(3,'2018-10-31 16:58:41.718055','127.0.0.1',NULL,'','delete','批量删除 10 个 消息',NULL,1),(4,'2018-11-03 11:59:23.347394','127.0.0.1',NULL,'','delete','批量删除 12 个 消息',NULL,1),(5,'2018-11-04 11:12:16.344058','127.0.0.1','139','这是管理员的信息！','create','已添加。',13,1),(6,'2018-11-04 11:39:42.563943','127.0.0.1','140','这是管理员发的消息！','create','已添加。',13,1),(7,'2018-11-04 12:56:54.966526','127.0.0.1','3','<Announcement:zjj>','create','已添加。',22,1),(8,'2018-11-04 13:13:23.612863','127.0.0.1','4','<Announcement:zjj>','create','已添加。',22,1),(9,'2018-11-04 13:13:31.593512','127.0.0.1','5','<Announcement:zjj>','create','已添加。',22,1),(10,'2018-11-04 13:14:19.732617','127.0.0.1','6','<Announcement:zjj>','create','已添加。',22,1),(11,'2018-11-05 15:38:16.222044','127.0.0.1','42','二手交易网站','delete','',12,1),(12,'2018-11-05 16:00:46.636728','127.0.0.1',NULL,'','delete','批量删除 1 个 thesis',NULL,1),(13,'2018-11-05 16:45:45.860935','127.0.0.1',NULL,'','delete','批量删除 1 个 thesis',NULL,1),(14,'2018-11-05 17:18:11.429208','127.0.0.1',NULL,'','delete','批量删除 3 个 消息',NULL,1),(15,'2018-11-05 17:18:24.985811','127.0.0.1',NULL,'','delete','批量删除 7 个 消息',NULL,1),(16,'2018-11-05 17:19:08.631732','127.0.0.1',NULL,'','delete','批量删除 1 个 message',NULL,1),(17,'2018-11-05 21:33:02.472676','127.0.0.1',NULL,'','delete','批量删除 1 个 message',NULL,1),(18,'2018-11-06 10:01:48.975256','127.0.0.1',NULL,'','delete','批量删除 1 个 tag',NULL,1),(19,'2018-11-06 10:59:06.359385','127.0.0.1',NULL,'','delete','批量删除 1 个 thesis',NULL,1),(20,'2018-11-06 11:05:05.082514','127.0.0.1','41','飞机大战游戏3','change','没有字段被修改。',12,1),(21,'2018-11-06 11:05:36.544801','127.0.0.1','58','test','change','修改 content 和 tags',12,1),(22,'2018-11-06 11:05:43.738900','127.0.0.1',NULL,'','delete','批量删除 1 个 thesis',NULL,1),(24,'2018-11-06 11:07:33.219474','127.0.0.1','201506401222','张俊桔','change','修改 thesis 和 is_choiced_thesis',9,1),(25,'2018-11-06 11:07:45.689307','127.0.0.1','58','test','delete','',12,1),(26,'2018-11-06 12:52:06.893884','127.0.0.1',NULL,'','delete','批量删除 1 个 message',NULL,1),(27,'2018-11-06 13:08:42.976551','127.0.0.1',NULL,'','delete','批量删除 4 个 announcements',NULL,1),(28,'2018-11-06 13:21:22.749777','127.0.0.1','7','<Announcement:zjj>','create','已添加。',22,1),(29,'2018-11-06 16:36:54.511145','127.0.0.1','201506401222','张俊桔','change','修改 read_announcement',9,1),(30,'2018-11-06 22:36:55.465725','127.0.0.1','201506401222','张俊桔','change','修改 read_announcement',9,1),(31,'2018-11-06 22:37:50.938004','127.0.0.1','8','<Announcement:zjj>','create','已添加。',22,1),(32,'2018-11-08 16:39:28.932769','127.0.0.1','1','VerifyThesis object (1)','create','已添加。',24,1),(33,'2018-11-08 16:42:52.502951','127.0.0.1',NULL,'','delete','批量删除 1 个 thesis',NULL,1),(34,'2018-11-08 23:01:44.211244','127.0.0.1',NULL,'','delete','批量删除 1 个 用户小组件',NULL,1);
/*!40000 ALTER TABLE `xadmin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `xadmin_usersettings`
--

DROP TABLE IF EXISTS `xadmin_usersettings`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `xadmin_usersettings` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `key` varchar(256) COLLATE utf8_vietnamese_ci NOT NULL,
  `value` longtext COLLATE utf8_vietnamese_ci NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `xadmin_usersettings_user_id_edeabe4a_fk_users_user_id` (`user_id`),
  CONSTRAINT `xadmin_usersettings_user_id_edeabe4a_fk_users_user_id` FOREIGN KEY (`user_id`) REFERENCES `users_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8 COLLATE=utf8_vietnamese_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `xadmin_usersettings`
--

LOCK TABLES `xadmin_usersettings` WRITE;
/*!40000 ALTER TABLE `xadmin_usersettings` DISABLE KEYS */;
INSERT INTO `xadmin_usersettings` VALUES (1,'dashboard:home:pos','',1),(2,'site-theme','/static/xadmin/css/themes/bootstrap-xadmin.css',1),(3,'users_user_editform_portal',',,,,|',1),(4,'users_studentuser_editform_portal',',,,,|',1),(5,'users_teacheruser_editform_portal',',,,,,thesis_set-group|',1);
/*!40000 ALTER TABLE `xadmin_usersettings` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `xadmin_userwidget`
--

DROP TABLE IF EXISTS `xadmin_userwidget`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `xadmin_userwidget` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `page_id` varchar(256) COLLATE utf8_vietnamese_ci NOT NULL,
  `widget_type` varchar(50) COLLATE utf8_vietnamese_ci NOT NULL,
  `value` longtext COLLATE utf8_vietnamese_ci NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `xadmin_userwidget_user_id_c159233a_fk_users_user_id` (`user_id`),
  CONSTRAINT `xadmin_userwidget_user_id_c159233a_fk_users_user_id` FOREIGN KEY (`user_id`) REFERENCES `users_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8 COLLATE=utf8_vietnamese_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `xadmin_userwidget`
--

LOCK TABLES `xadmin_userwidget` WRITE;
/*!40000 ALTER TABLE `xadmin_userwidget` DISABLE KEYS */;
/*!40000 ALTER TABLE `xadmin_userwidget` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-11-09 22:47:38
