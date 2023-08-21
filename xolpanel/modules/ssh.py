from xolpanel import *

@bot.on(events.CallbackQuery(data=b'ssh'))
async def ssh(event):
	async def ssh_(event):
		inline = [
[Button.inline("[ 🛒Trial SSH ]","trial-ssh"),
Button.inline("[ 🛒Create SSH ]","create-ssh")],
[Button.inline("[ 🛒Delete SSH ]","delete-ssh"),
Button.inline("[ 🛒Check Login SSH ]","login-ssh")],
[Button.inline("[ 🛒Show All User SSH ]","show-ssh")],
[Button.inline("‹ 🔙Main Menu ›","menu")]]
		z = requests.get(f"http://ip-api.com/json/?fields=country,region,city,timezone,isp").json()
		msg = f"""
**━━━━━━━━━━━━━━━━**
**⟨ SSH Menu ⟩**
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
		await ssh_(event)
	else:
		await event.answer("Access Denied🤣",alert=True)
