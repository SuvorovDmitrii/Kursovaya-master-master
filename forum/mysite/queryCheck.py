

class Check:
    def __init__(self, msg):
        self.txt = msg


    def txtCheck(self):

        electro_list = ['горит', 'светит', 'бьет', 'искрит', 'у меня', 'проводка', 'провода', 'провод', 'счетчик', 'щиток', 'щитовая', 'горят', 'светят', 'бьется', 'искрят', 'квартире', 'cвет', 'электричество', 'ток', 'тока']
        voda_list = ['течет', 'текут', 'капает', 'капают', 'протекает', 'протекают', 'теплой', 'воды', 'холодной', 'вода']
        dvor_list = ['асфальт', 'площадка', 'мусор', 'мусорка', 'светят', 'фонари', 'забор', 'канализация', 'лужи', 'грязь', 'яма', 'авария', 'скамеек', 'скамейка']
        blago_list = [] #благоустройство
        trash_list = [] #мусор
        gaz_list = [] #газоснобжение
        house_list = [] #многоквартирные дома(человейники)

        # Остальное не трогай!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        blago_num = 0
        trash_num = 0
        gaz_num = 0
        house_num = 0
        electro_num = 0
        voda_num = 0
        dvor_num = 0

        txt = self.txt.lower()
        lst = []
        lst = txt.replace('.', '').split()

        for x in range(len(electro_list)):
            electro = electro_list[x]
            for a in range(len(lst)):
                if lst[a] == electro:
                    electro_num += 1

        for x in range(len(voda_list)):
            voda = voda_list[x]
            for a in range(len(lst)):
                if lst[a] == voda:
                    voda_num += 1

        for x in range(len(dvor_list)):
            dvor = dvor_list[x]
            for a in range(len(lst)):
                if lst[a] == dvor:
                    dvor_num += 1
#Раскоменть когда напишешь списки слов
        # for x in range(len(blago_list)):
        #     blago = blago_list[x]
        #     for a in range(len(lst)):
        #         if lst[a] == blago:
        #             blago += 1
        #
        # for x in range(len(trash_list)):
        #     trash = trash_list[x]
        #     for a in range(len(lst)):
        #         if lst[a] == trash:
        #             trash_num += 1
        #
        # for x in range(len(gaz_list)):
        #     gaz = dvor_list[x]
        #     for a in range(len(lst)):
        #         if lst[a] == gaz:
        #             gaz_num += 1
        #
        # for x in range(len(house_list)):
        #     house = house_list[x]
        #     for a in range(len(lst)):
        #         if lst[a] == house:
        #             house += 1

        return [dvor_num, voda_num, electro_num, blago_num, trash_num, gaz_num, house_num]
