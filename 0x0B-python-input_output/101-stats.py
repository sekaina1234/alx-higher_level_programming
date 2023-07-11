#!/usr/bin/python3

import sys

metrics = {
    '200': 0,
    '301': 0,
    '400': 0,
    '401': 0,
    '403': 0,
    '404': 0,
    '405': 0,
    '500': 0
}

total_file_size = 0
count = 0

try:
    for line in sys.stdin:
        count += 1
        data = line.split()

        if len(data) > 2:
            status_code = data[-2]
            file_size = int(data[-1])
            total_file_size += file_size

            if status_code in metrics:
                metrics[status_code] += 1

        if count % 10 == 0:
            print(f"File size: {total_file_size}")
            for code, value in sorted(metrics.items()):
                if value > 0:
                    print(f"{code}: {value}")

except KeyboardInterrupt:
    pass

finally:
    print(f"File size: {total_file_size}")
    for code, value in sorted(metrics.items()):
        if value > 0:
            print(f"{code}: {value}")
