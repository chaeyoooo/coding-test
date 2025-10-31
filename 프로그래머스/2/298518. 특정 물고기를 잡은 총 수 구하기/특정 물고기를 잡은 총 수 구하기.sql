-- 코드를 작성해주세요
-- FISH_INFO
-- ID,              FISH_TYPE,          LENGTH,         TIME
-- 잡은 물고기의 ID, 물고기의 종류(숫자), 잡은 물고기의 길이(cm), 물고기를 잡은 날짜

-- FISH_NAME_INFO
-- FISH_TYPE,       FISH_NAME
-- 물고기의 종류(숫자), 물고기의 이름(문자)

SELECT COUNT(*) AS FISH_COUNT
FROM FISH_INFO
WHERE FISH_TYPE IN(
    SELECT FISH_TYPE
    FROM FISH_NAME_INFO
    WHERE FISH_NAME = 'BASS' OR FISH_NAME = 'SNAPPER'
)