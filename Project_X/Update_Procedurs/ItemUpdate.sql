CREATE PROCEDURE ItemUpdate
 @Name NVARCHAR(100) NULL
,@Description NVARCHAR(4000) NULL
,@Code NCHAR(10) NULL
AS
BEGIN
UPDATE Item set [Name] = ISNULL(@Name,Name)
              ,[Description] = isnull(@Description,[Description])
			  ,[Code] = ISNULL (@Code,Code)
Where ItemID = (Select ItemID From Item Where [Name] = @Name OR Code = @COde)

END


EXEC ItemUpdate   @Name = 'Kandulu'
                 ,@Description = NULL
				 ,@Code = 'KA103'
