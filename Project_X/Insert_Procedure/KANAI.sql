CREATE PROCEDURE KANAI
 @FLOORID INT
,@STARTING_NUMBER INT
,@ENDING_NUMBER INT AS
BEGIN
	IF NOT EXISTS(SELECT 1 FROM KANA WHERE FLOORID = @FLOORID)
	begin  
      declare 
              @KANACODE INT
			  ,@RecordStatusID INT
SELECT 
@RecordStatusID  = '1'
 SET @KANACODE  =    @STARTING_NUMBER
WHILE  @KANACODE  <= @ENDING_NUMBER
BEGIN
 INSERT INTO KANA  (FLOORID,
                    KANACODE,
					RecordStatusID
					) 
			      

 VALUES (@FLOORID,
         @KANACODE,
		 @RecordStatusID
		 )
SET @KANACODE  =  @KANACODE  + 1 END;
		 END
END
 
 
 SELECT * FROM KANA

 EXEC dbo.[KANAI] @FLOORID = 1,@STARTING_NUMBER = 100,@ENDING_NUMBER = 150
 EXEC dbo.KANAI @FLOORID = 2,@STARTING_NUMBER = 201,@ENDING_NUMBER = 244
 EXEC dbo.KANAI @FLOORID = 3,@STARTING_NUMBER = 300,@ENDING_NUMBER = 350
 EXEC dbo.KANAI @FLOORID = 4,@STARTING_NUMBER = 400,@ENDING_NUMBER = 450
 EXEC dbo.KANAI @FLOORID = 5,@STARTING_NUMBER = 500,@ENDING_NUMBER = 550
 EXEC dbo.KANAI @FLOORID = 6,@STARTING_NUMBER = 600,@ENDING_NUMBER = 650
 