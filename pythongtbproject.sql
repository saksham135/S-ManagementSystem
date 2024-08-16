-- phpMyAdmin SQL Dump
-- version 5.3.0-dev+20220826.811789df3c
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Aug 27, 2022 at 09:27 AM
-- Server version: 10.4.24-MariaDB
-- PHP Version: 8.1.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `pythongtbproject`
--

-- --------------------------------------------------------

--
-- Table structure for table `course`
--

CREATE TABLE `course` (
  `Dname` varchar(100) NOT NULL,
  `Cname` varchar(100) NOT NULL,
  `Duration` varchar(100) NOT NULL,
  `Fee` float NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `course`
--

INSERT INTO `course` (`Dname`, `Cname`, `Duration`, `Fee`) VALUES
('Bca', 'Accounts', '4years', 90000),
('Barch', 'Architecture', '6years', 100000),
('Ece', 'Bsc', '4 years', 30000),
('Cse', 'btech', '3years', 20000),
('Cse', 'diploma', '4years', 50000),
('Arch', 'llb', '5years', 10000000),
('Cse', 'mca', '2years', 40000),
('Mce', 'mtech', '5years', 100000);

-- --------------------------------------------------------

--
-- Table structure for table `department`
--

CREATE TABLE `department` (
  `Dname` varchar(100) NOT NULL,
  `Hod` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `department`
--

INSERT INTO `department` (`Dname`, `Hod`) VALUES
('Arch', 'saksham'),
('Barch', 'Rohit'),
('Bca', 'Sushil'),
('Bla', 'rajesh'),
('Cse', 'Sunita'),
('Ece', 'Rajesh'),
('Mce', 'Jatin');

-- --------------------------------------------------------

--
-- Table structure for table `sdoubt`
--

CREATE TABLE `sdoubt` (
  `RollNo` int(10) NOT NULL,
  `Name` varchar(100) NOT NULL,
  `Sname` varchar(100) NOT NULL,
  `Sdoubt` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `sdoubt`
--

INSERT INTO `sdoubt` (`RollNo`, `Name`, `Sname`, `Sdoubt`) VALUES
(1, 'saksham', 'English', 'Doubts in chapter 2.\n'),
(2, 'Akash', 'Hindi', 'Facing Problem in Chapter 3 Question?\n');

-- --------------------------------------------------------

--
-- Table structure for table `student`
--

CREATE TABLE `student` (
  `RollNo` int(10) NOT NULL,
  `Name` varchar(100) NOT NULL,
  `Phone` varchar(20) NOT NULL,
  `Gender` varchar(100) NOT NULL,
  `DOB` date NOT NULL,
  `Address` varchar(100) NOT NULL,
  `Department` varchar(100) NOT NULL,
  `Courses` varchar(100) NOT NULL,
  `Pic` varchar(300) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `student`
--

INSERT INTO `student` (`RollNo`, `Name`, `Phone`, `Gender`, `DOB`, `Address`, `Department`, `Courses`, `Pic`) VALUES
(1, 'Saksham', '8146938734', 'male', '2004-01-25', 'Jalandhar\n\n\n\n', 'Ece', 'Bsc', '1661495178boy2.jpg'),
(4, 'Hitika', '921606651', 'female', '2099-02-24', 'Mumbai\n\n', 'Arch', 'llb', 'default_user.png'),
(7, 'kiran', '9056318734', 'female', '2080-05-14', 'chandigarh\n\n', 'Cse', 'diploma', '1661581212b1.jpg'),
(45, 'rohit saini', '3456789', 'male', '2004-08-12', 'jammu\n', 'Bca', 'Accounts', 'default_user.png'),
(87, 'rty', '78965412', 'male', '2006-08-10', 'gurgaon\n\n', 'Barch', 'Architecture', '1661581228b1.jpg');

-- --------------------------------------------------------

--
-- Table structure for table `subject`
--

CREATE TABLE `subject` (
  `Sname` varchar(100) NOT NULL,
  `Sincharge` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `subject`
--

INSERT INTO `subject` (`Sname`, `Sincharge`) VALUES
('Arts', 'Ankit'),
('English', 'Karan'),
('Hindi', 'Mohit'),
('Maths', 'Ashok');

-- --------------------------------------------------------

--
-- Table structure for table `teacher`
--

CREATE TABLE `teacher` (
  `TeacherId` int(10) NOT NULL,
  `Name` varchar(100) NOT NULL,
  `Phone` varchar(20) NOT NULL,
  `Gender` varchar(100) NOT NULL,
  `DOB` date NOT NULL,
  `Address` varchar(100) NOT NULL,
  `Subject` varchar(100) NOT NULL,
  `Qualification` varchar(100) NOT NULL,
  `Pic` varchar(300) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `teacher`
--

INSERT INTO `teacher` (`TeacherId`, `Name`, `Phone`, `Gender`, `DOB`, `Address`, `Subject`, `Qualification`, `Pic`) VALUES
(234, 'saksham', '78965412', 'male', '2000-08-10', 'mumbai\n\n', 'English', 'Bca', '1661495537boy2.jpg'),
(458, 'fggg', '444444', 'female', '2094-08-11', 'jaipur\n\n', 'Maths', 'Phd', '1661580517boy2.jpg'),
(567, 'sad', '344567', 'male', '1997-08-07', 'up\n', 'Arts', 'B.com', 'default_user.png'),
(678, 'isha', '555666', 'female', '2089-08-11', 'up\n\n', 'Hindi', 'M.A', '1661581248b1.jpg');

-- --------------------------------------------------------

--
-- Table structure for table `tquali`
--

CREATE TABLE `tquali` (
  `Sname` varchar(100) NOT NULL,
  `Qualification` varchar(100) NOT NULL,
  `Tperiod` varchar(100) NOT NULL,
  `Charges` float NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `tquali`
--

INSERT INTO `tquali` (`Sname`, `Qualification`, `Tperiod`, `Charges`) VALUES
('Arts', 'B.com', '6years', 200000),
('English', 'Bca', '2years', 60000),
('Hindi', 'M.A', '5years', 100000),
('Maths', 'Phd', '7years', 120000);

-- --------------------------------------------------------

--
-- Table structure for table `user`
--

CREATE TABLE `user` (
  `Uname` varchar(100) NOT NULL,
  `Password` varchar(100) NOT NULL,
  `Utype` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `user`
--

INSERT INTO `user` (`Uname`, `Password`, `Utype`) VALUES
('Akash', '345', 'Employee'),
('ashok23', '123456', 'Admin'),
('kiran', '12345', 'Teacher'),
('Saksham12', '23456', 'Admin');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `course`
--
ALTER TABLE `course`
  ADD PRIMARY KEY (`Cname`);

--
-- Indexes for table `department`
--
ALTER TABLE `department`
  ADD PRIMARY KEY (`Dname`);

--
-- Indexes for table `sdoubt`
--
ALTER TABLE `sdoubt`
  ADD PRIMARY KEY (`RollNo`);

--
-- Indexes for table `student`
--
ALTER TABLE `student`
  ADD PRIMARY KEY (`RollNo`);

--
-- Indexes for table `subject`
--
ALTER TABLE `subject`
  ADD PRIMARY KEY (`Sname`);

--
-- Indexes for table `teacher`
--
ALTER TABLE `teacher`
  ADD PRIMARY KEY (`TeacherId`);

--
-- Indexes for table `tquali`
--
ALTER TABLE `tquali`
  ADD PRIMARY KEY (`Qualification`);

--
-- Indexes for table `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`Uname`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
