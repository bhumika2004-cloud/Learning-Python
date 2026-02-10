# smiley face: 😊
EMOJI={
    ':)':'😊'
}
def replace_smiley(text):
    sentence=text.replace(":)", EMOJI[":)"])
    return sentence

