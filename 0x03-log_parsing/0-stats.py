#!/usr/bin/python3
import sys
import re
from signal import signal, SIGINT

# Regex for matching input format
pattern = re.compile(
    r'(?P<ip>\S+) - \[(?P<date>.+?)\] "GET /projects/260 HTTP/1\.1" '
    r'(?P<status>\d{3}) (?P<size>\d+)'
)

# Initialize counters
total_size = 0
status_codes = {code: 0 for code in ["200", "301", "400", "401",
                                     "403", "404", "405", "500"]}
line_count = 0


def print_metrics():
    """Print total size and status code counts."""
    print(f"File size: {total_size}")
    for status in sorted(status_codes):
        if status_codes[status] > 0:
            print(f"{status}: {status_codes[status]}")


def handle_interrupt(signal_received, frame):
    """Print metrics and exit on keyboard interrupt."""
    print_metrics()
    sys.exit(0)


# Handle CTRL + C
signal(SIGINT, handle_interrupt)

# Read each line from stdin
for line in sys.stdin:
    match = pattern.match(line)
    if match:
        total_size += int(match.group("size"))
        status_code = match.group("status")
        if status_code in status_codes:
            status_codes[status_code] += 1

    # Print metrics every 10 lines
    line_count += 1
    if line_count % 10 == 0:
        print_metrics()

# Final metrics printout
print_metrics()
