#!/usr/bin/python3
import sys
import re
import signal

# Initialize counters
total_file_size = 0
status_code_counts = {200: 0, 301: 0, 400: 0, 401: 0,
                      403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0

# Define regular expression in two parts
l1 = (r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3} - \[.*?\] \"GET /projects/260 ")
l2 = r"HTTP/1\.1\" (\d{3}) (\d+)$"
log_format_regex = re.compile(l1 + l2)


def print_statistics():
    """Prints the accumulated statistics."""
    print(f"File size: {total_file_size}")
    for code in sorted(status_code_counts.keys()):
        if status_code_counts[code] > 0:
            print(f"{code}: {status_code_counts[code]}")


def signal_handler(sig, frame):
    """Handles the signal for graceful shutdown."""
    print_statistics()
    sys.exit(0)


# Set up the signal handler for CTRL + C
signal.signal(signal.SIGINT, signal_handler)

# Read from stdin line by line
try:
    for line in sys.stdin:
        line = line.strip()
        match = log_format_regex.match(line)
        if match:
            status_code = int(match.group(1))
            file_size = int(match.group(2))

            # Update the total file size and the status code count
            total_file_size += file_size
            if status_code in status_code_counts:
                status_code_counts[status_code] += 1

        line_count += 1

        # Print statistics every 10 lines
        if line_count % 10 == 0:
            print_statistics()

except KeyboardInterrupt:
    # Print the statistics when interrupted by CTRL + C
    print_statistics()
    sys.exit(0)

# Print the final statistics if the loop finishes naturally
print_statistics()