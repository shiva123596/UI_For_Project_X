
CREATE PROCEDURE C3_TransactionI
    @FarmerID INT,
    @NoOfBags INT,
    @Description NVARCHAR(4000) = NULL,
    @ParentTransactionID INT
AS
BEGIN
    -- Declare variables to hold RecordStatusID and other required values
    DECLARE @RecordStatusID INT;
    DECLARE @TransactionTypeID INT = 2;  -- Set TransactionTypeID to 2
    DECLARE @ItemID INT, @VarietyID INT, @KanaBlockMapID INT;
    DECLARE @ParentNoOfBags INT;
    DECLARE @CurrentChildBags INT;

    -- Set RecordStatusID to 1
    SET @RecordStatusID = 1;

    -- Fetch values from the parent transaction including NoOfBags
    SELECT 
        @ItemID = Parent.ItemID,
        @VarietyID = Parent.VarietyID,
        @KanaBlockMapID = Parent.KanaBlockMapID,
        @ParentNoOfBags = Parent.NoOfBags
    FROM 
        [Transaction] Parent
    WHERE 
        Parent.TransactionID = @ParentTransactionID;

    -- Calculate the total NoOfBags of all child transactions
    SELECT 
        @CurrentChildBags = ISNULL(SUM(Child.NoOfBags), 0)
    FROM 
        [Transaction] Child
    WHERE 
        Child.ParentTransactionID = @ParentTransactionID;

    -- Check if adding the new transaction's NoOfBags exceeds the parent's NoOfBags
    IF (@CurrentChildBags + @NoOfBags) <= @ParentNoOfBags
    BEGIN
        -- Insert the transaction details into the [Transaction] table
        INSERT INTO [Transaction] (
            FarmerID,
            RecordStatusID,
            TransactionTypeID,
            ParentTransactionID,
            ItemID,
            VarietyID,
            KanaBlockMapID,
            NoOfBags,
            Description
        ) VALUES (
            @FarmerID,
            @RecordStatusID,
            @TransactionTypeID,
            @ParentTransactionID,
            @ItemID,
            @VarietyID,
            @KanaBlockMapID,
            @NoOfBags,
            @Description
        );

        -- Recalculate the total NoOfBags of all child transactions after the insert
        SELECT 
            @CurrentChildBags = ISNULL(SUM(Child.NoOfBags), 0)
        FROM 
            [Transaction] Child
        WHERE 
            Child.ParentTransactionID = @ParentTransactionID;

        -- Check if the total NoOfBags of child transactions equals the parent's NoOfBags
        IF @CurrentChildBags = @ParentNoOfBags
        BEGIN
            -- Update RecordStatusID to 2 if condition is met
            UPDATE [Transaction]
            SET RecordStatusID = 2
            WHERE TransactionID = @ParentTransactionID;
        END
    END
    ELSE
    BEGIN
        -- Raise an error if the condition is violated
        RAISERROR ('Total NoOfBags in child transactions exceeds NoOfBags in parent transaction.', 16, 1);
    END
END;




--Exec dbo.C3_TransactionI @FirstName = '',@Phone = 8099892109, @ParentTransactionID = 17, @NoOfBags = 14

--select * from [Transaction] where FarmerID = 2

