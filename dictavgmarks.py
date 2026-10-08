student={
    101:{"name":"Aditi","scores":[78,85,90]},
         102:{"name":"Rahul","scores":[45,60,50]},
         103:{"name":"Sneha","scores":[48,87,90]},
         104:{"name":"Manasi","scores":[70,95,60]},
         105:{"name":"Krushna","scores":[56,56,78]}
         }
for sid,details in student.items():
    avg=sum(details["scores"]/len(details["scores"]))
    details["Average"]=avg
    details["Passed"]=avg>=50
print("Studnts who passed :")
for sid,details in student.items():
    if details["passed"]:
        print(details["Name"])