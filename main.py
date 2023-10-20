import re
from bs4 import BeautifulSoup
import os
import sys
import glob


def convert(file: str) -> dict:
    soup = BeautifulSoup(file, 'html.parser')
    display_qs = soup.find_all('div', class_='display_question')

    pair = {}
    for display in display_qs:
        question = display.find('div', class_='question_text').get_text()
        # print(question)

        ans_list = []
        answers = display.find_all('div', class_='correct_answer')
        for ans in answers:
            answer = ans.select('.select_answer .answer_text')
            ans_list.extend([a.get_text() for a in answer])

        pair[question] = ans_list[0]
    return pair


def write_pairs(pairs: dict, location: str):
    base_name = os.path.basename(location)
    name_without_extension = os.path.splitext(base_name)[0]
    output_file_path = os.path.join("./output", f"{name_without_extension}.txt")

    with open(output_file_path, "w", encoding="utf8") as f:
        for key in pairs.keys():
            f.write(f"{key}TOMMYISCOOLANDISABELLAISNOT{pairs[key]}ISABELLAISCOOLANDTOMMYISNOT")

    print(f'Flashcards written to {output_file_path}. To import into Quizlet:')

def main(folder_path):
    # Check if input folder exists
    if not os.path.exists(folder_path):
        print(f"The folder {folder_path} does not exist")
        return

    # Create a pattern for all files in the folder
    file_pattern = os.path.join(folder_path, '*')  # * means all files

    # Use glob to find all files in the folder
    files = glob.glob(file_pattern)

    for input_file in files:
        # Process each file
        file = open(input_file, "r", encoding="utf8").read().strip()
        pairs = convert(file)
        
        # Write the processed content to a new .txt file
        write_pairs(pairs, input_file)

if __name__ == "__main__":
    main("./input")