import os, csv, subprocess

CSVPATH = '/HOSTS.CSV'

MAC=subprocess.check_output("esxcli network ip interface list |grep MAC | cut -d ' ' -f 6",shell=True)
                                                                                                                                                                                                                                                                                    
MACADDR = MAC.split()
print("MAC Addresses:")
print(MACADDR)
with open(CSVPATH, 'rt') as csvFile:
        csvReader = csv.reader(csvFile)
        for csvRow in csvReader:
                if ((MACADDR[0]).decode('utf-8')) == csvRow[1]:
                        print("Running: esxcli system hostname set --fqdn=" + csvRow[0])
                        print("running: esxcli network ip interface ipv4 set --interface-name=vmk0 --ipv4=" + csvRow[2] + " --netmask=" + csvRow[3] + " --type=static --gateway=" + csvRow[4])
                        os.system("esxcli system hostname set --fqdn=" + csvRow[0])
                        os.system("esxcli network ip interface ipv4 set --interface-name=vmk0 --ipv4=" + csvRow[2] + " --netmask=" + csvRow[3] + " --type=static --gateway=" + csvRow[4])