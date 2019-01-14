import json


def read_reviews_from_file(file_name, app_name):
    with open(file_name) as json_file:
        data = json.load(json_file)
        # for p in data[app_name]:
        #     print('Name: ' + p['name'])
        #     print('Website: ' + p['website'])
        #     print('From: ' + p['from'])
        #     print('')
    return data[app_name]


def set_reviews():
    rev1 = "i enjoy the game but there are way too many ads. I'd rather pay a dollar than have to watch ads. " \
           "I'm uninstalling the game because of too many ads. Facebook floods us with ads. Google floods us with ads. " \
           "Verizon sold our numbers and now we get solicitations. my email app floods me with ads. Most apps flood " \
           "us with ads. I'M TIRED TO ADS!!!"

    rev2 = "it's a fun game but it has more ads than ive ever seen before and I've played a lot of games with ads. also it randomly keeps tryong to open my browser to something despite not clicking anything. sketchy. too bad its pretty fun and would be challenging for younger teens"
    rev3 = "Good time killer but those ADS! Play a level, get an ad. Play two levels, get an ad. Play another level, get another ad. Spend as much time hunting for a way to fill the glass as you do hunting (or waiting) for the faint gray \"X\"s to close the multilayered ads!"
    rev4 = "Its dumb that the ads are saying false information about the game to make the player think \"Oh, that looks so easy! I can totally beat that!\" And make them download the app. Why say false information when you can state true information? Too much ads that have false information.. Orverall, the game is pretty easy."
    rev5 = "This is a great wee game.. while away my time ... addictive can't stop playing. Really makes you think. hate it when i get stuck on a level I do try to not use the hints if I can help it.. definitely recommend."
    rev6 = "I block all ads on my phone so I don't have quite the bad experience that others have reported, but the game crashes every other level since the last update. It\'s unplayable. Such a shame, because it\'s a clever concept in the older vein of a where\'s my water."
    rev7 = "Not at all challenging. I tore through the first 50 levels and I'm BORED! it's cute enough so I'm giving it 2 stars. Cut back on the ads a bit and it would be 3. Make the puzzles more interesting and it might reach 4. It will never be a 5 star game. I should actually give it 1 star just because of the way it forces ad watching. Several times I earned a full 3 stars for a level but the game would only give me 2 stars on the level unless I watched an ad. Slime ball move!"
    rev8 = "ridiculous amount of ads. crashes repeatively. not very good at all. would recommend not wasting your time. iimpossible to see where you're drawing and there is no limit to what you can draw removing any challenge. graphics are cheap are flash game quality."
    rev9 = "DO NOT PAY FOR NO ADS- It's a con, and big flashing ad buttons remain, as does a nag about turning off ad tracking setting. I feel cheated."
    rev10 = "Clever game overwhelmed by flaws. 1) way too many ads. Loud, in-your-face ads every minute or so. And two back to back each time. 2) the ads stop my Spotify and don't restart it. I understand the need to pay the bills, but Happy Glass is obscene. 3) using fingers to draw precise lines doesn't work. Can't even see the lines I'm drawing on my phone until it is too late. Requires a pen. I considered buying the game to get rid of the ads but the last issue decided me against it."
    rev11 = "WAY to many ads. fun game but I waste way to much time waiting for an ad top finish. I don't watch them so they are pointless to me. after every single level is just ridiculous"
    rev12 = "ads arent as bad as most other games. but drawing is hard without your finger running into obstacles"
    rev13 = "Addictive as hell this game is very addictive that it cured my ebola............. highly recomended BTW this game doesn't need any update cuz it's perfect. So,Developers good job on this game. literally the best puzzle game ever"
    rev14 = "Too meny ads. And you can see hoe much is without ads, says only to give a payment method. I don't want to give my credit card number without knowing how much is kosts"
    rev15 = "Super fun game! One downfall...WAAAAAAAAYYY TOO MANY ADS. Maybe have them pop up every 5 rounds instead of each single round."
    rev16 = "Very addictive, very well made, perfect gameplay, clever puzzles. Don't miss it. Some crashes after level 70 (or after the last update) are not enough to loose a star."
    rev17 = "2 ads every 2 rounds seems excessive. watching the same ads 5 times in a row = not worth. greedy developerels"
    rev18 = "I not sure this called game with ads supported or ads with added game. I view more ads than playing the game. 2 stars because I have fun in Challenges mode without any ads. Unfortunately I will uninstall the game."
    rev19 = "Each try builds upon what you learned from previous experiences. Each level is a new challenge and makes me want to see what the NEXT puzzle has to offer. I wish there were fewer ads though."
    rev20 = "It is a great game and, it is also very unique which is good. I'm very good at Happy Glass, but it can be a little bit frustrating if you can't do the level and their is no hint. So overall it is a great game!"
    rev21 = "great game addictive. however paid for no ads £2.89 and still being bombarded with ads after every level just to collect all 3 stars that i earned from the level. please rectify."
    rev22 = "addicted ,challenging, and past timer good for a long trip and for waiting on a restaurant like today red lobster 1/6/2019 4:00 PM on dallas texas united states"
    rev23 = "An average looking game with some interesting mechanics that end up never being fully realized because all of the puzzles are designed to be too simple."
    rev24 = "just a bunch of crappy ads everywhere. you're better of not installing this in the first place. just too much of ads."
    rev25 = "Was on level 131 & again after the update i losted everything again this is the 3rd time it has happened after update PLEASE FIX IT AS my son loved playing this but he gets no prizes it says no internet..."
    rev26 = "really fun game. i cant enjoy a game if an ad pops up every 2 - 3 levels."
    rev27 = "The ads that pop up every tine you complete a level almost push me to deleting this game."
    rev28 = "great game. the only thing i dont like is that you cannot see the tip of the pencil under your finger. other than that i love it."
    rev29 = "nice game not to challenging but every so often you hit one level where you need to think outside the box so keeps you on your toes"
    rev30 = "Nice exercise for the brain. Addictive but also very satisfying. Let's see when the novelty wears off but for now I am certainly hooked."

    reviews = [rev1, rev2, rev3, rev4, rev5, rev6, rev7, rev8, rev9, rev10, rev11, rev12, rev13, rev14, rev15, rev16,
               rev17, rev18, rev19, rev20,
               rev21, rev22, rev23, rev24, rev25, rev26, rev27, rev28, rev29, rev30]
    return reviews


