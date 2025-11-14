-- 코드를 작성해주세요
-- FISH_INFO 물고기들의 정보
--      ID,         FISH_TYPE,         LENGTH,          TIME
-- 잡은 물고기의 ID, 물고기의 종류(숫자), 잡은 물고기의 길이(cm), 물고기를 잡은 날짜

-- FISH_NAME_INFO
-- FISH_TYPE,       FISH_NAME
-- 물고기의 종류(숫자), 물고기의 이름(문자)

SELECT FI.ID , FNI.FISH_NAME , FI.LENGTH
FROM FISH_INFO AS FI
JOIN FISH_NAME_INFO AS FNI
    ON FI.FISH_TYPE = FNI.FISH_TYPE
WHERE FI.LENGTH =   (
    SELECT MAX(LENGTH)
    FROM FISH_INFO
    WHERE  FISH_TYPE =FI.FISH_TYPE 
)
ORDER BY FI.ID
