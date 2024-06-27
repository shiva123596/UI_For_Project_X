CREATE PROCEDURE ItemI
 @Name nvarchar(100)
,@Description nvarchar(4000)
,@Code CHAR(10)
,@RecordStatusID INT
AS
BEGIN
	IF NOT EXISTS(SELECT 1 FROM Item WHERE Code = @Code)
	BEGIN
		INSERT INTO Item (Name,Description,Code,RecordStatusID)
		VALUES (@Name,@Description,@Code,@RecordStatusID)
	END
END
 

 SELECT * FROM [Item]

 EXEC dbo.ItemI  'Mirchi','delux kaya','Mi001',1
 EXEC dbo.ItemI  'Sanagalu','vast','Sa002',1
 EXEC dbo.ItemI  'Kandulu','i dont know','ka003',1
 EXEC dbo.ItemI  'Pasapu','anty biotic','Pa004',1
 EXEC dbo.ItemI  'Chintapandu','citrus Type','Ch005',1
 EXEC dbo.ItemI  'Mokkajonna','karn','Mo006',1
 EXEC dbo.ItemI  'Bellam','sugar cain product','Bl007',1
