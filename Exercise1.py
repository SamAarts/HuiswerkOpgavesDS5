file_path = input("Enter the path to the CSV file: ")
records = []
with open(file_path, 'r') as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        records.append(row)

total = sum(float(record['Grade']) for record in records)
average = total / len(records)

print(f"Average Grade: {average}")
print("--------------------")

filtered_records = [record for record in records if float(record['Grade']) >= 80.0]

print("Student Report")
print("--------------")



def display(dictionary: dict={})->None:
    '''
    A function that given a dictionary will print a key and its given values line by line

    : records should be a non empty dictionary
    '''
    if dictionary == {}:
        print('An empty dictionary was presented therefore there will be no output')
    else:
        for key,value in dictionary.items():
            print(f'{key}: {value}')
        print('--------------------')

for record in filtered_records:
    display(record)
