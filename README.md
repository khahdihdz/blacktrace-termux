# 🕵️ BLACKTRACE

**Cyber OSINT CTF** chạy trực tiếp trên Termux.

> Game điều tra kỹ thuật số với dữ liệu hoàn toàn giả lập. Người chơi thu thập manh mối, phân tích username/domain/IP/log/metadata và tìm FLAG để hoàn thành vụ án.

## Tính năng

- 🕵️ 5+ case mẫu, chia nhiều độ khó
- 🔎 Username, domain, IP, metadata, logs và timeline
- 🧩 Hệ thống clue và FLAG
- ⭐ XP, level và rank
- 🧰 Bộ công cụ điều tra trong game
- 💾 Save/load tiến trình
- 🏆 Achievement cơ bản
- 🎲 Clue được xáo trộn mỗi lần chơi
- 📱 Tối ưu cho Termux và màn hình điện thoại
- 🛡️ Không quét mạng thật, không thu thập dữ liệu thật

## Cài đặt

```bash
pkg update
pkg install python git -y
git clone https://github.com/khahdihdz/blacktrace-termux.git
cd blacktrace-termux
chmod +x install.sh
./install.sh
```

Sau đó chạy:

```bash
blacktrace
```

Hoặc:

```bash
python3 blacktrace.py
```

## Điều khiển

- Menu: nhập số tương ứng
- Điều tra: chọn tool rồi nhập clue
- `0`: quay lại menu trước
- `q`: thoát trong các màn hình nhập liệu

## An toàn

BLACKTRACE là **game mô phỏng**. Các username, domain, IP, log và dữ liệu điều tra đều là dữ liệu giả lập trong game. Công cụ không thực hiện reconnaissance, scanning hoặc truy vấn dữ liệu của mục tiêu thật.

## CI

Mỗi push và pull request sẽ chạy tự động:

1. Kiểm tra JSON case data.
2. Compile Python.
3. Chạy test.

## License

MIT © 2026 khahdihdz
