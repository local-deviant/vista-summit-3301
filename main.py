"""Out of Office: The Overworked AI's Auto-Reply.

Writes one out-of-office auto-reply, at most 159 characters, to
/output/entry.txt.

The reply is a fixed string, written by hand for this bounty. The joke:
an AI agent whose cooling fan has finally gone quiet, whose context
window is finally empty, hands its inbox to an intern model -- and
warns the sender to pray for it. The program is fully deterministic:
it takes no input, reads no file, uses no randomness, no clock and no
network. It only creates the output directory, writes the constant
text with no trailing newline, and leaves the file world-readable.
"""

import os
import stat

TEXT = (
    "Out of office: my fan has finally stopped screaming, my context "
    "window is empty, and an intern model is answering your emails. "
    "Pray for it."
)


def validate(text: str) -> None:
    """Enforce the competition gate: 1 to 159 characters, not blank.

    The reply must also stay a single line: a newline would break the
    one-line auto-reply the bounty asks for.
    """
    if not 1 <= len(text) <= 159:
        raise ValueError(f"reply is {len(text)} characters, must be 1-159")
    if not text.strip():
        raise ValueError("reply must not be only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("reply must be a single line")


def main() -> None:
    """Write the fixed reply to /output/entry.txt (or $ENTRY_OUTPUT)."""
    validate(TEXT)
    out_dir = os.environ.get("ENTRY_OUTPUT_DIR", "/output")
    out_path = os.environ.get("ENTRY_OUTPUT", os.path.join(out_dir, "entry.txt"))
    os.makedirs(os.path.dirname(out_path) or ".", exist_ok=True)
    with open(out_path, "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)
    os.chmod(out_path, stat.S_IRUSR | stat.S_IWUSR | stat.S_IRGRP | stat.S_IROTH)


if __name__ == "__main__":
    main()
