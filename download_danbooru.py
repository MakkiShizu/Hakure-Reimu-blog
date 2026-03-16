#!/usr/bin/env python3
"""
Download anime images from Danbooru using waifuc
"""
from waifuc.source import DanbooruSource
from waifuc.export import SaveExporter

# Set output directory
output_dir = r"D:\hexo-blog\source\images\danbooru_waifuc"

# Create source - search for hakurei_reimu (博丽灵梦)
source = DanbooruSource(
    tags=['hakurei_reimu'],
    min_size=800,
)

# Create exporter to save to local directory
exporter = SaveExporter(output_dir)

# Export the images (first 5 will be downloaded by default)
exporter.export_from(source)

print(f"Downloaded images to {output_dir}")
