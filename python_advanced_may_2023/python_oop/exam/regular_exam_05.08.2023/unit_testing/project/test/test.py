from unittest import TestCase, main
from project.second_hand_car import SecondHandCar



class TestSecondHandCar(TestCase):
        def setUp(self):
            self.car = SecondHandCar("Toyota Camry", "Sedan", 20000, 12000.0)


        def test_correct_initialization(self):
            self.assertEqual("Toyota Camry", self.car.model)
            self.assertEqual("Sedan", self.car.car_type)
            self.assertEqual(20000, self.car.mileage)
            self.assertEqual(12000.0, self.car.price)
            self.assertEqual([], self.car.repairs)


        def test_set_invalid_price(self):
            with self.assertRaises(ValueError) as ve:
                self.car.price = 0.5
            self.assertEqual('Price should be greater than 1.0!', str(ve.exception))


        def test_set_invalid_mileage(self):
            with self.assertRaises(ValueError) as ve:
                self.car.mileage = 50
            self.assertEqual('Please, second-hand cars only! Mileage must be greater than 100!', str(ve.exception))


        def test_set_promotional_price(self):
            result = self.car.set_promotional_price(11000.0)
            self.assertEqual('The promotional price has been successfully set.', result)
            self.assertEqual(11000.0, self.car.price)


        def test_promotion_price_higher_than_current_value_error_rise(self):
            with self.assertRaises(ValueError) as ve:
                self.car.set_promotional_price(13000.0)
            self.assertEqual('You are supposed to decrease the price!', str(ve.exception))


        def test_need_repair(self):
            result = self.car.need_repair(500.0, "Replace Brake Pads")
            self.assertEqual('Price has been increased due to repair charges.', result)
            self.assertEqual(12500.0, self.car.price)
            self.assertEqual(["Replace Brake Pads"], self.car.repairs)


        def test_repair_price_greater_than_current_value_error(self):
            result = self.car.need_repair(7000.0, "Replace Engine")
            self.assertEqual('Repair is impossible!', result)
            self.assertEqual(12000.0, self.car.price)
            self.assertEqual([], self.car.repairs)


        def test_comparison_same_type(self):
            car2 = SecondHandCar("Honda Civic", "Sedan", 18000, 10000.0)
            result = self.car > car2
            self.assertEqual(True, result)

            result = self.car < car2
            self.assertEqual(False, result)


        def test_comparison_different_type(self):
            car3 = SecondHandCar("Ford F150", "Truck", 25000, 15000.0)
            result = self.car > car3
            self.assertEqual('Cars cannot be compared. Type mismatch!', result)

            result = self.car < car3
            self.assertEqual('Cars cannot be compared. Type mismatch!', result)


        def test_str_representation_valid(self):
            self.assertEqual(f"""Model Toyota Camry | Type Sedan | Milage 20000km\nCurrent price: 12000.00 | Number of Repairs: 0""", str(self.car))



if __name__ == "__main__":
    main()


