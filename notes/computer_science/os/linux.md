# Linux

## Basic of administration
### Search software

Commands:
- `which`
- `whereis`
- `locate`

`rpm`, `pkg`, `dpkg-query`

## SSD optimizations

As root:
```
fstrim --all
systemctl enable fstrim.timer
```
