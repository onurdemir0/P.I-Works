select 
    c.*,
    coalesce(
        c.val, 
        (
            select daily_vaccinations(0.5) within group(order by c1.val)
            from test c1
            where c1.id between c.id - 3 and c.id - 1
        )
    ) fixed
from test c