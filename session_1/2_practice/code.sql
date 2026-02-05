-- Enable readable output format
.mode columns
.headers on

-- Instructions for students:
-- 1. Open SQLite in terminal: sqlite3 library.db
-- 2. Load this script: .read code.sql
-- 3. Exit SQLite: .exit


-- write your sql code here
--1 select Books.title, Members.name, Loans.loan_date from Loans join Books on Loans.book_id = Books.id, Members on Loans.member_id = Members.id;
--2 select Books.title, Loans.loan_date from Loans left join Books on Books.id = Loans.book_id;
--3 select name, Books.title from LibraryBranch join Books on LibraryBranch.id = Books.branch_id;
--4 select name, count(Books.id) as Num_of_books from LibraryBranch join Books on LibraryBranch.id = Books.branch_id group by name;
--5 select name, count(Books.id) as Num_of_books from LibraryBranch join Books on LibraryBranch.id = Books.branch_id group by name having Num_of_books>7;
--6 select name, count(Loans.id) as num_of_loans from Members join Loans on Members.id = Loans.member_id group by name;
--7 select name, count(Loans.id) as num_of_loans from Members Left join Loans on Members.id = Loans.member_id group by name having num_of_loans=0;
--8 select LibraryBranch.name, Books.title, count(Loans.id) from Books join LibraryBranch on Books.branch_id = LibraryBranch.id, Loans on Books.id = Loans.book_id group by Books.title;
--9
select Members.name, Loans.loan_date
from Members left join Loans on Members.id = Loans.member_id
group by Members.name 
having Loans.return_date > date('now')
-- not sure about 9