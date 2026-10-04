#!/usr/bin/env python3
import json, os, random
from pathlib import Path

ROOT = Path(__file__).resolve().parent
DATA = ROOT / "data" / "cases.json"
I18N = ROOT / "data" / "i18n.json"
SAVE = Path.home() / ".blacktrace_save.json"
RANKS = [(0,"Rookie"),(250,"Analyst"),(700,"Investigator"),(1400,"Elite"),(2500,"Blacktrace")]

def load(path):
    with path.open(encoding="utf-8") as f: return json.load(f)

def state():
    try: s = load(SAVE)
    except Exception: s = {}
    s.setdefault("xp",0); s.setdefault("solved",[]); s.setdefault("achievements",[]); s.setdefault("lang","vi")
    return s

def save(s): SAVE.write_text(json.dumps(s,ensure_ascii=False,indent=2),encoding="utf-8")
def rank(xp):
    r="Rookie"
    for need,name in RANKS:
        if xp >= need: r=name
    return r
def tr(ui,k,lang): return ui[lang].get(k,ui["en"].get(k,k))
def bi(ui,k): return f"{ui['vi'].get(k,k)} / {ui['en'].get(k,k)}"
def ctext(ui,c,k,lang):
    if k in ("title","objective") and lang=="en":
        return ui["cases"].get(str(c["id"]),{}).get(k,c.get(k,""))
    return c.get(k,"")
def clear(): os.system("clear" if os.name!="nt" else "cls")
def banner(ui,lang):
    print("\033[1;36m╔══════════════════════════════════════╗")
    print("║          BLACKTRACE v1.1             ║")
    print(f"║      {tr(ui,'banner',lang):^36}║")
    print("╚══════════════════════════════════════╝\033[0m")
def pause(ui,lang): input("\n"+tr(ui,"press",lang))

def profile(s,ui,lang):
    print(f"\n⭐ {tr(ui,'xp',lang)}: {s['xp']} | {tr(ui,'rank',lang)}: {rank(s['xp'])}")
    print(f"🕵️ {tr(ui,'cases_solved',lang)}: {len(s['solved'])}")
    print(f"🏆 {tr(ui,'achievements',lang)}: {len(s['achievements']) if 'achievements' in ui else len(s['achievements'])}")
    print(f"🌐 {tr(ui,'language',lang)}: {'Tiếng Việt' if lang=='vi' else 'English'}")

def show_case(c,seen,ui,lang):
    print(f"\n\033[1;33mCASE #{c['id']} — {ctext(ui,c,'title',lang)}\033[0m")
    print(f"{tr(ui,'difficulty',lang)}: {c['difficulty']}")
    print(f"{tr(ui,'objective',lang)}: {ctext(ui,c,'objective',lang)}\n")
    for i,x in enumerate(c["clues"],1):
        print(f"[{i}] {'✓' if x['id'] in seen else '?'} {x['label']}")

def tool(c,ui,lang):
    names=["search","whois","dns","ipinfo","metadata","logs","timeline","decode"]
    print("\n🧰 "+bi(ui,"tools"))
    for i,n in enumerate(names,1): print(f"[{i}] {n}")
    q=input("> ").strip()
    if not q.isdigit() or not 1<=int(q)<=len(names):
        print(tr(ui,"invalid",lang)); return
    name=names[int(q)-1]
    print(f"\n[{name}] {tr(ui,'analyzing',lang)}")
    hits=[x for x in c["clues"] if name in x.get("tools",[])]
    if hits:
        for x in hits: print(f"→ {x['label']}: {x['value']}")
    else: print("→ "+tr(ui,"noresult",lang))

