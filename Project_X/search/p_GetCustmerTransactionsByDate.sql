create procedure p_GetCustmerTransactionsByDate
 @FromDate DATETIME
,@ToDate DATETIME
as
begin
SELECT * FROM v_Transaction
where TransactionDate >= @FromDate and TransactionDate <= @ToDate
end

EXEC p_GetCustmerTransactionsByDate      @FromDate = '2020-07-22 17:44:22.527'
                                        ,@ToDate   = '2020-07-30 17:44:22.527'
