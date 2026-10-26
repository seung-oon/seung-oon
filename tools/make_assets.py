"""Profile README art in the Monoline palette (the portfolio site's design system).

Writes assets/{hero,footer,stat-*}-{light,dark}.svg. Run: python tools/make_assets.py
Text and figures in the stat cards are copied from README.md; change both together.
"""
import os

THEMES = {
    'light': dict(surface='#ffffff', line='#e5e5e2', sunken='#f1f1ef', ink='#111214', muted='#5c5f66',
                  signal='#0f7b5f', strong='#8a8a85', dots='#111214'),
    'dark': dict(surface='#141517', line='#2a2c30', sunken='#1c1d20', ink='#ededec', muted='#9da0a6',
                 signal='#3ddc97', strong='#6b6f76', dots='#ededec'),
}
SANS = "'Segoe UI', -apple-system, BlinkMacSystemFont, 'Noto Sans KR', 'Malgun Gothic', 'Apple SD Gothic Neo', Helvetica, Arial, sans-serif"
MONO = "ui-monospace, SFMono-Regular, Consolas, 'Liberation Mono', Menlo, monospace"
OUT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'assets')


def hero(c):
    # Name first, nothing competing with it: no blocks, one signal caret, a faint dot field on the right.
    dots = ''.join(f'<circle cx="{x}" cy="{y}" r="1.3"/>' for y in range(52, 140, 16) for x in range(652, 800, 16))
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 830 176" role="img" aria-label="Seungyoon Kim — Backend Developer, Medical AI Research">
  <rect x="0.5" y="0.5" width="829" height="175" rx="15.5" fill="{c['surface']}" stroke="{c['line']}"/>
  <g fill="{c['muted']}" fill-opacity=".28">{dots}</g>
  <text x="44" y="54" font-family="{MONO}" font-size="13" letter-spacing="1.6" fill="{c['muted']}">BACKEND · MEDICAL AI RESEARCH</text>
  <text x="42" y="112" font-family="{SANS}" font-size="52" font-weight="700" letter-spacing="-1.4" fill="{c['ink']}">Seungyoon Kim</text>
  <rect x="424" y="75" width="14" height="38" fill="{c['signal']}"/>
  <text x="44" y="148" font-family="{MONO}" font-size="14" fill="{c['signal']}">seungyoon-portfolio.vercel.app</text>
</svg>
'''


def stat(c, eyebrow, number, title, sub, label):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 270 112" width="270" height="112" role="img" aria-label="{label}">
  <rect x="0.5" y="0.5" width="269" height="111" rx="11.5" fill="{c['surface']}" stroke="{c['line']}"/>
  <rect x="242" y="18" width="10" height="10" rx="5" fill="{c['signal']}"/>
  <text x="20" y="28" font-family="{MONO}" font-size="11" letter-spacing="1.4" fill="{c['signal']}">{eyebrow}</text>
  <text x="19" y="62" font-family="{SANS}" font-size="25" font-weight="700" letter-spacing="-0.5" fill="{c['ink']}">{number}</text>
  <text x="20" y="84" font-family="{SANS}" font-size="13.5" font-weight="600" fill="{c['ink']}">{title}</text>
  <text x="20" y="100" font-family="{SANS}" font-size="12" fill="{c['muted']}">{sub}</text>
</svg>
'''


def footer(c):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 830 56" role="img" aria-label="seungyoon-portfolio.vercel.app">
  <line x1="0" y1="8.5" x2="830" y2="8.5" stroke="{c['line']}"/>
  <rect x="345" y="30" width="8" height="8" rx="4" fill="{c['signal']}"/>
  <text x="361" y="38.5" font-family="{MONO}" font-size="13" fill="{c['muted']}">seungyoon-portfolio.vercel.app</text>
</svg>
'''


STATS = {
    'hidr': ('RESEARCH', '0.4550 → 0.5231', 'HI-DR 재현 · 확장 시도', '현재 방문 Jaccard · 약 20개 · 5-seed',
             'HI-DR 재현과 확장 시도, 후보 풀 재설계로 현재 방문 기준 Jaccard 0.4550에서 0.5231 (방문당 추천 약 20개로 맞춤, 재점수화 헤드 5-seed)'),
    'dcc': ('COMPETITION', '0.9835', '신고자 성별 분류 정확도', 'Wav2Vec2 · Validation 3,640통화',
            'DCC 예선 신고자 성별 분류 정확도 0.9835 (Wav2Vec2, Validation 3,640통화)'),
    'runify': ('BACKEND', 'Kafka · pgRouting', 'Runify 러닝 코스 생성 서버', '강남·서초 실그래프 · 서버 전담',
               'Runify 러닝 코스 생성 서버, Kafka와 pgRouting, 서버 전담 구현'),
}

for theme, c in THEMES.items():
    files = {f'hero-{theme}.svg': hero(c), f'footer-{theme}.svg': footer(c)}
    for key, args in STATS.items():
        files[f'stat-{key}-{theme}.svg'] = stat(c, *args)
    for name, text in files.items():
        with open(os.path.join(OUT, name), 'w', encoding='utf-8', newline='\n') as f:
            f.write(text)
        print('wrote', name)
