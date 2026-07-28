SELECT b.category,
       SUM(s.sales) AS total_sales
FROM book b
JOIN book_sales s USING(book_id)
WHERE s.sales_date >= '2022-01-01' AND
      s.sales_date < '2022-02-01'
GROUP BY b.category
ORDER BY b.category