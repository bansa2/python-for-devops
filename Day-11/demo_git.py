import requests

durl = requests.get("https://api.github.com/repos/kubernetes/kubernetes/pulls")

if durl.status_code == 200:
    ddata = durl.json()
    op = {}
 
    for dta in ddata:
        rj = dta["user"]["login"]
        if rj in ddata:
            op[rj] += 1
        else:
            op[rj] = 1
    print("Pr creator list")

    for rj,count in op.items():
        print(f"{rj}: {count} PR(s)")

else:
    print("Please enter correct url")