
CREATE PROCEDURE TransactionI
 @FirstName VARCHAR(225)
,@Phone BIGINT
,@NoOfBags INT
,@Description NVARCHAR(4000) = NULL
,@TransactionTypeID INT
,@ItemID INT
,@VarietyID INT
,@KanaBlockMapID INT
as
Begin
declare
 @FarmerID INT
,@RecordStatusID INT

SELECT @FarmerID = A.FarmerID
,@RecordStatusID = 1 FROM Farmer A
 join RecordStatus G on G.RecordStatusID = A.RecordStatusID
 WHERE A.FirstName  = @FirstName or A.Phone = @Phone
 INSERT INTO [Transaction] ( FarmerID
                            ,RecordStatusID
                            ,TransactionTypeID
    					    ,ItemID
						    ,VarietyID
						    ,KanaBlockMapID
						    ,NoOfBags
						    ,Description)
               
			     VALUES (    @FarmerID
				            ,@RecordStatusID
				            ,@TransactionTypeID
    					    ,@ItemID
						    ,@VarietyID
						    ,@KanaBlockMapID
						    ,@NoOfBags
						    ,@Description)
END




--EXEC dbo.TransactionI   @FirstName             = 'RAMA'
--                       ,@Phone 				   = 9879992109

					   	   
--                     ,@TransactionTypeID	   = 2
--					   ,@ItemID				   = 8
--					   ,@VarietyID			   = 1
--					   ,@KanaBlockMapID		   = 3
--					   ,@NoOfBags			   = 84