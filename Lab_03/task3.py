class MeterReading:
    def __init__(self, prev_reading, curr_reading, meter_type):
        self.prev_reading = prev_reading
        self.curr_reading = curr_reading
        self.meter_type = meter_type.lower()
        self.units_consumed = self.curr_reading - self.prev_reading
        self.cost_per_unit = self.calculate_cost_per_unit()
        self.total_bill = self.units_consumed * self.cost_per_unit

    def calculate_cost_per_unit(self):
        if self.units_consumed <= 100:
            if self.meter_type == 'residential':
                return 2
            elif self.meter_type == 'commercial':
                return 4
        elif 100 < self.units_consumed <= 250:
            if self.meter_type == 'residential':
                return 4
            elif self.meter_type == 'commercial':
                return 8
        else:
            if self.meter_type == 'residential':
                return 6
            elif self.meter_type == 'commercial':
                return 12
        # Default fallback
        return 0

    def display_bill(self):
        print("\n--- Current Bill ---")
        print(f"Meter Type        : {self.meter_type.capitalize()}")
        print(f"Previous Reading  : {self.prev_reading}")
        print(f"Current Reading   : {self.curr_reading}")
        print(f"Units Consumed    : {self.units_consumed}")
        print(f"Cost per Unit     : {self.cost_per_unit} rupees")
        print(f"Total Bill Amount : {self.total_bill} rupees")
        print("---------------------\n")

def main():
    try:
        prev = int(input("Enter previous month reading: "))
        curr = int(input("Enter current month reading: "))
        if curr < prev:
            print("Current reading cannot be less than previous reading.")
            return
        meter_type = input("Enter meter type (Residential/Commercial): ").strip().lower()
        if meter_type not in ['residential', 'commercial']:
            print("Invalid meter type. Please enter 'Residential' or 'Commercial'.")
            return
        meter = MeterReading(prev, curr, meter_type)
        meter.display_bill()
    except ValueError:
        print("Invalid input. Please enter integer values for readings.")

if __name__ == "__main__":
    main()
