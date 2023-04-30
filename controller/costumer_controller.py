from model.da.costumer_da import CostumerDa
from model.entity.costumer import Costumer


class CostumerController:
    @classmethod
    def save(cls, name, family, birth_date):
        costumer = Costumer(name, family, birth_date)
        costumer_da = CostumerDa()
        costumer_da.save(costumer)

    @classmethod
    def edit(cls, code, name, family, birth_date, active):
        costumer = Costumer(name, family, birth_date, active, code)
        costumer_da = CostumerDa()
        costumer_da.edit(costumer)

    @classmethod
    def remove(cls, code):
        costumer_da = CostumerDa()
        costumer_da.remove(code)

    @classmethod
    def find_all(cls):
        costumer_da = CostumerDa()
        return costumer_da.find_all()

    @classmethod
    def find_by_code(cls, code):
        costumer_da = CostumerDa()
        costumer = costumer_da.find_by_code(code)
        if costumer:
            costumer = costumer[0]
            costumer = Costumer(costumer[1], costumer[2], costumer[3], costumer[4], costumer[0])
            return costumer

    def find_by_name_family(self, name, family):
        costumer_da = CostumerDa()
        print(costumer_da.find_by_name_family(name, family))
