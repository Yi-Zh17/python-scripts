import HtmlMaker
import SSH

word_doc = str(input("Source file directory: "))
doc_title = str(input("Title: "))

server = str(input("Server: "))
password = str(input("Password: "))

destination = str(input("Destination: "))

# Put modified article in output folder
DOC_MODIFIED = "output/" + HtmlMaker.get_doc_fullname(word_doc)

print("Generating html code……")
HtmlMaker.page_build(word_doc, DOC_MODIFIED, doc_title)
print("Building webpage……")
HtmlMaker.html_maker(DOC_MODIFIED)
print("Uploading to server……")
SSH.ssh_tranfer(server, password, DOC_MODIFIED, destination)
print("Complete！")