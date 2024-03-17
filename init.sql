CREATE TABLE IF NOT EXISTS counter (
    id INT AUTO_INCREMENT PRIMARY KEY,
    count INT DEFAULT 0
);

INSERT INTO counter (count) VALUES (0);

CREATE TABLE IF NOT EXISTS access_log (
    id INT AUTO_INCREMENT PRIMARY KEY,
    access_time DATETIME,
    client_ip VARCHAR(50),
    internal_ip VARCHAR(50)
);

