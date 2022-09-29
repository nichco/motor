import csdl
import python_csdl_backend

class motor(csdl.Model):
    def initialize(self):
        pass
    def define(self):

        power_density = self.declare_variable('power_density') # (w/kg) ~3000-5000
        available_power = self.declare_variable('available_power')

        motor_weight = available_power/power_density

        self.register_output('motor_weight',motor_weight)


