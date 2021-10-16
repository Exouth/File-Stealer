# File-Stealer
Steal Files on a Windows Machine

### About
This Script will steal certain Files on a Windows Machine and sends them to a FTP Server.

## Preview
![alt text](https://github.com/Exouth/File-Stealer/blob/main/preview.gif?raw=true)

## Installation
- Install Python.
- PIP Installation ```pip install pywin32```.
- (Additional) Install ```pip install pyinstaller``` to convert to exe.

## Usage
1. Change ```FTPSERVER```, ```USERNAME``` and ```PASSWORD```.

2. Set your Directory if you need ```ftp_connection.cwd("files")```.

3. Convert your script with ```PyInstaller``` to exe.

4. Ready to Use!

## Additional
- Edit the ```extension``` variable to set the Filetype Target.
- Script can be run in the Background of an Application with ```MultiProcessing```.
- You can change ```get_desktop_path``` to a custom Path. So you can target a specific Path on the Machine.

### Use for Eductional Purposes only!
