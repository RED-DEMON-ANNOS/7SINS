import os,platform
os.system('git pull')
 
bsn=platform.architecture()[0]
if bsn=="32bit":
    __import__("ss").menu()
elif bsn=="64bit":
    __import__("zsins").menu()
 
