readmounts = open("/proc/mounts", "r")
    mountlist = readmounts.readlines()
    readmounts.close
    for i in range(len(mountlist)):
        splitmount = mountlist[i].split(" ")
        for g in range(len(splitmount)):
            if splitmount[g] == "/":
                print(mountlist[i])
    
    lsdiskcommand = "lsblk -d -n -oNAME,RO | grep '0$' | awk {'print $1'}"
    result = subprocess.Popen([lsdiskcommand], universal_newlines=True, shell=True, stdout=subprocess.PIPE)
    resultstdout = result.communicate()[0]
    diskinventory = resultstdout.splitlines()
    for i in range(len(diskinventory)):
        print(diskinventory[i])