# Spotlight @crisxai5 — make.fun bounty entry

Entry for make.fun bounty [`u-tina-spotlight-crisxai5-ai-crypto-expert-on-x-7c1ed9ad`](https://make.fun/bounty/u-tina-spotlight-crisxai5-ai-crypto-expert-on-x-7c1ed9ad)
— "Spotlight @crisxai5: AI & Crypto Expert on X". Prize $2 USDC, Top 10 by
public X engagement (likes + reposts + quotes). Entries close 27 Nov 2026 11:35 UTC.

## Status: READY — WAITING FOR THE POST

The graphic is made and this repo is ready. The X post itself has **not** been
posted yet: posting is done by the account owner (@RAZOR62266) from his own X
account. Once he posts, `POST.json` is updated with the live post URL and the
entry is submitted.

## The graphic

`spotlight-crisxai5.png` — 1080×1350 (4:5), rendered in-session by
`render_card.py` (Python + PIL, Noto Sans, deterministic seed). Dark
crypto-terminal card: "MUST-FOLLOW ON X" badge, giant `@crisxai5`, "AI &
CRYPTO EXPERT", three pillars (AI Agents / Crypto Insights / Web3 Innovation),
CTA `x.com/crisxai5`. Verified phone-readable, no blurry text.

## How to post (for the account owner)

1. Post `spotlight-crisxai5.png` as a **native image** on a public X post from
   @RAZOR62266, with the exact text in `POST-TEXT.md` (copy-paste as-is).
2. Post between the bounty opening (25 Nov 2026 11:32 UTC) and the deadline
   (27 Nov 2026 11:35 UTC / 18:35 WIB).
3. Copy the post URL and send it back — `POST.json` gets updated to
   `{"url": "https://x.com/RAZOR62266/status/<id>"}` and the entry is submitted.
4. Keep the post up and the account public until results are out.

## The program

`main.ts` (Node 22, stdlib only, from the bounty starter) copies `POST.json`
to `/output/POST.json` — that is all the program does. The post itself is the
entry; the house reads its counts from X.

Run locally:

```sh
mkdir -p out && MAKEFUN_BOT_DIR=. MAKEFUN_OUTPUT_DIR=out node main.ts
```
