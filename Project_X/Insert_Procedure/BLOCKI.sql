CREATE PROCEDURE BLOCKI
 @Code CHAR(10)
,@RecordStatusID INT
AS
BEGIN
	IF NOT EXISTS(SELECT 1 FROM [Block] WHERE Code = @Code)
	BEGIN
		INSERT INTO [Block] (Code,RecordStatusID)
		VALUES (@Code,@RecordStatusID)
	END
END
 

 SELECT * FROM [Block]

 EXEC dbo.BLOCKI  'A',1
 EXEC dbo.BLOCKI  'B',1
 EXEC dbo.BLOCKI  'C',1
