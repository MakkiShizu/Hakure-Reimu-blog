#!/usr/bin/env python3
"""
Download hakurei_reimu images from Danbooru using waifuc
- Tags: hakurei_reimu, solo, score:10+
- Rating: safe (g level)
"""
import os
import waifuc.config

# 设置代理
os.environ['HTTP_PROXY'] = 'http://127.0.0.1:7890'
os.environ['HTTPS_PROXY'] = 'http://127.0.0.1:7890'

# 配置 waifuc 使用代理
waifuc.config.HTTP_PROXY = 'http://127.0.0.1:7890'
waifuc.config.HTTPS_PROXY = 'http://127.0.0.1:7890'

from waifuc.source import DanbooruSource
from waifuc.export import SaveExporter
from waifuc.action import RatingFilterAction

# Output directory
output_dir = r"D:\hexo-blog\source\images\reimu_gallery"

# Create source with hakurei_reimu, solo tags and score:10+
source = DanbooruSource(
    tags=['hakurei_reimu', 'solo', 'score:10'],
    min_size=800,
)

# Create exporter
exporter = SaveExporter(output_dir)

# Filter for safe rating only (g level)
source.attach(RatingFilterAction(['safe']))

# Export ALL matching images (no limit)
print(f"Downloading safe rating images to {output_dir}")
print("This will download all matching images (no limit)...")
exporter.export_from(source)

print(f"Done! Images saved to {output_dir}")