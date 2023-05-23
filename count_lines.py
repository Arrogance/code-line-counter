#!/usr/bin/env python3

import os
import argparse
import sys
import time
import fnmatch

def count_lines_of_code(file_path):
    try:
        with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
            lines = f.readlines()
            return len(lines)
    except (IOError, OSError) as e:
        print(f"Error reading file: {file_path}. {e}", file=sys.stderr)
        return 0

def count_lines_parallel(directory, exclude_folders=None, ignore_extensions=None, ignore_files=None):
    file_paths = []
    for root, dirs, files in os.walk(directory):
        # Exclude specific folders if provided
        if exclude_folders is not None:
            dirs[:] = [d for d in dirs if d not in exclude_folders]

        for file in files:
            file_extension = os.path.splitext(file)[1]
            if ignore_extensions is not None and file_extension in ignore_extensions:
                continue

            file_path = os.path.join(root, file)

            # Ignore specific file names using wildcard patterns
            if ignore_files is not None and any(fnmatch.fnmatch(file, pattern) for pattern in ignore_files):
                continue

            file_paths.append(file_path)

    total_lines = 0
    try:
        from tqdm import tqdm
        progress_bar = tqdm(total=len(file_paths), desc="Counting lines in files")
        for file_path in file_paths:
            line_count = count_lines_of_code(file_path)
            total_lines += line_count
            progress_bar.update(1)
        progress_bar.close()
    except ImportError:
        for file_path in file_paths:
            line_count = count_lines_of_code(file_path)
            total_lines += line_count

    return total_lines, len(file_paths)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Count lines of code in a project, excluding specific folders, extensions, and files.")
    parser.add_argument("directory", help="Project directory path")
    parser.add_argument("-e", "--exclude", nargs="+", help="Folders to exclude from line count")
    parser.add_argument("-i", "--ignore", nargs="+", help="Extensions to ignore")
    parser.add_argument("-f", "--ignore-files", nargs="+", help="File names to ignore (supports wildcard patterns)")

    args = parser.parse_args()
    project_directory = args.directory
    excluded_folders = args.exclude if args.exclude is not None else []
    ignored_extensions = args.ignore if args.ignore is not None else []
    ignored_files = args.ignore_files if args.ignore_files is not None else []

    start_time = time.time()
    line_count, file_count = count_lines_parallel(project_directory, exclude_folders=excluded_folders, ignore_extensions=ignored_extensions, ignore_files=ignored_files)
    end_time = time.time()

    print("Total lines of code:", line_count)
    print("Total files processed:", file_count)
    print("Execution time:", round(end_time - start_time, 2), "seconds")
