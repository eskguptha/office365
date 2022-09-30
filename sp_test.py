
from SPConnector import SharePointConnector

FILE_DIR_PATH = "Your File Location Path"

# this will be the file name that it will be saved in SharePoint as 
FILE_NAME = 'FILE-NAME-WITH-EXTENSION'

# The folder in SharePoint that it will be saved under
FOLDER_NAME = '2020'

# Upload file to Office365 Sharepoint Directory
SharePointConnector().upload_file(FILE_DIR_PATH, FILE_NAME, FOLDER_NAME)

# Delete file in Office365 Sharepoint Directory 
SharePointConnector().delete_file(FILE_NAME, FOLDER_NAME)
