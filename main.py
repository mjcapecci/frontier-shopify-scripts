import os

filepath = '/Users/mikecapecci/Desktop/shopify-test-store'

# Base Directories
layout_dir = os.path.join(filepath, 'layout')
assets_dir = os.path.join(filepath, 'assets')

# Files to Edit
theme_file = os.path.join(layout_dir, 'theme.liquid')

with open(theme_file, "r") as f:
  lines = f.readlines()

for index, line in enumerate(lines):
    if line.startswith("</head>"):
        break
lines.insert(index, "\t{{ 'frontier.css' | asset_url | stylesheet_tag}}\n\n \t<script src=\"" + "{{ 'frontier.js' | asset_url}}\"" + " defer='defer'></script>\n\n" )

for index, line in enumerate(lines):
    if line.startswith('<link rel="preload" href=\"{{ \'theme.css\' | asset_url }}\" as="style">'):
        break
lines.insert(index, "TEST\n\n" )

with open(theme_file, "w") as f:
    contents = f.writelines(lines)





