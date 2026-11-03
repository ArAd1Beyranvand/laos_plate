FREE PALESTINE 🇮🇷🇵🇸 پاینده ایران

GO VEGAN 🌱

==================================

From the mighty people of Iran to the resilient people of Laos to view examples:

https://platexample.ir/#/discover/laos:python

# laos_plate

Laos's licence plates for plate_core: the 2001 series: the two-row provincial plates (private, government, company and taxable company, with the 2024 EV badge), and more.

## Languages

| Language | Folder | Example |
| --- | --- | --- |
| Flutter / Dart | [`flutter/`](https://github.com/ArAd1Beyranvand/laos_plate/tree/main/flutter) | [platexample](https://platexample.ir/#/discover/laos:flutter) |
| Kotlin | [`kotlin/`](https://github.com/ArAd1Beyranvand/laos_plate/tree/main/kotlin) | [platexample](https://platexample.ir/#/discover/laos:kotlin) |
| Python | [`python/`](https://github.com/ArAd1Beyranvand/laos_plate/tree/main/python) | [platexample](https://platexample.ir/#/discover/laos:python) |
| TypeScript | [`typescript/`](https://github.com/ArAd1Beyranvand/laos_plate/tree/main/typescript) | [platexample](https://platexample.ir/#/discover/laos:typescript) |

## Quick start

### Install (Python)

Copy `python/plates/countries/laos/` into `plate_core/python/plates/countries/`.

Then run the tests from `plate_core/python/`: `pytest`.

### Use

```python
from plates.countries.laos.data import SPECS, THEMES

spec = SPECS["la.provincial.vientiane_capital"]
theme = THEMES["LaosThemes.yellow"]
print(spec.id)
```

## Specs

The specs are the same in every language (they come from shared data).

- `la.provincial.vientiane_capital`
- `la.provincial_ev.vientiane_capital`
- `la.temporary`
- `la.diplomatic`
- `la.foreign_guest`
- `la.united_nations`
- `la.financial_institution`
- `la.public_security`
- `la.national_defence`

## Themes

- `LaosThemes.yellow`
- `LaosThemes.amber`
- `LaosThemes.government`
- `LaosThemes.white`
- `LaosThemes.taxable`
- `LaosThemes.international`
- `LaosThemes.security`

## Change it

- Pick a spec: use another key of `SPECS`.
- Pick a theme: use another key of `THEMES`.
- Validators: `VALIDATORS` maps the names `LaosValidator`, `LaosTemporaryValidator`, `LaosPrefixedValidator` to classes.

## License

See [LICENSE](https://github.com/ArAd1Beyranvand/laos_plate/blob/main/LICENSE).
