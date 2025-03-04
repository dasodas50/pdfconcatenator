from pypdf import PdfReader, PdfWriter


def insert_pages_between_pairs(input_pdf_path: str = 'input.pdf', body_pdf_path: str = 'body.pdf', output_pdf_base_path: str = 'Output', input_page_order: list = [0]) -> None:
    """This function inserts the pages of the input PDF file between the pages of the body PDF file."""

    # Open the input PDF file and the body PDF file
    input_pdf = PdfReader(input_pdf_path)
    body_pdf = PdfReader(body_pdf_path)

    # Count the number of pages in the input and body PDF files and the multiplier
    num_input_pages = len(input_pdf.pages)
    num_body_pages = len(body_pdf.pages)
    multiplier = len(input_page_order)

    # Check if the number of pages in the input document is correct
    if num_input_pages % multiplier != 0:
        raise ValueError(f"Count of pages in the input document must be multiple of multiplier: {multiplier}.")

    for order in input_page_order:
        if order > num_body_pages + multiplier or order < 0:
            raise ValueError(f"""Invalid page order in the input_page_order list: {order}.
                             Be careful, the page count starts from 0.""")

    # Index of the current output pdf
    doc_index = 1

    for i in range(0, num_input_pages, multiplier):

        output_pdf = PdfWriter()
        output_page_index = 0
        added_input_pages = 0

        while output_page_index < num_body_pages + multiplier or added_input_pages < multiplier:

            if output_page_index in input_page_order:
                output_pdf.add_page(input_pdf.pages[i + added_input_pages])
                output_page_index += 1
                added_input_pages += 1
                continue
            output_pdf.add_page(body_pdf.pages[output_page_index - added_input_pages])
            output_page_index += 1

        # Записуємо результуючий PDF
        with open(f"{output_pdf_base_path}_{doc_index}.pdf", "wb") as output_file:
            output_pdf.write(output_file)
            doc_index += 1


if __name__ == '__main__':

    # Path to the input PDF file
    input_pdf_path = 'input.pdf'
    # Path to the body pdf file
    body_pdf_path = 'body.pdf'
    # Base path for the output PDF files
    output_pdf_base_path = 'Output'
    # List of page orders in the input PDF file
    input_page_order = [0]

    insert_pages_between_pairs(input_page_order=input_page_order)
