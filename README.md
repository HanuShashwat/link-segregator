# Link Segregator

A simple Python utility script to efficiently segregate a mixed collection of links into two distinct categories: "Liked Links" and "Disliked Links". The script automatically filters the URLs and exports the segregated lists into clean, easy-to-read Excel spreadsheets.

## Features
- Fast O(1) filtering algorithm using Python sets.
- Automatically handles data formatting and exports to Excel (`.xlsx`).
- Flexibile input options: reads from both text files or hardcoded Python lists.
- Preserves the original order of your mixed links.

## Prerequisites
To run this project, you need to have the following installed on your system:
- **Python 3.6+**: You can download it from [python.org](https://www.python.org/downloads/).
- **pip**: The Python package installer (comes pre-installed with Python).

## Installation

1. **Clone the repository** (or download the project files):
   ```bash
   git clone https://github.com/HanuShashwat/link-segregator.git
   cd link-segregator
   ```

2. **Install the required dependencies**:
   The script relies on `pandas` and `openpyxl` to process data and generate Excel files. Install them by running:
   ```bash
   pip install -r requirements.txt
   ```

## Working Examples & Usage

Depending on the size of your lists, there are two ways to feed your data into the script.

### Method 1: Using Text Files (Recommended)
This is the best method for processing a large number of URLs.

1. Create a file named `liked_links.txt` in the main folder and paste your favorite URLs into it (one URL per line).
2. Create a file named `all_links.txt` in the main folder and paste your entire mixed collection of URLs into it (one URL per line).
3. Ensure the script is set up to read these files (lines 27 and 28 in `main.py` should be uncommented):
   ```python
   liked_links = read_links_from_file('liked_links.txt')
   all_links = read_links_from_file('all_links.txt')
   ```

### Method 2: Hardcoding Lists in the Script
If you only have a few links or want to do a quick test, you can paste them directly into the Python code.

1. Open `main.py`.
2. Locate the `liked_links` and `all_links` variables inside the `main()` function and replace the example URLs with your own:
   ```python
   liked_links = [
       "https://example.com/liked1",
       "https://example.com/liked2",
       "https://example.com/liked3"
   ]
   
   all_links = [
       "https://example.com/disliked1",
       "https://example.com/liked2",
       "https://example.com/liked1",
       "https://example.com/disliked2",
       "https://example.com/liked3"
   ]
   ```

### Running the Script

Once you have provided your data using either method above, run the following command in your terminal:
```bash
python main.py
```

### Output
The script will process your links and generate two new files in your project directory:
- **`liked_links.xlsx`**: Contains all the links you specifically marked as liked.
- **`disliked_links.xlsx`**: Contains all the remaining links from your mixed list that were not in your liked list.

> **Note:** The text (`.txt`) and Excel (`.xlsx`) files are intentionally ignored by `.gitignore` so your personal links aren't accidentally pushed to a public repository.

## Contact
If you have any queries, need help, or have suggestions for improvements, feel free to contact me at **[hanu@gaprio.in](mailto:hanu@gaprio.in)**.
