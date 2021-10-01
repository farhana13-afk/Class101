import dropbox

class TransferData: 
    def __init__(self, access_token):
        self.access_token = access_token
    
    def uploadFile(self, fileFrom, fileTo):
        dbx = dropbox.Dropbox(self.access_token)
        with open(fileFrom, 'rb') as f:
            dbx.files_upload(f.read(), fileTo)


def main():
    access_token = 'sl.A5izZ1U4r5wWB1-rFLT56HZ59FrspVVglYZIGdgovVmT2W3sGvozhumkoO24nz_phheNDkjKSUaP_kM7lPlgCyghygbR8dZRHPyCulJioUtZFGcfDAn3iJV81eilz7CP_n7uxk8'
    transferData = TransferData(access_token)
    fileFrom = 'test.txt'
    fileTo = '/test_dropbbox/ test.txt'
    transferData.uploadFile(fileFrom, fileTo)

main()