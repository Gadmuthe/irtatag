class Thermostat:
    def __init__(self, target_temp=25):
        self.target_temp = target_temp
        self.current_temp = 25  # Initial temperature

    def set_temperature(self, new_temp):
        self.current_temp = new_temp

    def adjust_temperature(self):
        if self.current_temp < self.target_temp:
            self.current_temp += 1
            return f"Increasing temperature. Current temperature: {self.current_temp}°C"
        elif self.current_temp > self.target_temp:
            self.current_temp -= 1
            return f"Decreasing temperature. Current temperature: {self.current_temp}°C"
        else:
            return f"Temperature is at the target level of {self.target_temp}°C"

# Example usage:
thermostat = Thermostat(target_temp=28)  # Set target temperature
print(thermostat.adjust_temperature())  # Simulate adjusting temperature
print(thermostat.adjust_temperature())  # Simulate adjusting temperature again
thermostat.set_temperature(28)  # Change current temperature manually
print(thermostat.adjust_temperature())  # Simulate adjusting temperature after manual change