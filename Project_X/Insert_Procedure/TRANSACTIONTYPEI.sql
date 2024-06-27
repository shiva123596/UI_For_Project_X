CREATE PROCEDURE TRANSACTIONTYPEI
 @Name NVARCHAR(50)
,@RecordStatusID INT
AS
BEGIN
	IF NOT EXISTS(SELECT 1 FROM transactiontype WHERE NAME = @NAME)
	BEGIN
		INSERT INTO transactiontype (Name,RecordStatusID)
		VALUES (@Name,@RecordStatusID)
	END
END
 

 SELECT * FROM transactiontype

 EXEC dbo.TRANSACTIONTYPEI 'checkin', 1
 EXEC dbo.TRANSACTIONTYPEI 'checkout', 1
