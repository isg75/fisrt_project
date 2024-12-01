-- Client completion rate
CREATE OR REPLACE VIEW view_latest_steps_per_visit AS (
    SELECT client_id, visitor_id, visit_id, process_step, MAX(date_time) AS last_date_time
    FROM client_visits
    GROUP BY client_id, visitor_id, visit_id, process_step
);

WITH cte_distinct_client_stats AS (
	SELECT
		COUNT(DISTINCT CASE WHEN process_step = 'confirm' THEN client_id END) AS completed_clients,
		COUNT(DISTINCT client_id) AS total_clients
	FROM view_latest_steps_per_visit
)
SELECT *, ROUND(completed_clients * 100.0 / total_clients, 2) AS completion_rate_percentage
FROM cte_distinct_client_stats;

-- Time spent on each step
WITH cte_step_durations_per_visit AS (
    SELECT
		*,
        TIMESTAMPDIFF(
			SECOND, 
            LAG(last_date_time) OVER (PARTITION BY client_id, visitor_id, visit_id ORDER BY last_date_time), 
            last_date_time
        ) AS time_spent_seconds
    FROM view_latest_steps_per_visit
)
SELECT process_step, ROUND(AVG(time_spent_seconds), 2) AS avg_time_seconds
FROM cte_step_durations_per_visit
WHERE process_step <> 'start'
GROUP BY process_step
ORDER BY process_step='confirm', process_step='step_3', process_step='step_2', process_step='step_1', process_step='start';

-- Error rate
WITH
cte_step_orders AS (
    SELECT *, ROW_NUMBER() OVER (PARTITION BY client_id, visitor_id, visit_id ORDER BY last_date_time) AS step_order
    FROM view_latest_steps_per_visit
),
cte_errors AS (
	SELECT so1.client_id, so1.visitor_id, so1.visit_id, COUNT(*) AS errors
	FROM cte_step_orders so1
	JOIN cte_step_orders so2 ON so1.client_id = so2.client_id AND so1.visit_id = so2.visit_id AND so1.step_order < so2.step_order
	WHERE so1.process_step != so2.process_step
	GROUP BY so1.client_id, so1.visitor_id, so1.visit_id
),
cte_total_transitions AS (
    SELECT client_id, visitor_id, visit_id, COUNT(*) - 1 AS total_transitions
    FROM cte_step_orders
    GROUP BY client_id, visitor_id, visit_id
),
cte_error_stats AS (
	SELECT SUM(e.errors) AS total_errors, SUM(t.total_transitions) AS total_transitions
    FROM cte_total_transitions t
    LEFT JOIN cte_errors e ON t.client_id = e.client_id AND t.visit_id = e.visit_id
)
SELECT COALESCE(ROUND(total_errors / total_transitions, 2), 0) AS error_rate_percentage
FROM cte_error_stats;

-- Completion rate per step
WITH
cte_step_counts AS (
    SELECT process_step, COUNT(DISTINCT client_id, visitor_id, visit_id) AS num_visits
    FROM view_latest_steps_per_visit
    GROUP BY process_step
),
cte_total_visits AS (
    SELECT COUNT(DISTINCT client_id, visitor_id, visit_id) AS total_visits
    FROM view_latest_steps_per_visit
    WHERE process_step = 'start'
)
SELECT sc.process_step, sc.num_visits, ROUND(sc.num_visits * 100.0 / tv.total_visits, 2) AS completion_rate_percentage
FROM cte_step_counts sc
CROSS JOIN cte_total_visits tv
ORDER BY sc.num_visits DESC;
