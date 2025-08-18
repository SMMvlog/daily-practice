# Table A
# 1
# 1
# 0
# 1
 
# Table B
# 1
# null
# 1
# 0

# inner join

# 1

# left join

# 1
# 1
# 0
# 1

# right join
# 1
# null
# 1
# 0

# full outer join

# 1 1
# 1 null
# 0 null
# 1 null


# We have an IPL team list in a single column table like this:
# col1
# ------
# RCB
# CSK
# MI
# PBKS
 
# We need to generate a match schedule such that:
#  1. Each team plays with every other team exactly once.
#  2. No duplicate combinations (e.g,. if RCB vs CSK is listed, CSK vs RCB shouldn't be repeated)
 



# SELECT id, employee, month, sales
# 	FROM public.sales;

# SELECT *, 
#        LEFT(CAST(sales AS TEXT), length(cast(sales as text)) - 2) || 'xx' AS encrypted_sales
# FROM public.sales;

# SELECT *,sales - lead(sales,1) over(partition by employee order by case month when 'Jan' then 1 when 'Feb' then 2 when 'Mar' then 3 when 'Apr' then 4 end) as pre_month_sales from public.sales;

# select *,ROW_NUMBER() over(order by sales desc)as sales_order from sales;
# select *,FIRST_VALUE(sales) over(partition by employee order by sales desc) as first_month_sale from sales;
# select *,sum(sales) over(partition by employee) as total_sales from sales;

# select *, NTILE(3) over(order by sales desc) as employee_grp from public.sales;

# select *,first_value(sales) over(partition by employee order by sales desc) as high_sale,last_value(sales) over(partition by employee) as lower_sale
# from public.sales;




# Table A
# 1
# 1
# 0
# 1
 
# Table B
# 1
# null
# 1
# 0


# inner join
# (1,1),(1,3)
# (2,1),(2,3)
# (3,4)
# (4,1),(4,3)

# left join
# (1,1),(1,3)
# (2,1),(2,3)
# (3,4)
# (4,1),(4,3)

# right join
# (1,1),(2,1),(4,1)
# (null,2)
# (1,3),(2,3),(4,3)
# (3,4)

# full outer join
# (1,1),(1,3)
# (2,1),(2,3)
# (3,4)
# (4,1),(4,3)
# (null,2)






