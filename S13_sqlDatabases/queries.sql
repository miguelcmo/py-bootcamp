-- ============================================================================
-- CHINOOK DATABASE - SQL STEP-BY-STEP TUTORIAL
-- From Basic to Advanced Topics
-- ============================================================================
-- This tutorial uses the Chinook database which contains music store data
-- Tables include: Artist, Album, Track, Genre, Playlist, Customer, Invoice, 
-- Employee, and more.
-- 
-- To run this series of exercises you need to install DBCode extension
-- DBCode - Database Management developes by dbcode.io
-- ============================================================================


-- ============================================================================
-- SECTION 1: BASIC SQL QUERIES
-- ============================================================================

-- STEP 1: SELECT all data from a single table
-- Task: Get all artists in the database
SELECT * FROM Artist;

-- STEP 2: SELECT specific columns
-- Task: Get artist names only (not all columns)
SELECT Name FROM Artist;

-- STEP 3: LIMIT results to a specific number of rows
-- Task: Get only the first 10 artists
SELECT Name FROM Artist LIMIT 10;

-- STEP 4: DISTINCT - Remove duplicate values
-- Task: Get unique countries where customers are located
SELECT DISTINCT Country FROM Customer;

-- STEP 5: WHERE clause - Filter data by conditions
-- Task: Get all customers from USA
SELECT * FROM Customer WHERE Country = 'USA';

-- STEP 6: WHERE with AND condition
-- Task: Get all customers from USA in the state of CA
SELECT FirstName, LastName, City, State, Country 
FROM Customer 
WHERE Country = 'USA' AND State = 'CA';

-- STEP 7: WHERE with OR condition
-- Task: Get all customers from either USA or Canada
SELECT FirstName, LastName, Country 
FROM Customer 
WHERE Country = 'USA' OR Country = 'Canada';

-- STEP 8: WHERE with IN clause
-- Task: Get all customers from USA, Canada, or Mexico
SELECT FirstName, LastName, Country 
FROM Customer 
WHERE Country IN ('USA', 'Canada', 'Mexico');

-- STEP 9: WHERE with LIKE operator for text pattern matching
-- Task: Get all artists whose name contains 'The'
SELECT Name FROM Artist WHERE Name LIKE '%The%';

-- STEP 10: WHERE with comparison operators
-- Task: Get all tracks that cost more than $1.00
SELECT Name, UnitPrice 
FROM Track 
WHERE UnitPrice > 1.00 
ORDER BY UnitPrice DESC;


-- ============================================================================
-- SECTION 2: INTERMEDIATE SQL - ORDERING, AGGREGATION, GROUPING
-- ============================================================================

-- STEP 11: ORDER BY - Sort results in ascending order
-- Task: List all genres in alphabetical order
SELECT Name FROM Genre ORDER BY Name ASC;

-- STEP 12: ORDER BY - Sort in descending order
-- Task: Get customers sorted by last name in reverse order
SELECT FirstName, LastName 
FROM Customer 
ORDER BY LastName DESC;

-- STEP 13: ORDER BY multiple columns
-- Task: Sort customers by country first, then by city
SELECT FirstName, LastName, Country, City 
FROM Customer 
ORDER BY Country ASC, City ASC;

-- STEP 14: COUNT - Count total records
-- Task: Count how many customers are in the database
SELECT COUNT(*) AS TotalCustomers FROM Customer;

-- STEP 15: COUNT with WHERE clause
-- Task: Count how many customers are from USA
SELECT COUNT(*) AS USACustomers FROM Customer WHERE Country = 'USA';

-- STEP 16: SUM - Add up numeric values
-- Task: Get total revenue from all invoices
SELECT SUM(Total) AS TotalRevenue FROM Invoice;

-- STEP 17: AVG - Calculate average value
-- Task: What is the average track price?
SELECT AVG(UnitPrice) AS AverageTrackPrice FROM Track;

-- STEP 18: MIN and MAX - Find minimum and maximum values
-- Task: Find the cheapest and most expensive tracks
SELECT 
    MIN(UnitPrice) AS CheapestTrack,
    MAX(UnitPrice) AS MostExpensiveTrack
FROM Track;

