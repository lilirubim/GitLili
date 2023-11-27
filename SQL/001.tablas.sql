CREATE TABLE `demo3`.`customers` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(45) NOT NULL,
  `NIF` VARCHAR(9) NULL,
  `edad` INT NULL,
  `salary` DECIMAL(14,2) NULL,
  `activo` TINYINT(1) NULL,
  `fecha de cumpleanos` DATE NULL,
  `biography` TEXT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `NIF_UNIQUE` (`NIF` ASC) VISIBLE)
ENGINE = InnoDB;

INSERT INTO `demo3`.`customers` (`nombre`, `NIF`, `edad`, `salary`, `activo`, `fecha de cumpleanos`, `biography`) VALUES ('prueba', '12345678R', '30', '3000.25', '1', '2023-01-23', 'sdfasgafgasvcafsafgaadfgd');
INSERT INTO `demo3`.`customers` (`nombre`, `NIF`, `edad`, `salary`, `activo`, `fecha de cumpleanos`, `biography`) VALUES ('prueba2', '23456789P', '40', '1236525', '0', '1990-01-01', 'çl~ç,zçxfbvlzkmbzkxmvcçkç');
INSERT INTO `demo3`.`customers` (`nombre`, `NIF`, `edad`, `salary`, `activo`, `fecha de cumpleanos`, `biography`) VALUES ('prueba3', '98765432E', '34', '1254896.99', '1', '1995-05-30', 'patrsojgalfkladifjgalkfdlafjvoi');
