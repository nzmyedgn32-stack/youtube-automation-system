#!/usr/bin/env python3
"""
Scheduler for YouTube Automation System
Runs pipeline on a schedule (daily, weekly, etc.)
"""

import logging
import schedule
import time
from datetime import datetime

from app.pipeline import VideoAutomationPipeline

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger(__name__)


def run_pipeline_job() -> None:
    """
    Job to run the complete pipeline
    """
    logger.info("=" * 50)
    logger.info(f"Pipeline işi başlıyor: {datetime.now()}")
    logger.info("=" * 50)

    try:
        pipeline = VideoAutomationPipeline()
        result = pipeline.run()
        logger.info(f"Pipeline başarı ile tamamlandı")
        logger.info(f"Video: {result['selected_title']}")
    except Exception as e:
        logger.error(f"Pipeline hatası: {e}", exc_info=True)

    logger.info("=" * 50)


def schedule_daily(hour: int = 9, minute: int = 0) -> None:
    """
    Schedule pipeline to run daily at specified time
    
    Args:
        hour: Hour (0-23)
        minute: Minute (0-59)
    """
    time_str = f"{hour:02d}:{minute:02d}"
    schedule.every().day.at(time_str).do(run_pipeline_job)
    logger.info(f"Pipeline günlük {time_str} saatinde çalışacak")


def schedule_interval(hours: int = 24) -> None:
    """
    Schedule pipeline to run at regular intervals
    
    Args:
        hours: Interval in hours
    """
    schedule.every(hours).hours.do(run_pipeline_job)
    logger.info(f"Pipeline her {hours} saatte çalışacak")


def start_scheduler() -> None:
    """
    Start the scheduler and run jobs
    """
    logger.info("Scheduler başlatılıyor...")
    while True:
        schedule.run_pending()
        time.sleep(60)


if __name__ == "__main__":
    logger.info("YouTube Automation Scheduler")
    schedule_daily(hour=9)
    # schedule_interval(hours=12)  # Alternative: every 12 hours
    start_scheduler()
