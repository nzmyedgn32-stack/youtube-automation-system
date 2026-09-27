#!/usr/bin/env python3
"""
Google Trends RSS Parser
Fetches trending search topics from Google Trends RSS feed
"""

import logging
import xml.etree.ElementTree as ET
from typing import List

import requests

logger = logging.getLogger(__name__)


def fetch_google_trends_rss(region: str = "TR") -> List[str]:
    """
    Fetch trending topics from Google Trends RSS feed
    
    Args:
        region: Country/region code (e.g., 'TR', 'US', 'GB')
    
    Returns:
        List of trending topics
    """
    url = f"https://trends.google.com/trends/trendingsearches/daily/rss?geo={region}"
    try:
        logger.info(f"Google Trends RSS'ten veri çekiliyor ({region})...")
        response = requests.get(url, timeout=20)
        response.raise_for_status()
        root = ET.fromstring(response.content)
        topics = []
        for item in root.findall("./channel/item"):
            title = item.findtext("title")
            if title:
                clean = title.replace("- Google Trends", "").strip()
                if clean:
                    topics.append(clean)
        logger.info(f"✅ {len(topics)} trend bulundu")
        return topics[:10]
    except Exception as e:
        logger.warning(f"Google Trends RSS hatası: {e}")
        return []


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    trends = fetch_google_trends_rss()
    for i, topic in enumerate(trends, 1):
        print(f"{i}. {topic}")
