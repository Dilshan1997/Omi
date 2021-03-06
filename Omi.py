import random
import threading
import re
import time

card_types = ['Spades', 'Diamonds', 'Hearts', 'Clubs']
card = {'A': 13, 'K': 12, 'Q': 11, 'J': 10, '10': 9, '9': 8, '8': 7, '7': 6}
m1_card_pack=list()
m2_card_pack=list()
m3_card_pack=list()
m4_card_pack=list()
t1_kata = 10
t2_kata = 10
key_card_type=""
card_pack = list()
shuffeld_card_pack = list()
round_card_type=""
class OmiGame:

    def shuffele_card_pack(self):
        for card_type in card_types:
            for i in card.keys():
                card_pack.append(card_type + " " + i)
        # print(card_pack)

        # card pack shuffeled
        x=32
        for i in range(x):
            shuffel_card=card_pack[random.randrange(0, x)]
            card_pack.remove(shuffel_card)
            shuffeld_card_pack.append(shuffel_card)
            x=x-1
        # print(shuffeld_card_pack)


    def __init__(self,t1,t2,m1,m2,m3,m4):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3
        self.m4 = m4
        self.t1=[self.m1,self.m3]
        self.t2 = [self.m2, self.m4]

    #Key card type called
    def key_card_called(self,player):
        print("###New Match Start### \n")
        if player==self.m1:
            first_four_cards=[shuffeld_card_pack[i] for i in range(4)]
            print(first_four_cards)
            key_card_type=input("Plz chose the key card type: ")
        else:
            key_card_type=random.choice(card_types)
        return key_card_type


    #card_serve
    def card_serve(self):
        print(len(shuffeld_card_pack))
        for i in range(0,8):
            m1_card_pack.append(shuffeld_card_pack[i])
        for i in range(8,16):
            m2_card_pack.append(shuffeld_card_pack[i])
        for i in range(16,24):
            m3_card_pack.append(shuffeld_card_pack[i])
        for i in range(24,32):
            m4_card_pack.append(shuffeld_card_pack[i])
        # print(m1_card_pack)



    def match(self,key_card_type,start_from):
        while(True):
            time.sleep(1)
            print("###New Round Start### \n")
            print("key card type is: ", key_card_type,"\n")
            round_four_cards=self.round(start_from)

            m1_card_list=re.split(" ",round_four_cards[0])
            # print(m1_card_list)
            m2_card_list= re.split(" ", round_four_cards[1])
            # print(m2_card_list)
            m3_card_list=re.split(" ",round_four_cards[2])
            # print(m3_card_list)
            m4_card_list = re.split(" ", round_four_cards[3])
            # print(m4_card_list)


            m1_card_value = card[m1_card_list[1]]
            m2_card_value = card[m2_card_list[1]]
            m3_card_value = card[m3_card_list[1]]
            m4_card_value = card[m4_card_list[1]]


            if m1_card_list[0] == key_card_type or m2_card_list[0]==key_card_type or m3_card_list[0]==key_card_type or m4_card_list[0]==key_card_type:
                if m1_card_list[0]==key_card_type:
                    m1_card_value = m1_card_value + 10

                if m2_card_list[0]==key_card_type:
                    m2_card_value =m2_card_value + 10

                if m3_card_list[0] == key_card_type:
                    m3_card_value = m3_card_value + 10

                if m4_card_list[0]==key_card_type:
                    m4_card_value = m4_card_value+ 10
            m1_card_pack.remove(round_four_cards[0])
            m2_card_pack.remove(round_four_cards[1])
            m3_card_pack.remove(round_four_cards[2])
            m4_card_pack.remove(round_four_cards[3])

            # print(m1_card_value,m2_card_value,m3_card_value,m4_card_value)
            round_four_cards=[m1_card_value,m2_card_value,m3_card_value,m4_card_value]
            # print(max(round_four_cards))
            winner=""
            time.sleep(1)
            if(m1_card_value==max(round_four_cards)):
                print(f"##This round winners are {self.t1}## \n")
                winner=self.m1

            elif (m2_card_value == max(round_four_cards)):
                print(f"##This round winners are {self.t2}## \n")
                winner = self.m2
            elif (m3_card_value == max(round_four_cards)):
                print(f"##This round winners are {self.t1}## \n")
                winner = self.m3
            elif (m4_card_value == max(round_four_cards)):
                print(f"This round winners are {self.t2}## \n")
                winner = self.m4

            if(m1_card_value==max(round_four_cards) or m3_card_value==max(round_four_cards)):
                self.round_count_t1+=1

            else:
                self.round_count_t2+=1

            if(self.round_count_t1==5):
                print(f"this round winner is {self.t1}")
                t2_kata=-1
                return t2_kata
            elif(self.round_count_t2==5):
                print(f"This round winner is {self.t2}")
                t1_kata=-1
                return t1_kata
            elif(self.round_count_t2==4 and self.round_count_t1==4):
                print("This round is draw")
                return 0
            # print(winner)
            time.sleep(1)
            return self.match(key_card_type, winner)

    def start_match(self):
        order_of_called_thurumpu=[self.m1,self.m2,self.m3,self.m4]
        player = order_of_called_thurumpu[0]
        self.round_count_t1=0
        self.round_count_t2=0
        while(True):
            self.shuffele_card_pack()
            if player==order_of_called_thurumpu[3]:
                player = order_of_called_thurumpu[0]
                print('start from:',player)
            key_card_type=self.key_card_called(player)
            # print(key_card_type)
            self.card_serve()
            #match proccess
            kata = self.match(key_card_type,player)
            player= order_of_called_thurumpu[order_of_called_thurumpu.index(player)+1]
            if kata==10:
                print("Winner")



    def round(self,player):
        m1_card=""
        m2_card=""
        m3_card=""
        m4_card=""
        if player==self.m1:
            print(m1_card_pack)
            m1_card=input("Your turn- ")
            print(f'{self.m1} - {m1_card}')
            time.sleep(2)
            m2_card=self.card_selected_process(m1_card,m2_card_pack)
            print(f'{self.m2} - {m2_card}')
            time.sleep(2)
            m3_card=self.card_selected_process(m1_card,m3_card_pack)
            print(f'{self.m3} - {m3_card}')
            time.sleep(2)
            m4_card=self.card_selected_process(m1_card,m4_card_pack)
            print(f'{self.m4} - {m4_card}')

        elif player==self.m2:
            m2_card = random.choice(m2_card_pack)
            print(f'{self.m2} - {m2_card}')
            time.sleep(2)
            m3_card = self.card_selected_process(m2_card,m3_card_pack)
            print(f'{self.m3} - {m3_card}')
            time.sleep(2)
            m4_card = self.card_selected_process(m2_card,m4_card_pack)
            print(f'{self.m4} - {m4_card}')
            time.sleep(2)
            print(m1_card_pack)
            m1_card=input("Your turn- ")
            print(f'{self.m1} - {m1_card}')
            time.sleep(2)


        elif player==self.m3:
            m3_card = random.choice(m3_card_pack)
            print(f'{self.m3} - {m3_card}')
            time.sleep(2)
            m4_card = self.card_selected_process(m3_card,m4_card_pack)
            print(f'{self.m4} - {m4_card}')
            time.sleep(2)
            print(m1_card_pack)
            m1_card = input("Your turn- ")
            print(f'{self.m1} - {m1_card}')
            time.sleep(2)
            m2_card = self.card_selected_process(m3_card,m2_card_pack)
            print(f'{self.m2} - {m2_card}')
            time.sleep(2)

        elif player==self.m4:
            m4_card = random.choice(m4_card_pack)
            print(f'{self.m4} - {m4_card}')
            time.sleep(2)
            print(m1_card_pack)
            m1_card = input("Your turn- ")
            print(f'{self.m1} - {m1_card}')
            time.sleep(2)
            m2_card = self.card_selected_process(m4_card,m2_card_pack)
            print(f'{self.m2} - {m2_card}')
            time.sleep(2)
            m3_card = self.card_selected_process(m4_card,m3_card_pack)
            print(f'{self.m3} - {m3_card}')
            time.sleep(2)
        return m1_card, m2_card, m3_card, m4_card


    def card_selected_process(self,initial_card,player_card_pack):
        spades_cards=list()
        diamonds_cards=list()
        hearts_cards=list()
        clubs_cards=list()
        card_type_using_round=re.split(" ",initial_card)
        #print(card_type_using_round)
        for j in range(0,len(m1_card_pack)):
            o_card=player_card_pack[j]
            card=re.split(" ",player_card_pack[j])
            if card_type_using_round[0]=="Spades" and card_type_using_round[0]==card[0]:
                spades_cards.append(o_card)
            elif card_type_using_round[0]=="Diamonds" and card_type_using_round[0]==card[0]:
                diamonds_cards.append(o_card)
            elif card_type_using_round[0]=="Hearts" and card_type_using_round[0]==card[0]:
                 hearts_cards.append(o_card)
            elif card_type_using_round[0]=="Clubs" and card_type_using_round[0]==card[0]:
                clubs_cards.append(o_card)

        if(card_type_using_round[0]=="Spades" and len(spades_cards)>0):
            selected_card=random.choice(spades_cards)
            return selected_card
        elif(card_type_using_round[0]=="Diamonds" and len(diamonds_cards)>0):
            selected_card = random.choice(diamonds_cards)
            return selected_card
        elif (card_type_using_round[0] == "Hearts" and len(hearts_cards)>0):
            selected_card = random.choice(hearts_cards)
            return selected_card
        elif (card_type_using_round[0] == "Clubs" and len(clubs_cards) > 0):
            selected_card = random.choice(clubs_cards)
            return selected_card
        else:
            return random.choice(player_card_pack)


game=OmiGame("d1","d2","lal","kal","Lokz","chal")
game.start_match()











