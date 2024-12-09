""" Advent of Code solver """
with open("aoc2024/9/input.txt", 'r', encoding='utf8') as file_handle:
    inp = file_handle.readline().strip()

def updatelowestfree(spaces, position, lowestfree):
    if spaces not in lowestfree or lowestfree[spaces] > position:
        lowestfree[spaces] = position

def checksum(disk):
    return sum(pos * int(val) for pos, val in enumerate(disk) if val != ".")

def defrag(disk):
    return [val for val in disk if val != "."]

def getbest(space, lowestfree):
    return min((pos for s, pos in lowestfree.items() if s >= space), default=99999999)

def setnextlowest(val, freespaces, lowestfree):
    for i in sorted(freespaces.keys()):
        if freespaces[i] == val:
            lowestfree[val] = i
            break

def changefilealloc(files, freespaces, lowestfree):
    newfiles = {}
    for oldpos in reversed(files):
        newpos = getbest(files[oldpos][1], lowestfree)
        if newpos >= oldpos:
            newfiles[oldpos] = files[oldpos]
        else:
            newfiles[newpos] = files[oldpos]
            spaceleft = freespaces[newpos] - files[oldpos][1]
            if spaceleft > 0:
                freespaces[newpos + files[oldpos][1]] = spaceleft
            freespaces.pop(newpos)
            newfreespace = files[oldpos][1]
            afterpos = oldpos + files[oldpos][1]
            if afterpos in freespaces:
                newfreespace += freespaces.pop(afterpos)
            freebefore = oldpos
            while freebefore not in freespaces and freebefore >= 0:
                freebefore -= 1
            if freebefore >= 0 and freebefore + freespaces[freebefore] == oldpos:
                freespaces[freebefore] += newfreespace
            else:
                freespaces[oldpos] = newfreespace
            setnextlowest(files[oldpos][1] + spaceleft, freespaces, lowestfree)
            if spaceleft > 0:
                setnextlowest(spaceleft, freespaces, lowestfree)
    return newfiles

def allocfiles(files, disk_length):
    newdisk = []
    offset = 0
    while offset < disk_length:
        if offset in files:
            newdisk.extend([files[offset][0]] * files[offset][1])
            offset += files[offset][1]
        else:
            newdisk.append(".")
            offset += 1
    return newdisk

def task1(disk):
    return checksum(defrag(disk))

def task2(files, freespaces, lowestfree, disk_length):
    newfiles = changefilealloc(files, freespaces, lowestfree)
    return checksum(allocfiles(newfiles, disk_length))

disk = []
freespaces = {}
lowestfree = {}
files = {}
id = 0
for pos, val in enumerate(inp):
    fill = "."
    if pos % 2 == 0:
        fill = id
        files[len(disk)] = [id, int(val)]
        id += 1
    else:
        if int(val) > 0:
            freespaces[len(disk)] = int(val)
            updatelowestfree(int(val), len(disk), lowestfree)
    disk.extend([fill] * int(val))

disk_length = len(disk)

print(task2(files, freespaces, lowestfree, disk_length))
print(task1(disk))
