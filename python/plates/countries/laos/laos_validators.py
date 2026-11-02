"""Port of laos_plate/lib/src/laos_validators.dart. Hand-ported; codegen never overwrites this file."""
from __future__ import annotations

import re
from typing import Set

from plates.core.validators.plate_validator import GatedPlateValidator, PlateEntry, PlateValidation, is_digits_of_length


class LaosClassLetters:
    passenger_car: Set[str] = {'ກ', 'ຂ', 'ຄ', 'ນ', 'ມ', 'ຣ', 'ລ', 'ວ', 'ຫ', 'ອ', 'ຮ'}
    motorbike: Set[str] = {'ຈ', 'ຍ', 'ດ', 'ຕ', 'ທ'}
    tricycle: Set[str] = {'ສ'}
    heavy_truck: Set[str] = {'ບ'}
    all: Set[str] = {'ກ', 'ຂ', 'ຄ', 'ນ', 'ມ', 'ຣ', 'ລ', 'ວ', 'ຫ', 'ອ', 'ຮ', 'ຈ', 'ຍ', 'ດ', 'ຕ', 'ທ', 'ສ', 'ບ'}


class LaosValidator(GatedPlateValidator):
    gate_group = "serial"

    reason_letters = "The register is two consonants."
    reason_class = "The first consonant is not a vehicle-class letter."
    reason_serial = "The number is four digits."

    def judge(self, entry: PlateEntry) -> PlateValidation:
        letters = entry.group("letters")
        if len(letters) != 2:
            return PlateValidation.invalid(self.reason_letters)
        if letters[0] not in LaosClassLetters.all:
            return PlateValidation.invalid(self.reason_class)
        if not is_digits_of_length(entry.group("serial"), 4):
            return PlateValidation.invalid(self.reason_serial)
        return PlateValidation.valid()


class LaosTemporaryValidator(GatedPlateValidator):
    gate_group = "serial"

    reason_letters = "The register is two consonants."
    reason_serial = "The number is one digit and three."
    reason_expiry = "The expiry date is 2-4-2 digits."

    def judge(self, entry: PlateEntry) -> PlateValidation:
        if len(entry.group("letters")) != 2:
            return PlateValidation.invalid(self.reason_letters)
        if not is_digits_of_length(entry.group("digit"), 1) or not is_digits_of_length(entry.group("serial"), 3):
            return PlateValidation.invalid(self.reason_serial)
        if not is_digits_of_length(entry.group("expiryLead"), 2) or not is_digits_of_length(entry.group("expiryYear"), 4) or not is_digits_of_length(entry.group("expiryTail"), 2):
            return PlateValidation.invalid(self.reason_expiry)
        return PlateValidation.valid()


class LaosPrefixedValidator(GatedPlateValidator):
    gate_group = "serial"

    reason_code = "The code is two digits."
    reason_serial = "The number is two or four digits."

    def judge(self, entry: PlateEntry) -> PlateValidation:
        has_code = entry.spec.indices_of_group("code")
        if has_code and not is_digits_of_length(entry.group("code"), 2):
            return PlateValidation.invalid(self.reason_code)
        serial_len = 2 if has_code else 4
        if is_digits_of_length(entry.group("serial"), serial_len):
            return PlateValidation.valid()
        return PlateValidation.invalid(self.reason_serial)
