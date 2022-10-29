DROP TABLE IF EXISTS `users`;
CREATE TABLE `users` (
	  `user_id` int NOT NULL AUTO_INCREMENT,
	  `username` varchar(32) DEFAULT NULL,
	  `pwd` varchar(255) DEFAULT NULL,
	  `email_id` varchar(64) DEFAULT NULL,
	  `prof_img` varchar(64) DEFAULT 'default_prof_img.png',
	  `is_active` int DEFAULT '0',
	  PRIMARY KEY (`user_id`),
	  UNIQUE KEY `username` (`username`)
);
DROP TABLE IF EXISTS `messages`;
CREATE TABLE `messages` (
	  `sender_id` int NOT NULL,
	  `receiver_id` int NOT NULL,
	  `msg` varchar(255) NOT NULL,
	  `time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
	  `sender_flag` bit(1) DEFAULT b'1',
	  `receiver_flag` bit(1) DEFAULT b'1',
	  PRIMARY KEY (`sender_id`,`receiver_id`,`time`,`msg`),
	  KEY `receiver_id` (`receiver_id`),
	  CONSTRAINT `messages_ibfk_1` FOREIGN KEY (`sender_id`) REFERENCES `users` (`user_id`) ON DELETE CASCADE,
	  CONSTRAINT `messages_ibfk_2` FOREIGN KEY (`receiver_id`) REFERENCES `users` (`user_id`) ON DELETE CASCADE
);
