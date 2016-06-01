import datetime

import pelican.signals

def fixdatetime(content):
    ds = content.metadata.get('time')
    if ds is None or not hasattr(content, 'date'):
        return
    fmt = content.settings.get('TIME_FORMAT', '%H:%M')
    time = datetime.datetime.strptime(ds, fmt)
    published = content.date
    published = published.replace(hour=time.hour,
                                  minute=time.minute,
                                  second=time.second)
    content.date = published

def register():
    pelican.signals.content_object_init.connect(fixdatetime)
