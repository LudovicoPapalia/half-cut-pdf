# half-cut-pdf
Cut a PDF in half

## GitHub README Description for PDF Splitting Code

### PDF Vertical Splitter

This Python script provides a convenient way to split PDF documents vertically in half. It is designed to handle PDF files of any length, efficiently processing an unlimited number of pages. The script automatically measures the horizontal length of each page and performs a central cut, saving the resulting halves into a new PDF file.

#### Features:
- **Automatic Measurement**: Automatically calculates the horizontal length of each PDF page.
- **Central Splitting**: Divides each page precisely in the middle.
- **Efficiency**: Capable of processing a large number of pages swiftly.
- **Flexibility**: Works with any standard PDF file.

#### How It Works:
The script utilizes the `PyPDF2` library to read and write PDF files. It creates deep copies of each page in the original PDF and then adjusts their dimensions to split them into left and right halves. These halves are then sequentially added to a new PDF document, which is saved to the specified output path.

#### Usage:
1. Ensure `PyPDF2` is installed in your Python environment.
2. Place the script in your project directory.
3. Modify the `split_pdf_vertically` function call at the end of the script with the path of your source PDF and the desired output path.
4. Run the script.

#### Example:
To split a PDF located at `path/of/source.pdf` and save the output to `path/of/final_product.pdf`, use the following line:
```python
split_pdf_vertically("path/of/source.pdf", "path/of/final_product.pdf")
```

#### Requirements:
- Python 3.x
- PyPDF2 library

*Note: The script is intended for use with standard PDF files. Non-standard or encrypted PDFs might require additional handling not covered by this script. This code and libraries may for some reason corrupt your files. Use the program only on backups and in any case use the code at your own risk.*
