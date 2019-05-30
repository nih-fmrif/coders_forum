#!/usr/bin/env python
with open('template.html') as template, open('slides.md') as readme, open('slides.html', 'w') as pres:
    pres.write(
        template.read()
        .replace('PLACEHOLDERPLACEHOLDERPLACEHOLDER', readme.read())
    )
