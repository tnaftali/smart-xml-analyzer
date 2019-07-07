class HtmlItem(object):
    def __init__(self, html_code, path):
        self.html_code = " ".join(str(html_code, 'utf-8').split())
        self.path = path
    
    def tostring(self):
        print("\tHTML Code: {}\n\tXPath: {}\n".format(self.html_code, self.path))