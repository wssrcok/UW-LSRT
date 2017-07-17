import urllib2

site = urllib2.urlopen("https://sdb.admin.uw.edu/timeschd/uwnetid/sln.asp?QTRYR=AUT+2017&SLN=13862")
content = site.read()
if "** Closed **" in content:
    print("Closed!")
else:
   print("Open!")
