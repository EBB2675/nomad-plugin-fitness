from __future__ import annotations


APPLE_HEALTH_METRIC_TYPES: dict[str, str] = {
    # Activity and movement
    'HKQuantityTypeIdentifierStepCount': 'step_count',
    'HKQuantityTypeIdentifierActiveEnergyBurned': 'active_energy',
    'HKQuantityTypeIdentifierBasalEnergyBurned': 'basal_energy',
    'HKQuantityTypeIdentifierDistanceWalkingRunning': 'distance_walking_running',
    'HKQuantityTypeIdentifierAppleExerciseTime': 'exercise_time',

    # Heart and cardio
    'HKQuantityTypeIdentifierHeartRate': 'heart_rate',
    'HKQuantityTypeIdentifierRestingHeartRate': 'resting_heart_rate',
    'HKQuantityTypeIdentifierWalkingHeartRateAverage': 'walking_heart_rate_average',
    'HKQuantityTypeIdentifierHeartRateVariabilitySDNN': 'heart_rate_variability',
    'HKQuantityTypeIdentifierVO2Max': 'vo2_max',

    # Respiratory and oxygen
    'HKQuantityTypeIdentifierOxygenSaturation': 'oxygen_saturation',
    'HKQuantityTypeIdentifierRespiratoryRate': 'respiratory_rate',

    # Body measurements
    'HKQuantityTypeIdentifierBodyMass': 'body_mass',

    # Sleep and standing
    'HKCategoryTypeIdentifierSleepAnalysis': 'sleep_duration',
    'HKCategoryTypeIdentifierAppleStandHour': 'stand_hours',
}


APPLE_HEALTH_WORKOUT_TYPES: dict[str, str] = {
    'HKWorkoutActivityTypeWalking': 'walking',
    'HKWorkoutActivityTypeRunning': 'running',
    'HKWorkoutActivityTypeCycling': 'cycling',
    'HKWorkoutActivityTypeIndoorCycling': 'indoor_cycling',
    'HKWorkoutActivityTypeVolleyball': 'volleyball',
    'HKWorkoutActivityTypeTraditionalStrengthTraining': 'strength_training',
    'HKWorkoutActivityTypeFunctionalStrengthTraining': 'strength_training',
    'HKWorkoutActivityTypeHiking': 'hiking',
    'HKWorkoutActivityTypeSwimming': 'swimming',
    'HKWorkoutActivityTypeYoga': 'yoga',
}


PREFERRED_METRIC_UNITS: dict[str, str | None] = {
    'step_count': 'count',
    'heart_rate': '1/minute',
    'resting_heart_rate': '1/minute',
    'walking_heart_rate_average': '1/minute',
    'heart_rate_variability': 'ms',
    'active_energy': 'kcal',
    'basal_energy': 'kcal',
    'distance_walking_running': 'meter',
    'vo2_max': 'ml/kg/min',
    'oxygen_saturation': 'percent',
    'respiratory_rate': '1/minute',
    'sleep_duration': 'hour',
    'body_mass': 'kg',
    'exercise_time': 'minute',
    'stand_hours': 'count',
    'other': None,
}


def normalize_metric_type(source_type: str | None) -> str:
    if not source_type:
        return 'other'
    return APPLE_HEALTH_METRIC_TYPES.get(source_type, 'other')


def normalize_workout_type(source_workout_type: str | None) -> str:
    if not source_workout_type:
        return 'other'
    return APPLE_HEALTH_WORKOUT_TYPES.get(source_workout_type, 'other')


def preferred_unit_for_metric(metric_type: str | None) -> str | None:
    if not metric_type:
        return None
    return PREFERRED_METRIC_UNITS.get(metric_type)


def is_supported_metric_type(source_type: str | None) -> bool:
    if not source_type:
        return False
    return source_type in APPLE_HEALTH_METRIC_TYPES


def is_supported_workout_type(source_workout_type: str | None) -> bool:
    if not source_workout_type:
        return False
    return source_workout_type in APPLE_HEALTH_WORKOUT_TYPES