-- STEP 19: GROUP BY - Aggregate data by category
-- Task: Count how many tracks are in each genre
SELECT Genre.Name, COUNT(Track.TrackId) AS TrackCount
FROM Track
JOIN Genre ON Track.GenreId = Genre.GenreId
GROUP BY Genre.Name
ORDER BY TrackCount DESC;

-- STEP 20: GROUP BY with multiple columns
-- Task: Count customers by country and state
SELECT Country, State, COUNT(*) AS CustomerCount
FROM Customer
WHERE Country = 'USA'
GROUP BY Country, State
ORDER BY CustomerCount DESC;

-- STEP 21: HAVING clause - Filter grouped results
-- Task: Find genres with more than 50 tracks
SELECT Genre.Name, COUNT(Track.TrackId) AS TrackCount
FROM Track
JOIN Genre ON Track.GenreId = Genre.GenreId
GROUP BY Genre.Name
HAVING COUNT(Track.TrackId) > 50
ORDER BY TrackCount DESC;

-- STEP 22: Multiple aggregate functions in one query
-- Task: Get summary statistics for each album
SELECT 
    Album.Title,
    Artist.Name,
    COUNT(Track.TrackId) AS NumberOfTracks,
    AVG(Track.UnitPrice) AS AveragePrice,
    SUM(Track.Milliseconds) AS TotalDuration
FROM Album
JOIN Artist ON Album.ArtistId = Artist.ArtistId
JOIN Track ON Album.AlbumId = Track.AlbumId
GROUP BY Album.AlbumId
ORDER BY NumberOfTracks DESC
LIMIT 20;


-- ============================================================================
-- SECTION 3: INTERMEDIATE SQL - JOINS
-- ============================================================================

-- STEP 23: INNER JOIN - Get matching records from both tables
-- Task: Get track names with their genre names
SELECT Track.Name, Genre.Name
FROM Track
INNER JOIN Genre ON Track.GenreId = Genre.GenreId
LIMIT 20;

-- STEP 24: INNER JOIN with multiple tables
-- Task: Get track name, album title, and artist name together
SELECT 
    Track.Name AS TrackName,
    Album.Title AS AlbumTitle,
    Artist.Name AS ArtistName,
    Genre.Name AS Genre
FROM Track
INNER JOIN Album ON Track.AlbumId = Album.AlbumId
INNER JOIN Artist ON Album.ArtistId = Artist.ArtistId
INNER JOIN Genre ON Track.GenreId = Genre.GenreId
LIMIT 20;

-- STEP 25: LEFT JOIN - Include all records from left table
-- Task: List all albums and their track count (including albums with no tracks)
SELECT 
    Album.Title,
    Artist.Name,
    COUNT(Track.TrackId) AS TrackCount
FROM Album
LEFT JOIN Track ON Album.AlbumId = Track.AlbumId
LEFT JOIN Artist ON Album.ArtistId = Artist.ArtistId
GROUP BY Album.AlbumId
LIMIT 20;

-- STEP 26: RIGHT JOIN (simulated with LEFT JOIN)
-- Task: Get all genres with their track count
SELECT 
    Genre.Name,
    COUNT(Track.TrackId) AS TrackCount
FROM Genre
LEFT JOIN Track ON Genre.GenreId = Track.GenreId
GROUP BY Genre.GenreId
ORDER BY TrackCount DESC;

-- STEP 27: JOIN with WHERE clause for filtering
-- Task: Get all rock and pop tracks priced under $1.50
SELECT 
    Track.Name,
    Genre.Name,
    Track.UnitPrice
FROM Track
INNER JOIN Genre ON Track.GenreId = Genre.GenreId
WHERE Genre.Name IN ('Rock', 'Pop') AND Track.UnitPrice < 1.50
ORDER BY Track.UnitPrice DESC;

-- STEP 28: Multiple JOINs with aggregation
-- Task: Show customers and their total spending
SELECT 
    Customer.FirstName,
    Customer.LastName,
    Customer.Country,
    COUNT(Invoice.InvoiceId) AS NumberOfInvoices,
    SUM(Invoice.Total) AS TotalSpending
FROM Customer
LEFT JOIN Invoice ON Customer.CustomerId = Invoice.CustomerId
GROUP BY Customer.CustomerId
ORDER BY TotalSpending DESC
LIMIT 20;


-- ============================================================================
-- SECTION 4: ADVANCED SQL - SUBQUERIES
-- ============================================================================

