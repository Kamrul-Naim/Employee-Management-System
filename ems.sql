-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Nov 24, 2024 at 03:01 AM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `ems`
--

-- --------------------------------------------------------

--
-- Table structure for table `data`
--

CREATE TABLE `data` (
  `Id` varchar(30) DEFAULT NULL,
  `Name` varchar(50) DEFAULT NULL,
  `Phone` varchar(15) DEFAULT NULL,
  `Role` varchar(50) DEFAULT NULL,
  `Gender` varchar(20) DEFAULT NULL,
  `Salary` varchar(15) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `data`
--

INSERT INTO `data` (`Id`, `Name`, `Phone`, `Role`, `Gender`, `Salary`) VALUES
('101', 'Kamrul', '01619938404', 'Web Developer', 'Male', '69000'),
('102', 'Mehedi Hasan', '01505509562', 'Web Developer', 'Male', '70000'),
('103', 'Amir Hamza', '01785430972', 'Web Developer', 'Male', '50000'),
('104', 'Horidas', '1719938404', 'Network Engineer', 'Male', '700000'),
('105', 'Anamika', '1890562389', 'Business Analyst', 'Female', '150000'),
('106', 'Jidni', '01907852410', 'Cloud Architect', 'Male', '70000');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
