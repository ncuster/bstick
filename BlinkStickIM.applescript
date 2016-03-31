# This is a very basic state change AppleScript file that will
# call out to my blinkstick python app to light up the count
# of unread messages, and eventually will light it up with different
# colors if the messages originate from certain people.

tell application "System Events" to set adiumisrunning to (name of processes) contains "Adium"
if adiumisrunning then
	tell application "Adium"
		set tabs to count of chats
		set unreads to 0
		#return chat 1
		repeat with loopi from 1 to tabs
			set unreads to unreads + (unread message count of chat loopi)
		end repeat
		#		return unreads
	end tell
else
	return "off"
end if

#tell application "Adium" to get properties
#do shell script "~NCUSTER/ncuster/scripts/BlinkStickRed.sh " & unreads
#display dialog "my variable: " & tabs
