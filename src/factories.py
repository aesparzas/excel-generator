import factory
import random
from faker import Factory as faker_factory


fake = faker_factory.create()
MODE = ['TRUCK', 'LTL', 'VESSEL OCEAN', 'RAIL', 'PLANE']
FREIGHT = ['I', 'O', 'B']


class LTL():
	pass

class Truck():
	pass

class Record(factory.Factory):
	record_id = factory.LazyAttribute( lambda x: random.randint(1,10) )
	client_code =  factory.LazyAttribute( lambda x: fake.sentence(nb_words = 1) )
	vendor_type = factory.LazyAttribute( lambda x: fake.company() )
	rate_type = 'AP'
	external_rate_source = 'CZARLITE'
	mode = factory.LazyAttribute( lambda x: fake.sentence(ext_word_list = MODE, nb_words = 1) )
	equipment = factory.LazyAttribute( lambda x: fake.license_plate() )
	route = 'CSXT BUFF CN'
	fuel_program = 'DOE BASE 1.21'
	round_trip = ''
	incoterms = ''
	freight_terms = factory.LazyAttribute( lambda x: fake.sentence(ext_word_list = FREIGHT, nb_words = 1) )
	notes = ''
	geography_exclusion = factory.lazy_attribute( lambda x: fake.pybool() )
	origin_location_code = 'LAX|LGB|VAN'
	origin_region = ''
	origin_city = factory.lazy_attribute( lambda x: str(
						fake.city()) + str(
						fake.country_code(representation="alpha-2"))  )
	origin_county = ''
	origin_state = ''
	origin_zip = ''
	origin_zip_range = ''
	origin_country = factory.LazyAttribute( lambda x: fake.country() )
	destination_location_code = ''
	destination_region = ''
	destination_city = ''
	destination_county = factory.LazyAttribute( lambda x: fake.country() )
	destination_state = ''
	destination_zip = ''
	destination_zip_range = ''
	destination_country = ''
	efective_date = factory.lazy_attribute(
							lambda x: fake.date_time_between(
							start_date="now", end_date="+15d", tzinfo=None ) )
	expiration_date = ''
	load_id = ''
	chargetype = ''
	uom = ''
	instance = ''
	auto_apply = ''
	apply_at_level = ''
	band_uom_min = ''
	band_uom_max = ''
	flat_charge = ''
	rate = ''
	minimum_charge = ''
	maximum_charge = ''
	base_charge = ''
	excess_rate = ''
	discount_rate = ''
	currency_code = ''
	allow_deficit = factory.lazy_attribute( lambda x: fake.pybool() )
	allow_higher_down = factory.lazy_attribute( lambda x: fake.pybool() )
	authority_publisher = ''
	authority_release = ''
	authority_section = ''
	authority_item = ''
	authority_effective_date = ''
	authority_expiration_date = ''
	low_commodity_code = ''
	high_commodity_code = ''
	low_class = ''
	high_class = ''
	as_class = ''
	constraint = ''

	class Meta:
		model = dict



def generate_rows(num_rows):
	return Record.build_batch( size=num_rows )