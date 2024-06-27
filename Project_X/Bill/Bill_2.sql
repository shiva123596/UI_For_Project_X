CREATE PROCEDURE Bill_2
    @Phone BIGINT,
    @TransactionID INT
AS
BEGIN
    SELECT  
        A.Farmer,
        A.PHONE,
        A.FarmerID,
        A.VILLAGE,
        UPPER(FORMAT(A.Transactiondate, 'dd-MMM-yyyy')) AS FROM_DATE,
        UPPER(FORMAT(GETDATE(), 'dd-MMM-yyyy')) AS TO_DATE,
        A.noofbags,
        (DATEDIFF(YEAR, A.Transactiondate, GETDATE()) / 1) + 1 AS YEARS,
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
            A.noofbags * (((DATEDIFF(YEAR, A.Transactiondate, GETDATE()) / 1) + 1) * 170), 
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
        (SELECT A2.noofbags - (SELECT SUM(A3.NoOfBags) 
                               FROM v_Transaction A3
                               WHERE A3.Phone = @Phone
                                 AND A3.TransactionStatus = 'Active' 
                                 AND A3.ParentTransactionID = @TransactionID)
         FROM v_Transaction A2 
         WHERE A2.Phone = @Phone
           AND A2.TransactionStatus = 'Active' 
           AND A2.TransactionID = @TransactionID
        ) AS BalanceBags
    FROM 
        v_Transaction A
    LEFT JOIN 
        loan C ON A.FarmerID = C.FarmerID
    WHERE 
        A.Phone = @Phone
        AND A.TransactionID IN (@TransactionID)
        AND A.TransactionStatus = 'Active';
END



--exec Bill_2 @phone = 8099892109, @TransactionID = 17 
