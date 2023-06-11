# Adding list items
my_subjects = ["S.ST","Math","English","Urdu","Islamyat"]
my_marks = [10,12,20,10,16]
sum = 0
for j in range (0,5):
    print(f"{my_subjects[j]} {my_marks[j]}")
for i in range (0,5):
    sum = sum + my_marks[i]
print (f"Total = {sum}")    