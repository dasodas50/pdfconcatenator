# PDFConcatenator - Insert Pages Between Pairs

This Python script is designed to insert pages of an input PDF between the pages of a body PDF according to a specified order. It generates output PDFs with the interleaved pages optimized for scenarios like contracts, agreements, and NDAs.

## Use Cases

This tool is ideal for managing documents with identical main bodies but varying specific pages (e.g., first and last). It efficiently assembles these PDFs by interleaving scanned unique pages with a consistent body document.

### How It Works

1. **Scenario**: For documents that are 10 pages long with unique first and last pages:
   
2. **Preparation**:
   - **Scan Unique Pages**: Scan only differing pages (e.g., first and last pages).
   - **Stacking**: Stack them sequentially (e.g., first-last, first-last).
   - **Input File**: Compile these pages into a single PDF to use alongside your `body.pdf`.

3. **Using the Script**:
   - Specify the order using a list (e.g., `[0, 9]` for 10-page documents).
   - Run the script with your specified PDFs and page order.

4. **Output**:
   - The script outputs complete PDFs by placing unique pages in their specified positions.
   - Craft documents according to variations or needs, regardless of sets’ unique page counts.

## Requirements and Constraints

To ensure correct operation, follow these guidelines:

- **File Naming**: 
  - Default input PDF: `input.pdf`.
  - Default body PDF: `body.pdf`.
  - Modify these names directly in the script or pass alternative arguments.

- **Page Order List**:
  - Use consecutive numbers [e.g., `0, 1, 2, 3`] in increasing order.
  - Begin from zero (zero-based indexing).
  - Ensure list values are within total page count limits (e.g., max index for 15 pages is 14).
  - Format must be a list, even for a single value (e.g., `[0]`).

- **Considerations**:
  - Ensure the body is scanned once, saved as `body.pdf`.
  - Confirm total page numbers to adjust `input_page_order` correctly.

### Example Command

Given a `[0, 9]` `input_page_order` for a 10-page document:

```python
insert_pages_between_pairs(
    input_pdf_path='input.pdf',
    body_pdf_path='body.pdf',
    output_pdf_base_path='Output',
    input_page_order=[0, 9]
)
```

This integrates specified pages, producing finalized documents efficiently.

### Example

For processing 5 documents:
- Scan, stack, and utilize an order like `[0, 9]`.
- The script produces 5 PDFs, each correctly assembled.

## Features

- Interleave pages based on specified insertion order.
- Automatic generation of multiple output PDFs.
- Customize outputs to match different document requirements.

## Requirements

- Python 3.x
- [pypdf package](https://pypi.org/project/pypdf/)

## Installation

Clone and set up the repository:

```bash
git clone https://github.com/yourusername/your-repo-name.git
cd your-repo-name
```

Install dependencies:

```bash
pip install pypdf
```

## Usage

Place your `input.pdf` and `body.pdf` in the directory or specify paths:

Execute the script:

```bash
python your_script_name.py
```

### Parameters

- **input_pdf_path**: Path for input PDF.
- **body_pdf_path**: Path for body PDF.
- **output_pdf_base_path**: Naming base for output PDFs.
- **input_page_order**: Positions in `body.pdf` for insertion.

Customize for various documents:

### Steps to Customize

1. **Duplicate the Script**: For new document types, copy script and rename (e.g., `process_contracts.py`).

2. **Adjust Paths**:
   - Set `input_pdf_path` and `body_pdf_path` for particular documents.

3. **Modify Page Order**:
   - Adjust `input_page_order` as needed for the document type.

4. **Tailor Output Naming**:
   - Ensure `output_pdf_base_path` reflects purpose (e.g., `Output_Contracts`).

5. **Optional Enhancements**:
   - Consider abstracting logic for varying configurations.

### Example Configuration

#### Script 1: Processing Contracts
```python
input_pdf_path = 'input_contracts.pdf'
body_pdf_path = 'body_contracts.pdf'
output_pdf_base_path = 'Output_Contracts'
input_page_order = [0, 9]
```

#### Script 2: Processing NDAs
```python
input_pdf_path = 'input_ndas.pdf'
body_pdf_path = 'body_ndas.pdf'
output_pdf_base_path = 'Output_NDAs'
input_page_order = [1, 7]
```

## Acknowledgments

- Thanks to existing PDF tools for inspiration.
- Uses the pypdf library for PDF operations.
