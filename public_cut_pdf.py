#it cuts a pdf long his vertical in half
#remember to custom the code in the last line before running it

from PyPDF2 import PdfReader, PdfWriter
import copy

def split_pdf_vertically(input_pdf_path, output_pdf_path):
    reader = PdfReader(input_pdf_path)
    writer = PdfWriter()

    for page in reader.pages:
        original_width = page.mediabox.upper_right[0]
        original_height = page.mediabox.upper_right[1]

        # Creazione delle copie delle pagine originali
        left_page = copy.deepcopy(page)
        right_page = copy.deepcopy(page)

        # Imposta le nuove dimensioni del mediabox per la pagina di sinistra
        left_page.mediabox.upper_right = (original_width / 2, original_height)

        # Imposta le nuove dimensioni del mediabox per la pagina di destra
        right_page.mediabox.lower_left = (original_width / 2, 0)

        # Aggiunta delle pagine al writer
        writer.add_page(left_page)
        writer.add_page(right_page)

    # Salvataggio del nuovo PDF
    with open(output_pdf_path, "wb") as output_pdf:
        writer.write(output_pdf)

# Uso della funzione
split_pdf_vertically("path/of/source.pdf", "path/of/final_product.pdf")
