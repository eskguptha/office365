# Office365 using shareplum
Getting started is easy. Just create some credentials you will use to connect to SharePoint with HttpNtlmAuth and pass the url and credentials to the Site object. 
https://shareplum.readthedocs.io/en/latest/tutorial.html

# Office365 using REST API
https://pypi.org/project/Office365-REST-Python-Client/

Office 365 Authentication
For Office 365 Sharepoint is just as easy. The Office365 class grabs a login token from Microsoft’s login servers then It logins the Sharepoint site and uses the cookie for Authentication. Make sure to put just the root url for the site in Office365 and add Https:// at start.

Access REST API
You can access aditional features by utilizing the SharePoint REST API in SharePlum. To access this API you must specify a SharePoint version higher than 2013 when creating your Site object.

SharePoint Versions
The available version options are given below:

Version.v2007 (default)
Version.v2010
Version.v2013
Version.v2016
Version.v2019
Version.v365
There are currently only 2 actual versions implemented: 2007 and 365. v2010 is an alias for v2007 and v2013, v2016, and v2019 are aliases for v365.


