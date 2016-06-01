import datetime

import pelican.contents
import pelican.signals

def defaultunpublished(content):
    if isinstance(content, pelican.contents.Article):
        if 'status' not in content.metadata:
            content.status = 'draft'
    elif isinstance(content, pelican.contents.Page):
        if 'status' not in content.metadata:
            content.status = 'hidden'

def register():
    pelican.signals.content_object_init.connect(defaultunpublished)