-- STEP 29: Subquery in WHERE clause
-- Task: Find tracks that cost more than the average track price
SELECT Name, UnitPrice
FROM Track
WHERE UnitPrice > (SELECT AVG(UnitPrice) FROM Track)
ORDER BY UnitPrice DESC;

-- STEP 30: Subquery with IN operator
-- Task: Find customers who have made purchases over $50
SELECT FirstName, LastName, Email
FROM Customer
WHERE CustomerId IN (
    SELECT CustomerId 
    FROM Invoice 
    WHERE Total > 50
)
ORDER BY LastName;

-- STEP 31: Subquery with NOT IN operator
-- Task: Find genres that have NO tracks in any playlist
SELECT Name 
FROM Genre 
WHERE GenreId NOT IN (
    SELECT DISTINCT Genre.GenreId
    FROM Track
    JOIN PlaylistTrack ON Track.TrackId = PlaylistTrack.TrackId
    JOIN Playlist ON PlaylistTrack.PlaylistId = Playlist.PlaylistId
    JOIN Genre ON Track.GenreId = Genre.GenreId
);

-- STEP 32: Correlated subquery
-- Task: Find albums with more tracks than the average
SELECT 
    Album.Title,
    Artist.Name,
    (SELECT COUNT(*) FROM Track WHERE Track.AlbumId = Album.AlbumId) AS TrackCount
FROM Album
JOIN Artist ON Album.ArtistId = Artist.ArtistId
WHERE (SELECT COUNT(*) FROM Track WHERE Track.AlbumId = Album.AlbumId) > 
    (SELECT AVG(TrackCount) FROM (
        SELECT COUNT(*) AS TrackCount FROM Track GROUP BY AlbumId
    ))
LIMIT 20;

-- STEP 33: Subquery in FROM clause (derived table)
-- Task: Get the average revenue per customer per country
SELECT 
    Country,
    AVG(CustomerRevenue) AS AvgRevenuePerCustomer,
    COUNT(*) AS NumberOfCustomers
FROM (
    SELECT 
        Customer.Country,
        Customer.CustomerId,
        SUM(Invoice.Total) AS CustomerRevenue
    FROM Customer
    LEFT JOIN Invoice ON Customer.CustomerId = Invoice.CustomerId
    GROUP BY Customer.CustomerId
)
GROUP BY Country
ORDER BY AvgRevenuePerCustomer DESC;

-- STEP 34: Subquery with CASE statement
-- Task: Classify customers by spending level
SELECT 
    FirstName,
    LastName,
    COALESCE(SUM(Invoice.Total), 0) AS TotalSpent,
    CASE 
        WHEN COALESCE(SUM(Invoice.Total), 0) > 50 THEN 'High Spender'
        WHEN COALESCE(SUM(Invoice.Total), 0) > 20 THEN 'Medium Spender'
        ELSE 'Low Spender'
    END AS SpendingLevel
FROM Customer
LEFT JOIN Invoice ON Customer.CustomerId = Invoice.CustomerId
GROUP BY Customer.CustomerId
ORDER BY TotalSpent DESC;


-- ============================================================================
-- SECTION 5: ADVANCED SQL - WINDOW FUNCTIONS & COMMON TABLE EXPRESSIONS
-- ============================================================================

-- STEP 35: ROW_NUMBER window function
-- Task: Rank customers by their total spending
SELECT 
    FirstName,
    LastName,
    TotalSpent,
    ROW_NUMBER() OVER (ORDER BY TotalSpent DESC) AS RankBySpending
FROM (
    SELECT 
        Customer.FirstName,
        Customer.LastName,
        COALESCE(SUM(Invoice.Total), 0) AS TotalSpent
    FROM Customer
    LEFT JOIN Invoice ON Customer.CustomerId = Invoice.CustomerId
    GROUP BY Customer.CustomerId
)
LIMIT 20;

-- STEP 36: RANK window function
-- Task: Get rank of tracks by price within each genre
SELECT 
    Genre,
    TrackName,
    UnitPrice,
    RANK() OVER (PARTITION BY Genre ORDER BY UnitPrice DESC) AS PriceRank
