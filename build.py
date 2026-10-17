# build.py: inline the CRM's leads.json into template.html -> index.html
import json, os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
leads = json.load(open("../locallift-crm/leads.json", encoding="utf-8"))
keep = ("id", "cat", "batch", "name", "contact", "phone", "rating", "reviews", "area", "site", "video", "note")
leads = [{k: l.get(k, "") for k in keep} for l in leads]
t = open("template.html", encoding="utf-8").read()
assert t.count("/*LEADS*/[]") == 1
data = json.dumps(leads, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")
open("index.html", "w", encoding="utf-8").write(t.replace("/*LEADS*/[]", data))
print(len(leads), "leads ->", "index.html")
