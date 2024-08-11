import time
import os
import pyautogui

pyautogui.FAILSAFE = True

screenshot_path = "cards/"
arr = os.listdir(screenshot_path)
print(arr)
first_card_y_location = 795

cards = ['1.c.png', '1.d.png', '1.h.png', '1.s.png',
         '2.c.png', '2.d.png', '2.h.png', '2.s.png',
         '3.c.png', '3.d.png', '3.h.png', '3.s.png',
         '4.c.png', '4.d.png', '4.h.png', '4.s.png',
         '5.c.png', '5.d.png', '5.h.png', '5.s.png',
         '6.c.png', '6.d.png', '6.h.png', '6.s.png',
         '7.c.png', '7.d.png', '7.h.png', '7.s.png',
         '8.c.png', '8.d.png', '8.h.png', '8.s.png',
         '9.c.png', '9.d.png', '9.h.png', '9.s.png',
         '10.c.png', '10.d.png', '10.h.png', '10.s.png',
         '11.c.png', '11.d.png', '11.h.png', '11.s.png',
         '12.c.png', '12.d.png', '12.h.png', '12.s.png',
         '13.c.png', '13.d.png', '13.h.png', '13.s.png']

# 檢查每個卡片是否存在
for card in cards:
    card_path = os.path.join(screenshot_path, card)
    if os.path.exists(card_path):
        print(f"圖片 {card} 存在")
    else:
        print(f"圖片 {card} 不存在")


def update_table():
    table_cards = []
    region = (423, 132, 1336, 639)  #(423,132)(1468,771)

    for card in cards:
            card_path = os.path.join(screenshot_path, card)
            loc = pyautogui.locateOnScreen(card_path, region = region, confidence = 0.97)
            if loc != None:
                print(f"Found the table image {card} at:", loc)
                table_cards.append({"card": card, "location": loc})
    return table_cards

def update_hand():
    hand_cards = []
    region = (428, 770, 937, 217)
    suits = ['c', 'd', 'h', 's']

    for suit in suits:
        for num in range(13):
            card = str(num+1) + '.' + str(suit) + '.png'
            card_path = os.path.join(screenshot_path, card)
            loc = pyautogui.locateOnScreen(card_path, region=region, confidence=0.97)
            if loc is not None:
                print(f"Found the hand image {card} at:", loc)
                hand_cards.append({"suit": suit, "number": num+1, "card": card, "location": loc})
    return hand_cards

def pick_a_card(adjacent_cards):
    for hand_card, table_card in adjacent_cards:
        pyautogui.click(hand_card['location'])
        print(f"Clicked on the adjacent card {hand_card['card']} at:", hand_card['location'])
        break

def subtract_cards(hand_card, table_card):
    # 提取牌的點數信息
    hand_number = int(hand_card['card'].split('.')[0])  # 假設文件名格式是 "數字.花色.png"
    hand_suit = hand_card['card'].split('.')[1]

    table_number = int(table_card['card'].split('.')[0])
    table_suit = table_card['card'].split('.')[1]

    # 检查花色是否相同，如果相同则返回点数差值
    if hand_suit == table_suit:
        return hand_number - table_number
    else:
        # 如果花色不同，可以返回一個特定值或者引发一個異常，具體取决於你的需求
        return None

def find_adjacent_cards(hand_cards, table_cards):
    adjacent_cards = []
    for hand_card in hand_cards:
        for table_card in table_cards:
            if hand_card['card'].split('.')[1] == table_card['card'].split('.')[1]:
                difference = subtract_cards(hand_card, table_card)
                if difference == 1 or difference == -1:
                    adjacent_cards.append((hand_card, table_card))
    print(adjacent_cards)
    return  adjacent_cards


def playable(hand_cards, table_cards, region):
    region = (428, 770, 937, 217)
    has_seven_club = any(card['card'] == '7.c.png' for card in hand_cards)
    if has_seven_club:
        print("可以出任何花色的七")
        card = '7.c.png'
        card_path = os.path.join(screenshot_path, card)
        loc = pyautogui.locateOnScreen(card_path, region=region, confidence=0.98)
        center = pyautogui.center(loc)
        pyautogui.click(center)

    else:
        print("出非梅花7的牌")
        adjacent_cards = find_adjacent_cards(hand_cards, table_cards)
        if not adjacent_cards:
            if any(card['card'] == '7.d.png' for card in hand_cards):
                card_path = os.path.join(screenshot_path, '7.d.png')
                loc = pyautogui.locateOnScreen(card_path, region=region, confidence=0.98)
                center = pyautogui.center(loc)
                pyautogui.click(center)
            elif any(card['card'] == '7.h.png' for card in hand_cards):
                card_path = os.path.join(screenshot_path, '7.h.png')
                loc = pyautogui.locateOnScreen(card_path, region=region, confidence=0.98)
                center = pyautogui.center(loc)
                pyautogui.click(center)
            elif any(card['card'] == '7.s.png' for card in hand_cards):
                card_path = os.path.join(screenshot_path, '7.s.png')
                loc = pyautogui.locateOnScreen(card_path, region=region, confidence=0.98)
                center = pyautogui.center(loc)
                pyautogui.click(center)
            else:
                fold(hand_cards)
        else:
            pick_a_card(adjacent_cards)

def find_the_lowest(hand_cards):
    region =  (428, 770, 937, 217)  #手牌的範圍
    if not hand_cards:
        return None
    lowest_card = hand_cards[0]  # 將第一张牌先假設為最小的
    for card in hand_cards[1: ]:
        hand_number = int(card['card'].split('.')[0])  # 假設文件名格式是 "數字.花色.png"
        lowest_number = int(lowest_card['card'].split('.')[0])

        if hand_number <= lowest_number:
            lowest_card = card

    return lowest_card

def fold(hand_cards):
    if find_the_lowest(hand_cards) != None:
        lowest_card = find_the_lowest(hand_cards)
        pyautogui.click(lowest_card['location'])
        print(f"Clicked on the folded card {lowest_card['card']} at:", lowest_card['location'])


region = (526, 780, 667, 204)  # Define the region here (526,780)(1193,984)
hand_cards = update_hand()
print(hand_cards)
for round in range(13) :
    print("now is range ", round)
    table_cards = update_table()
    hand_cards = update_hand()
    playable(hand_cards, table_cards, region)
    time.sleep(1)
