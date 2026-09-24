def main():

import random

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

print("~" * 40)
print()
print("   Hoş geldinizzz!")

print()
print("~" * 40)

ROUNDS = 5
round_num = 1
score = 0
used = []

while round_num <= ROUNDS:
  
  word, hint = random.choice(word_bank)

  while (word, hint) in used:
    word, hint = random.choice(word_bank)

  used.append((word, hint))

  letters = list(word)
  random.shuffle(letters)
  scrambled_word = "".join(letters).upper()

  print()
  print(f"Round {round_num}")
  print()
  print(f"Scrambled: {scrambled_word}")
  print()

  guess = input("Guess the word (or type 'hint' / 'skip' / 'quit'): ").strip().lower()

  if guess == "hint":
    print()
    print(f"Hint: {hint}")
    print()
    guess = input("Your guess (or 'skip' / 'quit'): ").strip().lower()

  if guess == "quit":
    print("Thanks for playing!")
    break
  elif guess == "skip":
    print(f"Skipped! The word was '{word}'.")
  elif guess == word:
    score += 1
    print("✅  Correct!")
  else:
    print(f"❌ Sorry, the word was '{word}'.")

  round_num += 1

print()
print(f"Final score: {score}/{ROUNDS}")
print

if score == 5:
  print("Flawless! All tests passing, zero bugs.")
elif score == 4: 
  print("Near perfect, only one failing test!")
elif score == 3:
  print("Good effort! The code runs, and that's what counts.")
else: 
  print("Have you tried turning it off and on again?")

if __name__ == "__main__":
    main()
