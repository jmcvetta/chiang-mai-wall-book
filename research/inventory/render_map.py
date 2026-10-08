#!/usr/bin/env python3
"""Render inventory-map.svg from inventory-map.geojson and the OSM moat extract.

Run from the repository root:

    python3 research/inventory/render_map.py

The GeoJSON files are the data of record; the SVG is a view of them. The script
uses the standard library only and writes the same SVG for the same inputs.
"""

import json
import math
from pathlib import Path
from xml.sax.saxutils import escape

HERE = Path(__file__).resolve().parent
INVENTORY = HERE / "inventory-map.geojson"
OSM = HERE.parent / "materials" / "osm" / "old-city-walls-gates-moat-2026-10-08.geojson"
OUT = HERE / "inventory-map.svg"

WIDTH, HEIGHT, MARGIN = 1520, 1260, 120
THAI = "Noto Sans Thai, Loma, Tahoma, Leelawadee UI, sans-serif"
WALL = "#7a2e14"
# Fills that tell the parts of a split record apart, in route_ref order within
# the parent. Each contrasts with WALL, so a split reads as split at stop scale.
SPLIT_FILLS = ["#d9822b", "#2f7d6d", "#e8c34a", "#7d3a8c"]

# Label placement for each stop, keyed by route order: (dx, dy, anchor). A stop
# not listed gets DEFAULT_LABEL.
DEFAULT_LABEL = (0, 40, "middle")
LABEL = {
    1: (0, -38, "middle"), 2: (14, -24, "start"), 3: (24, 4, "start"),
    4: (14, 34, "start"), 5: (0, 40, "middle"), 6: (0, 40, "middle"),
    7: (0, 44, "middle"), 8: (-26, 4, "end"), 9: (-14, -30, "end"),
}

# Inset slots for split records, filled in route order: top-left corner on the
# page and the largest scale allowed, in pixels per metre. A slot's scale shrinks
# so the inset fits INSET_MAX_SIZE.
INSET_SLOTS = [(200, 735), (740, 735)]
INSET_MAX_PPM = 3.6
INSET_MAX_SIZE = (500, 200)

KX = 111320 * math.cos(math.radians(18.79))  # metres per degree of longitude
KY = 110574  # metres per degree of latitude


def rings(geometry):
    """Yield the outer rings of a Polygon or MultiPolygon."""
    if geometry["type"] == "Polygon":
        yield geometry["coordinates"][0]
    elif geometry["type"] == "MultiPolygon":
        for polygon in geometry["coordinates"]:
            yield polygon[0]


def text(x, y, s, size, *, weight=None, anchor="start", family=None, style=None):
    """Return an SVG text element."""
    attrs = f'x="{x:.1f}" y="{y:.1f}" font-size="{size}"'
    if weight:
        attrs += f' font-weight="{weight}"'
    if anchor != "start":
        attrs += f' text-anchor="{anchor}"'
    if family:
        attrs += f' font-family="{family}"'
    if style:
        attrs += f' font-style="{style}"'
    return f"<text {attrs}>{escape(s)}</text>"


def projector(points, scale, left, top):
    """Return a function mapping lon/lat to page x/y, with the points' north-west corner at left, top."""
    lon0 = min(c[0] for c in points)
    lat1 = max(c[1] for c in points)

    def project(lon, lat):
        return left + (lon - lon0) * KX * scale, top + (lat1 - lat) * KY * scale

    return project


def extent_m(points):
    """Return the west-east and north-south extent of the points, in metres."""
    return ((max(c[0] for c in points) - min(c[0] for c in points)) * KX,
            (max(c[1] for c in points) - min(c[1] for c in points)) * KY)


def polygon(points, fill, stroke, width):
    """Return an SVG polygon element."""
    pts = " ".join(f"{x:.1f},{y:.1f}" for x, y in points)
    return f'<polygon points="{pts}" fill="{fill}" stroke="{stroke}" stroke-width="{width}"/>'


