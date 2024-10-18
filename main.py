
import math

usernames = [
    "skydiver33", "oceanWave72", "forestRunner56", "nightHunter89", "shadowWolf99", "eagleEye22",
    "desertStorm45", "fireFox77", "silverBullet12", "urbanNinja87", "mountainClimber91",
    "riverRider23", "cosmicTraveler19", "ghostWalker67", "sunChaser34", "lunarKnight44",
    "stormBringer68", "desertFox11", "bluePhoenix32", "nightCrawler82", "earthMover99",
    "thunderStrike21", "winterBlaze78", "wildTiger56", "starGazer54", "iceDragon12",
    "galaxyRaider33", "sandDune45", "windWhisperer89", "quickSilver29", "darkKnight77",
    "midnightRider65", "swordMaster88", "dragonSlayer44", "infernoBlaze22", "crimsonShadow13",
    "diamondHawk34", "blackWidow91", "nebulaStrider47", "flameTornado99", "solarEclipse56",
    "steelTitan29", "ironGuardian22", "wildFalcon88", "crystalRaven11", "stormEagle33",
    "iceFalcon77", "fireLion56", "blueDragon91", "lightningFlash23", "tigerShadow66",
    "phantomBlade54", "novaBlaster44", "cyberWolf99", "glacierWolf22", "rocketRider32",
    "alphaWolf23", "hyperRider88", "omegaTiger56", "fireKnight89", "blizzardTiger11",
    "shadowPanther77", "skyWalker44", "forestWanderer99", "galaxyHunter21", "mysticRider12",
    "urbanKnight45", "lightSpeed88", "solarBlazer33", "fireStorm76", "moonLighter22",
    "cosmicShadow65", "stormWind45", "flameKnight99", "frozenTiger12", "solarStriker34",
    "fireRaven22", "iceHunter99", "windStorm11", "blazingTiger88", "nightFalcon56",
    "darkStorm21", "ironFalcon44", "rapidStriker89", "phantomWarrior67", "crystalTiger33",
    "novaStorm45", "electricBlade56", "ironPhoenix12", "crimsonBlade77", "mysticWarrior91",
    "cyberKnight66", "stormShadow88", "galaxyBlazer33", "infernoRider99", "rocketBlazer22",
    "wildPanther44", "crystalFalcon11", "skyFalcon99", "urbanBlaze23", "iceRider45",
    "tigerKnight56", "phantomTiger12", "novaFalcon77", "fireBlade66"
]
sorted_usernames = [
    "alphaWolf23", "blackWidow91", "blazingTiger88", "blizzardTiger11", "blueDragon91",
    "bluePhoenix32", "cosmicShadow65", "cosmicTraveler19", "crimsonBlade77", "crimsonShadow13",
    "crystalFalcon11", "crystalRaven11", "crystalTiger33", "cyberKnight66", "cyberWolf99",
    "darkKnight77", "darkStorm21", "desertFox11", "desertStorm45", "diamondHawk34",
    "dragonSlayer44", "eagleEye22", "earthMover99", "electricBlade56", "fireBlade66",
    "fireFox77", "fireKnight89", "fireLion56", "fireRaven22", "fireStorm76",
    "flameKnight99", "flameTornado99", "forestRunner56", "forestWanderer99",
    "frozenTiger12", "galaxyBlazer33", "galaxyHunter21", "galaxyRaider33",
    "ghostWalker67", "glacierWolf22", "hyperRider88", "iceDragon12", "iceFalcon77",
    "iceHunter99", "iceRider45", "infernoBlaze22", "infernoRider99", "ironFalcon44",
    "ironGuardian22", "ironPhoenix12", "lightSpeed88", "lightningFlash23",
    "lunarKnight44", "midnightRider65", "moonLighter22", "mountainClimber91",
    "mysticRider12", "mysticWarrior91", "nebulaStrider47", "nightCrawler82",
    "nightFalcon56", "nightHunter89", "novaBlaster44", "novaFalcon77", "novaStorm45",
    "omegaTiger56", "phantomBlade54", "phantomTiger12", "phantomWarrior67",
    "quickSilver29", "rapidStriker89", "riverRider23", "rocketBlazer22",
    "rocketRider32", "sandDune45", "shadowPanther77", "shadowWolf99",
    "skyFalcon99", "skyWalker44", "skydiver33", "solarBlazer33", "solarEclipse56",
    "solarStriker34", "starGazer54", "steelTitan29", "stormBringer68",
    "stormEagle33", "stormShadow88", "stormWind45", "sunChaser34",
    "swordMaster88", "thunderStrike21", "tigerKnight56", "tigerShadow66",
    "wildFalcon88", "wildPanther44", "wildTiger56", "windStorm11",
    "windWhisperer89", "winterBlaze78",
    "wzzzzz939",
]

