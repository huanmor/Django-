SELECT title , stock FROM books WHERE stock = 0 ;
# 球状闪电 0 ,白夜行 0 
#选择库存为0的书

SELECT id,title , price FROM books 
ORDER BY  price DESC, id ASC 
LIMIT 3;
#白夜行 , 解忧杂货店 , 球状闪电
#按降序选择最高的三本书,同价按序号升序排序

SELECT title , price FROM books
WHERE price BETWEEN 20 AND 40 
ORDER BY price DESC;
#活着 , 彷徨 , 三体 , 许三观卖血记 , 球状闪电 , 解忧杂货店 , 白夜行
#选择20-40的书输出 , 按照价格降序排序

SELECT b.title , a.id ,a.name AS author , b.price
FROM books AS b
JOIN authors AS a ON b.author_id = a.id
ORDER BY b.id ;
#关联books表和authors表,并按照authors表的作者id降序排列

UPDATE books SET stock = 4 
   WHERE title = '活着' ;#重置活着的库存,要不然多次运行后就变成0了
SELECT title , stock FROM books
WHERE title = '活着';
UPDATE books SET stock = stock - 1 
WHERE title = '活着' AND stock > 0 ;#保证库存大于0
SELECT title , stock FROM books 
WHERE title='活着' ;
;
#活着 stock = 4 
#活着 stock = 3 

INSERT INTO books(title , author_id , price , stock , published_at)
VALUES('删除演示', (SELECT id FROM authors WHERE name='鲁迅'), 22.00, 6, '1926-08-01');#添加书目

SELECT * FROM books;
DELETE FROM books
WHERE title = '删除演示';#删除书目
SELECT * FROM books#输出全books表
#


