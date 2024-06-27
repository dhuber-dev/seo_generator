import sys
import argparse
from docx import Document
from openai import OpenAI

template_path = 'seo_example.docx'
# prompt = f"Schreibe einen SEO Text zum Produkt {product_name}. Für das Produkt existieren die Kategorien {product_categories}."


def find_and_replace(doc, text2find, text2insert):
    for paragraph in doc.paragraphs:
        if text2find in paragraph.text:
            paragraph.text = paragraph.text.replace(text2find, text2insert)


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

    text_to_add = 'sample text'

    doc = Document(template_path)  # Load the template
    find_and_replace(doc, text2find='<product_name>', text2insert=args.product_name)  # Insert the product name
    doc.save(args.output_path)  # Save the new document
    print(f"Text added and new document saved as {args.output_path}")
