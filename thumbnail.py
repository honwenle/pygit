#!/usr/bin/env python
# -*- coding: utf-8 -*-

import Image
im = Image.open('test.jpg')
#print im.format, im.size, im.mode
im.thumbnail((200, 100))
im.save('thumb.jpg', 'JPEG')