def case_loop(c,s,ui,lang):
    if c["id"] in s["solved"]: print("\n✓ "+tr(ui,"already",lang)); pause(ui,lang); return
    seen=set()
    while True:
        clear(); banner(ui,lang); show_case(c,seen,ui,lang)
        print(f"\n[a] {tr(ui,'open',lang)}  [t] {tr(ui,'tool',lang)}  [f] {tr(ui,'flag',lang)}  [q] {tr(ui,'quit',lang)}")
        q=input("> ").strip().lower()
        if q=="a":
            hidden=[x for x in c["clues"] if x["id"] not in seen]
            if hidden:
                x=random.choice(hidden); seen.add(x["id"]); print(f"\n🔎 {x['label']}\n{x['value']}")
            else: print("\n"+tr(ui,"all",lang))
            pause(ui,lang)
        elif q=="t": tool(c,ui,lang); pause(ui,lang)
        elif q=="f":
            if input("FLAG> ").strip()==c["flag"]:
                s["solved"].append(c["id"]); s["xp"]+=c["xp"]
                if len(s["solved"])==1 and "first_case" not in s["achievements"]:
                    s["achievements"].append("first_case"); print("\n🏆 "+tr(ui,"first",lang))
                print(f"\n🚩 {tr(ui,'correct',lang)}{c['xp']} XP"); save(s); pause(ui,lang); return
            print("\n❌ "+tr(ui,"wrong",lang)); pause(ui,lang)
        elif q=="q": return

def missions(cases,s,ui,lang):
    while True:
        clear(); banner(ui,lang); print("\n📂 "+tr(ui,"missions",lang))
        for c in cases:
            mark="✓" if c["id"] in s["solved"] else " "
            print(f"[{c['id']}] [{mark}] {ctext(ui,c,'title',lang)} — {c['difficulty']} — {c['xp']} XP")
        print("[0] "+bi(ui,"back")); q=input("> ").strip()
        if q=="0": return
        try: case_loop(next(c for c in cases if c["id"]==int(q)),s,ui,lang)
        except (ValueError,StopIteration): print(tr(ui,"invalid",lang)); pause(ui,lang)

def academy(ui,lang):
    lessons=[("1","academy_1"),("2","academy_2"),("3","academy_3"),("4","academy_4"),("5","academy_5"),("6","academy_6")]
    while True:
        clear(); banner(ui,lang); print("\n🎓 "+bi(ui,"academy"))
        for n,k in lessons: print(f"[{n}] {tr(ui,k,lang)}")
        print("[0] "+tr(ui,"back",lang)); q=input("> ").strip()
        if q=="0": return
        k=dict(lessons).get(q)
        if k:
            clear(); banner(ui,lang); print("\n📘 "+tr(ui,k,lang)); print(tr(ui,k+"_body",lang)); pause(ui,lang)
        else: print(tr(ui,"invalid",lang)); pause(ui,lang)

def language_menu(s,ui):
    clear(); print("[1] 🇻🇳 Tiếng Việt\n[2] 🇬🇧 English\n[0] Back")
    q=input("> ").strip()
    if q=="1": s["lang"]="vi"; save(s)
    elif q=="2": s["lang"]="en"; save(s)

def main():
    cases=load(DATA); ui=load(I18N); s=state()
    while True:
        lang=s["lang"]; clear(); banner(ui,lang); profile(s,ui,lang)
        for n,k in [("1","missions"),("2","academy"),("3","investigation"),("4","tools"),("5","profile"),("6","achievements"),("7","language"),("8","save"),("0","exit")]:
            print(f"[{n}] {bi(ui,k)}")
        q=input("\n> ").strip().lower()
        if q=="1": missions(cases,s,ui,lang)
        elif q=="2": academy(ui,lang)
        elif q=="3": print("\n🔎 "+tr(ui,"investigation_note",lang)) or pause(ui,lang)
        elif q=="4": print("\n🧰 "+tr(ui,"toolnote",lang)) or pause(ui,lang)
        elif q=="5": clear(); banner(ui,lang); profile(s,ui,lang); pause(ui,lang)
        elif q=="6":
            clear(); banner(ui,lang); print("\n🏆 "+tr(ui,"achievements",lang))
            print("✓ FIRST TRACE — "+tr(ui,"achievement_desc",lang) if "first_case" in s["achievements"] else "○ FIRST TRACE — "+tr(ui,"locked",lang)); pause(ui,lang)
        elif q=="7": language_menu(s,ui)
        elif q=="8": save(s); print("💾 "+tr(ui,"saved",lang)); pause(ui,lang)
        elif q in ("0","q"): save(s); print("\nBlacktrace session closed."); return

if __name__=="__main__":
    try: main()
    except KeyboardInterrupt: print("\n\nBlacktrace session closed.")
