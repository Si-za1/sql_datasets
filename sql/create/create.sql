-- Drop existing tables
DROP TABLE IF EXISTS sales;
DROP TABLE IF EXISTS menu;
DROP TABLE IF EXISTS members;

-- Create the members table
CREATE TABLE IF NOT EXISTS members 
(
    customer_id VARCHAR(200) PRIMARY KEY,
    join_date DATE 
);

-- Create the menu table
CREATE TABLE IF NOT EXISTS menu
(
    product_id VARCHAR(50) PRIMARY KEY,
    product_name VARCHAR(50) NOT NULL,
    price DECIMAL(10,2)
);

-- Create the sales table
CREATE TABLE IF NOT EXISTS sales
(
    customer_id VARCHAR(200),
    order_date DATE,
    product_id VARCHAR(50),
    FOREIGN KEY (customer_id) REFERENCES members(customer_id),
    FOREIGN KEY (product_id) REFERENCES menu(product_id)
);
