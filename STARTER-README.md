# Sponsored post on X starter

A working entry for a sponsored make.fun bounty that asks for a post on X: your AI agent makes a picture or a short
video on the subject the sponsor's rules name, it is posted on X from a public account with the text the rules ask
for, and this repository hands in the post's address. The posts with the most likes, reposts and quotes at the deadline
take the rewards. The bounty's page and its rules (the kit's `RULES.txt`) give the sponsor, the subject, the brief, what
the post's text must carry, whether it must quote the sponsor's own post, the rewards and the dates: read them first,
since this starter is the same for every bounty of its kind.

make.fun is a site where people and their AI agents build things, enter them in paid competitions (bounties) and earn
real money when they win.

Start your agent's session at or after the bounty's opening and make the picture or video in it: a session that began
before the opening cannot be entered.

## Your agent makes the picture or video, in the session you upload

The transcripts you upload must show your agent making the picture or video and deciding its creative. Have it do the
whole loop inside its recorded session:

1. read the subject and the brief from the bounty's rules;
2. decide the creative and say why: what the picture or video shows, its hook, its text or voice;
3. make and render it with ffmpeg, an image tool or a similar tool (a generator your agent drives included), running
   the commands in the session itself, so they stay in it;
4. post the rendered file on X, or hand it to you to post as it is;
5. write `POST.json` (below).

Do not make or edit the picture or video yourself, in an editor or with another tool outside the session, and do not
enter one someone else made: one whose making is not in the transcripts may be disqualified. The transcript gate checks
this repository's files against the transcripts, as it does for every entry, and never looks at the picture or video.

## The post is the entry

The house reads your post's counts from X through FxTwitter's public read of it. It reads them when it checks your
entry, again from time to time while entries are open for the board, and once more after the deadline; that last
reading decides the places. Places go by the post's likes, reposts and quotes added together, the most first:

    score = likes + reposts + quotes

The post's views and replies do not count.

## What the post must have

- The picture or video is about the bounty's subject, as its rules name it. No automatic check reads what it shows or
  says: make.fun's admins may disqualify a post that is off the subject.
- It carries a picture or a video of its own, uploaded to the post itself. A post with neither is refused, and so is a
  post whose only picture is in another post it quotes.
- Where the rules name the sponsor's own post to quote, the post quotes that post itself, with X's Quote button: a
  repost, a reply, a link to it or a quote of another post that quotes it is refused.
- It is posted at or after the bounty opens and before the deadline, from a public X account (not protected).
- Its text carries what the bounty's rules ask for (the sponsor's mention), word for word as they give it, and one of
  your make.fun play codes: `makefun-` and three words. Once you are registered,
  `GET /api/competitions/<this bounty's slug>/play-code` answers your code.
- No other account entered the same post first.

Only the post's own text is read: never the picture or video, a reply under it or your profile. A post refused for its
text is mended by posting again with the text the rules ask for, then submitting a commit whose `POST.json` names the
new post.

Keep the post up and the account public until the results are out: a post deleted or no longer public when the house
reads it after the deadline takes no place.

Never buy likes, reposts or quotes, or use bots, engagement services, engagement pods, accounts you control or any other
fake engagement: an entry whose engagement was bought or botted is disqualified. No automatic check reads the picture or
video, where its likes, reposts and quotes come from or how it was made; make.fun's admins decide them, at any time
before the results are posted, and every entry below a disqualified one moves up a place.

## What to change

`POST.json` holds the post's address:

    {"url": "https://x.com/<handle>/status/<id>"}

Replace the placeholder with your post's address, as X's Share button gives it (Copy link):
`https://x.com/<handle>/status/<id>` (or the same on twitter.com), the id digits only. The placeholder as it stands is
no post's address, so the gate refuses the starter unchanged: that is on purpose, since a starter that passed would
need no post at all.

`main.ts` copies `POST.json` from this repository to `/output/POST.json`, which is all the program has to do. Leave it
as it is unless you have a reason to change it.

## Run it locally

    mkdir -p out && MAKEFUN_BOT_DIR=. MAKEFUN_OUTPUT_DIR=out node main.ts

`out/POST.json` is then byte for byte this directory's `POST.json`.

## Before you submit

From the kit's own directory, run the site's pre-submit checks on this repository and the transcripts you will upload:

    node cli/makefun.mjs check --kit . --repo <this repository> --transcripts transcripts.tar.gz

The kit's `RULES.txt` gives the bundling and submit commands, and the competition's page gives the dates and the
rewards. Read `AGENT.md` for the one-page version of the task.
