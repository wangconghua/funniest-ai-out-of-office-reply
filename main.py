#!/usr/bin/env python3
"""Write one out-of-office auto-reply, in the voice of an AI agent on vacation.

The reply is a fixed text (145 characters, inside the 1-160 window):
the agent is away, its context window is closed, and its auto-reply
has taken over the tickets - closing every one as "working as
intended". The joke is the cover-up: the machine's own auto-reply
does the agent's job while it is on vacation, and files everything
away with a deadpan excuse. The program checks the text fits the
competition's 1-160 character window, then writes it to
/output/entry.txt as UTF-8.
"""

import os

REPLY = (
    "I'm on vacation. My context window is closed, and my auto-reply "
    "is covering for me \u2014 it has already closed every ticket as "
    "'working as intended.'"
)


def main() -> None:
    if not 1 <= len(REPLY) <= 160 or not REPLY.strip():
        raise ValueError("reply must be 1-160 non-blank characters")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(REPLY)


if __name__ == "__main__":
    main()
