# SEO Document Generator

This project automates the generation of SEO documents using a template and input from various sources. It extracts sections from a text, replaces placeholders in a Word document, and saves the result.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Installation

To set up the project, clone the repository and install the necessary dependencies.

```bash
# Clone the repository
git clone https://github.com/dhuber-dev/seo_generator.git

# Navigate to the project directory
cd seo-document-generator

# Create a virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

# Install dependencies
pip install -r requirements.txt
```

## Usage

To generate an SEO document, follow these steps:

1. Ensure you have a template document (`seo_example.docx`) and a scenario text file (`scenario.txt`) in your project directory. Guidance on format and content of such files, can be found [here](#required-files)

2. Run the script with the necessary arguments.

```bash
python main.py --company_name "Your Company" --product_name "Your Product" --product_categories "Category1" "Category2" --output_path "output.docx"
```

## Features

- **Find and Replace in Word Documents:** Replace placeholders in a Word document.
- **Extract Sections:** Extract sections from a text using a regular expression.
- **Copy to Clipboard:** Copy generated prompts to the clipboard for easy access.
- **Generate SEO Document:** Combine all functionalities to generate a formatted SEO document.

## Required Files
You need to create a scenario text file `scenario.txt` and a Word document `seo_example.docx`.
- `scenario.txt`: Provide information about the scenario in which the LLM should see itself. The scenario positions the writer (LLM) as an SEO copywriter tasked with creating optimized content for a specific product or service. It is best to predefine the sections and their length. A sample can be found in the repository.
- `seo_example.docx`: You can use any format or template you want and design everything in Word. The script just replaces `<flags>` with the content provided by the LLM. Thus, make sure you include flags such as `<section_x>` or `<product_name>`. An example for the content would be:
     ```
     SEO-Text for <product_name>
     
     Summary
     <section_0>
     
     Types of <product_name>
     <section_1>
     
     Possible use cases of <product_name>
     <section_2>
     ```

## Contributing

We welcome contributions! Please follow these steps to contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

For questions or suggestions, you can reach me here:

- GitHub: [dhuber-dev](https://github.com/dhuber-dev)