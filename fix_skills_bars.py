import re

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

text = text.replace('<ol class="skill-ordered-list">', '<div class="skill-list-container">')
text = text.replace('</ol>', '</div>')

def map_level_to_percent(level):
    level = level.lower()
    if 'expert' in level: return '95'
    if 'advanced' in level: return '85'
    if 'proficient' in level: return '75'
    if 'intermediate' in level: return '65'
    return '50'

def replace_item(match):
    icon_text = match.group(1)
    icon_text = icon_text.replace('skill-ordered-name', 'skill-name')
    level = match.group(2)
    percent = map_level_to_percent(level)
    
    return f'''<div class="skill-item">
                            <div class="skill-header">
                                {icon_text}
                                <span class="skill-percent">{percent}%</span>
                            </div>
                            <div class="skill-bar">
                                <div class="skill-fill" data-width="{percent}"></div>
                            </div>
                        </div>'''

pattern = re.compile(
    r'<li class="skill-ordered-item">\s*<span class="skill-order-num">.*?</span>\s*(<span class="skill-ordered-name">.*?</span>)\s*<span class="skill-level-badge">(.*?)</span>\s*</li>',
    re.DOTALL
)

new_text = pattern.sub(replace_item, text)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(new_text)

print('Updated index.html skills list')
