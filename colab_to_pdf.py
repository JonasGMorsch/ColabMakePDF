# Original code from Stackoverflow
# https://stackoverflow.com/questions/60748816/convert-google-colab-notebook-to-pdf-html


###################### Check if  libary is on this runtime #####################

    try:
        import ipynbname
    except:
        %pip install ipynbname
        import ipynbname
        from google.colab import output
        output.clear() # erase collab console
    ################################################################################

#!apt-get install texlive texlive-xetex texlive-latex-extra pandoc
!apt-get install texlive-xetex
!pip install pypandoc
import re, pathlib, shutil, os
from google.colab import files

def colab_to_pdf():
    script_name = ipynbname.name()[7:]
    !gdown $script_name
    
    
    
    # Get a list of all ipynb in /content/
    for filepath in pathlib.Path("/content/").iterdir():
        if re.search(r"\w+.ipynb\b", filepath.name):
            print(filepath)
            output.clear() # erase collab console
            !jupyter nbconvert --to PDF {filepath}
            files.download(os.path.splitext(str(filepath))[0]+".pdf")
    
    #output.clear() # erase collab console
    return
