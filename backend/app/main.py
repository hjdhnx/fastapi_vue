#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File  : main.py
# Author: DaShenHan&道长-----先苦后甜，任凭晚风拂柳颜------
# Author's Blog: https://blog.csdn.net/qq_32394351
# Date  : 2023/12/3

from core.config import settings
from core import server

app = server.InitializeApp()

if __name__ == '__main__':
    import uvicorn

    # Don't set debug/reload equals True in release, because TimedRotatingFileHandler can't support multi-prcoess
    # please used "uvicorn --host 127.0.0.1 --port 8000 main:app --env-file ./configs/.env" run in release, and used "python main.py" in dev
    uvicorn.run(
        app='main:app',
        host=str(settings.HOST),
        port=settings.PORT,
        reload=settings.RELOAD,
        log_config=str(settings.LOGGING_CONFIG_FILE)
    )

"""
Celery schedule worker

1) start worker in project base path

    celery -A workers  worker -l info -c 1

2) start beat in project base path

    celery -A workers beat -l info

"""
