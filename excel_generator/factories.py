import factory
import random
from faker import Factory as Faker_factory
from datetime import timedelta
from chibi.atlas import Chibi_atlas


fake = Faker_factory.create()
ten_days = timedelta( days=10 )
one_day = timedelta( days=1 )


def build_rates( amount=5 ):
    result = []
    kw = Chibi_atlas()
    for i in range( amount):
        current = Rate.build( **kw )
        kw.low_class_aux = current.low_class
        result.append( current )
    return result


class Rate( factory.Factory ):
    low_class_aux = 0
    low_class = factory.lazy_attribute(
        lambda self: self.low_class_aux + fake.pyfloat(
            positive=True, min_value=50, max_value=150, right_digits=2 ) )
    high_class = factory.lazy_attribute(
        lambda self: self.low_class + fake.pyfloat(
            positive=True, min_value=50, max_value=150, right_digits=2 ) )
    as_class = factory.lazy_attribute( lambda self: self.low_class )

    @factory.post_generation
    def remove_extra( obj, create, extracted, **kw ):
        obj.pop( 'low_class_aux' )

    class Meta:
        model = Chibi_atlas


class LTL( factory.Factory ):
    record_id = factory.lazy_attribute(
        lambda x: fake.pyint( min_value=0, max_value=9999, step=1 ) )
    client_code = factory.lazy_attribute( lambda x: fake.company() )
    vendor_code = factory.lazy_attribute( lambda x: fake.license_plate() )
    rate_type = 'AP'
    external_rate_source = 'CZARLITE'
    mode = 'LTL'
    equipment = ''
    route = ''
    fuel_program = 'DOE BASE 1.21'
    round_trip = ''
    incoterms = ''
    freight_terms = 'B'
    notes = factory.lazy_attribute(
        lambda x: fake.paragraph(
            nb_sentences=3, variable_nb_sentences=True, ext_word_list=None ) )
    geography_exclusion = factory.lazy_attribute( lambda x: fake.pybool() )
    origin_location_code = ''
    origin_region = ''
    origin_city = ''
    origin_county = ''
    origin_state = 'WI,USA'
    origin_zip = ''
    origin_zip_range = ''
    origin_country = ''
    destination_location_code = ''
    destination_region = ''
    destination_city = ''
    destination_county = ''
    destination_state = 'WI,USA'
    destination_zip = ''
    destination_zip_range = ''
    destination_country = ''

    effective_date = factory.lazy_attribute(
        lambda x: fake.date_time_between(
            start_date="now", end_date="+15d", tzinfo=None ) )
    expiration_date = factory.lazy_attribute(
        lambda self: fake.date_time_between_dates(
            datetime_end=self.effective_date + ten_days,
            datetime_start=self.effective_date + one_day,
            tzinfo=None ) )

    load_id = ''
    chargetype = 'LH'
    uom = 'DR'
    instance = ''
    auto_apply = ''
    apply_at_level = ''
    band_uom_min = ''
    band_uom_max = ''
    flat_charge = ''
    rate = ''
    minimum_charge = '83.68'
    maximum_charge = ''
    base_charge = ''
    excess_rate = ''
    discount_rate = '78.70'
    currency_code = 'USD'
    allow_deficit = factory.lazy_attribute( lambda x: fake.pybool() )
    allow_higher_down = factory.lazy_attribute( lambda x: fake.pybool() )
    authority_publisher = 'CZ'
    authority_release = 'LITE'
    authority_section = ''
    authority_item = ''

    authority_effective_date = factory.lazy_attribute(
        lambda x: fake.date_time_between(
            start_date="now", end_date="+15d", tzinfo=None ) )
    authority_expiration_date = factory.lazy_attribute(
        lambda self: fake.date_time_between_dates(
            datetime_end=self.authority_effective_date + ten_days,
            datetime_start=self.authority_effective_date + one_day,
            tzinfo=None ) )
    low_commodity_code = ''
    high_commodity_code = ''
    constraint = ''

    rates = factory.List([
        factory.SubFactory( Rate ) for i in range( random.randrange( 10 ) )
    ])
    rates = factory.lazy_attribute( lambda x: build_rates() )

    class Meta:
        model = Chibi_atlas
"""
RECORD ID
CLIENT CODE
VENDOR CODE
RATE TYPE
EXTERNAL RATE SOURCE
MODE
EQUIPMENT
ROUTE
FUEL PROGRAM
ROUND TRIP
INCOTERMS
FREIGHT TERMS
NOTES
GEOGRAPHY EXCLUSION
ORIGIN LOCATION CODE
ORIGIN REGION
ORIGIN CITY
ORIGIN COUNTY
ORIGIN STATE
ORIGIN ZIP
ORIGIN ZIP RANGE
ORIGIN COUNTRY
DESTINATION LOCATION CODE
DESTINATION REGION
DESTINATION CITY
DESTINATION COUNTY
DESTINATION STATE
DESTINATION ZIP
DESTINATION ZIP RANGE
DESTINATION COUNTRY
EFFECTIVE DATE
EXPIRATION DATE
LOAD ID
CHARGETYPE
UOM
INSTANCE
AUTO APPLY
APPLY AT LEVEL
BAND UOM MIN
BAND UOM MAX
FLAT CHARGE
RATE
MINIMUM CHARGE
MAXIMUM CHARGE
BASE CHARGE
EXCESS RATE
DISCOUNT RATE
CURRENCY CODE
ALLOW DEFICIT
ALLOW HIGHER DOWN
AUTHORITY PUBLISHER
AUTHORITY RELEASE
AUTHORITY SECTION
AUTHORITY ITEM
AUTHORITY EFFECTIVE DATE
AUTHORITY EXPIRATION DATE
LOW COMMODITY CODE
HIGH COMMODITY CODE
LOW CLASS
HIGH CLASS
AS CLASS
CONSTRAINT
"""
