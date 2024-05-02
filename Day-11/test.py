import requests

demo_url = requests.get("https://api.github.com/repos/kubernetes/kubernetes/pulls")

if demo_url.status_code == 200:
    pull_data = demo_url.json()

    pull_output = {}

    for pull in pull_data:
        ddata = pull["user"]["login"]
        if ddata in pull_data:
            pull_output[ddata] += 1
        else:
            pull_output[ddata] = 1
        
    print("Below is the detail of user and pr created")

    for ddata,count in pull_output.items():
        print(f"{ddata}: {count} PR(s)")

else:
    print("YOur url is wrong with status code",{demo_url.status_code})