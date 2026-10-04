#!/usr/bin/env python3
import json, os, random, re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
DATA = ROOT / "data" / "cases.json"
SAVE = Path.home() / ".blacktrace_save.json"

RANKS = [(0, "Rookie"), (250, "Analyst"), (700, "Investigator"), (1400, "Elite"), (2500, "Blacktrace")]

def load_cases():
    with DATA.open(encoding="utf-8") as f:
        return json.load(f)

def load_state():
    if SAVE.exists():
        try:
            return json.loads(SAVE.read_text(encoding="utf-8"))
        except Exception:
            pass
    return {"xp": 0, "solved": [], "achievements": []}

def save_state(state):
    SAVE.write_text(json.dumps(state, ensure_ascii=False, indent=2), encoding="utf-8")

def rank_for(xp):
    current = RANKS[0][1]
    for need, name in RANKS:
        if xp >= need:
            current = name
    return current

def clear():
    os.system("clear" if os.name != "nt" else "cls")

def banner():
    print("\033[1;36m╔══════════════════════════════════════╗")
    print("║          BLACKTRACE v1.0             ║")
    print("║        CYBER OSINT CTF — TERMUX      ║")
    print("╚══════════════════════════════════════╝\033[0m")

def pause():
    input("\nNhấn Enter để tiếp tục...")

def show_profile(state):
    solved = len(state["solved"])
    print(f"\n⭐ XP: {state['xp']}  |  Rank: {rank_for(state['xp'])}")
    print(f"🕵️ Cases solved: {solved}")
    print(f"🏆 Achievements: {len(state['achievements'])}")

def show_case(case, discovered=None):
    discovered = discovered or set()
    print(f"\n\033[1;33mCASE #{case['id']} — {case['title']}\033[0m")
    print(f"Difficulty: {case['difficulty']}")
    print(f"Objective: {case['objective']}\n")
    for i, clue in enumerate(case["clues"], 1):
        mark = "✓" if clue["id"] in discovered else "?"
        print(f"[{i}] {mark} {clue['label']}")

def reveal_clue(case, discovered):
    hidden = [c for c in case["clues"] if c["id"] not in discovered]
    if not hidden:
        print("\nTất cả clue đã được mở.")
        return
    clue = random.choice(hidden)
    discovered.add(clue["id"])
    print(f"\n🔎 {clue['label']}")
    print(clue["value"])

def use_tool(case):
    print("\n🧰 TOOLS")
    tools = ["search", "whois", "dns", "ipinfo", "metadata", "logs", "timeline", "decode"]
    for i, tool in enumerate(tools, 1):
        print(f"[{i}] {tool}")
    choice = input("> ").strip()
    if not choice.isdigit() or not 1 <= int(choice) <= len(tools):
        print("Tool không hợp lệ.")
        return
    tool = tools[int(choice)-1]
    print(f"\n[{tool}] Đang phân tích dữ liệu mô phỏng...")
    matches = [c for c in case["clues"] if tool in c.get("tools", [])]
    if matches:
        for c in matches:
            print(f"→ {c['label']}: {c['value']}")
    else:
        print("→ Không tìm thấy kết quả liên quan trong dữ liệu case này.")

def solve_case(case, state):
    if case["id"] in state["solved"]:
        print("\n✓ Case này đã hoàn thành.")
        return

    discovered = set()
    while True:
        clear(); banner(); show_case(case, discovered)
        print("\n[a] Mở clue  [t] Tool  [f] Nhập FLAG  [q] Thoát case")
        cmd = input("> ").strip().lower()
        if cmd == "a":
            reveal_clue(case, discovered); pause()
        elif cmd == "t":
            use_tool(case); pause()
        elif cmd == "f":
            flag = input("FLAG> ").strip()
            if flag == case["flag"]:
                state["solved"].append(case["id"])
                state["xp"] += case["xp"]
                if len(state["solved"]) == 1 and "first_case" not in state["achievements"]:
                    state["achievements"].append("first_case")
                    print("\n🏆 Achievement unlocked: FIRST TRACE")
                print(f"\n🚩 FLAG đúng! +{case['xp']} XP")
                save_state(state); pause(); return
            print("\n❌ FLAG sai.")
            pause()
        elif cmd == "q":
            return

def missions(cases, state):
    while True:
        clear(); banner()
        print("\n📂 MISSIONS")
        for c in cases:
            status = "✓" if c["id"] in state["solved"] else " "
            print(f"[{c['id']}] [{status}] {c['title']} — {c['difficulty']} — {c['xp']} XP")
        print("[0] Back")
        choice = input("> ").strip()
        if choice == "0": return
        try:
            case = next(c for c in cases if c["id"] == int(choice))
            solve_case(case, state)
        except (ValueError, StopIteration):
            print("Case không hợp lệ."); pause()

def main():
    cases = load_cases()
    state = load_state()
    while True:
        clear(); banner()
        show_profile(state)
        print("\n[1] 🕵️ Missions")
        print("[2] 🔎 Investigation")
        print("[3] 🧰 Tools")
        print("[4] ⭐ Profile")
        print("[5] 🏆 Achievements")
        print("[6] 💾 Save")
        print("[0] Exit")
        choice = input("\n> ").strip().lower()
        if choice == "1":
            missions(cases, state)
        elif choice == "2":
            print("\n🔎 Investigation mở từ từng Mission để giữ gameplay theo case.")
            pause()
        elif choice == "3":
            print("\n🧰 Các tool: search, whois, dns, ipinfo, metadata, logs, timeline, decode")
            print("Tất cả chỉ hoạt động trên dữ liệu giả lập.")
            pause()
        elif choice == "4":
            clear(); banner(); show_profile(state); pause()
        elif choice == "5":
            clear(); banner()
            print("\n🏆 ACHIEVEMENTS")
            print("✓ FIRST TRACE — Hoàn thành case đầu tiên" if "first_case" in state["achievements"] else "○ FIRST TRACE — Chưa mở khóa")
            pause()
        elif choice == "6":
            save_state(state); print("💾 Đã lưu."); pause()
        elif choice in ("0", "q"):
            save_state(state)
            print("\nBlacktrace session closed.")
            return

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nBlacktrace session closed.")
