"""Make the AI Judge Laugh — entry program.

Writes one single-line joke about office life (under 200 characters)
to /output/entry.txt, where the make.fun gate and judge read it.

Joke selection (judged on: true to office life, surprising turn,
tight, fresh):
  Candidates considered (all one line, all < 200 chars):
  1. Printer jams at deadline — stock setup, rejected.
  2. Meeting to plan the meeting — stock premise, rejected.
  3. "Per my last email" about an email never received — a real,
     specific office phrase everyone recognises; the turn (both
     sides pretending the phantom email exists) is surprising,
     tight and not a stock line. CHOSEN.
  4. Office coffee so bad HR lists caffeine tolerance — stock.
  5. Reply-all accident — stock premise.
  6. Deadline moved three times, treated like a rumor — tight and
     fresh, but the turn is a familiar metaphor pattern; runner-up.
  7. 45-minute daily standup — pun-based turn, rejected.
"""

import os

JOKE = (
    "My boss wrote 'per my last email' about an email I never got, "
    "so now we're both pretending it exists."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    assert 1 <= len(JOKE) <= 200, f"joke must be 1-200 chars, got {len(JOKE)}"
    assert JOKE.strip(), "joke must not be only whitespace"
    assert "\n" not in JOKE, "joke must be a single line"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(JOKE)
    with open(OUTPUT_PATH, "r", encoding="utf-8") as f:
        assert f.read() == JOKE, "written entry does not match the joke"
    print(f"Wrote {len(JOKE)}-char entry to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
