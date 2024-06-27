drop VIEW v_Transaction 

CREATE VIEW v_Transaction AS 
SELECT	
	F.FirstName+' '+F.LastName Farmer
	,F.FarmerID
	,F.Village
	,F.Phone
	,T.NoOfBags
	,T.TransactionID
	,T.ParentTransactionID
	,T.Description
	,TT.TransactionTypeID
	,TT.Name AS TransactionType
	,I.ItemID
	,I.Name AS Item
	,V.VarietyID
	,V.Name AS Variety 
	,E.KanaBlockKey
	,R.Name AS TransactionStatus
	,T.CreatedDate as TransactionDate
FROM [Transaction] T
JOIN Farmer F ON T.FarmerID = F.FarmerID
JOIN Item I ON I.ItemID = T.ItemID
JOIN Variety V ON V.VarietyID = T.VarietyID
join v_FloorKanaBlock E ON T.KanaBlockMapID = E.KanaBlockMapID
JOIN RecordStatus R ON R.RecordStatusID = T.RecordStatusID
JOIN TransactionType TT ON TT.TransactionTypeID = T.TransactionTypeID