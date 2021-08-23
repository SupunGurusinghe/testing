from django.db import models


# Component percentage data
class FertilizerComponents(models.Model):
    # data columns with its constraints
    component = models.CharField(max_length=255, primary_key=True)
    component_percentage = models.IntegerField()


# Initial plant fertilizer data
class PlantTermDetails(models.Model):
    # for avoid redundancy use variables
    LONG_TERM_COVER_CROP = 'Long'
    SHORT_TERM_COVER_CROP = 'Short'
    APPLICATION1 = '1st'
    APPLICATION2 = '2nd'
    APPLICATION3 = '3rd'

    # List for select plant type whether a short-term or long-term cover crop
    PLANT_TYPE_CHOICES = [
        (LONG_TERM_COVER_CROP, 'Long Term Cover Crops'),
        (SHORT_TERM_COVER_CROP, 'Short Term Cover Crops'),
    ]

    # List for select the application of planting
    TERM = [
        (APPLICATION1, 'Application 1'),
        (APPLICATION2, 'Application 2'),
        (APPLICATION3, 'Application 3'),
    ]

    # data columns with its constraints
    plant_name = models.CharField(max_length=255)
    plant_type = models.CharField(max_length=255, choices=PLANT_TYPE_CHOICES, default=LONG_TERM_COVER_CROP)
    plant_picture = models.ImageField(null=True, blank=True)
    planting_application = models.CharField(max_length=255, choices=TERM, default=APPLICATION1)
    organic = models.DecimalField(null=True, blank=True, max_digits=4, decimal_places=2)
    urea = models.DecimalField(null=True, blank=True, max_digits=4, decimal_places=2)
    tsp = models.DecimalField(null=True, blank=True, max_digits=4, decimal_places=2)
    mop = models.DecimalField(null=True, blank=True, max_digits=4, decimal_places=2)
    yala_mixture = models.DecimalField(null=True, blank=True, max_digits=5, decimal_places=2)
    maha_mixture = models.DecimalField(null=True, blank=True, max_digits=5, decimal_places=2)

    # Make composite primary key
    class Meta:
        unique_together = (('plant_name', 'planting_application'),)


# Fertilizer mixture detailed data for long-term cover crops
class LongTermCropDetails(models.Model):
    # data columns with its constraints
    plant = models.ForeignKey(PlantTermDetails, on_delete=models.PROTECT)
    component_type = models.ForeignKey(FertilizerComponents, on_delete=models.PROTECT)
    parts_by_weight = models.IntegerField()
    nutrient_percentage = models.DecimalField(max_digits=5, decimal_places=2)

    # Make composite primary key
    class Meta:
        unique_together = (('plant', 'component_type'),)


# Fertilizer test data
class FertilizerTest(models.Model):
    # for avoid redundancy use variables
    APPLICATION1 = '1st'
    APPLICATION2 = '2nd'
    APPLICATION3 = '3rd'

    # List for select the application of planting
    TERM = [
        (APPLICATION1, 'Application 1'),
        (APPLICATION2, 'Application 2'),
        (APPLICATION3, 'Application 3'),
    ]

    # data columns with its constraints
    test_id = models.CharField(max_length=255, primary_key=True)
    test_plant = models.ForeignKey(PlantTermDetails, on_delete=models.PROTECT)
    test_date = models.DateTimeField(null=True)
    test_organic = models.DecimalField(null=True, max_digits=4, decimal_places=2)
    test_urea = models.DecimalField(null=True, max_digits=4, decimal_places=2)
    test_tsp = models.DecimalField(null=True, max_digits=4, decimal_places=2)
    test_mop = models.DecimalField(null=True, max_digits=4, decimal_places=2)