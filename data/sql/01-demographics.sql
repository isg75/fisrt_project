-- Primary clients
SELECT c.*, COUNT(*) AS total_visits
FROM clients c
JOIN client_visits cv ON c.id = cv.client_id
GROUP BY c.id
ORDER BY total_visits DESC
LIMIT 10;

CREATE OR REPLACE VIEW view_client_visits AS (
    SELECT client_id, COUNT(*) AS num_visits
    FROM client_visits
    GROUP BY client_id
);

-- Age group
SELECT 
    CASE 
        WHEN c.age < 40 THEN 'Younger (Under 40)'
        WHEN c.age BETWEEN 40 AND 60 THEN 'Middle-aged (40-60)'
        ELSE 'Older (60+)' 
    END AS age_group,
    SUM(cv.num_visits) AS total_visits
FROM view_client_visits cv
JOIN clients c ON c.id = cv.client_id
GROUP BY age_group
ORDER BY total_visits DESC;

-- Tenure analysis
SELECT 
    CASE 
        WHEN c.tenure_years < 3 THEN 'New (1-2 year)'
        WHEN c.tenure_years < 5 THEN 'Moderately long (3-4 years)'
        ELSE 'Long-standing (5+ years)' 
    END AS tenure_group,
    SUM(cv.num_visits) AS total_visits
FROM view_client_visits cv
JOIN clients c ON c.id = cv.client_id
GROUP BY tenure_group
ORDER BY total_visits DESC;
