#!/usr/bin/env python3

import os
import argparse
import sys
import time

def count_lines_of_code(directory, exclude_folders=None, ignore_extensions=None):
    total_lines = 0
    file_count = 0

    for root, dirs, files in os.walk(directory):
        # Exclude specific folders if provided
        if exclude_folders is not None:
            dirs[:] = [d for d in dirs if d not in exclude_folders]

        for file in files:
            file_extension = os.path.splitext(file)[1]
            if ignore_extensions is not None and file_extension in ignore_extensions:
                continue

            file_path = os.path.join(root, file)
            try:
                with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
                    lines = f.readlines()
                    total_lines += len(lines)
            except (IOError, OSError) as e:
                print(f"Error reading file: {file_path}. {e}", file=sys.stderr)

            file_count += 1

    return total_lines, file_count

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Count lines of code in a project, excluding specific folders and extensions.")
    parser.add_argument("directory", help="Project directory path")
    parser.add_argument("-e", "--exclude", nargs="+", help="Folders to exclude from line count")
    parser.add_argument("-i", "--ignore", nargs="+", help="Extensions to ignore")

    args = parser.parse_args()
    project_directory = args.directory
    excluded_folders = args.exclude if args.exclude is not None else []
    ignored_extensions = args.ignore if args.ignore is not None else []

    start_time = time.time()
    line_count, file_count = count_lines_of_code(project_directory, exclude_folders=excluded_folders, ignore_extensions=ignored_extensions)
    end_time = time.time()

    print("Total lines of code:", line_count)
    print("Total files processed:", file_count)
    print("Execution time:", round(end_time - start_time, 2), "seconds")
