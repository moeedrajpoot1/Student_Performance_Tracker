class Student:
    def __init__(self, name, scores) -> None:
        self.name = name
        self.scores = scores

    def calculate_average(self):
       
        if not self.scores:
            return 0
        return sum(self.scores) / len(self.scores)
    
    def is_passing(self, passing_score=40):
     
        return all(score >= passing_score for score in self.scores)

class PerformanceTracker:
    def __init__(self):
        self.students = {}

    def add_student(self, name, scores):
    
        self.students[name] = Student(name, scores)

    def calculate_class_average(self):
      
        if not self.students:
            return 0
        total_average = sum(student.calculate_average() for student in self.students.values())
        return total_average / len(self.students)
    
    def display_student_performance(self):
       
        for student in self.students.values():
            avg_score = student.calculate_average()
            passing_status = "Passing" if student.is_passing() else "Not Passing"
            print(f"Student: {student.name}, Average Score: {avg_score:.2f}, Status: {passing_status}")

def input_student_data(tracker):

    while True:
        name = input("Enter student's name (or 'stop' to finish): ")
        if name.lower() == 'stop':
            break
        
        scores = []
        for subject in ['Math', 'Science', 'English']:
            while True:
                try:
                    score = int(input(f"Enter score for {subject}: "))
                    scores.append(score)
                    break  # Exit the inner loop if input is valid
                except ValueError:
                    print("Invalid input. Please enter an integer for the score.")
        
        tracker.add_student(name, scores)

def main():
    """Main function to execute the program."""
    tracker = PerformanceTracker()
    
    input_student_data(tracker)
    
    print("\nStudent Performance:")
    tracker.display_student_performance()
    
    class_average = tracker.calculate_class_average()
    print(f"\nClass Average Score: {class_average:.2f}")

if __name__ == "__main__":
    main()
