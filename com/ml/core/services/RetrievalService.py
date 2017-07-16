import os,json
def retrieveData():
    output = os.system("ohai >> /tmp/ohai")
    with open('/tmp/ohai', 'r') as content_file:
        return content_file.read()

