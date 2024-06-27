

CREATE VIEW v_FloorKanaBlock as
SELECT KBM.KanaBlockMapID,K.KanaID,K.KanaCode,B.BlockID,B.Code BlockCode,F.FloorID,F.Code FloorCode, LTRIM(K.KanaCode) + '('+TRIM(B.Code)+')' AS KanaBlockKey,KBM.RecordStatusID,R.Name from KanaBlockMap KBM
join Kana K ON K.KanaID = KBM.KanaID
JOIN [Block] B ON B.BlockID = KBM.BlockID
JOIN [Floor] F ON F.FloorID = K.FloorID 
JOIN RecordStatus R ON R.RecordStatusID = KBM.RecordStatusID