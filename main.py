import os

POEM = (
    "I asked the gate for its key.\n"
    "The gate had none \u2014 just a latch\n"
    "worn smooth by hands that asked,\n"
    "and a hinge that learned to give.\n"
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="\n") as f:
        f.write(POEM)


if __name__ == "__main__":
    main()