FROM (
    SELECT 
        Genre.Name AS Genre,
        Track.Name AS TrackName,
        Track.UnitPrice
    FROM Track
    JOIN Genre ON Track.GenreId = Genre.GenreId
)
WHERE PriceRank <= 5
ORDER BY Genre, PriceRank;

-- STEP 37: SUM window function (running total)
-- Task: Show invoice total with running sum for each customer
SELECT 
    Customer.FirstName,
    Customer.LastName,
    Invoice.InvoiceDate,
    Invoice.Total,
    SUM(Invoice.Total) OVER (
        PARTITION BY Customer.CustomerId 
        ORDER BY Invoice.InvoiceDate
    ) AS RunningTotal
FROM Customer
JOIN Invoice ON Customer.CustomerId = Invoice.CustomerId
LIMIT 30;

-- STEP 38: COMMON TABLE EXPRESSION (CTE) - WITH clause
-- Task: Get top 5 genres by track count, then show details
WITH GenreStats AS (
    SELECT 
        Genre.GenreId,
        Genre.Name,
        COUNT(Track.TrackId) AS TrackCount
    FROM Genre
    LEFT JOIN Track ON Genre.GenreId = Track.GenreId
    GROUP BY Genre.GenreId
    ORDER BY TrackCount DESC
    LIMIT 5
)
SELECT 
    GenreStats.Name,
    GenreStats.TrackCount,
    COUNT(PlaylistTrack.TrackId) AS TracksInPlaylists
FROM GenreStats
LEFT JOIN Track ON GenreStats.GenreId = Track.GenreId
LEFT JOIN PlaylistTrack ON Track.TrackId = PlaylistTrack.TrackId
GROUP BY GenreStats.GenreId
ORDER BY GenreStats.TrackCount DESC;

-- STEP 39: Multiple CTEs
-- Task: Find customers who spent more than average and their invoice count
WITH CustomerSpending AS (
    SELECT 
        Customer.CustomerId,
        Customer.FirstName,
        Customer.LastName,
        COALESCE(SUM(Invoice.Total), 0) AS TotalSpent
    FROM Customer
    LEFT JOIN Invoice ON Customer.CustomerId = Invoice.CustomerId
    GROUP BY Customer.CustomerId
),
AverageSpending AS (
    SELECT AVG(TotalSpent) AS AvgSpent FROM CustomerSpending
),
HighSpenders AS (
    SELECT 
        CustomerSpending.CustomerId,
        CustomerSpending.FirstName,
        CustomerSpending.LastName,
        CustomerSpending.TotalSpent
    FROM CustomerSpending
    WHERE CustomerSpending.TotalSpent > (SELECT AvgSpent FROM AverageSpending)
)
SELECT 
    HighSpenders.FirstName,
    HighSpenders.LastName,
    HighSpenders.TotalSpent,
    COUNT(Invoice.InvoiceId) AS InvoiceCount
FROM HighSpenders
LEFT JOIN Invoice ON HighSpenders.CustomerId = Invoice.CustomerId
GROUP BY HighSpenders.CustomerId
ORDER BY HighSpenders.TotalSpent DESC;


-- ============================================================================
-- SECTION 6: ADVANCED SQL - COMPLEX QUERIES
-- ============================================================================

-- STEP 40: UNION - Combine results from multiple queries
-- Task: Get a list of all names (artists, employees, customers)
SELECT 'Artist' AS Type, Name FROM Artist
UNION
SELECT 'Employee', FirstName || ' ' || LastName FROM Employee
UNION
SELECT 'Customer', FirstName || ' ' || LastName FROM Customer
ORDER BY Type, Name;

-- STEP 41: CASE statement for conditional logic
-- Task: Categorize tracks by duration
SELECT 
    Name,
    Milliseconds,
    CASE 
        WHEN Milliseconds < 180000 THEN 'Short (< 3 min)'
        WHEN Milliseconds < 300000 THEN 'Medium (3-5 min)'
        WHEN Milliseconds < 600000 THEN 'Long (5-10 min)'
        ELSE 'Very Long (> 10 min)'
    END AS DurationCategory
FROM Track
ORDER BY Milliseconds DESC
LIMIT 30;

