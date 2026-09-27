# Scheduler documentation

## Günlük Zamanlayıcı

### Kurulum

```bash
pip install schedule
```

### Kullanım

#### Günlük belirli saatte

```python
from scheduler import schedule_daily, start_scheduler

schedule_daily(hour=9, minute=0)  # Her gün saat 09:00'da
start_scheduler()
```

#### Saatlik aralıklar

```python
from scheduler import schedule_interval, start_scheduler

schedule_interval(hours=12)  # Her 12 saatte
start_scheduler()
```

### Bağımsız çalıştırma

```bash
python scheduler.py
```

## Cron Jobs ile Alternatif

### Linux/macOS

```bash
# Crontab açmak
crontab -e

# Her gün saat 09:00'da çalıştırmak
0 9 * * * cd /path/to/youtube-automation-system && /path/to/.venv/bin/python run_pipeline.py
```

### Windows Task Scheduler

1. Task Scheduler'ı aç
2. "Create Basic Task" seçin
3. Trigger: Daily, 09:00
4. Action: Program başlat
   - Program: `C:\path\to\.venv\Scripts\python.exe`
   - Arguments: `run_pipeline.py`
   - Start in: `C:\path\to\youtube-automation-system`
