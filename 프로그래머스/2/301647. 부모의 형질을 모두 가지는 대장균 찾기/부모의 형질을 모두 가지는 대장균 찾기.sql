-- 코드를 작성해주세요
-- ECOLI_DATA 
--         ID,     PARENT_ID, SIZE_OF_COLONY, DIFFERENTIATION_DATE, GENOTYPE
-- 대장균 개체의 ID, 부모 개체의 ID, 개체의 크기,       분화되어 나온 날짜,        개체의 형질

# 분화를 시작한 개체 ( 부모 개체 )
# 분화가 되어 나온 개체 ( 자식 개체 )


SELECT 
    C.ID,
    C.GENOTYPE,
    P.GENOTYPE AS PARENT_GENOTYPE
FROM 
    ECOLI_DATA AS C
JOIN 
    ECOLI_DATA AS P
    ON C.PARENT_ID = P.ID
WHERE
    (C.GENOTYPE & P.GENOTYPE) = P.GENOTYPE
ORDER BY C.ID;