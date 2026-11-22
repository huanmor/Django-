SELECT title , stock FROM books WHERE stock = 0 ;# 球状闪电 0 ,白夜行 0 


SELECT id,title , price FROM books 
ORDER BY  price DESC, id ASC 
LIMIT 3;
#白夜行 , 解忧杂货店 , 球状闪电

SELECT title , price FROM books
WHERE price BETWEEN 20 AND 40 
ORDER BY price DESC;
#活着 , 呐喊

SELECT b.title , a.name AS author , b.price
FROM books AS b
JOIN authors AS a ON b.author_id = a.id
ORDER BY b.id ;
#

UPDATE books SET stock = 4 
   WHERE title = '活着' ;
SELECT title , stock FROM books
WHERE title = '活着';
UPDATE books SET stock = stock - 1 
WHERE title = '活着' AND stock > 0 ;
SELECT title , stock FROM books 
WHERE title='活着' ;
;
#活着 stock = 4 

INSERT INTO books(title , author_id , price , stock , published_at)
VALUES('删除演示', (SELECT id FROM authors WHERE name='鲁迅'), 22.00, 6, '1926-08-01');

SELECT * FROM books;
DELETE FROM books
WHERE title = '删除演示';
SELECT * FROM books
#


