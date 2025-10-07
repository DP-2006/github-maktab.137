import json
import csv
import re

def process_log_file():
    try:
        with open('F://user.csv', 'r', encoding='utf-8') as file:
            lines = file.readlines()
    except FileNotFoundError:
        print("Error: server.log file not found")
        return


    valid_lines = []
    invalid_lines = []

    for line_num, line in enumerate(lines, 1):
        line = line.strip()
        if not line:
            continue

        #  :  timestamp, level, message
        match = re.match(line)
        if match:
            timestamp_str, level, message = match.groups()
            valid_lines.append({
                'line_number': line_num,
                'timestamp': timestamp_str,
                'level': level.upper(),
                'message': message
            })
        else:
            invalid_lines.append({
                'line_number': line_num,
                'content': line
            })

    create_output_files(valid_lines, invalid_lines)

def create_output_files(valid_lines, invalid_lines):
    #   errors.log=
    with open('errors.log', 'w', encoding='utf-8') as f:
        for item in invalid_lines:
            f.write(f"Line {item['line_number']}: {item['content']}\n")

# ERROR Cvs
    with open('errors.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['Line', 'Timestamp', 'Level', 'Message'])

        for line in valid_lines:
            if line['level'] == 'ERROR':
                writer.writerow([
                    line['line_number'],
                    line['timestamp'],
                    line['level'],
                    line['message']
                ])

    level_counts = {}
    for line in valid_lines:
        level = line['level']
        level_counts[level] += level_counts.get(level, 0)

    with open('summary.json', 'w', encoding='utf-8') as f:
        json.dump(level_counts, f, indent=4)

    print("Processing completed successfully!")
    print(f"Summary: {level_counts}")





def fib_gen(n):
    a, b = 0 , 1
    count = 0 
    while count < n:
        yield a 
        a, b = b ,a + b 
        count += 1 
        
for number in fib_gen(5):
    print(number)
    
         
