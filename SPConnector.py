import os
import json
from shareplum import Site, Office365
from shareplum.site import Version

USERNAME = "Your Email Id"
PASSWORD = "Your Passowrd"
SHAREPOINT_URL = "https://{domain}.sharepoint.com"
SHAREPOINT_SITE = "https://{domain}.sharepoint.com/sites/{Name}/"
SHAREPOINT_DOC = "Shared Documents/{Document}"

class SharePointConnector:
    """ SharePointConnector Class for to upload, delete, read, get list of files in Office365 Sharepoint """
    def auth(self):
        self.authcookie = Office365(SHAREPOINT_URL, username=USERNAME, password=PASSWORD).GetCookies()
        self.site = Site(SHAREPOINT_SITE, version=Version.v365, authcookie=self.authcookie)

        return self.site

    def connect_folder(self, folder_name):
        self.auth_site = self.auth()

        self.sharepoint_dir = '/'.join([SHAREPOINT_DOC, folder_name])
        self.folder = self.auth_site.Folder(self.sharepoint_dir)

        return self.folder

    def upload_file(self, file, file_name, folder_name):
        self._folder = self.connect_folder(folder_name)

        with open(file, mode='rb') as file_obj:
            file_content = file_obj.read()

        self._folder.upload_file(file_content, file_name)

    def delete_file(self, file_name, folder_name):

        self._folder = self.connect_folder(folder_name)

        self._folder.delete_file(file_name)
        
    def get_files(self, folder_name):
      pass
