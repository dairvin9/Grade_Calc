# Weighted Grade Calculator

# Lists of grades of each type
tests = []
homework = [] 
quizzes = []
culture_reports = []

# What percentage of the grade is what kind of assignment
test_weight = 80
homework_weight = 5
quiz_weight = 5
culture_report_weight = 10

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
for c in culture_reports:
	sum += c
	counter+= 1
if counter == 0:
        av_culture_reports = projected
else:
        av_culture_reports = sum/counter

grade = av_test_grades*test_weight + av_homework*homework_weight + av_quizzes*quiz_weight + av_culture_reports*culture_report_weight
print grade/100		
