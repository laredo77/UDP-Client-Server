import socket
import sys
import time


def update_line(data):
    # Deletes the line that needs to be updated #
    with open(sys.argv[4], "r") as file:
        lines = file.readlines()
    with open(sys.argv[4], "w") as file:
        for line in lines:
            if data not in line:
                file.write(line)


def final_time(ttl):
    # Returning the current time plus ttl #
    ts = time.time()
    ts = ts + int(ttl)
    return ts


def isLegal(current_final_time):
    # Checks whether the ttl of line is valid #
    ts = time.time()
    if ts > float(current_final_time):
        return False
    return True


def learn_line(new_data):
    # Learns a new address and adds it to the txt file #
    # To each new address adding time stamp #
    ttl = new_data.split(',')[2].rstrip()
    current_final_time = final_time(ttl)
    new_data = new_data.rstrip() + ',' + str(current_final_time) + '\n'
    f = open(sys.argv[4], "a")
    f.write(new_data)
    f.close()


def string_in_file(name_of_file, str1):
    # Checks whether the address in the file #
    with open(name_of_file, 'r') as readFile:
        # Searching the line in the file #
        for line in readFile:
            if str1 in line:
                try:
                    # The line already learned in the past #
                    # Recognized by time stamp in arg 3 #
                    if isLegal(line.split(',')[3]) is True:
                        return line
                    if isLegal(line.split(',')[3]) is False:
                        update_line(str1)
                except:
                    # The line is static #
                    # No time stamp in arg 3 #
                    return line

        # Doesnt founded in the current file #
        # Send the data to its parent #
        s.sendto(data, (sys.argv[2], int(sys.argv[3])))
        new_data, new_addr = s.recvfrom(1024)
        learn_line(new_data.decode('utf-8'))
        return new_data.decode('utf-8')


s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('', int(sys.argv[1])))

while True:
    data, addr = s.recvfrom(1024)
    b = string_in_file(sys.argv[4], data.decode('utf-8')).encode('utf-8')
    s.sendto(b, addr)
