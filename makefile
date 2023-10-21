.PHONY: run
run:
	python ./BOT/bot.py


.PHONY: fix-yt
fix-yt:
	pip install --upgrade --force-reinstall "git+https://github.com/ytdl-org/youtube-dl.git"
