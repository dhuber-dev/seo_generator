# -*- coding: utf-8 -*-
import argparse
from docx import Document
import re
import pyperclip


def find_and_replace(doc, text2find, text2insert):
    for paragraph in doc.paragraphs:
        if text2find in paragraph.text:
            paragraph.text = paragraph.text.replace(text2find, text2insert)


def extract_sections(text):
    section_pattern = r"##+ (.+?)\n\n(.+?)(?=##+ |\Z)"  # Regex pattern to capture each section
    extracted_sections = re.findall(section_pattern, text, re.DOTALL)
    return extracted_sections


if __name__ == "__main__":
    # Create ArgumentParser object
    parser = argparse.ArgumentParser(description='Create a new SEO text.')

    # Add positional arguments
    parser.add_argument('--product_name', type=str, help='Name of the product.')
    parser.add_argument('--product_categories', type=str, nargs='+',
                        help='Categories or types of the product (usually extracted from website filters).')
    parser.add_argument('--output_path', type=str, help='Output path for the resulting SEO docx-File.')

    args = parser.parse_args()  # Parse the arguments from command line

    if not (args.product_name and args.product_categories and args.output_path):
        parser.print_help()
        exit(1)

    """ BUILD PROMPT """
    prompt = (f"Schreibe einen SEO Text zum Produkt {args.product_name}. "
              f"Für das Produkt existieren die Kategorien {args.product_categories}.")

    # Open scenario text in read mode
    scenario_text_path = 'scenario.txt'
    with open(scenario_text_path, 'r', encoding='utf-8') as file:
        scenario = file.read()  # Read text from file

    full_prompt = scenario + '\n' + prompt
    pyperclip.copy(full_prompt)
    input('The generated prompt has been copied to your clipboard. Hit enter when you have copied and saved the LLM '
          'response to "response.txt"...')

    """ GET LLM RESPONSE """
    # TODO integrate LLM API of choice
    with open('response.txt', 'r', encoding='utf-8') as file:
        llm_response = file.read()  # Read text from file

    """ EXTRACT SECTIONS FROM LLM RESPONSE """
    sections = extract_sections(llm_response)

    # Print each section
    for section in sections:
        section_title = section[0]
        section_content = section[1]
        print(f"### {section_title}\n")
        print(section_content.strip())
        print("\n")

    """ GENERATE DOCUMENT """
    template_path = 'seo_example.docx'
    doc = Document(template_path)  # Load the template
    find_and_replace(doc, text2find='<product_name>', text2insert=args.product_name)  # Insert the product name

    for idx, (section_title, section_text) in enumerate(sections):
        find_and_replace(doc, text2find=f'<section_{idx}>', text2insert=section_text.replace('\n\n', ' '))
    doc.save(args.output_path)  # Save the new document
    print(f"Text added and new document saved as {args.output_path}")
