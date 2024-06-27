CREATE PROCEDURE VarietyI
 @ItemID int
,@Name nvarchar(100)
,@Description nvarchar(4000)
,@Code NCHAR(10)
,@RecordStatusID INT
AS
BEGIN
	IF NOT EXISTS(SELECT 1 FROM Variety WHERE Code = @Code)
	BEGIN
		INSERT INTO Variety (ItemID,Name,Description,Code,RecordStatusID)
		VALUES (@ItemID,@Name,@Description,@Code,@RecordStatusID)
	END
END
 

 SELECT * FROM [Variety]

 EXEC dbo.VarietyI  8,'Teja','fire','TJ001',1
 EXEC dbo.VarietyI  8,'22','','22002',1
 EXEC dbo.VarietyI  8,'Nallurisannalu','','NAL001',1
 EXEC dbo.VarietyI  8,'talu kayalu','','TLU000',1
 EXEC dbo.VarietyI  8,'delux','','DLX',1
 EXEC dbo.VarietyI  13,'popcorn','','PoP001',1
 EXEC dbo.VarietyI  14,'Black','','Bk001',1
 EXEC dbo.VarietyI  9,'Black','','SA003',1
 EXEC dbo.VarietyI  9,'White','','SA004',1

 delete from variety  

 dbcc checkident ('variety',reseed,0)