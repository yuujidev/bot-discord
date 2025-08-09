import discord
from discord.ext import commands
import random

TOKEN = "MTQwMzgyNDMzNTkwNjUzNzU4Mw.GaG9LE.B5ZncVn9fBXxNSTeFJOEJM2nk4LCiVdjJv53q4"  # Đừng public token thật

# ID kênh chỉ dành riêng cho bot
WELCOME_CHANNEL_ID = 1403834510289801299

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)

# Danh sách 7 câu chuyện
stories = [
    """Ngày xưa, sâu trong 🌲 Whispering Forest, có một con suối chỉ ngân lên tiếng hát khi trăng tròn. Người lữ khách nào dừng lại bên bờ, lắng nghe thật kỹ... sẽ nghe thấy giọng của những linh hồn xưa, kể về hành trình mà họ chưa kịp hoàn thành.""",
    """Có một cây cổ thụ ở giữa rừng, thân cây khắc đầy ký hiệu lạ. Ai chạm tay vào, sẽ thấy trái tim mình rung lên như nghe tiếng ai gọi... nhưng chẳng bao giờ thấy được gương mặt đó.""",
    """Đêm nọ, một cơn gió thì thầm tên của bạn, kéo bạn vào một lối mòn đầy lá khô. Mỗi bước đi, bạn nghe tiếng cười nhẹ nhàng vang vọng, cho đến khi nhận ra… mình đã lạc vào câu chuyện của chính mình.""",
    """Họ nói rằng, nếu bạn ngồi dưới tán thông vào lúc hoàng hôn, rừng sẽ kể cho bạn nghe một bí mật. Nhưng hãy cẩn thận… vì bí mật đó có thể đổi cả phần đời còn lại của bạn.""",
    """Giữa khu rừng, có một hồ nước phẳng lặng như gương. Không ai dám nhìn xuống lâu, vì hình ảnh phản chiếu không phải lúc nào cũng là chính bạn.""",
    """Người già trong làng kể rằng mỗi đêm đông, một bóng áo choàng trắng sẽ đi qua rừng, tay cầm đèn lồng. Nếu bạn theo sau… đừng mong quay lại con đường cũ.""",
    """Có một con đường không hề tồn tại trên bản đồ, chỉ xuất hiện khi bạn thật sự lạc lối. Và khi đã đi vào… bạn sẽ không còn muốn rời khỏi 🌲 Whispering Forest nữa.""",
    """Giữa màn sương dày, bạn thấy một cây cầu gỗ cũ. Bước qua giữa chừng, tiếng bước chân phía sau vang lên… nhưng khi quay lại, chẳng có ai.""",
    """Có một cánh cửa bằng đá trong rừng, không có bản lề, không có khe hở. Người ta nói, nếu áp tai vào, bạn sẽ nghe thấy tiếng hát ru.""",
    """Một đêm trăng, bạn nhìn thấy một ngọn đèn nhỏ chập chờn giữa tán lá. Khi tới gần, ánh sáng vụt tắt, để lại bóng tối và mùi hương hoa dại.""",
    """Người tiều phu già kể rằng, từng có lần ông gặp một cô gái mặc váy trắng đi lạc trong rừng. Sáng hôm sau, ông thấy bức ảnh của cô trên bia mộ cũ.""",
    """Có một con chim hót ngược – tiếng hát của nó nghe như những lời thì thầm bằng ngôn ngữ lạ. Ai nghe lâu quá sẽ không tìm được đường ra.""",
    """Một gốc cây bị sét đánh mở ra khe hở nhỏ. Thò tay vào, bạn chạm phải thứ mềm mại như vải… nhưng khi kéo ra, chỉ còn lại mùi khói.""",
    """Trong khu rừng này, mỗi mùa thu, lá rụng theo hình xoắn ốc dẫn tới một hòn đá đen bóng. Không ai biết bên dưới hòn đá là gì.""",
    """Có một hồ nước đen như mực. Mỗi khi thả đá xuống, thay vì tiếng “tõm”, bạn nghe thấy tiếng cười khẽ vang lên.""",
    """Một con đường đất dẫn tới cây cổ thụ trăm tuổi. Ai vòng quanh cây ba lần sẽ thấy một bóng người đứng ở đúng vị trí mình xuất phát.""",
    """Gió trong khu rừng này đôi khi mang mùi của những món ăn bạn từng yêu thích… ngay trước khi có chuyện xấu xảy ra.""",
    """Người thợ săn trẻ nói rằng, có đêm anh thấy hàng trăm đôi mắt sáng trong bóng tối. Nhưng khi thắp đuốc, chỉ còn cây cối đứng im.""",
    """Trên vách đá cao ở rìa rừng, có khắc hàng chữ cổ đã mờ. Những đêm mưa lớn, chữ ấy phát sáng như được viết bằng lửa.""",
    """Họ kể rằng vào đêm đông lạnh nhất, bóng dáng một đoàn người đi xuyên rừng, im lặng, không để lại dấu chân. Nếu bạn gọi, họ sẽ quay lại… nhưng không phải bằng gương mặt con người."""

]

# Danh sách phản hồi khi nghe từ khóa
whispers = [
    "Shhh... rừng đang lắng nghe bạn.",
    "Tiếng thì thầm bạn nghe… không phải từ gió đâu.",
    "Mỗi chiếc lá rơi đều mang theo một câu chuyện.",
    "Bạn không tìm thấy rừng… rừng tìm thấy bạn.",
    "Hãy mở lòng… rừng sẽ kể cho bạn nghe điều bạn chưa từng biết."
    "Bạn có chắc tiếng gọi đó là của gió… hay là của ai khác?",
    "Rừng đã nhớ tên bạn… và nó sẽ không quên đâu.",
    "Mỗi bước chân bạn đi, đất dưới chân lại ghi nhớ.",
    "Ánh mắt nào đang dõi theo bạn từ sau những tán lá kia?",
    "Đừng trả lời tiếng thì thầm… trừ khi bạn muốn họ đến gần."
]

@bot.event
async def on_ready():
    print(f"🌲 Bot {bot.user} đã sẵn sàng.")

@bot.event
async def on_guild_join(guild):
    # Lấy kênh theo ID
    channel = bot.get_channel(WELCOME_CHANNEL_ID)
    if channel:
        embed = discord.Embed(
            title="🌲 Whispering Forest | Rừng Thì Thầm",
            description=(
                "Xin chào, ta là **Người Kể Truyện Thì Thầm**.\n"
                "Khu rừng này chứa vô vàn câu chuyện… và hôm nay, nó đã chọn bạn.\n"
                "Hãy ở lại và lắng nghe."
            ),
            color=0x2ecc71
        )
        embed.set_footer(text="🌲 Thuộc quyền sở hữu Whispering Forest | Rừng Thì Thầm")
        await channel.send(embed=embed)

# Lệnh kể chuyện
@bot.command(name="chuyen")
async def tell_story(ctx):
    story = random.choice(stories)
    await ctx.send(f"📖 {story}")

# Tự động phản hồi khi có từ khóa
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    
    content_lower = message.content.lower()
    if "rừng" in content_lower or "thì thầm" in content_lower:
        await message.channel.send(random.choice(whispers))
    
    await bot.process_commands(message)

bot.run(TOKEN)
