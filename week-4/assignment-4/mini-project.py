students = [
    {"name": "Jazmine", "score": 88, "subject": "Python"},
    {"name": "Luis",    "score": 74, "subject": "Data"},
    {"name": "Sara",    "score": 91, "subject": "Python"},
    {"name": "Marcus",  "score": 68, "subject": "Web"},
    {"name": "Priya",   "score": 95, "subject": "Data"},
    {"name": "Devon",   "score": 72, "subject": "Python"},
    {"name": "Mia",     "score": 83, "subject": "Web"},
    {"name": "Eli",     "score": 79, "subject": "Data"},
]
top_score = {"name": "", "score":0}
average_accum=0
subjects= set()
high_scorers=[]
for student in students:
    average_accum += student["score"]
    subjects.add(student["subject"])
    if student["score"] >= top_score["score"]:
        top_score["name"]=student["name"]
        top_score["score"]=student["score"]
    if student["score"] > 75:
        high_scorers.append(student["name"])
print(f'Top scorer:        {top_score["name"]} ({top_score["score"]}%)')
print(f'Class average:     {average_accum/len(students)}%')
print(f'Subjects offered:  {subjects}')
print(f'High scorers:      {high_scorers}')