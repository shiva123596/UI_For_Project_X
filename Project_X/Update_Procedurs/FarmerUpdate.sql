
CREATE PROCEDURE FarmerUpdate
 @FirstName  VARCHAR(225) null
,@LastName  VARCHAR(225) null
,@Village   VARCHAR(225) null
,@Mandal    VARCHAR(225) null
,@PANNumber CHAR(25) null
,@Phone     BIGINT	 null
,@Aadhar    BIGINT	 null
AS
BEGIN

update Farmer set FirstName = ISNULL(@FirstName ,FirstName) 
                 ,LastName = ISNULL(@LastName,LastName)
				 ,Village = ISNULL(@Village,Village)
				 ,Mandal = ISNULL(@Mandal,Mandal)
				 ,PANNumber = ISNULL(@PANNumber,PANNumber)
				 ,Phone = ISNULL(@Phone,Phone)
				 ,Aadhar = ISNULL(@Aadhar,Aadhar)
where FarmerID = (select FarmerID from Farmer where FirstName = @FirstName and LastName = @LastName or Phone = @Phone)

end


EXEC FarmerUUP  @FirstName = 'SAMBASIVARAO'
			  ,@LastName  = NULL
			  ,@Village   = 'AMARAVATI'
			  ,@Mandal    = null
			  ,@PANNumber = null
			  ,@Phone     = 8099892109
			  ,@Aadhar    = 54354634663433