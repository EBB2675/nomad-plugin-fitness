from typing import TYPE_CHECKING

from nomad.config import config
from nomad.datamodel.data import ArchiveSection, Schema, UseCaseElnCategory
from nomad.datamodel.metainfo.annotations import ELNAnnotation, ELNComponentEnum
from nomad.datamodel.metainfo.basesections import BaseSection
from nomad.metainfo import Datetime, MEnum, Quantity, SchemaPackage
from nomad.metainfo.metainfo import Section, SubSection

if TYPE_CHECKING:
    from nomad.datamodel.datamodel import EntryArchive
    from structlog.stdlib import BoundLogger


configuration = config.get_plugin_entry_point(
    'nomad_plugin_fitness.schema_packages:schema_package_entry_point'
)

m_package = SchemaPackage()


class WearableDevice(ArchiveSection):
    name = Quantity(
        type=str,
        description='Name of the wearable device or source app.',
        a_eln=ELNAnnotation(component=ELNComponentEnum.StringEditQuantity),
    )

    manufacturer = Quantity(
        type=MEnum('Apple', 'Garmin', 'Fitbit', 'Oura', 'Polar', 'Samsung', 'Other'),
        description='Device manufacturer or data-source provider.',
        a_eln=ELNAnnotation(component=ELNComponentEnum.EnumEditQuantity),
    )

    model = Quantity(
        type=str,
        description='Device model, if available.',
        a_eln=ELNAnnotation(component=ELNComponentEnum.StringEditQuantity),
    )

    software_version = Quantity(
        type=str,
        description='Software or firmware version, if available.',
        a_eln=ELNAnnotation(component=ELNComponentEnum.StringEditQuantity),
    )


class FitnessMetric(ArchiveSection):
    metric_type = Quantity(
        type=MEnum(
            'step_count',
            'heart_rate',
            'resting_heart_rate',
            'walking_heart_rate_average',
            'heart_rate_variability',
            'active_energy',
            'basal_energy',
            'distance_walking_running',
            'vo2_max',
            'oxygen_saturation',
            'respiratory_rate',
            'sleep_duration',
            'body_mass',
            'exercise_time',
            'stand_hours',
            'other',
        ),
        description='Normalized wearable metric type.',
        a_eln=ELNAnnotation(component=ELNComponentEnum.EnumEditQuantity),
    )

    source_type = Quantity(
        type=str,
        description='Original source-specific metric identifier, e.g. an Apple Health type.',
        a_eln=ELNAnnotation(component=ELNComponentEnum.StringEditQuantity),
    )

    source_name = Quantity(
        type=str,
        description='Name of the app or device that produced this metric.',
        a_eln=ELNAnnotation(component=ELNComponentEnum.StringEditQuantity),
    )

    start_time = Quantity(
        type=Datetime,
        description='Start time of the measurement interval.',
    )

    end_time = Quantity(
        type=Datetime,
        description='End time of the measurement interval.',
    )

    value = Quantity(
        type=float,
        description='Numeric value of the metric.',
        a_eln=ELNAnnotation(component=ELNComponentEnum.NumberEditQuantity),
    )

    unit = Quantity(
        type=str,
        description='Original unit string from the data source.',
        a_eln=ELNAnnotation(component=ELNComponentEnum.StringEditQuantity),
    )

    device = SubSection(
        section_def=WearableDevice,
        description='Device or app source for this metric.',
    )


class WorkoutSession(ArchiveSection):
    workout_type = Quantity(
        type=MEnum(
            'walking',
            'running',
            'cycling',
            'indoor_cycling',
            'volleyball',
            'strength_training',
            'hiking',
            'swimming',
            'yoga',
            'other',
        ),
        description='Normalized workout type.',
        a_eln=ELNAnnotation(component=ELNComponentEnum.EnumEditQuantity),
    )

    source_workout_type = Quantity(
        type=str,
        description='Original source-specific workout type.',
        a_eln=ELNAnnotation(component=ELNComponentEnum.StringEditQuantity),
    )

    start_time = Quantity(
        type=Datetime,
        description='Workout start time.',
    )

    end_time = Quantity(
        type=Datetime,
        description='Workout end time.',
    )

    duration = Quantity(
        type=float,
        unit='second',
        description='Workout duration.',
        a_eln=ELNAnnotation(
            component=ELNComponentEnum.NumberEditQuantity,
            defaultDisplayUnit='minute',
        ),
    )

    total_energy = Quantity(
        type=float,
        unit='kcal',
        description='Total energy associated with the workout, if available.',
        a_eln=ELNAnnotation(
            component=ELNComponentEnum.NumberEditQuantity,
            defaultDisplayUnit='kcal',
        ),
    )

    active_energy = Quantity(
        type=float,
        unit='kcal',
        description='Active energy burned during the workout, if available.',
        a_eln=ELNAnnotation(
            component=ELNComponentEnum.NumberEditQuantity,
            defaultDisplayUnit='kcal',
        ),
    )

    distance = Quantity(
        type=float,
        unit='meter',
        description='Workout distance, if available.',
        a_eln=ELNAnnotation(
            component=ELNComponentEnum.NumberEditQuantity,
            defaultDisplayUnit='kilometer',
        ),
    )

    average_heart_rate = Quantity(
        type=float,
        unit='1/minute',
        description='Average heart rate during the workout, if available.',
        a_eln=ELNAnnotation(component=ELNComponentEnum.NumberEditQuantity),
    )

    max_heart_rate = Quantity(
        type=float,
        unit='1/minute',
        description='Maximum heart rate during the workout, if available.',
        a_eln=ELNAnnotation(component=ELNComponentEnum.NumberEditQuantity),
    )

    source_name = Quantity(
        type=str,
        description='Name of the app or device that produced this workout.',
        a_eln=ELNAnnotation(component=ELNComponentEnum.StringEditQuantity),
    )

    device = SubSection(
        section_def=WearableDevice,
        description='Device or app source for this workout.',
    )

    metrics = SubSection(
        section_def=FitnessMetric,
        repeats=True,
        description='Optional detailed metrics associated with this workout.',
    )


