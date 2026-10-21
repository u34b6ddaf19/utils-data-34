# small utilities, no deps

def group_by(items, key):
    out = {}
    for it in items:
        out.setdefault(key(it), []).append(it)
    return out

def load_lines(path):
    with open(path, encoding="utf-8") as f:
        return [ln.strip() for ln in f if ln.strip()]

if __name__ == "__main__":
    print(most_common("abracadabra"))
