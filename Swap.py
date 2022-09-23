arr = [
    [3, 4, 6],
    [4, 7, 9],
    [7, 8, 2]
]
arr2 = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]
ip_c = ["127.0.128.1",
        "127.0.0.1",
        "17..0.1",
        "32sdrqew.sj.589.21",
        "432l.321.234.592",
        "432.321.234.592",
        "321234981774489",
        "..............",
        "0.1.2.3.4.5.6.7.8.9",
        "213.45.1.8",
        "1.2.3.4",
        "32.21.1.345",
        ".2.3.45.6.",
        "23456768......",
        "         .        .        ",
        "1.2.3.4",
        "208.109.181.228"
        ]
available = ["0", "1", "2", "3", "4", "5", "6", "7", "8", '9', "."]

def ip_valid(ip):
    total = ""
    times = 0
    stall = 0
    time = 0
    for i in range(len(ip)):
        if ip[i] in available:
            stall += 1
        elif not ip[i] in available:
            #print(ip[i])
            return "Not a Valid IP Address"
        if not ip[i] == ".":
            total += ip[i]
            #print(len(total))
            #print(len(total))
            #print(total)
        elif ip[i] == ".":
            times = times + 1
            if len(total)>0:
                if len(total) <= 3:
                    time = time + 1
                    #print(time)
                    #print(len(total))
                    total = ""
                else:
                    return "Not a Valid IP Address"
            else:
                return "Not a Valid IP Address"
        if len(total) >= 4:
            return "Not a Valid IP Address"
    if time == 3:
        stall = 0
    else:
        return "Not a Valid IP Address"
    if times == 3:
        return "This is a Valid IP Address"
    else:
        return "Not a Valid IP Address"


for ip in ip_c:

    result = ip_valid(ip)
    print(ip,result)
sums = [0, 1, 2, 6, 10]
sum = []
def run(start,list):
    var = 0
    for i in range(len(start)):
        var = var + start[i]
        list.append(var)
    return list
res = run(sums, sum)
print(res)
print(res)

