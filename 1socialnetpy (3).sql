-- phpMyAdmin SQL Dump
-- version 2.11.6
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Mar 14, 2022 at 04:16 PM
-- Server version: 5.0.51
-- PHP Version: 5.2.6

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `1socialnetpy`
--

-- --------------------------------------------------------

--
-- Table structure for table `comtb`
--

CREATE TABLE `comtb` (
  `id` bigint(250) NOT NULL auto_increment,
  `uname` varchar(250) NOT NULL,
  `frname` varchar(250) NOT NULL,
  `comment` varchar(250) NOT NULL,
  `Ccount` bigint(250) NOT NULL,
  `shareid` varchar(250) NOT NULL,
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=7 ;

--
-- Dumping data for table `comtb`
--

INSERT INTO `comtb` (`id`, `uname`, `frname`, `comment`, `Ccount`, `shareid`) VALUES
(1, 'sangeeth', 'rajiya', 'good', 0, '3'),
(2, 'sangeeth', 'rajiya', 'hai poda', 0, '3'),
(3, 'sangeeth', 'rajiya', 'hai poda', 1, '3'),
(4, 'sangeeth', 'rajiya', 'poda', 2, '3'),
(5, 'sangeeth', 'rajiya', 'poda', 1, '3'),
(6, 'sangeeth', 'rajiya', 'poda', 1, '3');

-- --------------------------------------------------------

--
-- Table structure for table `frlist`
--

CREATE TABLE `frlist` (
  `id` bigint(250) NOT NULL auto_increment,
  `uname` varchar(250) NOT NULL,
  `Frname` varchar(250) NOT NULL,
  `Status` varchar(250) NOT NULL,
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=3 ;

--
-- Dumping data for table `frlist`
--

INSERT INTO `frlist` (`id`, `uname`, `Frname`, `Status`) VALUES
(1, 'rajiya', 'sangeeth', 'Accept'),
(2, 'sangeeth', 'rajiya', 'Accept');

-- --------------------------------------------------------

--
-- Table structure for table `negtb`
--

CREATE TABLE `negtb` (
  `id` bigint(250) NOT NULL auto_increment,
  `words` varchar(250) NOT NULL,
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=5 ;

--
-- Dumping data for table `negtb`
--

INSERT INTO `negtb` (`id`, `words`) VALUES
(1, 'poda'),
(2, 'pode'),
(4, 'dog');

-- --------------------------------------------------------

--
-- Table structure for table `register`
--

CREATE TABLE `register` (
  `id` int(20) NOT NULL,
  `name` varchar(50) NOT NULL,
  `Gender` varchar(250) NOT NULL,
  `Age` varchar(250) NOT NULL,
  `address` varchar(50) NOT NULL,
  `email` varchar(50) NOT NULL,
  `pnumber` varchar(50) NOT NULL,
  `uname` varchar(50) NOT NULL,
  `password` varchar(50) NOT NULL,
  `image` varchar(50) NOT NULL,
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `register`
--

INSERT INTO `register` (`id`, `name`, `Gender`, `Age`, `address`, `email`, `pnumber`, `uname`, `password`, `image`) VALUES
(4, 'sangeeth', 'male', '20', 'No 16, Samnath Plaza, Madurai Main Road, Melapudhu', 'sangeeth5535@gmail.com', '9486365535', 'sangeeth', 'sangeeth', 'download (1).jpg'),
(5, 'rajiya', 'male', '20', 'No 16 samnath plaza, melapudur  trichy\r\nNo 16 samn', 'sangeeth5535@gmail.com', '9486365535', 'rajiya', 'rajiya', 'download.jpg');

-- --------------------------------------------------------

--
-- Table structure for table `sharetb`
--

CREATE TABLE `sharetb` (
  `id` bigint(250) NOT NULL auto_increment,
  `UserName` varchar(250) NOT NULL,
  `ImageInfo` varchar(250) NOT NULL,
  `Image` varchar(500) NOT NULL,
  `FrName` varchar(250) NOT NULL,
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=6 ;

--
-- Dumping data for table `sharetb`
--

INSERT INTO `sharetb` (`id`, `UserName`, `ImageInfo`, `Image`, `FrName`) VALUES
(2, 'sangeeth', 'natural', 'Hydrangeas.jpg', 'sangeeth'),
(3, 'sangeeth', 'natural', 'Hydrangeas.jpg', 'rajiya'),
(4, 'rajiya', 'natural', 'Hydrangeas.jpg', 'sangeeth'),
(5, 'rajiya', 'natural', 'Hydrangeas.jpg', 'sangeeth');
