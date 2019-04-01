#! python3
# Call this function by:
# import wordGetText - which is the name of the python file.
# print(wordGetText.getText('<insert name of docx file>'))

import docx
def getText(filename):
    doc = docx.Document(filename)
    fullText = []
    for para in doc.paragraphs:
        fullText.append(para.text)
    return '\n'.join(fullText)
