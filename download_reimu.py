#!/usr/bin/env python3
"""
Download hakurei_reimu images from Danbooru using waifuc
- Tags: hakurei_reimu, solo, score:10+
- Rating: safe
- Count: ~150
"""
from waifuc.source import DanbooruSource
from waifuc.export import SaveExporter
from waifuc.action import RatingFilterAction, FirstNSelectAction

# Output directory
output_dir = r"D:\hexo-blog\source\images\reimu_gallery"

# Create source with hakurei_reimu, solo tags and score:10+ (score:10 means score >= 10)
# Using score:10 as tag to filter by score
source = DanbooruSource(
    tags=['hakurei_reimu', 'solo', 'score:10'],
    min_size=800,
)

# Create exporter
exporter = SaveExporter(output_dir)

# Filter for safe rating only and select top 150
source.attach(RatingFilterAction(['safe']))
source.attach(FirstNSelectAction(150))

# Export
print(f"Downloading safe rating images to {output_dir}")
exporter.export_from(source)

print(f"Done! Images saved to {output_dir}")
