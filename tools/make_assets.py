"""Profile README art in the portfolio site's design system (studio grey, black type, one green action).

Writes assets/{hero,check-*,footer}-{light,dark}.svg. Run: python tools/make_assets.py <pretendard-dir>
Text is drawn as outlines from Pretendard, because GitHub shows SVG as an image and cannot load web fonts.
Pretendard OTFs: https://cdn.jsdelivr.net/gh/orioncactus/pretendard@v1.3.9/packages/pretendard/dist/public/static/
Text and figures in the check cards are copied from README.md; change both together.
"""
import os, sys
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen

THEMES = {
    'light': dict(ground='#d9d9d6', card='#f4f4f2', ink='#0e0e0e', muted='#45454a', before='#77777b', accent='#1f5c49', on_accent='#ffffff'),
    'dark': dict(ground='#161617', card='#232325', ink='#f4f4f2', muted='#a9a9ad', before='#8a8a8e', accent='#1f5c49', on_accent='#ffffff'),
}
OUT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'assets')
FONTS = {}


def font(weight):
    if weight not in FONTS:
        f = TTFont(os.path.join(sys.argv[1], f'Pretendard-{weight}.otf'))
        FONTS[weight] = (f, f.getGlyphSet(), f.getBestCmap(), f['head'].unitsPerEm, f['hmtx'])
    return FONTS[weight]


def text(s, x, y, size, weight='Regular', track=0.0, fill='#000', anchor='start'):
    """One line of text as an SVG path. Returns (svg, width). track is in em, like CSS letter-spacing."""
    f, gs, cmap, upm, hmtx = font(weight)
    scale = size / upm
    pen = SVGPathPen(gs)
    advance = 0.0
    names = [cmap.get(ord(ch), '.notdef') for ch in s]
    for name in names:
        advance += hmtx[name][0] * scale + track * size
    advance -= track * size
    ox = x - advance if anchor == 'end' else x
    cx = 0.0
    for name in names:
        gs[name].draw(TransformPen(pen, (scale, 0, 0, -scale, ox + cx, y)))
        cx += hmtx[name][0] * scale + track * size
    return f'<path fill="{fill}" d="{pen.getCommands()}"/>', advance


def hero(c):
    W, H = 1200, 440
    parts = [f'<rect width="{W}" height="{H}" fill="{c["ground"]}"/>']
    p, w1 = text('Seungyoon', 40, 196, 138, 'ExtraBold', -0.05, c['ink']); parts.append(p)
    p, w2 = text('Kim', 40, 334, 138, 'ExtraBold', -0.05, c['ink']); parts.append(p)
    right = W - 40
    for i, line in enumerate(['지도 위에서 경로를 계산하는 서버를 만들고,', '의료 추천 모델을 재현하는 연구를 합니다.', '김승윤 · 한성대학교 컴퓨터공학부 4학년']):
        p, _ = text(line, right, 222 + i * 32, 21, 'SemiBold' if i == 2 else 'Regular', -0.01, c['muted'] if i == 2 else c['ink'], 'end'); parts.append(p)
    label, lw = text('seungyoon-portfolio.vercel.app', 0, 0, 19, 'SemiBold', -0.01, c['on_accent'])
    bw = lw + 44
    p, _ = text('seungyoon-portfolio.vercel.app', right - bw + 22, 350, 19, 'SemiBold', -0.01, c['on_accent'])
    parts.append(f'<rect x="{right - bw:.1f}" y="316" width="{bw:.1f}" height="52" fill="{c["accent"]}"/>')
    parts.append(p)
    assert 40 + max(w1, w2) < right - bw - 24, 'headline runs into the right column'
    return svg(W, H, 'Seungyoon Kim · 지도 위에서 경로를 계산하는 서버를 만들고, 의료 추천 모델을 재현하는 연구를 합니다 · 김승윤, 한성대학교 컴퓨터공학부 4학년 · seungyoon-portfolio.vercel.app', parts)


def check(c, question, before, after, verdict, label):
    W, H = 440, 250
    parts = [f'<rect width="{W}" height="{H}" fill="{c["card"]}"/>']
    for i, line in enumerate(question):
        p, _ = text(line, 28, 46 + i * 28, 20, 'SemiBold', -0.02, c['ink']); parts.append(p)
    p, wb = text(before, 26, 166, 48, 'ExtraBold', -0.05, c['before']); parts.append(p)
    p, wa = text(' → ', 26 + wb, 166, 48, 'ExtraBold', -0.05, c['ink']); parts.append(p)
    p, wc = text(after, 26 + wb + wa, 166, 48, 'ExtraBold', -0.05, c['ink']); parts.append(p)
    assert 26 + wb + wa + wc < W - 20, f'{before} → {after} is too wide'
    p, _ = text(verdict, 28, 218, 17, 'SemiBold', -0.01, c['muted']); parts.append(p)
    return svg(W, H, label, parts)


def footer(c):
    W, H = 1200, 260
    p, w = text('seungyoon', 0, 0, 280, 'ExtraBold', -0.065, c['ink'])
    size = 280 * (W - 80) / w
    p, _ = text('seungyoon', 40, 30 + size * 0.74, size, 'ExtraBold', -0.065, c['ink'])
    return svg(W, H, 'seungyoon', [p])


def svg(w, h, label, parts):
    body = '\n  '.join(parts)
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}" role="img" aria-label="{label}">\n  {body}\n</svg>\n'


CHECKS = {
    'hidr': (['HI-DR 과다 추천 가설'], '0.4550', '0.5231', '가설과 다른 결과 · 후보 풀 재설계 · Jaccard',
             'HI-DR 과다 추천 가설은 틀렸고(방문당 후보 20.07개, 정답 20.16개), 후보 풀을 다시 설계해 현재 방문 기준 Jaccard 0.4550에서 0.5231'),
    'dcc': (['DCC 증상 분류 F1 개선'], '0.5967', '0.6599', '원인 확인 후 개선 · Macro F1@0.5',
            'DCC 예선 증상 다중 라벨 분류 Macro F1@0.5, 손실 가중 보정으로 0.5967에서 제출 0.6599'),
    'ddi': (['SafeDrug DDI 페널티의 군집별 영향'], '0.030', '0.016', '군집마다 다르게 작동 · 끄면 격차 감소',
            'SafeDrug DDI 페널티를 끄자 군집 간 초과 DDI 격차가 0.030에서 0.016으로 감소, k = 10, 4-seed 모두'),
}

if __name__ == '__main__':
    os.makedirs(OUT, exist_ok=True)
    for theme, c in THEMES.items():
        files = {f'hero-{theme}.svg': hero(c), f'footer-{theme}.svg': footer(c)}
        for key, args in CHECKS.items():
            files[f'check-{key}-{theme}.svg'] = check(c, *args)
        for name, body in files.items():
            with open(os.path.join(OUT, name), 'w', encoding='utf-8', newline='\n') as fh:
                fh.write(body)
            print(name, len(body) // 1024, 'KB')