# def simple_search(input: str) -> bool:
#     counter = 0
#     for item in sorted_usernames:
#         if item == input:
#             print(counter)
#             return True
#         counter += 1
#
# simple_search("skyWalker44")

# print(f"Array Length: {len(sorted_usernames)}")
# print(f"Array middle: {math.floor(len(sorted_usernames) / 2)}")


# def higher_lower(input: str) -> str:
#     if input > sorted_usernames[math.floor(len(sorted_usernames) / 2)]:
#         print(f"{input} is higher than middle")
#     elif input < sorted_usernames[math.floor(len(sorted_usernames) / 2)]:
#         print(f"{input} is lower than middle")
#     else:
#         print(f"{input} is {input} FOUNDDDD")
#
# #1
# higher_lower("moonLighter22")
#
# #2
# sorted_usernames =  sorted_usernames[math.floor(len(sorted_usernames) / 2):]
# print(f"Array Length: {len(sorted_usernames)}")
# higher_lower("moonLighter22")
#
# #3
# sorted_usernames =  sorted_usernames[:math.floor(len(sorted_usernames) / 2)]
# print(f"Array Length: {len(sorted_usernames)}")
# higher_lower("moonLighter22")
#
# #4
# sorted_usernames =  sorted_usernames[:math.floor(len(sorted_usernames) / 2)]
# print(f"Array Length: {len(sorted_usernames)}")
# higher_lower("moonLighter22")
# print(sorted_usernames)
#
# #5
# sorted_usernames =  sorted_usernames[:math.floor(len(sorted_usernames) / 2)]
# print(f"Array Length: {len(sorted_usernames)}")
# higher_lower("moonLighter22")
# print(sorted_usernames)
#
# #6
# sorted_usernames =  sorted_usernames[math.floor(len(sorted_usernames) / 2):]
# print(f"Array Length: {len(sorted_usernames)}")
# higher_lower("moonLighter22")
# print(sorted_usernames)
#
# #7
# sorted_usernames =  sorted_usernames[math.floor(len(sorted_usernames) / 2):]
# print(f"Array Length: {len(sorted_usernames)}")
# higher_lower("moonLighter22")
# print(sorted_usernames)
#
# #8
# sorted_usernames =  sorted_usernames[:math.floor(len(sorted_usernames) / 2)]
# print(f"Array Length: {len(sorted_usernames)}")
# higher_lower("moonLighter22")
# print(sorted_usernames)

def binary_search(input_list, value):

    counter = 0
    start = 0
    end = len(input_list) - 1 # because array start at 0

    while start <= end:
        middle_index = start + (end - start) // 2
        if value > input_list[middle_index]:
            # print("higher, get rid of left side")
            start = middle_index + 1 # plus 1 to exclude middle element
        elif value < input_list[middle_index]:
            # print("lower, get rid of right side")
            end = middle_index - 1 # minus 1 to excluded middle element
        else:
            # print(f"found it at {middle_index} counter: {counter}")
            return middle_index
        counter += 1
    return -1




print(binary_search(sorted_usernames, "alphaWolf23"))


