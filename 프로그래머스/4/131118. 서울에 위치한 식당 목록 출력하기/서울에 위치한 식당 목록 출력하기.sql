-- 코드를 입력하세요
-- REST_INFO
-- REST_REVIEW
-- 서울에 위치한 식당
-- 리뷰 평균점수는 소수점 세 번째 자리에서 반올림
-- 평균점수를 기준으로 내림차순 정렬
-- 평균점수가 같다면 즐겨찾기수를 기준으로 내림차순 정렬

select RIN.REST_ID, REST_NAME, FOOD_TYPE, FAVORITES, ADDRESS, SCORE
from REST_INFO as RIN
join (
    SELECT REST_ID, round(avg(REVIEW_SCORE), 2) as SCORE
    from REST_REVIEW
    group by REST_ID
) as RID
on RIN.REST_ID = RID.REST_ID
where ADDRESS like '서울%'
order by SCORE desc, FAVORITES desc
