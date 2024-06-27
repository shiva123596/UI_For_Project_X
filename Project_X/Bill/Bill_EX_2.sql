CREATE PROCEDURE Bill_EX_2
    @Phone BIGINT,
    @TransactionIDs NVARCHAR(MAX) = NULL
AS
BEGIN
    -- Use the split function to create a table of transaction IDs
    DECLARE @TransactionIDTable TABLE (TransactionID INT)

    IF @TransactionIDs IS NOT NULL
    BEGIN
        INSERT INTO @TransactionIDTable (TransactionID)
        SELECT CAST(Value AS INT)
        FROM dbo.SplitString(@TransactionIDs, ',')
    END

    -- The main query
    SELECT  
        A.Farmer,
        A.PHONE,
        A.FarmerID,
        A.VILLAGE,
        UPPER(FORMAT(
            COALESCE((SELECT Transactiondate 
                      FROM v_Transaction 
                      WHERE TransactionID = A.ParentTransactionID), A.Transactiondate),
            'dd-MMM-yyyy'
        )) AS FROM_DATE,
        UPPER(FORMAT(GETDATE(), 'dd-MMM-yyyy')) AS TO_DATE,
        A.noofbags,
        (DATEDIFF(YEAR, 
                  COALESCE((SELECT Transactiondate 
                            FROM v_Transaction 
                            WHERE TransactionID = A.ParentTransactionID), A.Transactiondate), 
                  GETDATE()) / 1) + 1 AS YEARS,
        FORMAT(
            (SELECT TOP 1 C.AmountSanctioned 
             FROM loan C 
             WHERE C.RecordStatusID = 1 
             AND C.FarmerID = A.FarmerID), 
            'C0', 
            'HI-in'
        ) AS LOAN,
        C.BondNumber,
        FORMAT(
            A.noofbags * (((DATEDIFF(YEAR, 
                                     COALESCE((SELECT Transactiondate 
                                               FROM v_Transaction 
                                               WHERE TransactionID = A.ParentTransactionID), A.Transactiondate), 
                                     GETDATE()) / 1) + 1) * 170), 
            'C0', 
            'HI-in'
        ) AS REAL_RENT,
        FORMAT(
            (SELECT SUM(A2.noofbags * (((DATEDIFF(YEAR, A2.Transactiondate, GETDATE()) / 1) + 1) * 170))
             FROM v_Transaction A2 
             WHERE A2.Phone = @Phone
               AND A2.TransactionStatus = 'Active'),
            'C0', 
            'HI-in'
        ) AS TOTAL_RENT,
        A.ParentTransactionID,
        A.TransactionID,
        ISNULL(
            (SELECT A2.noofbags - COALESCE((
                SELECT SUM(A3.NoOfBags) 
                FROM v_Transaction A3
                WHERE A3.Phone = @Phone
                  AND A3.TransactionStatus = 'Active' 
                  AND A3.ParentTransactionID = A.TransactionID
            ), 0)
            FROM v_Transaction A2 
            WHERE A2.Phone = @Phone
              AND A2.TransactionStatus = 'Active' 
              AND A2.TransactionID = A.TransactionID
            ), A.noofbags) AS BalanceBags
    FROM 
        v_Transaction A
    LEFT JOIN 
        loan C ON A.FarmerID = C.FarmerID
    WHERE 
        A.Phone = @Phone
        AND (A.TransactionID IN (SELECT TransactionID FROM @TransactionIDTable) OR @TransactionIDs IS NULL)
        AND A.TransactionStatus = 'Active';
END;




--exec Bill_EX_2 @Phone = 8099892109, @TransactionIDs = '17';

--select * from RecordStatus

--select * from farmer

--select * from v_Transaction