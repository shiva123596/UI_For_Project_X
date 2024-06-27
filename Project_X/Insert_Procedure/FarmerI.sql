CREATE PROCEDURE FarmerI
 @FirstName VARCHAR(225)
,@LastName VARCHAR(225)
,@Village VARCHAR(225)
,@Mandal VARCHAR(225)
,@PANNumber CHAR(25)
,@Phone BIGINT
,@Aadhar BIGINT

AS
BEGIN
	IF NOT EXISTS(SELECT 1 FROM Farmer WHERE PanNumber = @PanNumber)
	BEGIN
		INSERT INTO farmer (FirstName,LastName,Village,Mandal,PANNumber,Phone,Aadhar,RecordStatusID)
		VALUES (@FirstName,@LastName,@Village,@Mandal,@PANNumber,@Phone,@Aadhar,1)
	END
END




EXEC dbo.FarmerI 'siva','Koritala','Jonnalagadda','Narasaraopet','HULPK9554A','8099892208','423541018544'
delete from farmer where phone = '8099892108'