# Make PDF (and HTML!) from Colab Notebook 📋

Simple utility function that lets you convert your colab notebook(s) to PDF(s).

## Usage
1. Verify the notebook you want to convert is shared to "anyone with the link" with at least "viewer" privilege 
2. Verify the notebook you want to convert is executed and saved.
3. Copy & Paste the below code in a new code cell, at the bottom of the notebook and run it, to make a PDF:
    
```bash
!wget -O make.py https://raw.githubusercontent.com/JonasGMorsch/ColabMakePDF/master/make.py
import make; make.pdf()
```
or, for HTML:

```bash
!wget -O make.py https://raw.githubusercontent.com/JonasGMorsch/ColabMakePDF/master/make.py
import make; make.html()
```
4. Wait about a minute (on first run) for the file to be sent to your browser
