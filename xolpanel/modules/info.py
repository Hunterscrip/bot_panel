from xolpanel import *

@bot.on(events.CallbackQuery(data=b'info'))
async def info(event):
	async def info_(event):
		inline = [
[Button.inline("[ Facebook ]","https://facebook.com/Ronaldhet"),
Button.inline("[ Telegram ]","https://t.me/Putri24V")],
[Button.url("[ GitHub Repo ]","https://github.com/akudedi"),
Button.url("[ Telegram Channel ]","https://t.me/HAYOSIASTORE")]]
		z = requests.get(f"http://ip-api.com/json/?fields=country,region,city,timezone,isp").json()
		msg = f"""
**━━━━━━━━━━━━━━━━**
**⟨ About SSH BOT ⟩**
**━━━━━━━━━━━━━━━━**
**» Service:** `SSH`
**» Hostname/IP:** `{DOMAIN}`
**» ISP:** `{z["isp"]}`
**» Country:** `{z["country"]}`
**» 🤖@ProjectDedi_bot**
**━━━━━━━━━━━━━━━━**
"""
		await event.edit(msg,buttons=inline)
	sender = await event.get_sender()
	a = valid(str(sender.id))
	if a == "true":
		await info_(event)
	else:
		await event.answer("Access Denied🤣",alert=True)
