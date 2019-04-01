import imapclient
import implib
import pyzmail
import bs4
import webbrowser

implib._MAXLINE=10000000
imapObj = imapclient.IMAPClient('imap.gmail.com', ssl=True)
imapObj.login(input('Enter email login -> '), input('Enter your email password -> '))
imapObj.select_folder('INBOX', readonly=True)
UIDs = imapObj.search(['SINCE', '01-Mar-2019'])
foundElements=[]
for emailAddr in UIDs:
    rawMessages = imapObj.fetch(emailAddr,  ['BODY[]', 'FLAGS'])
    message = pyzmail.PyzMessage.factory(rawMessages[emailAddr][b'BODY[]'])
    try:
        stuff=message.html_part.get_payload().decode(message.html_part.charset)
    except:
        print('Could not download this message!!!')
        continue
    soup=bs4.BeautifulSoup(stuff)    
    elem=soup.select('a')
    for i in range(0,  len(elem)):
        #print(i)
        #print(elem[i].getText())
        if 'subscription' in elem[i].getText():
            foundElements.append(elem[i].get('href'))
            break
    if len(foundElements)==1:
        break
for link in foundElements:
    webbrowser.open(link)    
print(foundElements)
imapObj.logout()