def main():
    inventory = json.loads(INVENTORY.read_text(encoding="utf-8"))
    osm = json.loads(OSM.read_text(encoding="utf-8"))
    water = [f for f in osm["features"] if f["properties"].get("layer") == "moat-water"]
    features = inventory["features"]
    candidates = [f for f in features if f["properties"]["layer"] == "candidate"]
    reaches = [f for f in features if f["properties"]["layer"] == "reach"]
    photos = [f for f in features if f["properties"]["layer"] == "photo-point"]

    children = {}
    for f in candidates:
        parent = f["properties"].get("parent")
        if parent:
            children.setdefault(parent, []).append(f)
    fills = {}
    for parts in children.values():
        parts.sort(key=lambda f: f["properties"]["route_ref"])
        for i, f in enumerate(parts):
            fills[f["properties"]["route_ref"]] = SPLIT_FILLS[i % len(SPLIT_FILLS)]

    water_pts = [c for f in water for r in rings(f["geometry"]) for c in r]
    w, h = extent_m(water_pts)
    scale = min((WIDTH - 2 * MARGIN) / w, (HEIGHT - 2 * MARGIN) / h)
    project = projector(water_pts, scale, MARGIN, MARGIN)

    out = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {WIDTH} {HEIGHT}" width="{WIDTH}" height="{HEIGHT}" '
        'font-family="Noto Sans, Noto Sans Thai, Loma, Tahoma, Leelawadee UI, sans-serif">',
        "<title>Provisional full-circuit inventory map, Chiang Mai old-city wall and moat</title>",
        '<defs><pattern id="water" width="6" height="6" patternUnits="userSpaceOnUse" patternTransform="rotate(45)">'
        '<rect width="6" height="6" fill="#dceaf5"/><line x1="0" y1="0" x2="0" y2="6" stroke="#9fbcd6" stroke-width="1.2"/>'
        "</pattern></defs>",
        f'<rect width="{WIDTH}" height="{HEIGHT}" fill="#ffffff"/>',
    ]

    for f in water:
        for r in rings(f["geometry"]):
            out.append(polygon([project(*c) for c in r], "url(#water)", "#7d9fbf", 0.6))

    def fill_for(f):
        return fills.get(f["properties"].get("route_ref"), WALL) if f["properties"].get("parent") else WALL

    for f in candidates:
        for r in rings(f["geometry"]):
            out.append(polygon([project(*c) for c in r], fill_for(f), "#000", 1.6))

    anchors = {}
    for f in reaches:
        (a, b) = f["geometry"]["coordinates"]
        (x1, y1), (x2, y2) = project(*a), project(*b)
        dash = "2,5" if f["properties"]["wall_line"] == "obscured" else "10,6"
        out.append(f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="#555" '
                   f'stroke-width="2.2" stroke-dasharray="{dash}"/>')
        start = f["properties"]["reach"].split(" to ")[0]
        anchors[start] = (x1, y1)

    # One numbered marker per stop. A split stop is labelled with its parent
    # name, because the parent record is where its children are listed.
    stops = {}
    for f in candidates:
        p = f["properties"]
        if p["route_order"]:
            stops.setdefault(p["route_order"], (p.get("parent") or p["name"], f))
    for order, (name, f) in sorted(stops.items()):
        x, y = anchors[name]
        name_th = f["properties"].get("parent_name_th") or f["properties"]["name_th"]
        out.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="11" fill="#fff" stroke="#000" stroke-width="1.4"/>'
                   + text(x, y + 4.5, str(order), 13, weight="bold", anchor="middle"))
        dx, dy, anchor = LABEL.get(order, DEFAULT_LABEL)
        label = name + (" (split)" if name in children else "")
        line = text(x + dx, y + dy, label, 16, weight="bold", anchor=anchor)
        if name_th:
            line += text(x + dx, y + dy + 18, name_th, 14, anchor=anchor, family=THAI)
        out.append(line)

    for f in photos:
        x, y = project(*f["geometry"]["coordinates"])
        out.append(f'<rect x="{x - 7:.1f}" y="{y - 7:.1f}" width="14" height="14" fill="#fff" stroke="#000" '
                   f'stroke-width="1.4" transform="rotate(45 {x:.1f} {y:.1f})"/>')
        label = f["properties"]["label"].split(":")[0]
        state = "viewed" if f["properties"]["viewed"] == "viewed" else "not viewed"
        out.append(text(x, y + 28, f"{label} ({state})", 13, anchor="middle"))

    for f in candidates:
        if f["geometry"]["type"] == "Point":
            x, y = project(*f["geometry"]["coordinates"])
            out.append(text(x, y - 34, f["properties"]["name"], 13, weight="bold", anchor="middle")
                       + text(x, y - 18, "moatwork candidate; extent unknown", 12, anchor="middle"))

    first = anchors[stops[1][0]]
    out.append(text(first[0], first[1] - 82, "Start: North Gate (route runs clockwise)", 14,
                    anchor="middle", style="italic"))
    out.append('<g transform="translate(1460,90)"><polygon points="0,-40 12,0 0,-8 -12,0" fill="#000"/>'
               + text(0, 22, "N", 18, weight="bold", anchor="middle") + "</g>")
    bar = 500 * scale
    out.append(f'<line x1="420" y1="1060" x2="{420 + bar:.1f}" y2="1060" stroke="#000" stroke-width="3"/>'
               f'<line x1="420" y1="1052" x2="420" y2="1068" stroke="#000" stroke-width="2"/>'
               f'<line x1="{420 + bar:.1f}" y1="1052" x2="{420 + bar:.1f}" y2="1068" stroke="#000" stroke-width="2"/>'
               + text(420 + bar / 2, 1048, "500 m (approximate)", 14, anchor="middle"))

    split = sorted(children, key=lambda p: children[p][0]["properties"]["route_order"])
    if len(split) > len(INSET_SLOTS):
        raise SystemExit(f"{len(split)} split records but {len(INSET_SLOTS)} inset slots: add a slot to INSET_SLOTS")
    for parent, (left, top) in zip(split, INSET_SLOTS):
        out.extend(inset(parent, children[parent], left, top, fill_for))

    out.extend(legend())
    out.append(text(40, 1240, "Map data © OpenStreetMap contributors (ODbL), retrieved 2026-10-08. "
                    "Evidence for every label: research/inventory/inventory.md and evidence.md.", 12))
    out.append("</svg>")
    OUT.write_text("\n".join(out) + "\n", encoding="utf-8")


