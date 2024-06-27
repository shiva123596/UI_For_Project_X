CREATE PROCEDURE LoanI
 @BondNumber INT
,@AvgBagWeight int
,@MarketPrise int
,@LoanForBag int
,@AmountSanctioned FLOAT
,@RequestDate DATETIME
,@ApproveDate DATETIME
,@FarmerID INT
,@BankID int
AS 
BEGIN
Declare @NetWeight int
       ,@ApprxCost FLOAT
       ,@AmountEligible Float
	   ,@TransactionID int
	   ,@RecordStatusID int
 SELECT @RecordStatusID = 1,@TransactionID = [TransactionID],@NetWeight = CONVERT(FLOAT,((NoOfBags)*@AvgBagWeight))
      ,@ApprxCost = (((NoOfBags)*@AvgBagWeight/100)*@MarketPrise)
	  ,@AmountEligible = (NoOfBags*@LoanForBag)  FROM [TRANSACTION]
	 
	  WHERE FarmerID = @FarmerID

INSERT INTO Loan (RecordStatusID,BankID,FarmerID,TransactionID,BondNumber,NetWeight,ApprxCost,AmountEligible,AmountSanctioned,RequestDate,ApproveDate)
VALUES (@RecordStatusID,@BankID,@FarmerID,@TransactionID,@BondNumber,@NetWeight,@ApprxCost,@AmountEligible,@AmountSanctioned,@RequestDate,@ApproveDate)
END

--EXEC LoanI @FarmerID         = 3
--          ,@BankID           = 1
--          ,@BondNumber		 = 559
--		  ,@AvgBagWeight     = 42
--          ,@MarketPrise      = 14000
--          ,@LoanForBag       = 2000
--          ,@AmountSanctioned = 80000
--          ,@RequestDate		 = '2020-07-25 16:22:46.093'
--          ,@ApproveDate		 = '2020-07-25 16:22:46.093'






