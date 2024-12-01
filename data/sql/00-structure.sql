DROP DATABASE IF EXISTS vanguard;
CREATE DATABASE vanguard;

use vanguard;

CREATE TABLE clients (
	id INT PRIMARY KEY,
    tenure_years FLOAT,
    tenure_months FLOAT,
    age FLOAT,
    gender ENUM('F', 'M', 'U', 'X'),
    num_accounts INT,
    balance FLOAT,
    calls_6_months INT,
    logons_6_months INT
);

CREATE TABLE client_experiments (
	id INT PRIMARY KEY,
	client_id INT,
    variation ENUM('Test', 'Control'),
    
    FOREIGN KEY(client_id) REFERENCES clients(id)
);

CREATE TABLE client_visits (
    id INT PRIMARY KEY,
    client_id INT,
    visitor_id VARCHAR(255),
    visit_id VARCHAR(255),
    process_step VARCHAR(255),
    date_time DATETIME
);
