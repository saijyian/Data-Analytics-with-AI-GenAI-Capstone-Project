--Task 1 — Schema (sql/schema.sql) — 6 marks
--Three tables, matching the taught CREATE TABLE syntax (column name, data type, NOT NULL, DEFAULT, PRIMARY KEY, FOREIGN KEY ... REFERENCES):

--customers(customer_id VARCHAR(10) PRIMARY KEY, name VARCHAR(50) NOT NULL, city VARCHAR(50) NOT NULL, city_tier INT NOT NULL, signup_date DATE NOT NULL, acquisition_source VARCHAR(20) NOT NULL)
--products(product_id VARCHAR(10) PRIMARY KEY, product_name VARCHAR(100) NOT NULL, category VARCHAR(30) NOT NULL, price DECIMAL(10,2) NOT NULL)
--orders(order_id VARCHAR(10) PRIMARY KEY, customer_id VARCHAR(10) NOT NULL, product_id VARCHAR(10) NOT NULL, order_date DATE NOT NULL, quantity INT NOT NULL, discount_pct INT, payment_method VARCHAR(10) NOT NULL, rating INT, returned INT NOT NULL DEFAULT 0, FOREIGN KEY (customer_id) REFERENCES customers(customer_id), FOREIGN KEY (product_id) REFERENCES products(product_id))
--Note discount_pct and rating deliberately have no NOT NULL — real orders can be un-rated or promo-code-free, so NULL is the correct representation, not an error to constrain away.

--SQL CODE
--Creating the database for MamaEarth
CREATE DataBase MamaEarth;
Use MamaEarth;

--Creating the schemas of the three Tables
--Table 01: Customers
CREATE TABLE customers (
    customer_id VARCHAR(10) PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    city VARCHAR(50) NOT NULL,
    city_tier INT NOT NULL,
    signup_date DATE NOT NULL,
    acquisition_source VARCHAR(20) NOT NULL
);

--Table 02: Products
CREATE TABLE products (
    product_id VARCHAR(10) PRIMARY KEY,
    product_name VARCHAR(100) NOT NULL,
    category VARCHAR(30) NOT NULL,
    price DECIMAL(10,2) NOT NULL
);

--Table 01: Orders
CREATE TABLE orders (
    order_id VARCHAR(10) PRIMARY KEY,
    customer_id VARCHAR(10) NOT NULL,
    product_id VARCHAR(10) NOT NULL,
    order_date DATE NOT NULL,
    quantity INT NOT NULL,
    discount_pct INT,
    payment_method VARCHAR(10) NOT NULL,
    rating INT,
    returned INT NOT NULL DEFAULT 0,

    FOREIGN KEY (customer_id)
        REFERENCES customers(customer_id),

    FOREIGN KEY (product_id)
        REFERENCES products(product_id)
);
