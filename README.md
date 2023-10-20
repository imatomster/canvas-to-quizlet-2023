# Flashcards Conversion Script

This script is designed to read HTML files, extract question-answer pairs, and write them to new text files. It's useful for converting structured HTML content into a plain text format that can be imported into tools like Quizlet.

## Prerequisites

Before you download and run this script, you must have Python installed on your computer. If you don't have Python, you can download it from [python.org](https://www.python.org/downloads/). This script was tested with Python 3.8, but it should work with other versions as well.

You also need to have `beautifulsoup4` installed in your Python environment since the script uses Beautiful Soup for HTML parsing. You can install it using pip:

```
pip install beautifulsoup4
```

## How to Download

1. Clone the repository containing the script. If the script is hosted on a platform like GitHub, you can use the following command:

   ```
   git clone <URL of the repository>
   ```

   Replace `<URL of the repository>` with the actual URL of the Git repository hosting the script.

   If you prefer, you can also download the repository as a ZIP file and then extract it on your local machine.

2. Navigate to the directory containing the script:

   ```
   cd <directory-containing-script>
   ```

   Replace `<directory-containing-script>` with the name of the directory.

## How to Use ! ! !

1. First go to Canvas and right click the page -> save as an HTML and download it

2. Before running the script, put all the canvas files you want to download in the input folder.

3. You can run the script using the following command:

   ```
   python main.py
   ```

4. The script will output all the question: answer pairings in output, from which you can copy and paste into Quizlet.

## Delimeters

The current delimeters are as follows:

- between question and answerTOMMYISCOOLANDISABELLAISNOT
- between each question: ISABELLAISCOOLANDTOMMYISNOT
