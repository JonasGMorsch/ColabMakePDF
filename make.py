# Jonas G. Morsch
#
# Credits to:
# https://stackoverflow.com/questions/60748816/convert-google-colab-notebook-to-pdf-html
# https://github.com/hurshd0/colab_notebook_to_pdf/

import re, pathlib, os
from google.colab import files

def prepare():
    get_ipython().system("pip install ipynbname --quiet")
    import ipynbname
    script_id = ipynbname.name()[7:]
    get_ipython().system("gdown {script_id}")
    return

def pdf():
    prepare()
    get_ipython().system("pip install pypandoc --quiet")
    get_ipython().system("apt-get install texlive texlive-xetex texlive-latex-extra pandoc --quiet")
    # Get a list of all ipynb in /content/
    for filepath in pathlib.Path("/content/").iterdir():
        if re.search(r"\w+.ipynb\b", filepath.name):
            get_ipython().system("jupyter nbconvert --to PDF '{filepath}' --log-level ERROR")
            files.download(os.path.splitext(str(filepath))[0]+".pdf")
    return
    
def html():
    prepare()
    # Get a list of all ipynb in /content/
    for filepath in pathlib.Path("/content/").iterdir():
        if re.search(r"\w+.ipynb\b", filepath.name):
            get_ipython().system("jupyter nbconvert --to html '{filepath}' --log-level ERROR")
            files.download(os.path.splitext(str(filepath))[0]+".html")
    return
