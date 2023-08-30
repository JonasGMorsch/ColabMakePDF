# Original code from Stackoverflow
# https://stackoverflow.com/questions/60748816/convert-google-colab-notebook-to-pdf-html

# Modified to add https://github.com/t-makaro/nb_pdf_template Makaro's template that
# fixes any margin related issues.

def colab_to_pdf(notebook_pattern: str, notebooks_folder_name = 'Colab Notebooks'):

    """Simple utility function that converts colab notebooks to pdf.


    Parameters
    ----------
    notebook_pattern: str
        You can use either notebook file name or regex pattern to find notebooks you want to
        convert to PDFs.
        e.g. notebook_pattern = "kaggle.+./ipynb" will find notebooks that contain the prefix `kaggle`

    notebooks_folder_name: str
        Colab notebooks folder name, by default it's `Colab Notebooks` you can change it to any other folder you like. 
    """

    import os, glob
    import re, pathlib 
    
    if not isinstance(notebook_pattern, str):
        raise TypeError(f"variable passed was not a string object, instead it is {type(notebook_pattern)} object.")
    
    # Mount gdrive if not mounted
    gdrive_mount_point = '/content/drive'
    if not os.path.isdir(gdrive_mount_point):
        from google.colab import drive
        drive.mount(gdrive_mount_point, force_remount=True)

    notebooks_folder_path = gdrive_mount_point / pathlib.Path(f"MyDrive/{notebooks_folder_name}")  
    # Verify is colab notebooks path is valid
    if not os.path.isdir(notebooks_folder_path):
        raise FileNotFoundError(f"noteboooks folder path {notebooks_folder_path} not found, try again!")

    # Get a list of all your Notebooks
    notebooks = [x for x in pathlib.Path(notebooks_folder_path).iterdir() if 
             re.search(notebook_pattern, x.name, flags = re.I)]

    if not (len(notebooks) > 0):
        raise FileNotFoundError(f"can't find the notebooks given {notebook_pattern} regex pattern ☹️, Please Try Again!")

    # Install nbconvert dependencies
    get_ipython().system("apt update && apt install texlive-xetex texlive-fonts-recommended texlive-generic-recommended")

    # Check if template exists, remove it if it does
    old_templates = glob.glob("*.tplx*" )
    if len(old_templates) > 0:
        print("="*80)
        print(f"\n\nFound {len(old_templates)} template(s), removing them...") 
        for template in old_templates:
            print(f"\t removing {template}")
            os.remove(template)
    print("="*80)
    # Add Makaro's classic template that fixes any margin related issues.
    get_ipython().system("wget https://raw.githubusercontent.com/t-makaro/nb_pdf_template/master/nb_pdf_template/templates/classic.tplx")
    

    # Convert found notebooks to PDF
    for i, n in enumerate(notebooks):
        print(f"\nProcessing  [{i+1:{len(str(len(notebooks)))}d}/{len(notebooks)}]  {n.name}\n")
        try:
            get_ipython().system(f"jupyter nbconvert --to pdf '{n.as_posix()}'")
        except:
            return("nbconvert error")
        
    return('File converted successfully and saved to Google Drive, please check your Colab Notebooks folder 😄')
