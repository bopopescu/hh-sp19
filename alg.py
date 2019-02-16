def run_algorithm(Semester):
    averages = []
    for courses in Semester.get_courses():
        for asst in courses.get_asst():
            
