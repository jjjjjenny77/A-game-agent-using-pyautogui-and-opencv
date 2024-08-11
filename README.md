# A-game-agent-using-pyautogui-and-opencv
> This note record and share the midterm project of python course about using pyautohui and opencv to create a game agent
## How to run the code
* Download the code and the cards file
* Open them as a same project
* Run the code and open the game page: https://laijunbin.github.io/sevens/v1/index.html
* Then the game agent will start playing the game for you!
## Game rules:
* 有梅花七的玩家先出，但不一定要先出梅花七
* 有牌可以出就一定要出，若沒有牌可以出則需蓋一張牌，蓋牌規則如下：
  - 挑最小的牌去蓋
    - 例如你沒牌可出，有梅花A，那就蓋他
  - 挑蓋了之後對其他玩家影響(總和)大於自己的蓋
    - 例如你沒牌可出，但有黑桃8，沒有黑桃9~K，那麼你蓋掉黑桃8，對其他玩家影響最大
    - 或者是你有愛心8和Q，你也可以蓋掉愛心8，因為另外三家總會蓋掉9、10、J、K
    - 承上，當然你要蓋掉Q也無所謂，總是會有人蓋一張K
* 直到沒有牌時，遊戲結束
