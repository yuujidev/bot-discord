# Whispering Forest - Discord Bot

Discord Bot với chủ đề **Whispering Forest | Rừng Thì Thầm**, được viết bằng Python và thư viện `discord.py`.

Bot có chức năng kể những câu chuyện bí ẩn về khu rừng và tự động phản hồi khi thành viên nhắc đến các từ khóa liên quan.

## Chức năng

- Bot tự động thông báo khi sẵn sàng.
- Gửi lời chào khi Bot được thêm vào server.
- Lệnh `!chuyen` để kể một câu chuyện ngẫu nhiên.
- Tự động phản hồi khi tin nhắn có từ:
  - `rừng`
  - `thì thầm`
- Sử dụng Embed để tạo thông báo chào mừng.
- Có nhiều câu chuyện và câu phản hồi ngẫu nhiên.
- Sử dụng `random` để lựa chọn nội dung.

## Công nghệ sử dụng

- Python 3
- discord.py
- Discord Bot API

## Cấu trúc

```text
Whispering-Forest/
│
├── bot.py
└── README.md
Cài đặt
1. Cài Python

Cài Python 3 từ trang chính thức:

https://www.python.org/

Kiểm tra Python:

python --version
2. Cài thư viện discord.py

Mở Terminal hoặc CMD:

pip install discord.py
Cấu hình Bot

Trong file bot.py, cần cấu hình Token của Discord Bot:

TOKEN = "YOUR_BOT_TOKEN"

Không đăng Token thật lên GitHub hoặc chia sẻ công khai.

Nên sử dụng biến môi trường hoặc file .env để lưu Token khi triển khai thực tế.

Cấu hình Channel

Thay ID kênh:

WELCOME_CHANNEL_ID = 12

bằng ID của kênh Discord mà Bot sẽ gửi lời chào khi được thêm vào server.

Ví dụ:

WELCOME_CHANNEL_ID = 123456789012345678
Discord Intents

Bot sử dụng:

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

Trong Discord Developer Portal cần bật các Intent cần thiết, đặc biệt là:

Message Content Intent
Server Members Intent
Chạy Bot

Mở Terminal tại thư mục project và chạy:

python bot.py

Nếu Bot hoạt động thành công, Terminal sẽ hiển thị:

Bot đã sẵn sàng.
Các lệnh
Kể chuyện

Sử dụng:

!chuyen

Bot sẽ chọn ngẫu nhiên một câu chuyện trong danh sách và gửi vào kênh.

Ví dụ:

!chuyen

Bot có thể trả về một câu chuyện về khu rừng.

Phản hồi tự động

Khi thành viên gửi tin nhắn có chứa:

rừng

hoặc:

thì thầm

Bot sẽ tự động gửi một câu phản hồi ngẫu nhiên.

Ví dụ:

Người dùng: Khu rừng này thật bí ẩn.

Bot:

Shhh... rừng đang lắng nghe bạn.
Hoạt động của Bot

Bot có hai loại xử lý chính:

Command

Bot nhận lệnh:

!chuyen

và thực hiện hàm:

@bot.command(name="chuyen")
async def tell_story(ctx):
Event

Bot sử dụng các Event của Discord:

@bot.event
async def on_ready():

để xử lý khi Bot đăng nhập thành công.

Ngoài ra:

@bot.event
async def on_guild_join(guild):

được sử dụng để gửi lời chào khi Bot được thêm vào server.

Bot cũng sử dụng:

@bot.event
async def on_message(message):

để kiểm tra nội dung tin nhắn và phản hồi các từ khóa.

Lưu ý bảo mật

Không đưa Discord Bot Token thật lên GitHub.

Không nên viết:

TOKEN = "token_that_is_really_used"

trong repository Public.

Nếu Token đã bị lộ, hãy vào Discord Developer Portal và tạo lại Token mới.

Mục đích dự án

Dự án được thực hiện nhằm tìm hiểu:

Python cơ bản
Lập trình Bot Discord
Discord API
Event và Command
Hàm bất đồng bộ async/await
Xử lý chuỗi
Danh sách trong Python
Lựa chọn dữ liệu ngẫu nhiên
Embed Message
Quản lý Discord Intents
Tác giả

Whispering Forest | Rừng Thì Thầm

Discord Bot Project


**Có một lỗi nhỏ trong code của bạn** ở đoạn `whispers`:

```python
"Bạn không tìm thấy rừng… rừng tìm thấy bạn.",
"Hãy mở lòng… rừng sẽ kể cho bạn nghe điều bạn chưa từng biết."
"Bạn có chắc tiếng gọi đó là của gió… hay là của ai khác?",

Thiếu dấu , sau "biết.", nên Python sẽ tự nối 2 chuỗi thành một câu. Sửa thành:

"Hãy mở lòng… rừng sẽ kể cho bạn nghe điều bạn chưa từng biết.",
"Bạn có chắc tiếng gọi đó là của gió… hay là của ai khác?",
