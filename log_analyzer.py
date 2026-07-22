import re

def analyze_log(file_path):
    error_pattern = re.compile(r"ERROR|Error|error")
    errors_found = []

    try:
        with open(file_path, "r") as log_file:
            for line_number, line in enumerate(log_file, start=1):
                if error_pattern.search(line):
                    errors_found.append((line_number, line.strip()))
    except FileNotFoundError:
        print(f"Log file not found: {file_path}")
        return

    if errors_found:
        print("Errors found:")
        for line_number, error in errors_found:
            print(f"Line {line_number}: {error}")
    else:
        print("No errors found in the log file.")

if __name__ == "__main__":
    log_path = "system.log"  # Change this to your log file name
    analyze_log(log_path)
