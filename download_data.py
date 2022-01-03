import os
import gdown
import zipfile
# id of goodle drive = 1OletxmPYNkz2ltOr9pyT0b0iBtUWxslh

url = 'https://drive.google.com/uc?id=1OletxmPYNkz2ltOr9pyT0b0iBtUWxslh'
downloaded_zip_file = 'NERdata.zip'
gdown.download(url, downloaded_zip_file, quiet=False)
# now let's unzip the sownloaded zip file 
with zipfile.ZipFile(downloaded_zip_file, 'r') as zip_ref:
    zip_ref.extractall('NERdata')
    
    
# remove the zip file

os.remove(downloaded_zip_file) 


# use only one data