# Weighted Grade Calculator

tests = []
homework = [] 
quizzes = []
exams = []
culture_reports = []

projected = 90 # if no grades are in a category, this value is assigned


sum = 0
counter = 0
for test in tests:
	sum += test
	counter+= 1
if counter == 0:
        av_test_grades = projected
else:
        av_test_grades = sum/counter

sum = 0
counter = 0
for quiz in quizzes:
	sum += quiz
	counter+= 1
if counter == 0:
        av_quizzes = projected
else:
        av_quizzes = sum/counter
	
sum = 0
counter = 0
for hw in homework:
	sum += hw
	counter+= 1
if counter == 0:
        av_homework = projected
else:
        av_homework = sum/counter

sum = 0
counter = 0
for e in exams:
	sum += e
	counter+= 1
if counter == 0:
        av_exams = projected
else:
        av_exams = sum/counter

sum = 0
counter = 0
for c in culture_reports:
	sum += c
	counter+= 1
if counter == 0:
        av_culture_reports = projected
else:
        av_culture_reports = sum/counter

grade = av_test_grades*30 + av_homework*30 + av_quizzes*10 + av_culture_reports*10 + av_exams*20
print grade/100		
