import random
import string
import os

USERS = 2

def loadIPAddresses():
    gpus_ip = []
    f = open('./ip_addresses_gpu.txt', 'r')
    for l in f:
        gpus_ip.append(l[:-1])
    f.close()

    cpus_ip = []
    f = open('./ip_addresses_cpu.txt', 'r')
    for l in f:
        cpus_ip.append(l[:-1])
    f.close()

    assert len(gpus_ip) == len(cpus_ip)
    ret = []
    for i in range(len(gpus_ip)):
        ret.append((gpus_ip[i], cpus_ip[i]))

    return ret

def randomStringDigits(stringLength=6):
    """Generate a random string of letters and digits """
    lettersAndDigits = string.ascii_letters + string.digits
    return ''.join(random.choice(lettersAndDigits) for i in range(stringLength))

def createPage(ip, username, key):
    
    filename = './keys/'+key+'.md'
    if not os.path.exists(os.path.dirname(filename)):
        try:
            os.makedirs(os.path.dirname(filename))
        except OSError as exc: # Guard against race condition
            if exc.errno != errno.EEXIST:
                raise

    f = open(filename, 'w+')
    f.write("---\n")
    f.write("layout: default\n")
    f.write("comments: false\n")
    f.write("permalink: /"+key+"/\n")
    f.write("---\n")
    f.write("### Module: FPChecker\n")
    f.write("ssh "+username+"@"+ip[0]+"\n")
    f.write("### Module: FLiT, Precimonious, ADAPT\n")
    f.write("ssh "+username+"@"+ip[1]+"\n")
    f.close()

def main():
    global USERS
    
    print "Genarating keys..."
    
    ips = loadIPAddresses()
    
    f = open('user.txt', 'w')
    f.write('-----\n')
    for ip in ips:
        for n in range(USERS):
            username = "user"+str(n+1)
            key = randomStringDigits(8)
            createPage(ip, username, key)
            f.write('http://fpanalysistools.org/'+key+'\n')
            f.write('username: '+username+'\n')
            f.write('-----\n')

    f.close()


main()