-- STEP 42: Complex query with multiple conditions
-- Task: Find top customers in each country with their top genre preference
WITH CustomerInvoices AS (
    SELECT 
        Customer.CustomerId,
        Customer.FirstName,
        Customer.LastName,
        Customer.Country,
        SUM(Invoice.Total) AS TotalSpent
    FROM Customer
    LEFT JOIN Invoice ON Customer.CustomerId = Invoice.CustomerId
    GROUP BY Customer.CustomerId
),
TopCustomersPerCountry AS (
    SELECT 
        CustomerId,
        FirstName,
        LastName,
        Country,
        TotalSpent,
        ROW_NUMBER() OVER (PARTITION BY Country ORDER BY TotalSpent DESC) AS Rank
    FROM CustomerInvoices
    WHERE TotalSpent > 0
)
SELECT 
    Country,
    FirstName,
    LastName,
    TotalSpent,
    Rank
FROM TopCustomersPerCountry
WHERE Rank <= 3
ORDER BY Country, Rank;

-- STEP 43: Recursive query simulation - Employee hierarchy
-- Task: Show employee reporting structure
SELECT 
    Employee.EmployeeId,
    Employee.FirstName || ' ' || Employee.LastName AS EmployeeName,
    Employee.Title,
    COALESCE(Manager.FirstName || ' ' || Manager.LastName, 'No Manager') AS ManagerName
FROM Employee
LEFT JOIN Employee Manager ON Employee.ReportsTo = Manager.EmployeeId
ORDER BY Employee.ReportsTo, Employee.FirstName;

-- STEP 44: STRING functions and manipulation
-- Task: Format customer contact information
SELECT 
    UPPER(FirstName) || ' ' || UPPER(LastName) AS FullName,
    LOWER(Email) AS EmailLower,
    LENGTH(FirstName) AS FirstNameLength,
    SUBSTR(Phone, 1, 3) AS AreaCode,
    Country
FROM Customer
LIMIT 20;

-- STEP 45: Date functions
-- Task: Analyze invoices by month
SELECT 
    STRFTIME('%Y-%m', InvoiceDate) AS Month,
    COUNT(*) AS InvoiceCount,
    SUM(Total) AS MonthlyRevenue,
    AVG(Total) AS AverageInvoiceAmount
FROM Invoice
GROUP BY STRFTIME('%Y-%m', InvoiceDate)
ORDER BY Month DESC;

-- STEP 46: Complex aggregation with multiple grouping levels
-- Task: Sales analysis by artist and genre
SELECT 
    Artist.Name AS ArtistName,
    Genre.Name AS GenreName,
    COUNT(DISTINCT Track.TrackId) AS NumberOfTracks,
    COUNT(DISTINCT InvoiceLine.InvoiceId) AS NumberOfSales,
    SUM(InvoiceLine.Quantity) AS TotalQuantitySold,
    ROUND(SUM(InvoiceLine.Quantity * InvoiceLine.UnitPrice), 2) AS TotalRevenue
FROM Artist
INNER JOIN Album ON Artist.ArtistId = Album.ArtistId
INNER JOIN Track ON Album.AlbumId = Track.AlbumId
INNER JOIN Genre ON Track.GenreId = Genre.GenreId
INNER JOIN InvoiceLine ON Track.TrackId = InvoiceLine.TrackId
GROUP BY Artist.ArtistId, Genre.GenreId
ORDER BY TotalRevenue DESC
LIMIT 30;

-- STEP 47: Self-join to find relationships
-- Task: Find employees in the same city
SELECT 
    E1.FirstName || ' ' || E1.LastName AS Employee1,
    E2.FirstName || ' ' || E2.LastName AS Employee2,
    E1.City
FROM Employee E1
INNER JOIN Employee E2 ON E1.City = E2.City AND E1.EmployeeId < E2.EmployeeId
ORDER BY E1.City, E1.FirstName;

-- STEP 48: Cross join with filtering
-- Task: Find all possible combinations of genres and media types
SELECT 
    Genre.Name AS Genre,
    MediaType.Name AS MediaType,
    COUNT(Track.TrackId) AS TrackCount
FROM Genre
CROSS JOIN MediaType
LEFT JOIN Track ON Genre.GenreId = Track.GenreId 
    AND MediaType.MediaTypeId = Track.MediaTypeId
GROUP BY Genre.GenreId, MediaType.MediaTypeId
HAVING TrackCount > 0
ORDER BY TrackCount DESC;

