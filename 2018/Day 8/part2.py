with open("Day 8.txt","r") as f: inputt = f.read().strip()
# with open("example.txt","r") as f: inputt = f.read().strip()


data = list(map(int, inputt.split(" ")))
# print(data)
# exit()

root_metas = set()

root_childs = {}


def find_value(data):
    child_count = data.pop(0)
    metadata_count = data.pop(0)
    children = [find_value(data) for x in range(child_count)]
    metadata = [data.pop(0) for x in range(metadata_count)]
    if not children:
        return sum(metadata)
    else:
        values_wanted = [children[x-1] for x in metadata if x-1 in range(child_count)]
        return sum(values_wanted)

def val(t):
    ch = t.pop(0)
    md = t.pop(0)
    vals = [val(t) for _ in range(ch)]
    mdata = [t.pop(0) for _ in range(md)]
    if ch == 0:
        return sum(mdata)
    return sum(vals[i-1] if i-1 in range(ch) else 0 for i in mdata)


print(find_value(list(data)))



