# Code Line Counter

The Code Line Counter is a script that counts the lines of code in a project. It provides the flexibility to exclude specific paths and file extensions from the line count.

## Features

- Counts the lines of code in your project.
- Allows excluding specific paths and file extensions from the line count.
- Supports various programming languages and file types.

## Usage

1. Ensure you have Python installed on your system (version 3 or above).
2. Clone this repository or download the `count_lines.py` script.
3. Open a terminal or command prompt and navigate to the directory where the script is located.
4. Run the script using the following command: 
```shell
python count_lines.py [project_directory] [-e EXCLUDE_FOLDERS...] [-i IGNORE_EXTENSIONS...]
```
- Replace `[project_directory]` with the path to your project directory.
- Use the optional `-e` or `--exclude` flag followed by one or more folder names to exclude specific folders from the line count.
- Use the optional `-i` or `--ignore` flag followed by one or more file extensions to ignore specific file extensions during the line count.

5. The script will display the total lines of code in the project, excluding the specified folders and file extensions.

## Requirements

- Python 3.x

## Optional Progress Bar

The script can optionally utilize the `tqdm` package to display a progress bar during the line counting process. If the `tqdm` package is installed, the progress bar will be displayed. If it is not installed, a simple print statement will be used instead.

To install the `tqdm` package, use the following command:
```shell
pip install tqdm
```

If you don't wish to use the progress bar or prefer not to install the `tqdm` package, you can still run the script without any issues.

## Example Usage

Count the lines of code in a project directory:
```shell
python count_lines.py /path/to/your/project
```

- Count lines of code in a project, excluding the `tests` and `docs` folders:
```shell
python count_lines.py /path/to/your/project -e tests docs
```

- Count lines of code in a project, excluding the `tests` folder and ignoring `.txt` and `.log` file extensions:
```shell
python count_lines.py /path/to/your/project -e tests -i .txt .log
```

## Notes

- The script currently supports counting lines of code for files encoded in UTF-8.

## License

This script is licensed under the [MIT License](LICENSE).
