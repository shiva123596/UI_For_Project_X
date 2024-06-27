SELECT * FROM [TRANSACTION]

Create Procedure TransactionUpdate
 @FarmerID int
,@TransactionID int null
,@Description nvarchar(4000) NULL
,@ItemID int NULL
,@VarietyID int NULL
,@NoOfBags int NULL
,@KanaBlockMapID int NULL
AS
BEGIN
	IF  EXISTS(SELECT RecordStatusID FROM [TRANSACTION] WHERE FarmerID = @FarmerID and RecordStatusID = 1 and TransactionID = @TransactionID)
	BEGIN
update [transaction] 
set NoOfBags = ISNULL(@NoOfBags,NoOfBags)
   ,KanaBlockMapID = ISNULL(@KanaBlockMapID,KanaBlockMapID)
   ,[Description] = ISNULL(@Description,[Description])
   ,ItemID = ISNULL(@ItemID,ItemID)
   ,VarietyID = ISNULL(@VarietyID,VarietyID)
where FarmerID = @FarmerID and TransactionID = @TransactionID
  END
END


 EXEC TransactionUpdate @FarmerID = 2
                       ,@TransactionID = 7
                      
                       ,@Description = NULL
                       ,@ItemID = NULL
                       ,@VarietyID = NULL
                       ,@NoOfBags = 48
                       ,@KanaBlockMapID = null

