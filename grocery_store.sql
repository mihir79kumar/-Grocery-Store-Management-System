-- SQL Schema for Grocery Store Management System Database
-- Create the database if it does not exist
CREATE DATABASE IF NOT EXISTS grocery_store;
USE grocery_store;

-- 1. Create 'uom' (Units of Measure) table
CREATE TABLE IF NOT EXISTS uom (
  uom_id INT AUTO_INCREMENT PRIMARY KEY,
  uom_name VARCHAR(45) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- Seed initial Units of Measure
INSERT INTO uom (uom_id, uom_name) VALUES 
(1, 'Each'), 
(2, 'Kg')
ON DUPLICATE KEY UPDATE uom_name=VALUES(uom_name);

-- 2. Create 'products' table
CREATE TABLE IF NOT EXISTS products (
  product_id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(100) NOT NULL,
  uom_id INT NOT NULL,
  price_per_unit DOUBLE NOT NULL,
  FOREIGN KEY (uom_id) REFERENCES uom (uom_id) ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- Seed initial sample products
INSERT INTO products (product_id, name, uom_id, price_per_unit) VALUES
(1, 'Toothpaste', 1, 30.0),
(2, 'Rice', 2, 50.0),
(3, 'Potatoes', 2, 15.0),
(4, 'Banana', 1, 5.0)
ON DUPLICATE KEY UPDATE name=VALUES(name), uom_id=VALUES(uom_id), price_per_unit=VALUES(price_per_unit);

-- 3. Create 'orders' table
CREATE TABLE IF NOT EXISTS orders (
  order_id INT AUTO_INCREMENT PRIMARY KEY,
  customer_name VARCHAR(100) NOT NULL,
  total DOUBLE NOT NULL,
  datetime DATETIME NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- 4. Create 'order_details' table (association table with foreign keys)
CREATE TABLE IF NOT EXISTS order_details (
  order_id INT NOT NULL,
  product_id INT NOT NULL,
  quantity DOUBLE NOT NULL,
  total_price DOUBLE NOT NULL,
  PRIMARY KEY (order_id, product_id),
  FOREIGN KEY (order_id) REFERENCES orders (order_id) ON UPDATE CASCADE ON DELETE CASCADE,
  FOREIGN KEY (product_id) REFERENCES products (product_id) ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
