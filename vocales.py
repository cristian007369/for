frase=input("Digite una frase: ") 
As,a="aáäAÁÄ",0
Es,e="eéëEÉË",0
Is,i="iíïIÍÏ",0
Os,o="oóöOÓÖ",0
Us,u="uúüUÚÜ",0
for w in frase:
    if w in As:
        a+=1
    elif w in Es:
        e+=1
    elif w in Is:
        i+=1
    elif w in Os:
        o+=1
    elif w in Us:
        u+=1
print(f"En la frase hay {a} vocales a")
print(f"En la frase hay {e} vocales e")
print(f"En la frase hay {i} vocales i")
print(f"En la frase hay {o} vocales o")
print(f"En la frase hay {u} vocales u")