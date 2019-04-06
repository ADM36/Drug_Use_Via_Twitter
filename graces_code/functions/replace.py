import numpy as np
import pandas as pd
import csv
import re

def replace_utf(df):
    emoji_dict = {'…': '...', '•': '', '”': '"', '—': '-', '™': '', '“': '":', '😵': '<dizzy>', '’': "'", '✨': '<sparkles>',
    '😳': '<flushed>', '☺': '<smile>', '💊': '<pill>', '😴': '<sleeping>', '😕': '<confused>', '😐': '<neutral>',
    '😒': '<unamused>', '🍌': '<banana>', '👍': '<thumbsup>', '–': '-', '🙌': '<raisinghands>','❤': '<heart>',
    '😣': '<perservering>', '😑': '<expressionless>', '✌': '<victoryhand>', '😩': '<weary>', '😎': '<sunglasses>',
    '😂': '<laughing>', '✅': '<checkmark>', '👌': '<okhand>', '🍸': '<cocktail>','😰': '<coldsweat>', '❏': '',
    '💉': '<syringe>', '💆': '<massage>', '👽': '<alien>', '💤': '<sleeping>', '\u200f': '', '😫': '<tired>',
    '🎶': '<musicnotes>', '😋': '<delicious>', '😁': '<grinning>', '💋': '<kiss>', '✋': '<raisedhand>',
    '👋': '<wavinghand>', '💯': '<100>', '😈': '<smilingdevil>', '―': '-', '😔': '<pensive>', '😡': '<pouting>',
    '🙅': '<no>', '😘': '<kissyface>', '🌀': '<cyclone>', '👺': '<goblin>', '😦': '<frowning>', '😟': '<worried>', '‘': "'",
    '😖': '<confounded>', '😥': '<disappointed>', '↑': '<uparrow>', '🙊': '<speaknoevil>', '🙈': '<seenoevil>',
    '🌠': '<shootingstar>', '⚡': '<voltage>', '💨': '<dash>', '😃': '<smiling>', '😬': '<grimace>', '◆': '<diamond>',
    '🔫': '<pistol>', '😪': '<sleepy>', '💰': '<moneybag>', '😭': '<crying>', '😍': '<hearteyes>', '👿': '<frowningdevil>',
    '😆': '<smiling>', '✔': '<checkmark>', '👎': '<thumbsdown>', '📝': '<memo>', '😤': '<triumph>', '☀': '*',
    '😉': '<winking>', '😱': '<fear>', '♥': '<heart>', '🌝': '<fullmoon>', '💩': '<poop>', '👯': '<friendship>',
    '👏': '<clap>', '☝': '<pointup>', '😮': '<openmouth>', '😲': '<astonished>', '😞': '<disappointed>', '😏': '<smirking>',
    '🙋': '<raisinghand>', '🍕': '<pizza>', '🍔': '<hamburger>', '🍟': '<fries>', '🍗': '<chicken>', '🍝': '<spaghetti>',
    '🍤': '<shrimp>', '€': '<euro>', '🌚': '<newmoon>', '💔': '<brokenheart>', '😢': '<crying>', '😷': '<facemask>',
    '👉': '<pointright>', '😺': '<smile>', '😛': '<tongue>', '😌': '<relieved>', '⊙': '*', '‿': '_', '✿': '*',
    '😙': '<kissyface>', '😗': '<kissyface>', '😊': '<smile>', '↓': '<downarrow>', '😅': '<sweat>', '💁': '<sassy>',
    '👲': '<chinesecap>', '💘': '<heartarrow>', '😜': '<wink>', '💖': '<heart>', '✗': '<x>', '②': '<2>', '⬆': '<uparrow>',
    '♫': '<music>', '♡': '<heart>', '🐘': '<elephant>', '🐗': '<boar>', '🐒': '<monkey>', '👸': '<queen>', '🔥': '<fire>',
    '🌿': '<herb>', '👐': '<openhands>', '💪': '<muscle>', '😠': '<angry>', '🐧': '<penguin>', '➔': '<rightarrow>',
    '🙇': '<bowing>', '🎧': '<headphones>', '😨': '<fearful>', '😝': '<tongue>', '💃': '<dancing>', '‼': '!!',
    '😓': '<coldsweat>', '😹': '<laughing>', '💀': '<skull>', '🔬': '<microscope>', '💭': '<thought>', '➡': '<rightarrow>',
    '🙍': '<frown>', '👵': '<old>', '😧': '<anguished>', '⭐': '<star>', '👀': '<eyes>', '≥': ' greater than ', '≤': ' less than ',
    '💸': '<money>', '🌸': '<flower>', '💥': '<collision>', '😶': '<nomouth>', '⃣': '', '😄': '<smile>', '💫': '<dizzy>',
    '🔪': '<knife>', '\u2006': '', '👮': '<police>', '🙆': '<ok>', '🏀': '<basketball>', '👭': '<friendship>',
    '🙀': '<weary>', '🙏': '<pray>', '⛽': '<fuel>', '🏼': '', '🎄': '<tree>', '👠': '<shoe>', '🍁': '<leaf>',
    '😯': '<hushed>', '🌄': '<sunrise>', '💗': '<heart>', '🔙': '<back>', '🔚': '<end>', '🔜': '<soon>', '🎁': '<present>',
    '🎅': '<santa>', '⛄': '<snowman>', '🏃': '<run>', '🎥': '<camera>', '🐶': '<dog>', '💓': '<heart>', '🌼': '<flower>',
    '😀': '<smile>', '💍': '<ring>', '💕': '<heart>', '😚': '<kissyface>', '🎉': '<party>', '🎇': '<firework>',
    '🎆': '<firework>', '🎈': '<balloon>', '☹': '<frown>', '💜': '<heart>', '🐸': '<frog>', '☕': '<tea>', '‑': '-',
    '🔌': '<plug>', '🐈': '<cat>', '📷': '<camera>', '👴': '<old>', '👧': '<young>', '👬': '<friendship>', '🍓': '<strawberry>',
    '👹': '<ogre>', '💚': '<heart>', '⭕': '<circle>', '👊': '<fist<', '👇': '<pointdown>', '🍭': '<lolipop>',
    '😾': '<pouting>', '≠': ' does not equal ', '😇': '<innocent>', '🙉': '<hearnoevil>', '🍜': '<ramen>', '🐥': '<chick>',
    '❗': '!', '🌙': '<moon>', '⁰': '^0', '✖': 'x', '⬇': '<downarrow>', '🏂': '<surf>', '⚓': '<anchor>', '👼': '<angel>',
    '♪': '<music>', '🍻': '<beer>', '🐰': '<bunny>', '💙': '<heart>', '❌': 'x', '🚘': '<car>', '🚂':'<train>',
    '🚬': '<cigarette>','🚫': '<noentry>', '🚮': '<litter>'}


    tweet_text = df['tweet_text'].to_list()

    cleaned = []
    for tweet in tweet_text:
        cleaned.append(re.sub(u'[\U0001f300-\U0001f700]|[\u2000-\u3000]', lambda m: ' ' + emoji_dict.get(m.group()) + ' ',tweet))

    df['tweet_text'] = cleaned

    return df
