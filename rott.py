from ip2geotools.databases.noncommercial import DbIpCity
import time

try:
        print("""

█▀▀█ █▀▀█ ▀▀█▀▀ ▀▀█▀▀ █░░░█ █▀▀ ░▀░ █░░ █▀▀ █▀▀█ 
█▄▄▀ █░░█ ░░█░░ ░░█░░ █▄█▄█ █▀▀ ▀█▀ █░░ █▀▀ █▄▄▀ 
▀░▀▀ ▀▀▀▀ ░░▀░░ ░░▀░░ ░▀░▀░ ▀▀▀ ▀▀▀ ▀▀▀ ▀▀▀ ▀░▀▀
        """)
        print("""by:𝖉𝖗.𝖉𝖊𝖕𝖊""")
        print('-----------')
        print('')
        ip = input("Enter the IP adress:")
        print('')
        for x in range (0,5):  
         b = "Locating" + "." * x
         print (b, end="\r")
         time.sleep(1)
        #real shit starts here
        response = DbIpCity.get(ip, api_key='free')
        print('')
        print('')
        print("===========informations===========")
        print('IP adress: '+str(response.ip_address))
        print('City: '+response.city)
        print('Reigon: '+response.region)
        print('Latitude: '+ str(response.latitude))
        print('Longitude: '+ str(response.longitude))
        print('===================================')
except KeyboardInterrupt:
        print('')
        print("exited")