emp={'name':['jyothsna','hari','lahari','ramya','swathi'],'age':[20,30,45,10,57],'salary':[10000,2000,300,49997,200]}
print("The employee dataset is:",emp)
print("total salary of the employee:",sum(emp['salary']))
print("the minimun salary is:",min(emp['salary']))
print("the maximun salary is:",max(emp['salary']))
#print(" max salary of the employee name:",min(emp['name']))
max_salary_index = emp['salary'].index(max(emp['salary']))

# Get the name of the employee with the maximum salary
employee_with_max_salary = emp['name'][max_salary_index]

print(f"The employee with the maximum salary is: {employee_with_max_salary}")
for name, salary in zip(emp['name'], emp['salary']):
    if salary > 25000:
        print(name)
