CREATE TABLE payments (
    payment_id INT AUTO_INCREMENT PRIMARY KEY,
    order_id INT NOT NULL,
    amount DECIMAL(10,2),
    payment_date DATE,
    method VARCHAR(50),
    status VARCHAR(20)
);

-- Sample data
INSERT INTO payments (order_id, amount, payment_date, method, status) VALUES
(1, 150.50, '2025-04-11', 'Credit Card', 'success'),
(2, 89.99, '2025-05-06', 'PayPal', 'pending');