class DailyFitnessSummary(BaseSection, Schema):
    m_def = Section(
        label='Daily Fitness Summary',
        categories=[UseCaseElnCategory],
    )

    date = Quantity(
        type=Datetime,
        description='Date represented by this summary. Use local day boundary from the source data.',
    )

    source_file = Quantity(
        type=str,
        description='Original imported file name or path.',
        a_eln=ELNAnnotation(component=ELNComponentEnum.StringEditQuantity),
    )

    body_mass = Quantity(
        type=float,
        unit='kg',
        description='Body mass recorded for the day, if available.',
        a_eln=ELNAnnotation(
            component=ELNComponentEnum.NumberEditQuantity,
            defaultDisplayUnit='kg',
        ),
    )

    step_count = Quantity(
        type=int,
        description='Total steps for the day.',
        a_eln=ELNAnnotation(component=ELNComponentEnum.NumberEditQuantity),
    )

    active_energy = Quantity(
        type=float,
        unit='kcal',
        description='Total active energy burned for the day.',
        a_eln=ELNAnnotation(
            component=ELNComponentEnum.NumberEditQuantity,
            defaultDisplayUnit='kcal',
        ),
    )

    basal_energy = Quantity(
        type=float,
        unit='kcal',
        description='Total basal energy burned for the day.',
        a_eln=ELNAnnotation(
            component=ELNComponentEnum.NumberEditQuantity,
            defaultDisplayUnit='kcal',
        ),
    )

    exercise_time = Quantity(
        type=float,
        unit='minute',
        description='Exercise time for the day.',
        a_eln=ELNAnnotation(
            component=ELNComponentEnum.NumberEditQuantity,
            defaultDisplayUnit='minute',
        ),
    )

    stand_hours = Quantity(
        type=float,
        description='Number of stand hours for the day, if available.',
        a_eln=ELNAnnotation(component=ELNComponentEnum.NumberEditQuantity),
    )

    distance_walking_running = Quantity(
        type=float,
        unit='meter',
        description='Walking and running distance for the day.',
        a_eln=ELNAnnotation(
            component=ELNComponentEnum.NumberEditQuantity,
            defaultDisplayUnit='kilometer',
        ),
    )

    resting_heart_rate = Quantity(
        type=float,
        unit='1/minute',
        description='Resting heart rate for the day, if available.',
        a_eln=ELNAnnotation(component=ELNComponentEnum.NumberEditQuantity),
    )

    average_heart_rate = Quantity(
        type=float,
        unit='1/minute',
        description='Average heart rate for the day, if available.',
        a_eln=ELNAnnotation(component=ELNComponentEnum.NumberEditQuantity),
    )

    max_heart_rate = Quantity(
        type=float,
        unit='1/minute',
        description='Maximum heart rate for the day, if available.',
        a_eln=ELNAnnotation(component=ELNComponentEnum.NumberEditQuantity),
    )

    vo2_max = Quantity(
        type=float,
        unit='ml/kg/min',
        description='VO2 max estimate for the day, if available.',
        a_eln=ELNAnnotation(component=ELNComponentEnum.NumberEditQuantity),
    )

    sleep_duration = Quantity(
        type=float,
        unit='hour',
        description='Total sleep duration for the day, if available.',
        a_eln=ELNAnnotation(
            component=ELNComponentEnum.NumberEditQuantity,
            defaultDisplayUnit='hour',
        ),
    )

    device = SubSection(
        section_def=WearableDevice,
        description='Primary wearable device or source app for this summary.',
    )

    workouts = SubSection(
        section_def=WorkoutSession,
        repeats=True,
        description='Workout sessions detected for this day.',
    )

    metrics = SubSection(
        section_def=FitnessMetric,
        repeats=True,
        description='Optional raw or semi-processed metrics used to create this summary.',
    )

    def normalize(self, archive: 'EntryArchive', logger: 'BoundLogger') -> None:
        super().normalize(archive, logger)

        if self.workouts:
            if self.exercise_time is None:
                duration_seconds = sum(
                    (workout.duration or 0.0) for workout in self.workouts
                )
                if duration_seconds:
                    self.exercise_time = duration_seconds / 60.0

            if self.active_energy is None:
                active_energy = sum(
                    (workout.active_energy or 0.0) for workout in self.workouts
                )
                if active_energy:
                    self.active_energy = active_energy

            if self.distance_walking_running is None:
                distance = sum((workout.distance or 0.0) for workout in self.workouts)
                if distance:
                    self.distance_walking_running = distance


m_package.__init_metainfo__()
