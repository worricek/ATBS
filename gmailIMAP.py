import imapclient
import implib

pw=input()
lg=input()
searchFilter=input()

implib._MAXLINE=10000000
imapObj = imapclient.IMAPClient('imap.gmail.com', ssl=True)
imapObj.login(lg,pw)
imapObj.select_folder('INBOX', readonly=True)
UIDs = imapObj.search(['FROM',  searchFilter])
rawMessages = imapObj.fetch(UIDs, ['BODY[]', 'FLAGS'])
import pyzmail
message = pyzmail.PyzMessage.factory(rawMessages[42217][b'BODY[]'])
message.get_subject()
message.get_addresses('from')
message.get_addresses('to')
message.get_addresses('cc')
message.get_addresses('bcc')
message.text_part != None
message.text_part.get_payload().decode(message.text_part.charset)
message.html_part != None
message.html_part.get_payload().decode(message.html_part.charset)

# Deleting  emails
imapObj.select_folder('INBOX', readonly=False)
UIDs = imapObj.search(['ON'', ''09-Jul-2015'])
UIDs
imapObj.delete_messages(UIDs)
{40066: ('\\Seen', '\\Deleted')}
imapObj.expunge()

imapObj.logout()
