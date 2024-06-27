
DROP PROCEDURE p_GetCustmerByPhone
GO
CREATE PROCEDURE p_GetCustmerByPhone
    @Phone BIGINT
AS
BEGIN
    /*
    EXEC p_GetCustmerByPhone  @Phone = '8099892109' 
    */
    SELECT top(1)
        Farmer,
        Village,
        Phone,
        (SELECT SUM(CASE WHEN TransactionTypeID = '1' THEN NoOfBags ELSE -NoOfBags END) 
         FROM v_Transaction 
         WHERE Phone = @Phone) AS TotalBagsIn, -- Added missing closing parenthesis and removed unnecessary SUM
        Item,
        UPPER(FORMAT(Transactiondate, 'dd-MMM-yyyy')) AS FROM_DATE, -- Added alias for FROM_DATE
        UPPER(FORMAT(GETDATE(), 'dd-MMM-yyyy')) AS TO_DATE, -- Added alias for TO_DATE
        (DATEDIFF(YEAR, TransactionDATE, GETDATE()) / 1) + 1 AS YEARS, -- Corrected column name spelling
        FORMAT((SELECT C.AmountSanctioned 
                FROM loan C -- Added alias C
                WHERE C.RecordStatusID = 1 
                AND Farmerid = (SELECT TOP 1 FarmerID 
                                FROM v_Transaction 
                                WHERE Phone = @Phone AND TransactionTypeid = 1)
               ), 'C0', 'HI-in') AS LOAN,
        C.BondNumber,
        FORMAT((SELECT SUM(CASE WHEN TransactionTypeID = '1' THEN NoOfBags ELSE -NoOfBags END)
                FROM v_Transaction 
                WHERE TransactionStatus = 'Active' 
                AND Phone = @Phone)
               * (((DATEDIFF(YEAR, Transactiondate, GETDATE()) / 1) + 1) * 170), 'C0', 'HI-in') AS REAL_RENT
    FROM 
        v_Transaction A
    LEFT JOIN 
        LOAN C ON A.FARMERID = C.FARMERID
    WHERE 
        Phone = @Phone;
END


EXEC p_GetCustmerByPhone  @Phone = '8099892109' 
