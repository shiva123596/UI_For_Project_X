CREATE PROCEDURE VarietyUpdate
 @Name NVARCHAR(100) NULL
,@Description NVARCHAR(4000) NULL
,@Code NCHAR(10) NULL
AS
BEGIN
UPDATE Variety set [Name] = ISNULL(@Name,Name)
              ,[Description] = isnull(@Description,[Description])
			  ,[Code] = ISNULL (@Code,Code)
Where VarietyID = (Select VarietyID From Variety Where [Name] = @Name OR Code = @COde)

END


EXEC VarietyUpdate   @Name = 'Nallurisannalu'
                 ,@Description = NULL
				 ,@Code = 'NS001'
