E=open
D=print
import requests as C,json
D('Created by @JJ minimized for better speed <3')
def A(name):
	B=name;A=C.get(f"https://scratch.mit.edu/accounts/check_username/{B}/");A=A.json()[0];F=A['msg']
	if F=='valid username':D(f"Good username : {B}");A=E('goodAccounts.txt','a').write(f"\n{B}\n")
for B in E('usernamestocheck.txt').read().splitlines():A(B)
#created by jj this doesn't count as a line FYI
