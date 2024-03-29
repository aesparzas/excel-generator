import factory
import random
from faker import Factory as faker_factory
from datetime import timedelta
import logging

from util import field_empty_on_probability

PROB_EMPTY = 0.16
fake = faker_factory.create()
MODE = ['TRUCK', 'LTL', 'VESSEL OCEAN', 'RAIL', 'PLANE', 'MARINE']
PROB = [5, 3, 3, 2, 1, 10]
FREIGHT = ['I', 'O', 'B']
ten_days = timedelta(days=10)
one_day = timedelta(days=1)

logger = logging.getLogger( "excel-generator.factories" )

def get_mode():
    pass


class Record(factory.Factory):

    mandatory_attrs = ['record_id', 'efective_date']

    record_id = factory.Sequence(lambda x: x + 1)
    client_code = factory.LazyAttribute(
        lambda x: fake.sentence(nb_words=1)[:-1])
    vendor_type = factory.LazyAttribute(lambda x: fake.company())
    rate_type = 'AP'
    external_rate_source = 'CZARLITE'
    mode = factory.LazyAttribute( lambda x: str(random.choices( MODE,
        weights = PROB, k = 1 )) )
    equipment = factory.LazyAttribute(lambda x: fake.license_plate())
    route = 'CSXT BUFF CN'
    fuel_program = 'DOE BASE 1.21'
    round_trip = ''
    incoterms = ''
    freight_terms = factory.LazyAttribute( lambda x: random.choice( 'IOB' ) )
    notes = ''
    geography_exclusion = factory.lazy_attribute(lambda x: fake.pybool())
    origin_location_code = 'LAX|LGB|VAN'
    origin_region = ''
    origin_city = factory.lazy_attribute(lambda x: str(fake.city()) + str(
        fake.country_code(representation="alpha-2")))
    origin_county = ''
    origin_state = factory.LazyAttribute(
        lambda x: fake.state_abbr(include_territories=True))
    origin_zip = factory.LazyAttribute(lambda x: fake.zipcode())
    origin_zip_range = ''
    origin_country = factory.LazyAttribute(lambda x: fake.country())
    destination_location_code = 'PVG|SHA'
    destination_region = ''
    destination_city = factory.lazy_attribute(lambda x: str(fake.city()) +
        str(fake.country_code(representation="alpha-2")))
    destination_county = ''
    destination_state = factory.LazyAttribute(
        lambda x: fake.state_abbr(include_territories=True))
    destination_zip = factory.LazyAttribute(lambda x: fake.zipcode())
    destination_zip_range = ''
    destination_country = factory.LazyAttribute(lambda x: fake.country())
    efective_date = factory.lazy_attribute(
        lambda x: fake.date_time_between(
            start_date="now", end_date="+15d", tzinfo=None))
    expiration_date = factory.lazy_attribute(
        lambda self: fake.date_time_between_dates(
            datetime_end=self.authority_effective_date + ten_days,
            datetime_start=self.authority_effective_date + one_day,
            tzinfo=None))
    load_id = ''
    chargetype = 'LT'
    uom = 'ML'
    instance = '-'
    auto_apply = factory.lazy_attribute(lambda x: fake.pybool())
    apply_at_level = '1'
    band_uom_min = '0'
    band_uom_max = '10'
    flat_charge = '10.0'
    rate = '2.65'
    minimum_charge = '0'
    maximum_charge = '10'
    base_charge = '10'
    excess_rate = '1'
    discount_rate = '78.70'
    currency_code = 'USD'
    allow_deficit = factory.lazy_attribute(lambda x: fake.pybool())
    allow_higher_down = factory.lazy_attribute(lambda x: fake.pybool())
    authority_publisher = 'CZ'
    authority_release = 'AA'
    authority_section = 'REV1'
    authority_item = 'IL4 IB'
    authority_effective_date = factory.lazy_attribute(
        lambda self: fake.date_time_between(
            start_date=self.efective_date + one_day, end_date="+14d",
            tzinfo=None))
    authority_expiration_date = factory.lazy_attribute(
        lambda self: fake.date_time_between(
            start_date=self.expiration_date + one_day,
            end_date="+14d",
            tzinfo=None))
    low_commodity_code = factory.lazy_attribute(lambda x: fake.pyfloat(
        positive=True, min_value=120, max_value=500))
    high_commodity_code = ''
    low_class = factory.lazy_attribute(
        lambda self: fake.pyfloat(
            positive=True, min_value=50, max_value=150, right_digits=2))
    high_class = factory.lazy_attribute(
        lambda self: self.low_class + fake.pyfloat(
            positive=True, min_value=50, max_value=250, right_digits=4))
    as_class = ''
    constraint = ''

    class Meta:
        model = dict


class Marine(Record):
    mode = 'marine'
    client_code = ['KBXMOLEX','KBXMOLEX','KBXMOLEX','KBXMOLEX','KBXMOLEX']


class Rail(Record):
    pass


class Spot_Quote(Record):
    pass




def generate_rows(num_rows):
    factories = [ Marine, Record ]
    for i in range(num_rows):
        factory = random.choice( factories )
        logger.info( factory.__name__ )
        record = factory.build()
        for k, v in record.items():
            if k not in Record.mandatory_attrs:
                record[k] = field_empty_on_probability(PROB_EMPTY, v)
        yield record


