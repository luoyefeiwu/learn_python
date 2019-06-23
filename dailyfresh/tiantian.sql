/*
Navicat MySQL Data Transfer

Source Server         : localhost
Source Server Version : 80011
Source Host           : localhost:3306
Source Database       : tiantian

Target Server Type    : MYSQL
Target Server Version : 80011
File Encoding         : 65001

Date: 2019-06-24 00:23:38
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for auth_group
-- ----------------------------
DROP TABLE IF EXISTS `auth_group`;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of auth_group
-- ----------------------------

-- ----------------------------
-- Table structure for auth_group_permissions
-- ----------------------------
DROP TABLE IF EXISTS `auth_group_permissions`;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of auth_group_permissions
-- ----------------------------

-- ----------------------------
-- Table structure for auth_permission
-- ----------------------------
DROP TABLE IF EXISTS `auth_permission`;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=41 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of auth_permission
-- ----------------------------
INSERT INTO `auth_permission` VALUES ('1', 'Can add log entry', '1', 'add_logentry');
INSERT INTO `auth_permission` VALUES ('2', 'Can change log entry', '1', 'change_logentry');
INSERT INTO `auth_permission` VALUES ('3', 'Can delete log entry', '1', 'delete_logentry');
INSERT INTO `auth_permission` VALUES ('4', 'Can view log entry', '1', 'view_logentry');
INSERT INTO `auth_permission` VALUES ('5', 'Can add permission', '2', 'add_permission');
INSERT INTO `auth_permission` VALUES ('6', 'Can change permission', '2', 'change_permission');
INSERT INTO `auth_permission` VALUES ('7', 'Can delete permission', '2', 'delete_permission');
INSERT INTO `auth_permission` VALUES ('8', 'Can view permission', '2', 'view_permission');
INSERT INTO `auth_permission` VALUES ('9', 'Can add group', '3', 'add_group');
INSERT INTO `auth_permission` VALUES ('10', 'Can change group', '3', 'change_group');
INSERT INTO `auth_permission` VALUES ('11', 'Can delete group', '3', 'delete_group');
INSERT INTO `auth_permission` VALUES ('12', 'Can view group', '3', 'view_group');
INSERT INTO `auth_permission` VALUES ('13', 'Can add user', '4', 'add_user');
INSERT INTO `auth_permission` VALUES ('14', 'Can change user', '4', 'change_user');
INSERT INTO `auth_permission` VALUES ('15', 'Can delete user', '4', 'delete_user');
INSERT INTO `auth_permission` VALUES ('16', 'Can view user', '4', 'view_user');
INSERT INTO `auth_permission` VALUES ('17', 'Can add content type', '5', 'add_contenttype');
INSERT INTO `auth_permission` VALUES ('18', 'Can change content type', '5', 'change_contenttype');
INSERT INTO `auth_permission` VALUES ('19', 'Can delete content type', '5', 'delete_contenttype');
INSERT INTO `auth_permission` VALUES ('20', 'Can view content type', '5', 'view_contenttype');
INSERT INTO `auth_permission` VALUES ('21', 'Can add session', '6', 'add_session');
INSERT INTO `auth_permission` VALUES ('22', 'Can change session', '6', 'change_session');
INSERT INTO `auth_permission` VALUES ('23', 'Can delete session', '6', 'delete_session');
INSERT INTO `auth_permission` VALUES ('24', 'Can view session', '6', 'view_session');
INSERT INTO `auth_permission` VALUES ('25', 'Can add user info', '7', 'add_userinfo');
INSERT INTO `auth_permission` VALUES ('26', 'Can change user info', '7', 'change_userinfo');
INSERT INTO `auth_permission` VALUES ('27', 'Can delete user info', '7', 'delete_userinfo');
INSERT INTO `auth_permission` VALUES ('28', 'Can view user info', '7', 'view_userinfo');
INSERT INTO `auth_permission` VALUES ('29', 'Can add goods info', '8', 'add_goodsinfo');
INSERT INTO `auth_permission` VALUES ('30', 'Can change goods info', '8', 'change_goodsinfo');
INSERT INTO `auth_permission` VALUES ('31', 'Can delete goods info', '8', 'delete_goodsinfo');
INSERT INTO `auth_permission` VALUES ('32', 'Can view goods info', '8', 'view_goodsinfo');
INSERT INTO `auth_permission` VALUES ('33', 'Can add type info', '9', 'add_typeinfo');
INSERT INTO `auth_permission` VALUES ('34', 'Can change type info', '9', 'change_typeinfo');
INSERT INTO `auth_permission` VALUES ('35', 'Can delete type info', '9', 'delete_typeinfo');
INSERT INTO `auth_permission` VALUES ('36', 'Can view type info', '9', 'view_typeinfo');
INSERT INTO `auth_permission` VALUES ('37', 'Can add 购物车', '10', 'add_cartinfo');
INSERT INTO `auth_permission` VALUES ('38', 'Can change 购物车', '10', 'change_cartinfo');
INSERT INTO `auth_permission` VALUES ('39', 'Can delete 购物车', '10', 'delete_cartinfo');
INSERT INTO `auth_permission` VALUES ('40', 'Can view 购物车', '10', 'view_cartinfo');

-- ----------------------------
-- Table structure for auth_user
-- ----------------------------
DROP TABLE IF EXISTS `auth_user`;
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of auth_user
-- ----------------------------
INSERT INTO `auth_user` VALUES ('1', 'pbkdf2_sha256$120000$WmsFzjsADxRn$aVNOSKZxdldG2lMkixQ0yZILdy6VlxJ7meMCkWbRW84=', '2019-06-23 09:42:04.873354', '1', 'hcw', '', '', '897796171@qq.com', '1', '1', '2019-06-23 09:41:03.227480');

-- ----------------------------
-- Table structure for auth_user_groups
-- ----------------------------
DROP TABLE IF EXISTS `auth_user_groups`;
CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of auth_user_groups
-- ----------------------------

-- ----------------------------
-- Table structure for auth_user_user_permissions
-- ----------------------------
DROP TABLE IF EXISTS `auth_user_user_permissions`;
CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of auth_user_user_permissions
-- ----------------------------

-- ----------------------------
-- Table structure for df_cart_cartinfo
-- ----------------------------
DROP TABLE IF EXISTS `df_cart_cartinfo`;
CREATE TABLE `df_cart_cartinfo` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `count` int(11) NOT NULL,
  `goods_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `df_cart_cartinfo_goods_id_4357294f_fk_df_goods_goodsinfo_id` (`goods_id`),
  KEY `df_cart_cartinfo_user_id_db76e708_fk_df_user_userinfo_id` (`user_id`),
  CONSTRAINT `df_cart_cartinfo_goods_id_4357294f_fk_df_goods_goodsinfo_id` FOREIGN KEY (`goods_id`) REFERENCES `df_goods_goodsinfo` (`id`),
  CONSTRAINT `df_cart_cartinfo_user_id_db76e708_fk_df_user_userinfo_id` FOREIGN KEY (`user_id`) REFERENCES `df_user_userinfo` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of df_cart_cartinfo
-- ----------------------------

-- ----------------------------
-- Table structure for df_goods_goodsinfo
-- ----------------------------
DROP TABLE IF EXISTS `df_goods_goodsinfo`;
CREATE TABLE `df_goods_goodsinfo` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `gtitle` varchar(20) NOT NULL,
  `gpic` varchar(100) DEFAULT NULL,
  `gprice` decimal(5,2) NOT NULL,
  `isDelete` tinyint(1) NOT NULL,
  `gunit` varchar(20) NOT NULL,
  `gclick` int(11) NOT NULL,
  `gjianjie` varchar(200) NOT NULL,
  `gkucun` int(11) NOT NULL,
  `gcontent` longtext NOT NULL,
  `gtype_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `df_goods_goodsinfo_gtitle_8ec0f32b_uniq` (`gtitle`),
  KEY `df_goods_goodsinfo_gtype_id_63a02cef_fk_df_goods_typeinfo_id` (`gtype_id`),
  CONSTRAINT `df_goods_goodsinfo_gtype_id_63a02cef_fk_df_goods_typeinfo_id` FOREIGN KEY (`gtype_id`) REFERENCES `df_goods_typeinfo` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of df_goods_goodsinfo
-- ----------------------------

-- ----------------------------
-- Table structure for df_goods_typeinfo
-- ----------------------------
DROP TABLE IF EXISTS `df_goods_typeinfo`;
CREATE TABLE `df_goods_typeinfo` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `ttitle` varchar(20) NOT NULL,
  `isDelete` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of df_goods_typeinfo
-- ----------------------------
INSERT INTO `df_goods_typeinfo` VALUES ('13', '新鲜水果', '0');
INSERT INTO `df_goods_typeinfo` VALUES ('14', '海鲜水产', '0');
INSERT INTO `df_goods_typeinfo` VALUES ('15', '猪牛羊肉', '0');
INSERT INTO `df_goods_typeinfo` VALUES ('16', '禽类蛋品', '0');
INSERT INTO `df_goods_typeinfo` VALUES ('17', '新鲜蔬菜', '0');
INSERT INTO `df_goods_typeinfo` VALUES ('18', '速冻食品', '0');

-- ----------------------------
-- Table structure for df_user_userinfo
-- ----------------------------
DROP TABLE IF EXISTS `df_user_userinfo`;
CREATE TABLE `df_user_userinfo` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `uname` varchar(20) NOT NULL,
  `upwd` varchar(40) NOT NULL,
  `uemail` varchar(30) NOT NULL,
  `ushou` varchar(20) NOT NULL,
  `uaddress` varchar(100) NOT NULL,
  `uyoubian` varchar(6) NOT NULL,
  `uphone` varchar(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of df_user_userinfo
-- ----------------------------
INSERT INTO `df_user_userinfo` VALUES ('1', 'jerry', '7c222fb2927d828af22f592134e8932480637c0d', '897796171@qq.com', '', '', '', '');

-- ----------------------------
-- Table structure for django_admin_log
-- ----------------------------
DROP TABLE IF EXISTS `django_admin_log`;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of django_admin_log
-- ----------------------------
INSERT INTO `django_admin_log` VALUES ('1', '2019-06-23 13:54:16.423977', '13', '新鲜水果', '1', '[{\"added\": {}}]', '9', '1');
INSERT INTO `django_admin_log` VALUES ('2', '2019-06-23 13:54:42.104212', '14', '海鲜水果', '1', '[{\"added\": {}}]', '9', '1');
INSERT INTO `django_admin_log` VALUES ('3', '2019-06-23 13:55:11.339306', '14', '海鲜水产', '2', '[{\"changed\": {\"fields\": [\"ttitle\"]}}]', '9', '1');
INSERT INTO `django_admin_log` VALUES ('4', '2019-06-23 13:55:31.699965', '15', '猪牛羊肉', '1', '[{\"added\": {}}]', '9', '1');
INSERT INTO `django_admin_log` VALUES ('5', '2019-06-23 13:56:02.000088', '16', '禽类蛋品', '1', '[{\"added\": {}}]', '9', '1');
INSERT INTO `django_admin_log` VALUES ('6', '2019-06-23 13:56:26.768131', '17', '新鲜蔬菜', '1', '[{\"added\": {}}]', '9', '1');
INSERT INTO `django_admin_log` VALUES ('7', '2019-06-23 13:56:44.367723', '18', '速冻食品', '1', '[{\"added\": {}}]', '9', '1');

-- ----------------------------
-- Table structure for django_content_type
-- ----------------------------
DROP TABLE IF EXISTS `django_content_type`;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of django_content_type
-- ----------------------------
INSERT INTO `django_content_type` VALUES ('1', 'admin', 'logentry');
INSERT INTO `django_content_type` VALUES ('3', 'auth', 'group');
INSERT INTO `django_content_type` VALUES ('2', 'auth', 'permission');
INSERT INTO `django_content_type` VALUES ('4', 'auth', 'user');
INSERT INTO `django_content_type` VALUES ('5', 'contenttypes', 'contenttype');
INSERT INTO `django_content_type` VALUES ('10', 'df_cart', 'cartinfo');
INSERT INTO `django_content_type` VALUES ('8', 'df_goods', 'goodsinfo');
INSERT INTO `django_content_type` VALUES ('9', 'df_goods', 'typeinfo');
INSERT INTO `django_content_type` VALUES ('7', 'df_user', 'userinfo');
INSERT INTO `django_content_type` VALUES ('6', 'sessions', 'session');

-- ----------------------------
-- Table structure for django_migrations
-- ----------------------------
DROP TABLE IF EXISTS `django_migrations`;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of django_migrations
-- ----------------------------
INSERT INTO `django_migrations` VALUES ('1', 'contenttypes', '0001_initial', '2019-05-29 15:45:00.123261');
INSERT INTO `django_migrations` VALUES ('2', 'auth', '0001_initial', '2019-05-29 15:45:09.876833');
INSERT INTO `django_migrations` VALUES ('3', 'admin', '0001_initial', '2019-05-29 15:45:12.947248');
INSERT INTO `django_migrations` VALUES ('4', 'admin', '0002_logentry_remove_auto_add', '2019-05-29 15:45:13.123141');
INSERT INTO `django_migrations` VALUES ('5', 'admin', '0003_logentry_add_action_flag_choices', '2019-05-29 15:45:13.216080');
INSERT INTO `django_migrations` VALUES ('6', 'contenttypes', '0002_remove_content_type_name', '2019-05-29 15:45:14.917704');
INSERT INTO `django_migrations` VALUES ('7', 'auth', '0002_alter_permission_name_max_length', '2019-05-29 15:45:15.905481');
INSERT INTO `django_migrations` VALUES ('8', 'auth', '0003_alter_user_email_max_length', '2019-05-29 15:45:17.303620');
INSERT INTO `django_migrations` VALUES ('9', 'auth', '0004_alter_user_username_opts', '2019-05-29 15:45:17.450527');
INSERT INTO `django_migrations` VALUES ('10', 'auth', '0005_alter_user_last_login_null', '2019-05-29 15:45:18.368962');
INSERT INTO `django_migrations` VALUES ('11', 'auth', '0006_require_contenttypes_0002', '2019-05-29 15:45:18.449918');
INSERT INTO `django_migrations` VALUES ('12', 'auth', '0007_alter_validators_add_error_messages', '2019-05-29 15:45:18.534859');
INSERT INTO `django_migrations` VALUES ('13', 'auth', '0008_alter_user_username_max_length', '2019-05-29 15:45:19.475300');
INSERT INTO `django_migrations` VALUES ('14', 'auth', '0009_alter_user_last_name_max_length', '2019-05-29 15:45:20.728472');
INSERT INTO `django_migrations` VALUES ('15', 'df_user', '0001_initial', '2019-05-29 15:45:21.332097');
INSERT INTO `django_migrations` VALUES ('16', 'sessions', '0001_initial', '2019-05-29 15:45:22.005677');
INSERT INTO `django_migrations` VALUES ('17', 'df_goods', '0001_initial', '2019-06-16 14:49:06.711782');
INSERT INTO `django_migrations` VALUES ('18', 'df_user', '0002_auto_20190616_2248', '2019-06-16 14:49:06.759754');
INSERT INTO `django_migrations` VALUES ('19', 'df_goods', '0002_auto_20190620_2319', '2019-06-20 15:24:24.545195');
INSERT INTO `django_migrations` VALUES ('20', 'df_cart', '0001_initial', '2019-06-20 15:24:27.029490');

-- ----------------------------
-- Table structure for django_session
-- ----------------------------
DROP TABLE IF EXISTS `django_session`;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of django_session
-- ----------------------------
INSERT INTO `django_session` VALUES ('c74aaqizl7hr9ct8fs7nho6xqxv8v841', 'MWE4ZWFhOGRkZWMwYTM5ZmVkNjQ0MWYwYWUzNTVmOTJkM2QxY2ZiZjp7InVzZXJfaWQiOjEsInVzZXJfbmFtZSI6ImplcnJ5In0=', '2019-06-17 15:35:17.591964');
INSERT INTO `django_session` VALUES ('mirfbahgjo9rpelid0fdtdtwpg9yxzcp', 'NzI0ZWQ2Yzg1YjgzNmZjMmE2NmEyZjIzMGU2YjRiZDU4NGFjMDk1NTp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI1YjFjNTFlNDRkODA2MWJhOTFlNmRkMzYzODQ3ZTg4MzE5MDdmYWQ4In0=', '2019-07-07 09:42:04.939311');
INSERT INTO `django_session` VALUES ('nhawjtcufl0w64xt2xv6slzou0xwr42i', 'MWE4ZWFhOGRkZWMwYTM5ZmVkNjQ0MWYwYWUzNTVmOTJkM2QxY2ZiZjp7InVzZXJfaWQiOjEsInVzZXJfbmFtZSI6ImplcnJ5In0=', '2019-06-18 14:40:53.142802');
