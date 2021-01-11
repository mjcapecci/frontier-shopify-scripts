import os
from datetime import datetime

filepath = '/Users/mikecapecci/Desktop/shopify-test-store'

# Base directories
layout_dir = os.path.join(filepath, 'layout')
assets_dir = os.path.join(filepath, 'assets')

# Files to edit
theme_file = os.path.join(layout_dir, 'theme.liquid')

# Files to add
css_file = os.path.join(assets_dir, 'frontier.css')
js_file = os.path.join(assets_dir, 'frontier.js')

# HTML / Liquid to add to theme.liquid (as string)
include_css = "\t{{ 'frontier.css' | asset_url | stylesheet_tag}}\n\n"
include_js = "\t<script src=\"{{ 'frontier.js' | asset_url}}\"" + " defer='defer'></script>\n\n"
new_file_comment = "/* \n Author: Frontier Web Development\n Date: " + datetime.today().strftime('%Y-%m-%d') + "\n*/"

with open(theme_file, "r") as f:
  lines = f.readlines()

for index, line in enumerate(lines):
    if line.startswith("</head>"):
        break
lines.insert(index, include_css + include_js )

with open(theme_file, "w") as f:
    contents = f.writelines(lines)

with open(css_file, 'w') as css:
    css.write(new_file_comment)

with open(js_file, 'w') as js:
    js.write(new_file_comment)





