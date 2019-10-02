Set WshShell = WScript.CreateObject("WScript.Shell")
Comandline = "C:\Users\Max\AppData\Roaming\Spotify\Spotify.exe"
WScript.sleep 500
CreateObject("WScript.Shell").Run("spotify:user:keidakira:playlist:5uUdK24DebIwUe3yDtBjpX")
WScript.sleep 3000
WshShell.SendKeys " "