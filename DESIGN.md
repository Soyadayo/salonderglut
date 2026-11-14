# Design

Recorded 2026-11-14 from the built site. The source of truth is `assets/site.css`; the page structure comes from `build.py`.

## World

The studio name on the site is **Salon der Glut**, and its mark is the low-poly flame (`assets/mark-192.png`, `mark-512.png`; `logo-salon-der-glut-1080.png` is the full lockup). The YouTube channel is still called Haus Tacorari, so that name appears only where the text means the channel.


The site is the devlog's prompt card, turned into web pages. Every page opens the way a Haus Tacorari vertical video opens. A framed prompt types one line, with a block cursor. On the home page, an "AI" reply follows in steel blue. After that, the game answers in pictures. Each picture is a 16:9 window with one bold caption line under it.

A page ends the way a video ends. First comes the title card: the name large in mincho, then Salon der Glut, then "開発中". Last comes the sign-off, 「改善の余地、大いにあり」 / "Plenty of room to improve".

## Color

| Token | Value | Use |
|---|---|---|
| `--ground` | `#080606` | Page ground. Same as the video BG. |
| `--panel` | `#161311` | Image placeholder while loading |
| `--ink` | `#eee6dc` | Text |
| `--dim` | `#a1968d` | Secondary text, prompt frame, caret. The video DIM, raised slightly to reach 4.5:1. |
| `--rule` | `#4a423d` | Hairlines, scrollbar thumb |
| `--gold` | `#d9ad5e` (the sand facet of the flame logo) | The only action color: links on hover, the YouTube button, "see this game", focus ring, text selection |
| `--steel` | `#b0bec8` | The AI reply line, and nothing else |

The page is dark because visitors arrive from dark vertical videos, mostly on phones. It should feel continuous with the video they just watched.

## Type

No web fonts are loaded: the privacy policy promises no third-party requests. The faces are the ones the videos use, taken from the system.

- **Mincho** (Yu Mincho / Hiragino Mincho / Noto Serif JP). Game titles, the title card, the feature names in the list.
- **Gothic** (Yu Gothic / Hiragino Sans / Noto Sans JP). Body text, captions, the prompt line (bold), and the sign-off.
- **Palatino** (Palatino Linotype / Book Antiqua). Latin display, the studio name, and English body text.

Display sizes use clamp():

| Element | Size |
|---|---|
| Prompt line | 1.5 to 2.5rem |
| Title card | 2.4 to 4.25rem |
| Sign-off | 2 to 3.6rem |

## Components

- **Prompt card** (`.prompt`). A meta row with the label and the date, then a 3px frame with a 14px radius. Inside the frame: a `>` caret, the line (`h1`), and an optional reply. `assets/type.js` types the line once, which is the one authored motion on the site. Without JS, or with reduced motion, the full line is simply there.
- **Picture window** (`.shot`). A full-column 16:9 image (`object-fit: cover`) with a centered bold caption. Pixel-art images take `.pixel`, which sets `image-rendering: pixelated`.
- **Episode** (home, `.episode`). A picture window, then the game title in mincho, then the kind and status, then a gold "see this game →" link. The whole block is one link.
- **Copy and points** (`.copy`, `.points`). A reading column of 38rem; feature names in mincho over 1px rules.
- **Button** (`.button`). A 2px gold outline with an SVG YouTube icon. On hover it fills with gold.
- **Title card and sign-off** (`.titlecard`, `.verdict`).

## Layout

- One centered column of 52rem. The column echoes the vertical-video frame, so there is no wide desktop grid.
- Section spacing is generous: 4 to 7rem between episodes.
- At 40rem and below, the navigation wraps under the logo and the JA/EN switch sits on the right.

## Rules

- Gold is the only accent. Do not add more colors. Each game's color lives in its screenshots, not in the UI.
- Never edit the line 「村は燃えていた。」.
- No eyebrow labels, card grids, or gradient text.
