$Source = "C:\Users\user\AppData\Local\Programs\Microsoft VS Code\Code.exe"
$Target = "C:\Personal\Timely\Code.ico"

Add-Type -AssemblyName System.Drawing
$Bitmap = [System.Drawing.Icon]::ExtractAssociatedIcon($Source).ToBitmap()
$Icon = [System.Drawing.Icon]::FromHandle($Bitmap.GetHicon())
$File = New-Object System.IO.FileStream($Target, 'OpenOrCreate') 
$Icon.Save($File)
$File.Close()
$Icon.Dispose()