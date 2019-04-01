CREATE DATABASE IF NOT EXISTS `webdata`;
USE `webdata`;

CREATE TABLE IF NOT EXISTS `User Store` (
  `UID` varchar(45) NOT NULL,
  `Display Name` varchar(45) DEFAULT NULL,
  `Password` varchar(64) DEFAULT NULL,
  PRIMARY KEY (`UID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

CREATE TABLE IF NOT EXISTS `Video Store` (
  `UID` varchar(45) NOT NULL,
  `Video Name` varchar(256) NOT NULL,
  `Video Location` varchar(256) DEFAULT NULL,
  PRIMARY KEY (`UID`,`Video Name`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