-- STEP 49: NULL handling functions
-- Task: Clean up customer data with null values
SELECT 
    FirstName,
    LastName,
    COALESCE(Company, 'Individual') AS Company,
    COALESCE(State, 'N/A') AS State,
    IFNULL(Phone, 'No Phone') AS Phone,
    Country
FROM Customer
ORDER BY Country, LastName;

-- STEP 50: Complete business intelligence query
-- Task: Comprehensive sales dashboard for top performing artists
WITH ArtistSales AS (
    SELECT 
        Artist.ArtistId,
        Artist.Name AS ArtistName,
        COUNT(DISTINCT Album.AlbumId) AS TotalAlbums,
        COUNT(DISTINCT Track.TrackId) AS TotalTracks,
        COUNT(DISTINCT InvoiceLine.InvoiceId) AS UniqueCustomers,
        SUM(InvoiceLine.Quantity) AS TotalUnitsSold,
        ROUND(SUM(InvoiceLine.Quantity * InvoiceLine.UnitPrice), 2) AS TotalRevenue,
        ROUND(AVG(InvoiceLine.UnitPrice), 2) AS AveragePricePerTrack,
        MAX(Invoice.InvoiceDate) AS LastSaleDate
    FROM Artist
    LEFT JOIN Album ON Artist.ArtistId = Album.ArtistId
    LEFT JOIN Track ON Album.AlbumId = Track.AlbumId
    LEFT JOIN InvoiceLine ON Track.TrackId = InvoiceLine.TrackId
    LEFT JOIN Invoice ON InvoiceLine.InvoiceId = Invoice.InvoiceId
    GROUP BY Artist.ArtistId
)
SELECT 
    ROW_NUMBER() OVER (ORDER BY TotalRevenue DESC) AS Rank,
    ArtistName,
    TotalAlbums,
    TotalTracks,
    UniqueCustomers,
    TotalUnitsSold,
    TotalRevenue,
    AveragePricePerTrack,
    LastSaleDate
FROM ArtistSales
WHERE TotalRevenue > 0
ORDER BY TotalRevenue DESC
LIMIT 20;


-- ============================================================================
-- SECTION 7: PERFORMANCE OPTIMIZATION & BEST PRACTICES
-- ============================================================================

-- STEP 51: Index usage example (informational)
-- Task: Query that would benefit from indexes
-- Indexes typically exist on Primary Keys and Foreign Keys
-- This query demonstrates efficient use of indexed columns
SELECT 
    Customer.CustomerId,
    Customer.LastName,
    COUNT(Invoice.InvoiceId) AS PurchaseCount,
    SUM(Invoice.Total) AS TotalAmount
FROM Customer
WHERE Customer.Country = 'USA'  -- Filtered on indexed column
AND CustomerId IN (
    SELECT CustomerId FROM Invoice WHERE InvoiceDate > '2010-01-01'
)
GROUP BY Customer.CustomerId
ORDER BY TotalAmount DESC;

-- STEP 52: Query efficiency - Using EXISTS vs IN
-- Task: Find genres that have at least one track in a playlist
-- EXISTS is often more efficient than IN for large datasets
SELECT DISTINCT Genre.Name
FROM Genre
WHERE EXISTS (
    SELECT 1
    FROM Track
    WHERE Track.GenreId = Genre.GenreId
    AND EXISTS (
        SELECT 1
        FROM PlaylistTrack
        WHERE PlaylistTrack.TrackId = Track.TrackId
    )
)
ORDER BY Genre.Name;

-- ============================================================================
-- END OF TUTORIAL
-- ============================================================================
-- This tutorial covered:
-- BASIC: SELECT, WHERE, LIMIT, DISTINCT, LIKE, Comparison operators
-- INTERMEDIATE: ORDER BY, COUNT, SUM, AVG, MIN, MAX, GROUP BY, HAVING
--               JOINS (INNER, LEFT), multiple JOINs with aggregation
-- ADVANCED: Subqueries, Window Functions (ROW_NUMBER, RANK, SUM OVER)
--           CTEs (Common Table Expressions), UNION, CASE statements
--           Complex aggregations, String/Date functions, Self-joins
-- 
-- Practice each step individually and modify the queries to explore different
-- combinations and understand how different SQL concepts work together!
-- ============================================================================
