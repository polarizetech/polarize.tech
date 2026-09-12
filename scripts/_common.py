"""Shared helpers for the polarize.tech publishing gate.

Deliberately dependency-free (stdlib only) so the GitHub Action needs no install
step and so this never silently diverges from a pinned PyYAML version.

The two YAML dialects we parse are both narrow and machine-written:
  * polarizetech/research CITATIONS.yaml — flat `key:` blocks, 2-space scalars,
    4-space `- "string"` lists. Parsed the same way the research repo parses it.
  * post front matter — scalars, `- item` lists, and `>-` folded blocks. Anything
    fancier is rejected loudly rather than half-understood.
"""
import re
from pathlib import Path

SITE = Path(__file__).resolve().parent.parent

TIERS = ('A', 'B', 'C', 'SPEC')
TIER_RANK = {'A': 3, 'B': 2, 'C': 1, 'SPEC': 0}

# Files in the research repo we must never publish from.
FORBIDDEN_SOURCE_DIRS = ('RETRACTED/', 'archive/')


# --------------------------------------------------------------------------
# research repo: CITATIONS.yaml
# --------------------------------------------------------------------------
def load_ledger(path):
    """Read the flat, machine-written CITATIONS.yaml into {key: record}.

    Reads the same file as scripts/_lib.py:load_ledger in polarizetech/research,
    but tracks which list a `- item` belongs to. The upstream helper assumes every
    4-space list item is an author, which silently folds `used_in:` corpus paths
    into `authors:` — harmless for a grep-style audit, but it would print file
    paths as author names in a published bibliography.
    """
    led, cur, listkey = {}, None, None
    path = Path(path)
    if not path.exists():
        return led
    for line in path.read_text().splitlines():
        if line.startswith('#') or not line.strip():
            continue
        if not line.startswith(' ') and line.rstrip().endswith(':'):
            cur, listkey = line.rstrip()[:-1], None
            led[cur] = {'authors': [], 'used_in': []}
        elif cur is None:
            continue
        elif re.match(r'\s{4}- ', line):
            if listkey:
                led[cur].setdefault(listkey, []).append(_scalar(line.strip()[2:]))
        else:
            m = re.match(r'\s{2}(\w+):\s*(.*?)\s*(?:#.*)?$', line)
            if m:
                key, val = m.group(1), m.group(2).strip()
                if val == '':
                    listkey = key
                    led[cur].setdefault(key, [])
                else:
                    listkey = None
                    led[cur][key] = _scalar(val)
    return led


def load_generated(path):
    """Read a _data/*.yml file written by sync_research.py.

    Shape: top-level `key:` blocks, 2-space `field: "value"` scalars, and
    2-space `field:` list headers whose items are 4-space `- "value"`.
    """
    out, cur, listkey = {}, None, None
    path = Path(path)
    if not path.exists():
        return out
    for line in path.read_text().splitlines():
        if line.startswith('#') or not line.strip():
            continue
        if not line.startswith(' ') and line.rstrip().endswith(':'):
            cur, listkey = line.rstrip()[:-1], None
            out[cur] = {}
        elif cur is None:
            continue
        elif re.match(r'\s{4}- ', line):
            if listkey:
                out[cur].setdefault(listkey, []).append(_scalar(line.strip()[2:]))
        else:
            m = re.match(r'\s{2}(\w+):\s*(.*)$', line)
            if m:
                key, val = m.group(1), m.group(2).strip()
                if val == '':
                    listkey = key
                    out[cur][key] = []
                else:
                    listkey = None
                    out[cur][key] = _scalar(val)
    return out


def parse_claim(path):
    """Claim files carry a small header block, then markdown sections."""
    txt = Path(path).read_text()
    hdr = {}
    for line in txt.splitlines():
        if line.startswith('##') or line.startswith('# '):
            break
        m = re.match(r'(\w+):\s*(.*)', line)
        if m:
            hdr[m.group(1)] = m.group(2).strip()

    def _list(s):
        return [x.strip() for x in re.sub(r'[\[\]]', '', s or '').split(',') if x.strip()]

    ftr = {}
    for pair in _list(hdr.get('full_text_read', '').strip('{}')):
        if ':' in pair:
            k, val = pair.split(':', 1)
            ftr[k.strip()] = val.strip().lower() == 'true'

    return {
        'id': hdr.get('id'),
        'statement': hdr.get('statement', ''),
        'sources': _list(hdr.get('sources', '')),
        'full_text_read': ftr,
        'tier': hdr.get('tier'),
        'has_disproof': bool(_section(txt, 'Disproof conditions').strip()),
        'has_disconfirming': bool(_section(txt, 'disconfirming_evidence').strip()),
    }


