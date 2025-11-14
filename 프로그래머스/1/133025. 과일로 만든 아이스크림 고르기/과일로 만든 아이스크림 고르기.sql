-- 코드를 입력하세요
-- FIRST_HALF 주문 정보 ( 기본키 -> FLAVOR)
-- SHIPMENT_ID, FLAVOR, TOTAL_ORDER
-- 출하 번호, 아이스크림 맛, 상반기 아이스크림 총주문량

-- ICECREAM_INFO
--  FLAVOR,   INGREDITENT_TYPE(sugar_based , fruit_based)
-- 아이스크림 맛, 아이스크림의 성분 타입
SELECT II.FLAVOR 
FROM FIRST_HALF AS FH
    JOIN ICECREAM_INFO AS II
    ON FH.FLAVOR = II.FLAVOR
WHERE (II.INGREDIENT_TYPE = 'fruit_based') AND (FH.TOTAL_ORDER > 3000)
ORDER BY FH.TOTAL_ORDER DESC