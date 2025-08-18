# lst = [1,2,3,5,6,7,15,0,18,100]

# largest_num = 0
# second_largest_num = 0

# for i in lst:
#     if largest_num < i:
#         largest_num = i
# print(largest_num)
# for i in lst:
#     if second_largest_num < i and largest_num >i:
#         second_largest_num = i
        
# print(second_largest_num)

# s = "ABCDADCBADDDD"
# print(max(s))
# count_str = {}
# for i in s:
#     if i in count_str:
#         count_str[i] +=1
#     else:
#         count_str[i] =1
# max_val = 0
# k = ""
# for k,v in count_str.items():
#     if max_val < v
#       max_val = v




# Project table:

# +-------------+-------------+

# | project_id  | employee_id |

# +-------------+-------------+

# | 1           | 1           |

# | 1           | 2           |

# | 1           | 3           |

# | 2           | 1           |

# | 2           | 4           |

# +-------------+-------------+

# Employee table:

# +-------------+--------+------------------+

# | employee_id | name   | experience_years |

# +-------------+--------+------------------+

# | 1           | Khaled | 3                |

# | 2           | Ali    | 2                |

# | 3           | John   | 1                |

# | 4           | Doe    | 2                |

# +-------------+--------+------------------+
 
# Write an SQL query that reports the average experience years of all the employees for each project, rounded to 2 digits.
 
# #  select * FROM employee AVG(experience_years) group by employee_id;

# select p.project_id, ROUND(AVG(e.experience_years),2) AS average_experience
# FROM project p JOIN emplployee e ON p.employeed_id = e.employee_id group by p.project_id;
 
 
 
 
 
 
 
 
#  Input: 
# Weather table:
# +----+------------+-------------+
# | id | recordDate | temperature |
# +----+------------+-------------+
# | 1  | 2015-01-01 | 10          |
# | 2  | 2015-01-02 | 25          |
# | 3  | 2015-01-03 | 20          |
# | 4  | 2015-01-04 | 30          |
# +----+------------+-------------+



# Write a solution to find all dates' id with higher temperatures compared to its previous dates (yesterday).



class MyCustomError(Exception):
    """Custom exception with a message"""
    def __init__(self, message):
        super().__init__(message)
        self.message = message


lst = [-1,-2,-3,-4,-5,1,2,3,4,5]
# // first_time = -1,-2,3
# // second = -2-3,5
# // third = 1,2,-3
# // forth = 2,3,-5

result_lst = []
def abc():
    try:
        for i in range(len(lst)):
            for j in range(i+1,len(lst)):
                for k in range(j+1,len(lst)):
                    if sum([lst[i],lst[j],lst[k]]) == 0:
                        result_lst.append([lst[i],lst[j],lst[k]])
        return adasdafs
    except MyCustomError as me:
        return me

print(result_lst)

