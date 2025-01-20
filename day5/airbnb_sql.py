import db_profile as db

# 문제 1
def addNewProduct():
    with db.connection.cursor() as cursor:
        sql = "INSERT INTO Products (productName, price, stockQuantity, createDate) VALUES(%s, %s, %s, %s)"
        values = ('Python Bood', 29.99, 10, db.dt.now())
        cursor.execute(sql, values)
        db.connection.commit()

    cursor.close()

# Products 목록을 조회합니다.
def showProducts():
    with db.connection.cursor() as cursor:
        cursor.execute("SELECT * FROM Products")

        for book in cursor.fetchall():
            print(book)
    cursor.close()

# 문제 2
# Customers 테이블에서 모든 고객의 정보를 조회합니다.
def showCustomers():
    with db.connection.cursor() as cursor:
        cursor.execute("SELECT * FROM Customers")
        
        for customer in cursor.fetchall():
            print(customer)

# 문제 3
# 제품이 주문될 때마다 Products 테이블 해당 제품의 재고 감소
def updateProductStock(productID, stockQuantity):
    with db.connection.cursor() as cursor:
        # 업데이트
        sql = f"UPDATE Products SET stockQuantity = stockQuantity - {stockQuantity} WHERE productID = {productID}"
        cursor.execute(sql)
        db.connection.commit()
    cursor.close()


# 문제 4
# 고객별 총 주문 금액 계산
def showTotalAmount():
    with db.connection.cursor() as cursor:
        sql = "SELECT customerID, SUM(totalAmount) AS totalAmount FROM Orders GROUP BY customerID"
        cursor.execute(sql)
        
        for totalAmount in cursor.fetchall():
            print(totalAmount)

# 문제 5
# 고객 이메일 업데이트
def updateCustomersEmail(customerID, email):
    with db.connection.cursor() as curser:
        sql = f"UPDATE Customers SET email = %s WHERE customerID = %s"
        values = (email, customerID)
        curser.execute(sql, values)
        db.connection.commit()
    curser.close()

# 문제 6
# 주문 취소
def deleteOrders(orderID):
    with db.connection.cursor() as cursor:
        sql = "DELETE FROM Orders WHERE orderID = %s"
        values = (orderID)
        cursor.execute(sql, values)
        db.connection.commit()
    cursor.close()

# 문제 7 특정 제품 검색
def searchProduct(productName):
    with db.connection.cursor() as cursor:
        sql = "SELECT * FROM Products WHERE productName LIKE %s"
        values = (f'%{productName}%')
        cursor.execute(sql, values)
        db.connection.commit()
        datas = cursor.fetchall()
        print(datas)
    cursor.close()

# 문제 8 특정 고객의 모든 주문 조회
def getCustomerOrders(customerID):
    with db.connection.cursor() as cursor:
        sql = "SELECT * FROM Orders WHERE customerID = %s"
        values = (customerID)
        cursor.execute(sql, values)
        datas = cursor.fetchall()
        print(datas)
    cursor.close()

# 문제 9 가장 많이 주문한 고객 찾기
def findTopCustomer():
    with db.connection.cursor() as cursor:
        sql = "SELECT customerID, count(*) AS amount FROM Orders GROUP BY customerID ORDER BY amount DESC LIMIT 1"
        cursor.execute(sql)
        datas = cursor.fetchall()
        print(datas)
    cursor.close()

# 새로운 제품 추가
addNewProduct()

# 고객 목록 조회
showProducts()
showCustomers()

# 제품 재고 업데이트
updateProductStock(1, 1)

# 고객별 총 주문 금액 계산
showTotalAmount()

# 고객 이메일 업데이트
updateCustomersEmail(1, "update3@example.net")

# 주문 취소
deleteOrders(15)

# 특정 제품 검색
searchProduct("p")

# 특정 고객의 모든 주문 조회
getCustomerOrders(1)

# 가장 많이 주문한 고객 찾기
findTopCustomer()