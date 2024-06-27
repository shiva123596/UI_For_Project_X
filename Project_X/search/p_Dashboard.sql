
DROP PROCEDURE p_Dashboard
GO
CREATE PROCEDURE p_Dashboard
    @Phone BIGINT
AS
BEGIN
    /*
    EXEC p_Dashboard  @Phone = '8099892109' 
    */
    SELECT TOP(1)
        Farmer,
        Phone,
        (SELECT SUM(CASE WHEN TransactionTypeID = '1' THEN NoOfBags ELSE -NoOfBags END) 
         FROM v_Transaction WHERE Phone = @Phone) AS TotalBagsIn, -- Added alias and corrected parentheses
        Item,
        (DATEDIFF(YEAR, TransactionDATE, GETDATE()) / 1) + 1 AS [YEAR'S], -- Removed unneeded parentheses
        FORMAT((SELECT C.AmountSanctioned 
                FROM loan 
                WHERE C.RecordStatusID = 1 
                AND Farmerid = (SELECT TOP 1 FarmerID 
                                FROM v_Transaction 
                                WHERE Phone = @Phone AND TransactionTypeid = 1)
               ), 'C0', 'HI-in') AS LOAN, -- Added alias
        FORMAT((SELECT SUM(CASE WHEN TransactionTypeID = '1' THEN NoOfBags ELSE -NoOfBags END) 
                FROM v_Transaction 
                WHERE TransactionStatus = 'Active' 
                AND Phone = @Phone)
               * (((DATEDIFF(YEAR, Transactiondate, GETDATE()) / 1) + 1) * 170), 'C0', 'HI-in') AS REAL_RENT, -- Added alias
        FORMAT((SELECT SUM(CASE WHEN TransactionTypeID = '1' THEN NoOfBags ELSE -NoOfBags END) * 9000 
                FROM v_Transaction 
                WHERE TransactionStatus = 'Active' 
                AND Phone = @Phone), 'C0', 'HI-in') AS asset_value,a.FarmerID
    FROM 
        v_Transaction A
    LEFT JOIN 
        LOAN C ON A.FARMERID = C.FARMERID
    WHERE 
        Phone = @Phone;
END



--EXEC p_Dashboard  @Phone = '8886018104' 

--EXEC p_Dashboard  @Phone = '8099892109' 
