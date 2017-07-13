# JOIN products, tsins and productlines
SELECT 	a.idTsin, a.idProduct, b.Active, c.idProductLine, d.idProduct
FROM tsin_products a
	JOIN tsins b ON a.idTsin = b.idTsin
    JOIN productlines c ON b.idProductLine = c.idProductLine
    JOIN voucher d ON d.idProduct = a.idProduct
    limit 10;
    
    WHERE a.idProduct = 

# INFORMATION_SCHEMA
SELECT COLUMN_NAME, TABLE_NAME 
FROM INFORMATION_SCHEMA.COLUMNS 
WHERE COLUMN_NAME LIKE '%voucher%';

SELECT COLUMN_NAME, TABLE_NAME 
FROM INFORMATION_SCHEMA.COLUMNS 
WHERE COLUMN_NAME LIKE 'voucher';


SELECT * from tsin_products limit 10;
SELECT * from tsins limit 10;
SELECT * from productlines limit 10;
SELECT * from products limit 10;
SELECT * from voucher limit 10;
SELECT * from vouchers limit 10;

SELECT 	b.idOrderItem, a.idorder, a.orderdate, a.shippingmethod, a.paymentmethod,
		a.delivernotbefore, a.delivernotafter, b.promiseddeliverydate, a.weekenddelivery,
		b.idproduct, b.unitprice, b.status, b.dateshipped,
		b.datedelivered, a.auth, a.authdate,a.risk,
		a.warehouse, a.minleadtime, a.maxleadtime, b.ordertype,
		b.shippingdays, b.preordered,
        c.fullFilled
FROM orders a
	JOIN orderitems b ON a.idOrder = b.idorder
    JOIN wms2_line_order_items c ON b.idOrderItem = c.idOrderItem
ORDER BY b.idOrderItem DESC;
