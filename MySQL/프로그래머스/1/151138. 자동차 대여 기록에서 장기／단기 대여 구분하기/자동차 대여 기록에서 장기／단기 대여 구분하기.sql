SELECT history_id,
       car_id,
       start_date,
       end_date,
       IF (DATEDIFF(end_date, start_date) >= 29, '장기 대여', '단기 대여') AS rent_type
FROM car_rental_company_rental_history
WHERE start_date >= '2022-09-01' AND
      start_date < '2022-10-01'
ORDER BY history_id DESC