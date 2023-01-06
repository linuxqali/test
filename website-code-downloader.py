import urllib.request as u 

website_name = input("Enter Your Web-Site Name :")

source = u.urlopen(website_name)

source_read = source.read()

print(source_read)