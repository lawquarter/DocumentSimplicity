
## Overview

This is a Streamlit-based web application that allows users to analyze the readability of documents. It supports multiple file formats (PDF, DOCX) and direct text input. The app calculates various readability metrics and provides visualizations to compare documents across different categories.

## Features

- Upload multiple PDF and DOCX files
- Paste text directly for analysis
- Categorize documents (e.g., NECF, VIC)
- Calculate multiple readability metrics:
  - Flesch Reading Ease
  - Flesch-Kincaid Grade
  - SMOG Index
  - Coleman-Liau Index
  - Automated Readability Index
  - Dale-Chall Readability Score
  - Linsear Write Formula
  - Gunning Fog
- Visualize readability scores with interactive charts
- Compare readability across different document categories
- Export results as CSV

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/readability-analyzer.git
   cd readability-analyzer
   ```

2. Create a virtual environment (optional but recommended):
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Run the Streamlit app:
   ```
   streamlit run app.py
   ```

2. Open your web browser and go to `http://localhost:8501` (or the URL provided in the terminal).

3. Use the sidebar to select the input method (file upload or text input) and document category.

4. Upload files or paste text as needed.

5. Click the "Analyze Readability" button to process the documents.

6. View the results in the main panel, including readability scores and visualizations.

7. Use the "Download results as CSV" button to export the analysis results.

## Contributing

Contributions to the Readability Analyzer are welcome! Please follow these steps to contribute:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and commit them with clear, descriptive messages.
4. Push your changes to your fork.
5. Submit a pull request to the main repository.

Please ensure your code adheres to the existing style and includes appropriate tests and documentation.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

If you have any questions, issues, or suggestions, please open an issue on the GitHub repository or contact the maintainer at [connor@compliancequarter.com.au].

## Acknowledgments

- [Streamlit](https://streamlit.io/) for the web application framework
- [textstat](https://pypi.org/project/textstat/) for readability metrics calculations
- [PyPDF2](https://pypdf2.readthedocs.io/) and [python-docx](https://python-docx.readthedocs.io/) for document parsing
- [Plotly](https://plotly.com/python/) for interactive visualizations
