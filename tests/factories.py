from unittest import TestCase
from excel_generator.factories import LTL


class Test_factory_ltl( TestCase ):
    def test_should_work( self ):
        result = LTL.build()
        self.assertTrue( result )
        self.assertTrue( result.rates )
