# Python module

# Pavel_Karunas_Day4_Github Api Requests

**Description:**
1. This application takes following parameters at start:
	- --owner <username> (required)
	- --repo <reponame>
	- --created
	- --updated
	- --pushed
	- --issues
	- --subs
	- --version
2. Owner parameter determines Github username from which we will be gathering information (about user itself or his repo if --repo parameter specified).
3. Repo parameter determines Github repository name that belongs to user specified in required parametr.
4. Created parameter if used, shows repository creation date.
5. Updated parameter if used, shows repository update date.
6. Pushed parameter if used, shows repository push date.
7. Issues parameter if used, shows number of open issuies at repository.
8. Subs parameter if used, shows number of subscribers to repository.
9. Subs parameter if used, shows number of open issuies at repository.
10. Version parameter if used, shows application version and exits.
11. If repo parameter not specified apllication show information (user ID, number of public and private repos) about Github user specified in mandatory parameter.
12. After application is launched you will be promted for username and password, this information will be used for authentication at Github.

**Requirements:**
Python version 3.6 or above
Installed Requests package

**Examples of use:**

$ git_v1.py --help

$ git_v1.py --version
 
$ git_v1.py --owner PavelKarunas --repo DevOps_Lab_LDAP --created --updated --pushed --issues --subs

$ git_v1.py --owner PavelKarunas --repo DevOps_Lab_LDAP --subs --issues

$ git_v1.py --owner PavelKarunas


