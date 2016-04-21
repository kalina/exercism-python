
class Allergies():
    allergy_list = {'eggs':1, 'peanuts':2, 'shellfish':4,'strawberries':8,'tomatoes':16,'chocolate':32,'pollen':64,'cats':128}
    sorted_values = [x for x in allergy_list.iteritems()]
    sorted_values.sort(key=lambda x: x[1])
    sorted_values.reverse()

    #lst = []
    def __init__(self, score):
        self.lst = []
        self.score = score
        #find_allergies(score)
        #print self.sorted_values
        self.lst = self.find_allergies(score)

    def find_allergies(self, score):
        lst = []
        for allergin, value in self.sorted_values:
            if score >=  value:
                lst.append(allergin)
                score = score - value
        return lst

    def is_allergic_to(self, allergin):
        #global lst

        if allergin in self.lst:
            return True
        else:
            return False
