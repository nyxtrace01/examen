
#ENONCE
students=[
    ("Ali",12),
    ("Fatou",17),
    ("Moussa",9),
    ("Awa",14),
    ("Ibrahima",7)
]
#affiche tous les etudiants avec leurs notes
for student in students:
    print(f"Etudiant: {student[0]}, Note: {student[1]}")

#CALCULE T AFFICHE 

#la moyenne de la classe
total_notes=0
for student in students:
    total_notes += student[1]       
moyenne=total_notes/len(students)
print("La moyenne de la classe est:",moyenne)
#la note maximale 
max_note=students[0][1]
for student in students:
    if student[1] > max_note:
        max_note=student[1]
print("La note maximale est:",max_note)
#la note minimale   
min_note=students[0][1]
for student in students:
    if student[1] < min_note:
        min_note=student[1] 
print("La note minimale est:",min_note)
#la liste des etudiants admis
etudiants_reussite=[]
for student in students:
    if student[1] >= 10:
        etudiants_reussite.append(student[0])
print("Les etudiants admis sont:",etudiants_reussite)
#la liste des etudiants ajournees
etudiants_echec=[]
for student in students:
    if student[1] < 10:
        etudiants_echec.append(student[0])  
print("Les etudiants ajournes sont:",etudiants_echec)