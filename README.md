# Thumbnailer-3mf
Support to show of .3mf files thumbnails on Free Desktop Environments (like GNOME or KDE)

![capture](https://github.com/andesfreedesign/Thumbnailer-3mf/blob/main/capture.png)

### Installation on Debian-based distributions

- Open a terminal
- Copy the executable file

```
sudo cp 3mf-thumbnailer.py /usr/bin
```
- Give execution permissions
```
sudo chmod +x /usr/bin/3mf-thumbnailer.py
```
- Copy the  application/x-extension-3mf MIME type file
```
sudo cp 3mf.thumbnailer /usr/share/thumbnailers
```
- Copy the thumbnailer file
```
sudo cp 3mf-thumb-mime.xml /usr/share/mime/packages
```
- Update the MIME database
```
sudo update-mime-database /usr/share/mime
```

