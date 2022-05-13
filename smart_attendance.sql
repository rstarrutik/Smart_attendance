-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: May 13, 2022 at 05:09 AM
-- Server version: 10.4.22-MariaDB
-- PHP Version: 8.1.2

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `smart_attendance`
--

-- --------------------------------------------------------

--
-- Table structure for table `workers`
--

CREATE TABLE `workers` (
  `worker_name` varchar(45) DEFAULT NULL,
  `aadhar` int(45) NOT NULL,
  `date_of_birth` varchar(45) NOT NULL,
  `gender` varchar(45) NOT NULL,
  `bloodgroup` varchar(45) NOT NULL,
  `address` varchar(45) NOT NULL,
  `email` varchar(45) NOT NULL,
  `phone_no` varchar(45) NOT NULL,
  `city` varchar(45) NOT NULL,
  `worker_category` varchar(45) NOT NULL,
  `work_type` varchar(45) NOT NULL,
  `register_by` varchar(45) NOT NULL,
  `date_of_joining` varchar(45) DEFAULT NULL,
  `site_location` varchar(45) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `workers`
--

INSERT INTO `workers` (`worker_name`, `aadhar`, `date_of_birth`, `gender`, `bloodgroup`, `address`, `email`, `phone_no`, `city`, `worker_category`, `work_type`, `register_by`, `date_of_joining`, `site_location`) VALUES
('', 0, '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '', ''),
('r', 5, '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', 't', 'y'),
('d', 22, 'd', 'Yes', 'f', 'f', 'f', 'f', 'f', 'A:PUBLIC WORKS', 'Irrigation', 'd', 'd', 'd'),
('Rutik M', 21236545, '13/04/2000', 'Yes', 'AB+', 'Bhusawal', '0101@test.com', '9087654123', 'jalgaon', 'B:COMMUNITY ASSETS', 'flood management', 'Rut', '22/04/33', 'site@bambhoi');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `workers`
--
ALTER TABLE `workers`
  ADD PRIMARY KEY (`aadhar`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
