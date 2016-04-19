# This is a very basic state change AppleScript file that will
# call out to my blinkstick python app to light up the count
# of unread messages, and eventually will light it up with different
# colors if the messages originate from certain people.

set redUsers to (system attribute "RED_USERS")
set ledColor to "blue"

tell application "System Events" to set adiumisrunning to (name of processes) contains "Adium"
if adiumisrunning then
	tell application "Adium"
		set tabs to count of chats
		set unreads to 0
		#return chat 1
		
		repeat with loopi from 1 to tabs
			#set unreads to unreads + (unread message count of chat loopi)
			set localUnreads to (unread message count of chat loopi)
			set unreads to unreads + localUnreads
			set chatUser to id of (chat loopi)
			
			if (localUnreads > 0) and (chatUser is in redUsers) then
				log chatUser & " was in red_users"
				set ledColor to "red"
			end if
		end repeat
		
		do shell script "~NCUSTER/ncuster/scripts/simpleled.py " & unreads & " " & ledColor
	end tell
else
	return "Adium is not running"
end if

#tell application "Adium" to get properties
