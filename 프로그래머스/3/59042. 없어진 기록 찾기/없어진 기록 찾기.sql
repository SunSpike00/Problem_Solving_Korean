-- 코드를 입력하세요
-- 천재지변으로 ANIMAL_INS 테이블 유실
-- ANIMAL_OUTS에서는 모든 코드가 존재함.
-- 코드는 교집합 값을 제외한 순수 ANIMAL_INS의 값 출력

SELECT ai.ANIMAL_ID, ai.NAME
from ANIMAL_INS as ai
left join ANIMAL_OUTS as ao
UNION SELECT ao.ANIMAL_ID, ao.NAME
from ANIMAL_INS as ai
right join ANIMAL_OUTS as ao
where ai.ANIMAL_ID is null or ao.ANIMAL_ID is null