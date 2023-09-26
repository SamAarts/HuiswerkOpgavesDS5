def average_display():
    '''Display the avarage grade'''
    total = sum(float(record['Grade']) for record in records)
    average = total / len(records)
    print(f"Average Grade: {average}\n--------------------")

def student_report():
    '''Display 'Student Report' header'''
    print("Student Report\n--------------")

def record_display():
    ''''Display the records'''
    filtered_records = [record for record in records if float(record['Grade']) >= 80.0]
    for record in filtered_records:
        print(f"Name: {record['Name']}\nGrade: {record['Grade']}\n--------------------")

def display():
    '''Display the complete report'''
    average_display()
    student_report()
    record_display()

file_path = input("Enter the path to the CSV file: ")
records = []
with open(file_path, 'r') as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        records.append(row)

display()