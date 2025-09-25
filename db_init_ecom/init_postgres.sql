CREATE TABLE customers (
    customer_id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100) UNIQUE,
    phone VARCHAR(20),
    address TEXT
);

CREATE TABLE orders (
    order_id SERIAL PRIMARY KEY,
    customer_id INT REFERENCES customers(customer_id),
    order_date DATE NOT NULL,
    status VARCHAR(20),
    total_amount DECIMAL(10,2)
);

CREATE TABLE order_items (
    order_item_id SERIAL PRIMARY KEY,
    order_id INT REFERENCES orders(order_id),
    product_id VARCHAR(20),
    quantity INT,
    price DECIMAL(10,2)
);

-- Sample data
INSERT INTO customers (name, email, phone, address) VALUES
('Alice Johnson', 'alice@example.com', '1234567890', 'Dubai, UAE'),
('Bob Smith', 'bob@example.com', '9876543210', 'Sharjah, UAE');

INSERT INTO orders (customer_id, order_date, status, total_amount) VALUES
(1, '2025-04-10', 'delivered', 150.50),
(2, '2025-05-05', 'pending', 89.99);

INSERT INTO order_items (order_id, product_id, quantity, price) VALUES
(1, 'P1001', 2, 25.00),
(1, 'P2002', 1, 100.50),
(2, 'P1001', 1, 25.00),
(2, 'P3003', 1, 64.99);
