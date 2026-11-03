FREE PALESTINE 🇮🇷🇵🇸 پاینده ایران

GO VEGAN 🌱

==================================

From the mighty people of Iran to the resilient people of Laos to view examples:

https://platexample.ir/#/discover/laos:flutter

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

### Install

```yaml
dependencies:
  plate_core: ^0.12.0
  laos_plate: ^0.1.0
```

### Use

```dart
import 'package:plate_core/plate_core.dart';
import 'package:laos_plate/laos_plate.dart';

PlateCanvas(
  spec: LaosPlates.private,
  theme: LaosThemes.yellow,
  validator: const LaosValidator(),
  autoValidate: true,
  onChooseCharacter: noCharacterChooser,
);
```

## Specs

Each spec is one plate layout.

- `LaosPlates.of`(…)
- `LaosPlates.private`
- `LaosPlates.privateEv`
- `LaosPlates.government`
- `LaosPlates.company`
- `LaosPlates.companyEv`
- `LaosPlates.taxableCompany`
- `LaosPlates.temporary`
- `LaosPlates.diplomatic`
- `LaosPlates.foreignGuest`
- `LaosPlates.unitedNations`
- `LaosPlates.financialInstitution`
- `LaosPlates.publicSecurity`
- `LaosPlates.nationalDefence`

## Themes

- `LaosThemes.yellow`
- `LaosThemes.amber`
- `LaosThemes.government`
- `LaosThemes.white`
- `LaosThemes.taxable`
- `LaosThemes.international`
- `LaosThemes.security`

## Change it

`PlateCanvas` takes `spec:` (an entry of `LaosPlates`) and `theme:` (an entry of `LaosThemes`). Set `validator:` to `LaosClassLetters()` and `autoValidate: true` to show validation hints.

## Also included

- `LaosCountry` — the country panel.
- `LaosClassLetters` — the plate validator.

## Plates

Laos's licence plates: three designs, thirteen categories. Categories that
differ only by theme share one spec.

* Provincial — the province's name over two consonants and four digits.
  Groups `letters`, `serial`.
* Temporary — two consonants, a digit, a dash and three digits, over
  "ໝົດກຳນົດ" (expiry) and a date printed 2-4-2. Groups `letters`,
  `digit`, `serial`, `expiryLead`, `expiryYear`, `expiryTail`.
* Prefixed — fixed letters and digits on one row: `code` and `serial` for
  the international organisations' 2-2, `serial` for the police and
  defence plates' four.

Pair each with its theme in `themeOf`.

Not implemented: the pre-2001 series, which the article only dates.

## Part of plate

Painted by [`plate_core`](https://pub.dev/packages/plate_core); alphabets shared through [`plate_alphabet`](https://pub.dev/packages/plate_alphabet); optional character picker in [`plate_keypad`](https://pub.dev/packages/plate_keypad).

## License

See [LICENSE](https://github.com/ArAd1Beyranvand/laos_plate/blob/main/LICENSE).
