CREATE PROCEDURE RecordStatusI
@Name NCHAR(10)
,@Code NCHAR(10)
AS
BEGIN
	IF NOT EXISTS(SELECT 1 FROM RecordStatus WHERE Code = @Code)
	BEGIN
		INSERT INTO RecordStatus (Name,Code)
		VALUES (@Name,@Code)
	END
END
 

 SELECT * FROM RecordStatus

 EXEC dbo.RecordStatusI 'Active', 'A'
 EXEC dbo.RecordStatusI 'InActive', 'I'
 EXEC dbo.RecordStatusI 'Delete', 'D'
 EXEC dbo.RecordStatusI 'Approved', 'AP'
 EXEC dbo.RecordStatusI 'Rejected', 'R'
 EXEC dbo.RecordStatusI 'Settled', 'S' 



