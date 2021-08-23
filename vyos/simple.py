import getpass
import vymgmt

# getpass.getpass(prompt='Password: ', stream=None) 
vyos = vymgmt.Router('172.31.255.250', 'vyos', password=getpass.getpass(prompt='Password: ', stream=None), port=22)

vyos.login()
vyos.configure()
vyos.set("set system host-name "test-vyos"")

vyos.commit()
vyos.save()
vyos.exit()
vyos.logout()
