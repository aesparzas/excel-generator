import factory
import random
from faker import Factory as faker_factory


fake = faker_factory.create()
MODE = ['TRUCK', 'LTL', 'VESSEL OCEAN', 'RAIL', 'PLANE']


class LTL():
	pass

class Truck():
	pass

class Record(factory.Factory):
	record_id = factory.LazyAttribute(lambda x: random.randint(1,10))
	client_code =  factory.LazyAttribute(lambda x: fake.sentence(nb_words = 1))
	vendor_type = ''
	rate_type = ''
	external_rate_source = ''
	mode = factory.LazyAttribute(lambda x: fake.sentence(ext_word_list = MODE, nb_words = 1))
	equipment = ''
	route = ''
	fuel_program = ''
	round_trip = ''
	incoterms = ''
	freight_terms = ''
	notes = ''
	geography_exclusion = ''
	origin_location_code = ''
	origin_region = ''
	origin_city = ''
	origin_county = ''
	origin_state = ''
	origin_zip = ''
	origin_zip_range = ''
	origin_country = ''
	destination_location_code = ''
	destination_region = ''
	destination_city = ''
	destination_county = ''
	destination_state = ''
	destination_zip = ''
	destination_zip_range = ''
	destination_country = ''
	efective_date = ''
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
	allow_deficit = ''
	allow_higher_down = ''
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