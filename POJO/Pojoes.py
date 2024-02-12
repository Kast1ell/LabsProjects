class UserProfile:
    def __init__(self, id=None, user_login=None, user_password=None, first_name=None, last_name=None, phone=None, access_key=None):
        self.id = id
        self.user_login = user_login
        self.user_password = user_password
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone
        self.access_key = access_key


class Chemicals:
    def __init__(self, id=None, chemicals_name=None, chemical_formula=None, molar_mass=None, diffusion_coefficient=None):
        self.id = id
        self.chemicals_name = chemicals_name
        self.chemical_formula = chemical_formula
        self.molar_mass = molar_mass
        self.diffusion_coefficient = diffusion_coefficient


class Roles:
    def __init__(self, id=None, role_name=None, access_key=None):
        self.id = id
        self.role_name = role_name
        self.access_key = access_key


class Reports:
    def __init__(self, id=None, report_date=None, chemical_id=None, user_id=None, max_affected_area=None, affected_area=None, average_population_density=None, max_affected_people_count=None, affected_people_count=None):
        self.id = id
        self.report_date = report_date
        self.chemical_id = chemical_id
        self.user_id = user_id
        self.max_affected_area = max_affected_area
        self.affected_area = affected_area
        self.average_population_density = average_population_density
        self.max_affected_people_count = max_affected_people_count
        self.affected_people_count = affected_people_count
