CREATE PROCEDURE BankUpdate
@Name VARCHAR(255) null
,@Address VARCHAR(4000) null
,@Phone Varchar(10) null
AS
BEGIN
UPDATE Bank set [Name] = isnull(@Name,[Name])
               ,[Address] = ISNULL(@Address,[Address])
			   ,[Phone] = ISNULL(@Phone,[Phone])
Where BankID = (Select BankID from Bank Where Name = @Name or Phone = @Phone)

END


EXEC  BankUpdate @Name = 'ANDHRABANK'
                ,@Address = NULL
			    ,@Phone = 4567234553

