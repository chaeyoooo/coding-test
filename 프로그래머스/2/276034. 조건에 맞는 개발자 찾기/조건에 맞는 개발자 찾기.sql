-- 코드를 작성해주세요
-- SKILLCODES
-- NAME,    CATEGORY,   CODE
-- 스킬의 이름, 스킬의 범주, 스킬의 코드(2진수로 표현했을 때 각 bit로 구분될 수 있도록 2의 제곱수)

-- DEVELOPERS
-- ID,      FIRST_NAME, LAST_NAME, EMAIL, SKILL_CODE
-- 개발자의 ID, 이름,         성,      이메일,    스킬 코드 ( 400 이라면 CODE가 256,128,16)

SELECT ID,EMAIL,FIRST_NAME,LAST_NAME
FROM DEVELOPERS
WHERE SKILL_CODE & 256 != 0 OR
    SKILL_CODE & 1024 != 0
ORDER BY ID