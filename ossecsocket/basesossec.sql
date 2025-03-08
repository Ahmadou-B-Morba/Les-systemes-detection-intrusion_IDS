-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Hôte : 127.0.0.1:3306
-- Généré le : dim. 12 mai 2024 à 16:55
-- Version du serveur : 8.0.36
-- Version de PHP : 8.2.18

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de données : `basesossec`
--

-- --------------------------------------------------------

--
-- Structure de la table `tableossec`
--

DROP TABLE IF EXISTS `tableossec`;
CREATE TABLE IF NOT EXISTS `tableossec` (
  `num` int NOT NULL AUTO_INCREMENT,
  `rule_level` int NOT NULL,
  `rule_comment` varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_unicode_ci NOT NULL,
  `rule_sidid` int NOT NULL,
  `rule_firedtimes` int NOT NULL,
  `rule_groups` varchar(255) COLLATE utf8mb3_unicode_ci NOT NULL,
  `location` varchar(300) COLLATE utf8mb3_unicode_ci NOT NULL,
  `full_log` text COLLATE utf8mb3_unicode_ci NOT NULL,
  `hostname` varchar(300) COLLATE utf8mb3_unicode_ci NOT NULL,
  `program_name` varchar(300) COLLATE utf8mb3_unicode_ci NOT NULL,
  `decoder_desc` text COLLATE utf8mb3_unicode_ci NOT NULL,
  `agent_name` varchar(255) COLLATE utf8mb3_unicode_ci NOT NULL,
  `timestamp` datetime NOT NULL,
  `logfile` varchar(300) COLLATE utf8mb3_unicode_ci NOT NULL,
  `id` varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_unicode_ci NOT NULL,
  PRIMARY KEY (`num`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_unicode_ci;

--
-- Déchargement des données de la table `tableossec`
--

INSERT INTO `tableossec` (`num`, `rule_level`, `rule_comment`, `rule_sidid`, `rule_firedtimes`, `rule_groups`, `location`, `full_log`, `hostname`, `program_name`, `decoder_desc`, `agent_name`, `timestamp`, `logfile`, `id`) VALUES
(1, 2, 'Unknown problem somewhere in the system.', 1002, 13, 'syslog,errors', '/var/log/syslog', '2024-05-10T05:39:43.752715+01:00 ubuntu update-notifier[3478]: gtk_widget_get_scale_factor: assertion \'GTK_IS_WIDGET (widget)\' failed', 'ubuntu', 'update-notifier', '{}', 'ubuntu', '2024-05-10 05:39:44', '/var/log/syslog', '1715315984.54056');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
