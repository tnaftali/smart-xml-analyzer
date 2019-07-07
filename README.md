# Smart XML Analyzer

## Running the app (Python 3 Needed)
### Installing Needed Dependencies (Just One)
```bash
pip3 install lxml
```
### Run command
```bash
python3 app.py <input_origin_file_path> <input_other_sample_file_path> <original_element_id>
```

### With Given Samples As Parameters
```bash
python3 app.py samples/sample-0-origin.html samples/sample-1-evil-gemini.html make-everything-ok-button

python3 app.py samples/sample-0-origin.html samples/sample-2-container-and-clone.html make-everything-ok-button

python3 app.py samples/sample-0-origin.html samples/sample-3-the-escape.html make-everything-ok-button

python3 app.py samples/sample-0-origin.html samples/sample-4-the-mash.html make-everything-ok-button
```

## Comparison output for sample pages
### sample-0-origin.html - sample-1-evil-gemini.html - make-everything-ok-button
```bash
Original Element:
        HTML Code: <a id="make-everything-ok-button" class="btn btn-success" href="#ok" title="Make-Button" rel="next" onclick="javascript:window.okDone(); return false;"> Make everything OK </a>
        XPath: /html/body/div/div/div[3]/div[1]/div/div[2]/a

Closest Element:
        HTML Code: <a class="btn btn-success" href="#check-and-ok" title="Make-Button" rel="done" onclick="javascript:window.okDone(); return false;"> Make everything OK </a>
        XPath: /html/body/div/div/div[3]/div[1]/div/div[2]/a[2]
```
### sample-0-origin.html - sample-2-container-and-clone.html - make-everything-ok-button
```bash
Original Element:
        HTML Code: <a id="make-everything-ok-button" class="btn btn-success" href="#ok" title="Make-Button" rel="next" onclick="javascript:window.okDone(); return false;"> Make everything OK </a>
        XPath: /html/body/div/div/div[3]/div[1]/div/div[2]/a

Closest Element:
        HTML Code: <a class="btn test-link-ok" href="#ok" title="Make-Button" rel="next" onclick="javascript:window.okComplete(); return false;"> Make everything OK </a>
        XPath: /html/body/div/div/div[3]/div[1]/div/div[2]/div/a
```
### sample-0-origin.html - sample-3-the-escape.html - make-everything-ok-button
```bash
Original Element:
        HTML Code: <a id="make-everything-ok-button" class="btn btn-success" href="#ok" title="Make-Button" rel="next" onclick="javascript:window.okDone(); return false;"> Make everything OK </a>
        XPath: /html/body/div/div/div[3]/div[1]/div/div[2]/a

Closest Element:
        HTML Code: <a class="btn btn-success" href="#ok" title="Do-Link" rel="next" onclick="javascript:window.okDone(); return false;"> Do anything perfect </a>
        XPath: /html/body/div/div/div[3]/div[1]/div/div[3]/a
```
### sample-0-origin.html - sample-4-the-mash.html - make-everything-ok-button
```bash
Original Element:
        HTML Code: <a id="make-everything-ok-button" class="btn btn-success" href="#ok" title="Make-Button" rel="next" onclick="javascript:window.okDone(); return false;"> Make everything OK </a>
        XPath: /html/body/div/div/div[3]/div[1]/div/div[2]/a

Closest Element:
        HTML Code: <a class="btn btn-success" href="#ok" title="Make-Button" rel="next" onclick="javascript:window.okFinalize(); return false;"> Do all GREAT </a>
        XPath: /html/body/div/div/div[3]/div[1]/div/div[3]/a
```