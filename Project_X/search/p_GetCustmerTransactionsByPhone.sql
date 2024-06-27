CREATE PROC p_GetCustmerTransactionsByPhone
@Phone BIGINT 
AS
BEGIN
/*
 EXEC p_GetCustmerTransactionsByPhone  @Phone = '8099892109' 
*/
	SELECT 
	 Farmer
    ,Village
    ,Phone
    ,NoOfBags
    ,TransactionID
    ,Description
    ,TransactionTypeID
    ,TransactionType
    ,ItemID
    ,Item
    ,VarietyID
    ,Variety
    ,KanaBlockKey
    ,TransactionStatus
FROM v_Transaction
	WHERE Phone = @Phone
END