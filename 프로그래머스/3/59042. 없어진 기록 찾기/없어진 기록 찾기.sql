-- 코드를 입력하세요
-- 천재지변으로 ANIMAL_INS 테이블 유실
-- ANIMAL_OUTS에서는 모든 코드가 존재함.
-- 코드는 교집합 값을 제외한 순수 ANIMAL_INS의 값 출력

select ANIMAL_OUTS.ANIMAL_ID, ANIMAL_OUTS.NAME
from ANIMAL_OUTS
left outer join ANIMAL_INS
on ANIMAL_OUTS.ANIMAL_ID = ANIMAL_INS.ANIMAL_ID
where ANIMAL_INS.ANIMAL_ID is null