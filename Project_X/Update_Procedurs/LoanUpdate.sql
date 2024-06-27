
CREATE PROCEDURE LoanUpdate
 @BondNumber INT null
,@AmountSanctioned FLOAT null
,@RequestDate DATETIME null
,@ApproveDate DATETIME null
,@FarmerID INT
,@TransactionID int
AS 
BEGIN
	IF  EXISTS(SELECT RecordStatusID FROM Loan WHERE FarmerID = @FarmerID and RecordStatusID = 1 and TransactionID = @TransactionID)
BEGIN
Update Loan
set BondNumber = isnull(@BondNumber,BondNumber)
   ,AmountSanctioned = isnull(@AmountSanctioned,AmountSanctioned)
   ,RequestDate = isnull(@RequestDate,RequestDate)
   ,ApproveDate = isnull(@ApproveDate,ApproveDate)
	  WHERE FarmerID = @FarmerID and TransactionID = @TransactionID
   END
END

EXEC LoanUpdate            @FarmerID         = 2
                          ,@TransactionID    = 7
                          ,@BondNumber		 = null
                          ,@AmountSanctioned = 85000
                          ,@RequestDate		 = null
                          ,@ApproveDate		 = null