def _section(txt, name):
    m = re.search(rf'^##\s*{re.escape(name)}\s*$(.*?)(?=^##\s|\Z)', txt,
                  re.MULTILINE | re.DOTALL | re.IGNORECASE)
    return m.group(1) if m else ''


# --------------------------------------------------------------------------
# this repo: post front matter
# --------------------------------------------------------------------------
FM_RE = re.compile(r'\A---\s*\n(.*?)\n---\s*\n(.*)\Z', re.DOTALL)


class FrontMatterError(ValueError):
    pass


def split_post(path):
    """Return (front_matter_dict, body). Raises if front matter is absent."""
    txt = Path(path).read_text()
    m = FM_RE.match(txt)
    if not m:
        raise FrontMatterError(f'{path}: no YAML front matter')
    return parse_front_matter(m.group(1), path), m.group(2)


def parse_front_matter(block, path='<post>'):
    fm, key, mode = {}, None, None
    for raw in block.splitlines():
        if not raw.strip() or raw.lstrip().startswith('#'):
            continue

        # continuation of a folded (>-) scalar or a list
        if raw.startswith(('  ', '\t')) and key is not None:
            item = raw.strip()
            if mode == 'list':
                if not item.startswith('- '):
                    raise FrontMatterError(f'{path}: expected "- item" under {key}:, got {item!r}')
                fm[key].append(_scalar(item[2:]))
            elif mode == 'folded':
                fm[key] = (fm[key] + ' ' + item).strip()
            else:
                raise FrontMatterError(f'{path}: unexpected indented line under {key}: {item!r}')
            continue

        m = re.match(r'([A-Za-z_][\w-]*):\s*(.*)$', raw)
        if not m:
            raise FrontMatterError(f'{path}: cannot parse front-matter line {raw!r}')
        key, val = m.group(1), m.group(2).strip()
        if val in ('>-', '>', '|', '|-'):
            fm[key], mode = '', 'folded'
        elif val == '':
            fm[key], mode = [], 'list'
        elif val.startswith('[') and val.endswith(']'):
            # YAML flow sequence: `citations: []` or `claims: [A, B]`. Without this the
            # value became the STRING "[]", which downstream code iterates character by
            # character -- producing citation keys "[" and "]" and two failures that name
            # a bracket as if it were a ledger key. Found writing the first post that
            # legitimately cites nothing.
            inner = val[1:-1].strip()
            fm[key] = [_scalar(x) for x in inner.split(',') if x.strip()] if inner else []
            mode = 'list'
        else:
            fm[key], mode = _scalar(val), 'scalar'
    return fm


def _scalar(v):
    v = v.strip()
    if len(v) >= 2 and v[0] == v[-1] and v[0] in '"\'':
        v = v[1:-1]
    return v


# --------------------------------------------------------------------------
# citation keys used in a body
# --------------------------------------------------------------------------
# Both citation mechanisms count as citing a key in the body:
#   cite.html   — superscript marker, bibliography at the foot of the post
#   source.html — inline source card at the point of use (added 2026-09-12)
# A key cited by EITHER must be declared in front matter, and a declared key must
# be cited by one of them. Widening this regex rather than adding a second one
# keeps that both-directions check in a single place.
CITE_INCLUDE_RE = re.compile(
    r'\{%-?\s*include\s+(?:cite|source)\.html\s+key=["\']([A-Za-z0-9_-]+)["\']\s*-?%\}')


def cite_keys_in(body):
    """Ordered, de-duplicated citation keys actually used in the body."""
    seen, out = set(), []
    for k in CITE_INCLUDE_RE.findall(body):
        if k not in seen:
            seen.add(k)
            out.append(k)
    return out


def posts(include_drafts=False):
    found = sorted((SITE / '_posts').glob('*.md')) if (SITE / '_posts').exists() else []
    if include_drafts and (SITE / '_drafts').exists():
        found += sorted((SITE / '_drafts').glob('*.md'))
    return found


# --------------------------------------------------------------------------
# YAML emission (we only ever write strings, bools and lists of strings)
# --------------------------------------------------------------------------
def y(value):
    if isinstance(value, bool):
        return 'true' if value else 'false'
    s = str(value)
    return '"' + s.replace('\\', '\\\\').replace('"', '\\"') + '"'
