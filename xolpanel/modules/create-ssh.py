from xolpanel import *

@bot.on(events.CallbackQuery(data=b'create-ssh'))
async def create_ssh(event):
	async def create_ssh_(event):
		async with bot.conversation(chat) as user:
			await event.respond('**Username:**')
			user = user.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
			user = (await user).raw_text
		async with bot.conversation(chat) as pw:
			await event.respond("**Password:**")
			pw = pw.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
			pw = (await pw).raw_text
		async with bot.conversation(chat) as exp:
			await event.respond("**Choose Expiry Day**",buttons=[
[Button.inline("• 3 Day •","3"),
Button.inline("• 7 Day •","7")],
[Button.inline("• 30 Day •","30"),
Button.inline("• 60 Day •","60")]])
			exp = exp.wait_event(events.CallbackQuery)
			exp = (await exp).data.decode("ascii")
		cmd = f'useradd -e `date -d "{exp} days" +"%Y-%m-%d"` -s /bin/false -M {user} && echo "{pw}\n{pw}" | passwd {user}'
		try:
			subprocess.check_output(cmd,shell=True)
		except:
			await event.respond("**User Already Exist**")
		else:
			today = DT.date.today()
			later = today + DT.timedelta(days=int(exp))
			msg = f"""
<code>◇━━━━━━━━━━━━━━━━━◇</code>
<code>  SSH Premium Account   </code>
<code>◇━━━━━━━━━━━━━━━━━◇</code>
<code>Username        : </code> <code>$Login</code>
<code>Password        : </code> <code>$Pass</code>
<code>Expired          : </code> <code>$exp</code>
<code>◇━━━━━━━━━━━━━━━━━◇</code>
<code>IP               : </code> <code>$IP</code>
<code>ISP              : </code> <code>$ISP </code>
<code>CITY             : </code> <code>$CITY</code>
<code>Host             : </code> <code>$domen</code>
<code>User Limit        : </code> <code>${iplim} IP</code>
<code>Port OpenSSH    : </code> <code>22</code>
<code>Port Dropbear    : </code> <code>109, 143</code>
<code>Port SSH WS     : </code> <code>80, 8080</code>
<code>Port SSH SSL WS : </code> <code>443</code>
<code>Port SSL/TLS     : </code> <code>8443,8880</code>
<code>Port OVPN WS SSL : </code> <code>2086</code>
<code>Port OVPN SSL    : </code> <code>990</code>
<code>Port OVPN TCP    : </code> <code>1194</code>
<code>Port OVPN UDP    : </code> <code>2200</code>
<code>Proxy Squid        : </code> <code>3128</code>
<code>BadVPN UDP       : </code> <code>7100, 7300, 7300</code>
<code>◇━━━━━━━━━━━━━━━━━◇</code>
<code>SSH UDP VIRAL :</code> <code>$domen:1-65535@$Login:$Pass</code>
<code>◇━━━━━━━━━━━━━━━━━◇</code>
<code>HTTP COSTUM :</code> <code>$domen:80@$Login:$Pass</code>
<code>◇━━━━━━━━━━━━━━━━━◇</code>
<code>Host Slowdns    : </code> <code>$sldomain</code>
<code>Port Slowdns     : </code> <code>80, 443, 53</code> 
<code>Pub Key          : </code> <code> $slkey</code>
<code>◇━━━━━━━━━━━━━━━━━◇</code>
<code>Payload WS/WSS   : </code>
<code>GET / HTTP/1.1[crlf]Host: ${domen}[crlf]Connection: Keep-Alive[crlf]User-Agent: [ua][crlf]Upgrade: ws[crlf][crlf]</code>
<code>◇━━━━━━━━━━━━━━━━━◇</code>
<code>OpenVPN SSL      : </code> http://$domen:89/ssl.ovpn
<code>OpenVPN TCP      : </code> http://$domen:89/tcp.ovpn
<code>OpenVPN UDP      : </code> http://$domen:89/udp.ovpn
<code>◇━━━━━━━━━━━━━━━━━◇</code>
<code>Save Link Account: </code>http://$domen:89/ssh-$Login.txt
<code>◇━━━━━━━━━━━━━━━━━◇</code>
**» 🗓Expired Until:** `{later}`
**» 🤖@Rmblvpn**
**━━━━━━━━━━━━━━━━**
"""
			inline = [
[Button.url("[ Grup tele ]","t.me/configopok"),
Button.url("[ Channel ]","t.me/rmblvpn")]]
			await event.respond(msg,buttons=inline)
	chat = event.chat_id
	sender = await event.get_sender()
	a = valid(str(sender.id))
	if a == "true":
		await create_ssh_(event)
	else:
		await event.answer("Akses Ditolak😂",alert=True)
