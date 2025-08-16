# Asenna tarvittaessa gTTS: pip install gTTS
from gtts import gTTS

# Viikko 1 käsikirjoitus (voit laittaa tähän koko vihkon tekstin)
teksti = """
Kuuntele ja toista perässä.

Päivä yksi.
Opettele viisi verbiä: rakastaa, vihata, odottaa, auttaa, opiskella.
Tee viisi lausetta näillä verbeillä.
Lue yksi uutinen Selkosuomesta.

Päivä kaksi.
Opettele viisi verbiä: ihailla, pelätä, etsiä, käyttää, seurata.
Kirjoita päiväkirjaan kolme lausetta.
Kuuntele kymmenen minuuttia Selkouutisia.

...
(jatka tähän kaikki Päivä 3–7 + verbit, harjoitukset ja vastaukset)
"""

# Luo ääni suomeksi
tts = gTTS(text=teksti, lang='fi')

# Tallenna mp3-tiedostoksi
tts.save("Suomi_Aanitreenit_Viikko1.mp3")

print("MP3-tiedosto tallennettu: Suomi_Aanitreenit_Viikko1.mp3")
