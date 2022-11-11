# Write your MySQL query statement below

select id,'Root' as type
from Tree
where p_id is Null
union
select id,'Inner' as type
from Tree
where id in (select p_id from Tree) and p_id is not Null
union
select id,'Leaf' as type
from Tree
where id not in (select p_id from Tree where p_id is not Null) and p_id is not Null
