-- -- @ block 
-- SHOW tables:

-- ALTER TABLE members DROP COLUMN Name;


-- -- @ block 
-- describe loans

-- ALTER TABLE members
-- ADD COLUMN FirstName VARCHAR(100) AFTER MemberID,,
-- ADD COLUMN LastName VARCHAR(100) AFTER FirstName;


DESCRIBE members;
-- UPDATE Books
-- SET Status = 'Available';
-- UPDATE Loans

-- SET DueDate = CURDATE() - INTERVAL 1 DAY
-- WHERE LoanID = 13 AND MemberID = 3 AND BookID = 2 AND BorrowDate = '2025-01-11';


-- select * from loans

-- select * from members
-- 
-- select * from books

-- DELETE FROM books
-- WHERE author = "JK";

