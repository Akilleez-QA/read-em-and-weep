#!/usr/bin/env python3
"""Independent support walk for the pinned exact-Q normalized axes.

The induction is the one in degree-and-factor48.md: coordinate leaves have
unit exponent vectors; products add bounds; sums take minima and maxima;
a nonzero rational scalar does not change support. Cancellation can only
shrink support, so this is an enclosure. The walk does not expand
polynomials and does not import checks/verify_factor48.py.
"""
import argparse
import hashlib
import json
from fractions import Fraction
from pathlib import Path


def walk(data, axis):
    if axis not in range(4) or data.get("coefficientField") != "Q":
        raise ValueError("expected an exact-Q axis 0..3")
    bounds = {}
    for coordinate in range(4):
        if coordinate == axis:
            continue
        unit = tuple(int(i == coordinate) for i in range(4))
        bounds[coordinate] = (unit, unit, 1, 1)

    def coefficient(pair):
        if not isinstance(pair, list) or len(pair) != 2:
            raise ValueError("coefficient must be a numerator/denominator pair")
        numerator, denominator = int(pair[0]), int(pair[1])
        if denominator <= 0:
            raise ValueError("denominator must be positive")
        value = Fraction(numerator, denominator)
        if value == 0:
            raise ValueError("zero rational term")
        if [str(value.numerator), str(value.denominator)] != pair:
            raise ValueError("rational coefficient is not in lowest terms")
        return value

    def product(factors, limit):
        low = [0, 0, 0, 0]
        high = [0, 0, 0, 0]
        total_low = 0
        total_high = 0
        seen = set()
        for symbol, exponent in factors:
            if (
                type(symbol) is not int
                or type(exponent) is not int
                or exponent < 1
                or symbol not in bounds
                or symbol >= limit
                or symbol in seen
            ):
                raise ValueError("illegal polynomial factor or topological order")
            seen.add(symbol)
            left, right, degree_low, degree_high = bounds[symbol]
            low = [a + exponent * b for a, b in zip(low, left)]
            high = [a + exponent * b for a, b in zip(high, right)]
            total_low += exponent * degree_low
            total_high += exponent * degree_high
        return low, high, total_low, total_high

    for index, terms in enumerate(data["sumNodes"]):
        if not terms:
            raise ValueError("empty sum")
        choices = []
        for coeff, factors in terms:
            coefficient(coeff)
            choices.append(product(factors, 16 + index))
        bounds[16 + index] = (
            [min(choice[0][i] for choice in choices) for i in range(4)],
            [max(choice[1][i] for choice in choices) for i in range(4)],
            min(choice[2] for choice in choices),
            max(choice[3] for choice in choices),
        )
    outputs = []
    limit = 16 + len(data["sumNodes"])
    for output in data["outputs"]:
        coefficient(output["coefficient"])
        low, high, total_low, total_high = product(output["factors"], limit)
        outputs.append(
            {
                "coordinateMinimum": low,
                "coordinateMaximum": high,
                "totalMinimum": total_low,
                "totalMaximum": total_high,
                "factors": output["factors"],
            }
        )
    exposed = {symbol: exponent for symbol, exponent in outputs[1]["factors"]}
    others = [coordinate for coordinate in range(4) if coordinate != axis]
    if any(exposed.get(coordinate) != 48 for coordinate in others):
        raise ValueError("normalized output does not expose coordinate power 48")
    return {
        "axis": axis,
        "normalizedSumSymbols": len(data["sumNodes"]),
        "outputs": [
            {key: value for key, value in item.items() if key != "factors"}
            for item in outputs
        ],
        "exposedCoordinatePowers": {str(coordinate): exposed[coordinate] for coordinate in others},
        "strippedCoordinateUpperBound": outputs[1]["coordinateMaximum"][others[0]] - 48,
        "strippedTotalUpperBound": outputs[1]["totalMaximum"] - 3 * 48,
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--jets", type=Path, required=True)
    parser.add_argument(
        "--pins",
        type=Path,
        default=Path(__file__).resolve().parents[1]
        / "hm/current-scalar-geometric-dependencies/pins.json",
    )
    args = parser.parse_args()
    pins = json.loads(args.pins.read_text())["axes"]
    axes = []
    for axis in range(4):
        path = args.jets / "axes" / f"axis-{axis}.normalized.json"
        raw = path.read_bytes()
        digest = hashlib.sha256(raw).hexdigest()
        pin = pins[str(axis)]
        if digest != pin["normalizedSHA256"]:
            raise SystemExit(f"axis {axis} hash {digest} != pin {pin['normalizedSHA256']}")
        data = json.loads(raw)
        if data["inputSHA256"] != pin["leadingSHA256"]:
            raise SystemExit(f"axis {axis} leading hash mismatch")
        report = walk(data, axis)
        expected = pin["rootSupports"]
        if report["outputs"] != [
            {
                "coordinateMinimum": item["coordinateMinimum"],
                "coordinateMaximum": item["coordinateMaximum"],
                "totalMinimum": item["totalMinimum"],
                "totalMaximum": item["totalMaximum"],
            }
            for item in expected
        ]:
            raise SystemExit(f"axis {axis} support mismatch: {report['outputs']}")
        if report["normalizedSumSymbols"] != pin["normalizedSumSymbols"]:
            raise SystemExit(f"axis {axis} symbol count mismatch")
        if report["strippedCoordinateUpperBound"] != 164 or report["strippedTotalUpperBound"] != 305:
            raise SystemExit(f"axis {axis} stripped bounds {report}")
        axes.append({"normalizedSHA256": digest, "leadingSHA256": data["inputSHA256"], **report})
    print(json.dumps({"status": "PASS", "axes": axes}, indent=2))


if __name__ == "__main__":
    main()
