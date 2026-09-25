from fastapi import FastAPI
from pydantic import BaseModel
import random

app = FastAPI()

word_bank = [
    ("kahve", "sabahları ayılmak için içilen şey"),
    ("simit", "sabah kahvaltısında ya da yolda yenen, üzeri susamlı halka şeklindeki hamur işi"),
    ("şemsiye", "yağmurda ıslanmamak için başımızın üstünde tuttuğumuz şey"),
    ("otobüs", "durakta bekleriz, içine binip şehirde bir yerden bir yere gideriz"),
    ("anahtar", "kapıyı açmak için lazım olur, çoğu zaman en son aradığımız yerde çıkar"),
    ("gözlük", "iyi göremeyenlerin burnuna taktığı şey"),
    ("saat", "duvarda ya da bileğimizde durur, geç kaldığımızı bize hatırlatır"),
    ("ayna", "sabah kalkınca ilk baktığımız yer, saçımızın halini gösterir"),
    ("çay", "Türkiye'de günün her saati içilen, ince belli bardakta servis edilen sıcak içecek"),
    ("telefon", "hepimizin elinden düşürmediği, bildirimlerle sürekli bizi çağıran şey"),
]

# Endpoint 1: Yeni round başlat, karışık kelime döndür
@app.get("/round")
def yeni_round():
    word, hint = random.choice(word_bank)
    letters = list(word)
    random.shuffle(letters)
    scrambled = "".join(letters).upper()
    return {"scrambled": scrambled, "hint": hint, "answer": word}


# Endpoint 2: Tahmini kontrol et
class GuessInput(BaseModel):
    guess: str
    answer: str

@app.post("/guess")
def tahmin_kontrol(data: GuessInput):
    correct = data.guess.strip().lower() == data.answer.strip().lower()
    return {"correct": correct, "answer": data.answer}