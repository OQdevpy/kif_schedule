# kif_schedule


# botni serverga deploy qilish

- nano /etc/systemd/system/schedulebot.service
```sh
[Unit]
Description=KIF schedule bot
After=network.target

[Service]
User=root
WorkingDirectory=/var/www/kif_schedule/bot
ExecStart=/var/www/kif_schedule/bot/venv/bin/python /var/www/kif_schedule/bot/app.py
Restart=always

[Install]
WantedBy=multi-user.target

```
After making these changes, save the file, and then run:
- sudo systemctl daemon-reload
- sudo systemctl start schedulebot.service
- sudo systemctl enable schedulebot.service

Check the status of your service:

- sudo systemctl status schedulebot.service
