# 🕵️ BLACKTRACE

**Cyber OSINT CTF song ngữ Việt / English chạy trực tiếp trên Termux.**

> Game điều tra kỹ thuật số với dữ liệu hoàn toàn giả lập. Người chơi thu thập manh mối, phân tích username/domain/IP/log/metadata và tìm FLAG.

## ✨ Tính năng
- 🇻🇳 Tiếng Việt + 🇬🇧 English, chuyển đổi ngay trong game
- 🎓 **BLACKTRACE ACADEMY** dành cho newbie
- 🕵️ 5 case mẫu, từ Rookie đến Investigator
- 🔎 Username, domain, IP, metadata, logs và timeline
- 🧩 Clue + FLAG + XP + rank
- 🧰 Tool điều tra mô phỏng
- 💾 Lưu tiến trình và ngôn ngữ đã chọn
- 🏆 Achievement
- 📱 Tối ưu Termux/màn hình điện thoại
- 🛡️ Không quét mạng thật, không thu thập dữ liệu thật

## 🌐 Song ngữ

Lần đầu chạy mặc định là **Tiếng Việt**. Vào:

**Menu → [7] Language / Ngôn ngữ**

để chuyển giữa **Tiếng Việt** và **English**. Lựa chọn được lưu trong `~/.blacktrace_save.json`.

Case và mục tiêu có bản tiếng Anh; dữ liệu kỹ thuật như username, domain, IP, log và FLAG được giữ nguyên để gameplay không bị thay đổi.

## 🎓 BLACKTRACE ACADEMY
1. OSINT là gì?
2. Username Investigation
3. Domain & DNS
4. IP Investigation
5. Metadata
6. Log & Timeline

Người mới có thể học Academy trước rồi chuyển sang **Missions** để thực hành.

## 📲 Cài đặt
```bash
pkg update
pkg install python git -y
git clone https://github.com/khahdihdz/blacktrace-termux.git
cd blacktrace-termux
chmod +x install.sh
./install.sh
blacktrace
```

Hoặc: `python3 blacktrace.py`

## 🎮 Menu
- `1` Missions
- `2` BLACKTRACE Academy
- `3` Investigation
- `4` Tools
- `5` Profile
- `6` Achievements
- `7` Language / Ngôn ngữ
- `8` Save
- `0` Exit

Trong case: `a` mở clue · `t` dùng tool · `f` nhập FLAG · `q` thoát case

## 🛡️ An toàn
BLACKTRACE là **game mô phỏng**. Username, domain, IP, log, metadata và các kết quả điều tra đều là dữ liệu giả lập. Công cụ không thực hiện reconnaissance, scanning hoặc truy vấn mục tiêu thật.

## 🧪 CI
Mỗi push và pull request tự động kiểm tra JSON, localization Việt/English, compile Python và test.

## 📄 License

BLACKTRACE được phát hành theo **MIT License**.

Copyright © 2026 khahdihdz

Xem toàn văn tại file `LICENSE` trong repository.