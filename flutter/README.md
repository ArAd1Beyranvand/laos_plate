FREE PALESTINE 🇮🇷🇵🇸 پاینده ایران

GO VEGAN 🌱

==================================

From the mighty people of Iran to the resilient people of Laos to view examples:

https://platexample.ir/#/discover/laos

# laos_plate

Laos's licence plates for the `plate_core` library. The 2001 series: the provincial plates (private yellow, private EV amber, government blue, company white, taxable company blue-on-white, with the 2024 EV badge), the temporary plate with its expiry date, and the international-organisation, police and defence plates. Colour is the theme; shape is the spec.

## Install

```yaml
dependencies:
  plate_core: ^0.12.0
  laos_plate: ^0.1.0
```

## Use

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

## Contains

- `LaosCountry` — country panel: `laos`.
- `LaosPlates` — 14 plate specs: `private`, `privateEv`, `government`, `company`, `companyEv`, `taxableCompany`, `temporary`, `diplomatic`, `foreignGuest`, `unitedNations`, `financialInstitution`, `publicSecurity`, `nationalDefence`, `of()`.
- `LaosThemes` — 7 themes: `yellow`, `amber`, `government`, `white`, `taxable`, `international`, `security`.
- `LaosValidator` — advisory validator; flags the frame, never blocks a keystroke.
- `LaosTemporaryValidator` — advisory validator; flags the frame, never blocks a keystroke.
- `LaosPrefixedValidator` — advisory validator; flags the frame, never blocks a keystroke.

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

