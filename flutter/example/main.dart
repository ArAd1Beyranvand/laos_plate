import 'package:flutter/widgets.dart';
import 'package:plate_core/plate_core.dart';
import 'package:laos_plate/laos_plate.dart';

void main() =>
    runApp(PlateExampleApp(spec: LaosPlates.private, theme: LaosThemes.yellow));
