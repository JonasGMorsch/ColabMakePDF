# Original code from Stackoverflow
# https://stackoverflow.com/questions/60748816/convert-google-colab-notebook-to-pdf-html

def makepdf():

    get_ipython().system("pip install pypandoc")
    get_ipython().system("pip install ipynbname")
    get_ipython().system("apt-get install texlive texlive-xetex texlive-latex-extra pandoc")
    
    import re, pathlib, shutil, os, ipynbname
    from google.colab import files, output
    
    script_name = ipynbname.name()[7:]
    get_ipython().system("gdown {script_name}")
    
    # Get a list of all ipynb in /content/
    for filepath in pathlib.Path("/content/").iterdir():
        if re.search(r"\w+.ipynb\b", filepath.name):
            #print(filepath)
            output.clear() # erase collab console
            get_ipython().system("jupyter nbconvert --to PDF '{filepath}'")
            files.download(os.path.splitext(str(filepath))[0]+".pdf")
    return
