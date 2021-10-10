-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
-- -----------------------------------------------------
-- Schema books_db
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `books_db` ;

-- -----------------------------------------------------
-- Schema books_db
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `books_db` DEFAULT CHARACTER SET utf8 ;
USE `books_db` ;

-- -----------------------------------------------------
-- Table `books_db`.`authors`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `books_db`.`authors` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(45) NOT NULL,
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
AUTO_INCREMENT = 7
DEFAULT CHARACTER SET = utf8mb3;


-- -----------------------------------------------------
-- Table `books_db`.`books`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `books_db`.`books` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `title` VARCHAR(45) NOT NULL,
  `num_of_pages` INT NULL DEFAULT NULL,
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb3;


-- -----------------------------------------------------
-- Table `books_db`.`favorites`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `books_db`.`favorites` (
  `author_id` INT NOT NULL,
  `book_id` INT NOT NULL,
  PRIMARY KEY (`author_id`, `book_id`),
  INDEX `fk_authors_has_books_books1_idx` (`book_id` ASC) VISIBLE,
  INDEX `fk_authors_has_books_authors_idx` (`author_id` ASC) VISIBLE,
  CONSTRAINT `fk_authors_has_books_authors`
    FOREIGN KEY (`author_id`)
    REFERENCES `books_db`.`authors` (`id`),
  CONSTRAINT `fk_authors_has_books_books1`
    FOREIGN KEY (`book_id`)
    REFERENCES `books_db`.`books` (`id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb3;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
