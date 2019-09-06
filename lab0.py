def main():
	
	students = [ "Matthew", "Johnathan", "Bob" ]
	students.sort()
	print(students)
	
	first_name = students[0]
	first_name = first_name[:-1]
	print(first_name)
	
	longest_name = ""
	for student in students:
		if len(longest_name) < len(student):
			longest_name = student
	print(longest_name)

if __name__ == "__main__":
	main()
