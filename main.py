import sys
from docx import Document
from openai import OpenAI

prompt = f"Schreibe einen SEO Text zum Produkt {product_name}. Für das Produkt existieren die Kategorien {product_categories}."


def add_text_to_template(template_path, text_to_add, output_path):
    doc = Document(template_path)  # Load the template
    doc.add_paragraph(text_to_add)  # Add the text to the end of the document
    doc.save(output_path)  # Save the new document


def get_gpt_proposal(prompt):
    openai_client = OpenAI()

    response = openai_client.chat.completions.create(
        model="text-embedding-3-large",  # Use the GPT-4 model
        messages=prompt,
        max_tokens=150,  # Adjust the number of tokens as needed
        n=1,
        stop=None,
        temperature=0.7
    )

    # Extract and return the proposal text
    proposal_text = response['choices'][0]['message']['content'].strip()
    return proposal_text


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python script.py <product_name> <product_categories> <output_path>")
        sys.exit(1)

    # text_to_add = get_gpt_proposal(prompt)
    product_name = sys.argv[1]
    product_categories = sys.argv[2]
    output_path = sys.argv[3]

    add_text_to_template(template_path, text_to_add, output_path)
    print(f"Text added and new document saved as {output_path}")
