-- 코드를 입력하세요
-- ANIMAL_INS(동물 보호소에 들어온 동물의 정보)
-- ANIMAL_ID, ANIMAL_TYPE, DATETIME, INTAKE_CONDITION, NAME, SEX_UPON_INTAKE
-- 동물의 아이디, 생물 종,       보호 시작일, 보호 시작 시 상태, 이름,     성별 및 중성화 여부

-- ANIMAL_OUTS(동물 보호소에서 입양 보낸 동물의 정보)
-- ANIMAL_ID, ANIMAL_TYPE, DATETIME, NAME, SEX_UPON_OUTCOME
-- 동물의 아이디, 생물 종,       입양일,    이름,  성별 및 중성화 여부

-- 보호 시작일 보다 입양일이 더 바른 동물의 아이디와 이름을 조회
-- 보호 시작일이 빠른 순

SELECT 
    AI.ANIMAL_ID , AI.NAME 
FROM 
    ANIMAL_INS AS AI
JOIN ANIMAL_OUTS AS AO 
    ON AI.ANIMAL_ID = AO.ANIMAL_ID
WHERE AI.DATETIME > AO.DATETIME
ORDER BY AI.DATETIME ASC

