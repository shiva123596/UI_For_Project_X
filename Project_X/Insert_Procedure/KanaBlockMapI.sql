create procedure KanaBlockMapI
as
begin
	declare 
	          @recordstatusid int,
              @KanaID int,
			  @FloorID int,
			  @Kanacode int,
			  @Blockid int,
			  @Blockcode char(10)
		insert into kanablockmap (recordstatusID,kanaid,blockid)
		
	SELECT c.* FROM 
(select  1 AS recordstatusID,
a.kanaid,b.[blockid] from kana a
cross apply block b
) c left join KanaBlockMap KBM ON c.KanaID = KBM.KanaID AND c.blockID = KBM.BlockID
WHERE KBM.KanaBlockMapID IS NULL

 end

 

 SELECT * FROM KANABLOCKMAP

 EXEC KANABLOCKMAPI
 
