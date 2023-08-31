# Make PDF from Colab Notebook 📋

Simple utility function that lets you convert your colab notebook(s) to PDF(s).

## Usage
1. Verify the notebook you want to convert is shared to "anyone with the link" with at least "viewer" privilege 
2. Verify the notebook you want to convert is executed and saved.
3. Copy & Paste the below code in a new code cell, at the bottom of the notebook you whant to make a PDF
    
```bash
!rm -rf colab_to_pdf.py
!wget https://raw.githubusercontent.com/hurshd0/colab_notebook_to_pdf/master/colab_to_pdf.py
from colab_to_pdf import colab_to_pdf
colab_to_pdf(r"sample_notebook\.ipynb")
```
3. Wait about a minute (on first run) for the file to be sent to your browser
