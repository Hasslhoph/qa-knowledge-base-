import json, urllib.request, urllib.parse, os

TOKEN = os.environ["GITLAB_TOKEN"]
LAST = open(".yana_last_commit").read().strip()
API = "https://gitlab.wehive.digital/api/v4/projects/194"
VAULT = os.getcwd()

changed = []
page = 1
while page <= 10:
    url = f"{API}/repository/commits?ref_name=master&per_page=50&page={page}"
    req = urllib.request.Request(url, headers={"PRIVATE-TOKEN": TOKEN})
    commits = json.loads(urllib.request.urlopen(req).read())

    found = False
    for c in commits:
        if c["id"] == LAST:
            found = True
            break
        diff_url = f"{API}/repository/commits/{c['id']}/diff"
        diff_req = urllib.request.Request(diff_url, headers={"PRIVATE-TOKEN": TOKEN})
        diff_raw = urllib.request.urlopen(diff_req).read().decode("utf-8", "replace")
        for df in json.loads(diff_raw):
            p = df.get("new_path", "")
            if p.startswith("modules/") and p.endswith(".md") and not df.get("deleted_file"):
                changed.append(p)
    if found:
        break
    page += 1

if changed:
    with open("files.txt", "w") as f:
        for path in sorted(set(changed)):
            enc = urllib.parse.quote(path, safe="")
            raw_url = f"{API}/repository/files/{enc}/raw?ref=master"
            raw_req = urllib.request.Request(raw_url, headers={"PRIVATE-TOKEN": TOKEN})
            content = urllib.request.urlopen(raw_req).read()
            basename = path.split("/")[-1]
            with open(os.path.join(VAULT, basename), "wb") as fw:
                fw.write(content)
            f.write(path + "\n")