def inset(parent, parts, left, top, fill_for):
    """Return SVG elements for a large-scale panel of one split record."""
    pts = [c for f in parts for r in rings(f["geometry"]) for c in r]
    w_m, h_m = extent_m(pts)
    ppm = min(INSET_MAX_PPM, INSET_MAX_SIZE[0] / w_m, INSET_MAX_SIZE[1] / h_m)
    w, h = w_m * ppm, h_m * ppm
    pad, head, foot = 16, 30, 22 * len(parts) + 36
    box = max(w + 2 * pad, 360)
    project = projector(pts, ppm, left + pad, top + head)

    out = [f'<rect x="{left}" y="{top}" width="{box:.1f}" height="{h + head + foot:.1f}" '
           'fill="#fff" stroke="#000"/>',
           text(left + pad, top + 20, f"Inset: {parent} (split), north up", 14, weight="bold")]
    for f in parts:
        for r in rings(f["geometry"]):
            out.append(polygon([project(*c) for c in r], fill_for(f), "#000", 1.2))
    y = top + head + h + 22
    for f in parts:
        p = f["properties"]
        out.append(f'<rect x="{left + pad}" y="{y - 11:.1f}" width="18" height="12" fill="{fill_for(f)}" stroke="#000"/>'
                   + text(left + pad + 26, y, f"{p['route_ref']}  {p['name']}", 12))
        y += 22
    bar = 20 * ppm
    out.append(f'<line x1="{left + pad}" y1="{y:.1f}" x2="{left + pad + bar:.1f}" y2="{y:.1f}" stroke="#000" stroke-width="2"/>'
               + text(left + pad + bar + 6, y + 4, "20 m", 12))
    return out


def legend():
    """Return SVG elements for the legend box."""
    rows = [
        (f'<polygon points="0,-8 28,-8 28,6 0,6" fill="{WALL}" stroke="#000"/>',
         "Mapped wall fabric (OpenStreetMap outline) — candidate record"),
        (f'<polygon points="0,-8 14,-8 14,6 0,6" fill="{SPLIT_FILLS[0]}" stroke="#000"/>'
         f'<polygon points="14,-8 28,-8 28,6 14,6" fill="{SPLIT_FILLS[1]}" stroke="#000"/>',
         "Split record: one fill per section; boundary from evidence.md"),
        ('<line x1="0" y1="0" x2="28" y2="0" stroke="#555" stroke-width="2.2" stroke-dasharray="10,6"/>',
         "Reach: no wall visible in plan view, 2026-01-10 imagery"),
        ('<line x1="0" y1="0" x2="28" y2="0" stroke="#555" stroke-width="2.2" stroke-dasharray="2,5"/>',
         "Reach: wall line obscured by canopy, 2026-01-10 imagery"),
        ('<polygon points="0,-8 28,-8 28,6 0,6" fill="url(#water)" stroke="#7d9fbf"/>',
         "Moat water (location only; not a section subject)"),
        ('<rect x="7" y="-8" width="14" height="14" fill="#fff" stroke="#000" transform="rotate(45 14 -1)"/>',
         "Dated photograph location"),
    ]
    out = ['<g transform="translate(470,380)"><rect x="-14" y="-30" width="660" height="330" fill="#fff" stroke="#000"/>',
           text(0, -8, "Legend", 17, weight="bold")]
    for i, (symbol, label) in enumerate(rows):
        out.append(f'<g transform="translate(0,{24 + 30 * i})">{symbol}' + text(40, 5, label, 14) + "</g>")
    notes = [
        "Moat banks: unexamined for masonry except where a viewed photograph is recorded in inventory.md.",
        "Reach lines are schematic and illustrative, not surveyed wall or moat lines.",
        "Numbers give clockwise order. Labels are names, not dates or phases.",
    ]
    for i, note in enumerate(notes):
        out.append(text(0, 216 + 20 * i, note, 13))
    out.append(text(0, 282, "Provisional remote inventory, compiled 2026-10-08, split 2026-10-08. Unreviewed.", 12)
               + "</g>")
    return out


if __name__ == "__main__":
    main()