def set_reviews2():
    r1 = "Love the game. I have one quick question though,can I hack? I have root access and can easily hack the game,I'm not talking about medallions or anything,because I've met numerous hackers like the report I sent to you stated,and I would like to know If it would be okay to hack,but only if my opponent is a hacker,like if they place a super monkey on round 1 and upgrade it to temple of the sun God and such,If I ever get reports,you can ban me,If I don't,there's no harm done right? As they say,you have to beat fire with fire! Or in this case,beat hackers by hacking!"
    r2 = "A brilliant game that i keep on every device. Been playing for years now, and kept in the same clan for donks. Been having an issue and gets stuck on \"downloading vital data\", but a fresh install cleans that up. Just gotta link it to your G-account, to use the cloud saves. All the ninja kiwi games are fab to play. Even BTD6."
    r3 = "I loved your games when I was younger, even online battles. However, this game used to fun before you guys updated the game, now the game is absolute trash. Btd battles is like Clash Royale #2, just another complete pay-to-win game with power-ups. You don't need skill in order to win, just some \"good\" power-ups will give you a fast winning streak. I was hoping that you guys were better than Supercell, BUT I WAS WRONG. BTD Battles in my opinion is now officially a pay-to-win game."
    r4 = "Played against alot of higher level players, got destroied mostly. Usually went to upper 20s in waves, untill opponants decide to start sending MOABs and stuff. The daily wheel thing is super helpful. Also ranking rewards are extra good, and unlike most apps, the energy thing is ok."
    r5 = "It's a good game which is fun to play but every now and again the screen seems to be different on their side and my side. like the bloons will look like they are going through but the monkeys won't be attacking. might just be a glitch with my devices but if it's not please fix it."
    r6 = "NJNJAKIWI, YOU MUST BE SOOOOO DUMB. YOU ARE STILL ALLOWING THE ROUND 13 RAINBOW RUSH. ITS JUST A GAME ENDER, CUZ IT IS SO HARD TO DEFEND AGAINST! EVRYONE IS USING IT! ALSO, THE BLOONS WONT MAKE THE OPPONENT LOSE LIVES SOMETIMES, AND ITS SO ANNOYING BECAUSE THEY THEN TRY TO GET REVENGE!"
    r7 = "A very Fun strategy game. I usually play with my brother and it's still a good experience! The Ranking Rewards are boss because I always rank and play enough battles. Having an insane card battles deck is so much fun!! GG on a good game!!"
    r8 = "This game is rigged. I went into BFB Colosseum and went up against someone who had 20k matches played and has gotten Black Diamond in prestige and in the world multiple times, while I'm in a small clan. What happens next is when the maps are being chosen, ZEN GARDEN appears so I skip and then INDOOR POOLS! What?! I was so mad! He had tier four powers and I lost. Could you make the matching system better? Like whoever has close to the same amount of those green darts at the top of the screen? Thx!"
    r9 = "The actual game is great, it's being against other players that makes it awful. Everyone plays with the same dumb tactic, and it's like you can't even fight against it unless you do it before them. In the card mode, as soon as you reach round 19 they send the big red zeplin for Just $3000 and theres no way to have enough money to get anything to properly defend (unless you're on a map with water, then you can use the monkey pirate which is still $6000). In the normal game, they use basic mo"
    r10 = "The actual game is great, it's being against other players that makes it awful. Everyone plays with the same dumb tactic, and it's like you can't even fight against it unless you do it before them. In the card mode, as soon as you reach round 19 they send the big red zeplin for Just $3000 and theres no way to have enough money to get anything to properly defend (unless you're on a map with water, then you can use the monkey pirate which is still $6000). In the normal game, they use basic mo"
    r11 = "I'd give it a higher rating but for one thing: Why does it keep showing \"Downloading vital data\"? I've heard it's due to some kind of antivirus or private vpn preventing me from accessing the server, but I don't know how to resolve that on mobile. Quite annoying. If you guys somehow resolve the problem or let me know how to solve it, I'll give a 5 star because this is the best game ever :\")"
    r12 = "this game is flawless action packed and honestly I dont think this game needs any more updates it's already awesome . there is nothing that needs to be changed. this app is amazing I would defend it all day and Simon yes the cobra can be frustrating but it is possible if you are smart and have a really good defense it doesn't matter what the other player has. any way ninja kiwi keep up the great work and the technique I use is wiz, super monk, and banana farm. huge fan of yours share this plz"
    r13 = "an awesome game, if you can get past the pay to win and annoying ads. I dont know if this is a device issue, but I have to restart the game every time an ad shows up, since I cant close the ad. there is major pay to win, also. energy is an example. I love this game, but wish that ninjakiwi would not be so greedy."
    r14 = "Its an great game! Tough I don't like The way that Players can get rushed. Can you make a diffrent way to get Eco? Also I want ro get BTD6 but I Can't. Can you make it free or not? Please ninja kiwi?"
    r15 = "A very fun game to play when at home. The only real problem is disconnecting results in a loss a there are many toxic players to deal with."
    r16 = "You ruined the game so bad with powers and its so unfair. I'm literally gonna report anyone with four tier powers that plays in the lower arenas ."
    r17 = "this game has turned to trash all it is now is that people rush you at round 13 and most people who play cant defend the 20-30 regen zebras that are sent and if you can it doesnt matter because they will just send a few moabs or constantly rush you with zebras or rainbows till you die every game is around 5-10 minutes because of this and this game has now become very boring and toxic"
    r18 = "Suggestion. Check for root on game start up. If device is root don't let them play. Or add safeguards that check for impossible values like sudden 250 to 9999 income, or 500 gold to 999999, or impossible medallion amounts. There are too many cheaters please fix. I am playing probably 80% people that cheat. Update. Still tons of cheaters, guess the developer doesn't care. Update 2. There still seems to be a lot of cheaters but only with crazy amounts of medallions so it doesn't affect game play, so not a big deal. 1 star because customer support is extremely slow. Only one email per day, apparently closed weekends. Even if I reply back almost immediately I still have to wait till the next day. Been waiting over 5 days now just to fix one problem. Annoying...."
    r19 = "Used to be a good game, before they decided to add \"power upgrades\". Whats the point of me playing against people who have all of their powers upgraded to 3rd level and i have lvl 1? gives me a huge disadvantage. And to get that much exp you need to play about 150 games. The game is like some hard core MMORPG from 90s now."
    r20 = "Great game overall but had enough of losing due to connectivity problems and i know 100% its not from my side.. something needs to be done about this as i have no fair advantage at all. I can not compete for the prestige rankings for starters considering half my losses are due to apparent connection issues."
    r21 = "This game used to be amazing , now the game is just terrible. The new powers make the game Pay to win! You could have a very clearly advantage during the game but because the opposition has payed money to get 4th tier powers , such as moab boost , you dont stand a chance against a single moab even when using multiple 4th tier bloon jistsu ninjas... You need to make some huge balance changes or simply remove the new powers all together. I'll tell you now for a fact , 1000s of people agree with me"
    r22 = "I really enjoyed the game, but lately it has lagged a lot. It's harder for me to find matches. It will not load the leaderboard data so I cannot receive the rewards from that either."
    r23 = "Havent played the game for a while now, i was a club member! I go back on today to see the same username, however ive to start again!! No club member access now either! I paid for that and want it back! 😡 I have already emailed them yesterday and still haven't heard anything back yet!!"
    r24 = "Updating my review after the recent update. Just when I thought you couldn't f*** this game up further you prove me wrong. you've managed to sap the last bit of fun out with changes. Finally time to uninstall methinks."
    r25 = "This game is good. I haven't got any annoying ads. Not sure why people are complaining... Maybe this changed while i haven't played this game in 5 months XD."
    r26 = "It's a good strategy game. A problem is the match making system. They match you with over experienced players where they have huge power advantages against you."
    r27 = "man every time i play this game i out smart every person they put me aginst lolz this game is fun and easy step up your game btd ( ͡° ͜ʖ ͡°)"
    r28 = "the game itself is really fun, however there is one major drawback. It is full of empty heads who do nothing but spam you with balloons which means a game can be over in about 60 secs. What's the point ? it takes no skill or strategy to play this way and is just lazy play by people who obviously can't think. developers should look at implementing another arena of battle like the assault one but disable sending option so the people who actually want to PLAY the game can"
    r29 = "Nice Game very good graphics and controls and the gameplay is phenomenal BUT the only problem is that sometimes i look at the other persons side and they're taking damage but i dont see any balloons going in there its a glitch but besides that its a great game nice job!"
    r30 = "i love this game hard at the begging but once you get higher its more fun and easyer i play with my friend and brother all the time but recently the app has been weird on me and says \"donloading valid data\" and i have to delete it and re-install it but still love it"

    reviews = [r1, r2, r3, r4, r5, r6, r7, r8, r9, r10, r11, r12, r13, r14, r15, r16, r17, r18, r19, r20, r21, r22, r23,
               r24, r25, r26, r27, r28, r29, r30]

    return reviews
