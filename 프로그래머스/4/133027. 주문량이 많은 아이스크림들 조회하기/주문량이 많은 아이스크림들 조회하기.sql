-- 코드를 입력하세요

select flavor
from (
    select f.flavor, f.total_order + j.total_order as total_order
    from first_half as f
    inner join (
        select flavor, sum(total_order) as total_order
        from july
        group by flavor
    )j
    on f.flavor = j.flavor
)result_table
order by total_order desc limit 3