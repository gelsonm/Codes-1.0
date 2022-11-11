# Write your MySQL query statement below

# Approach 1
# select id,'Root' as type
# from Tree
# where p_id is Null
# union
# select id,'Inner' as type
# from Tree
# where id in (select p_id from Tree) and p_id is not Null
# union
# select id,'Leaf' as type
# from Tree
# where id not in (select p_id from Tree where p_id is not Null) and p_id is not Null

# Approach 2
SELECT id,
    CASE 
        WHEN p_id is NULL THEN 'Root'
        WHEN id IN (SELECT p_id FROM Tree) THEN 'Inner'
        ELSE 'Leaf'
        END AS type
        
FROM TREE

