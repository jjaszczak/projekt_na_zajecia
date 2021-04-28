



print("Oto one shot, krótka opowieść. Decyzje podejmuj rozważnie, a odpowiedzi formułuj dokładnie tak jak zadane są pytania. W razie problemów, spójrz w kod. Powodzenia!")

print("Z dalekiej krainy mrozu i śniegu długą drogę przebył do Programlandii młody poszukiwacz przygód. Jesteś nim ty. Programlandia jednak podzielona jest na wiele mniejszych landów, z których rozpatrujesz odwiedzić Pythron lub Cessię. Wybór należy do Ciebie. Pythron czy Cessia?")
wybrany_land = input()
if wybrany_land == "Cessia":
    print("Droga do Cessii nie była długa. Kilka dni pieszo, i mogłeś przekroczyć bramy pięknej, choć niebezpiecznej krainy. Czeka Cię tu wiele ryzykownych, choć opłacalnych przygód.")
elif wybrany_land == "Pythron":
    print("Droga do Pythronu okazała się o wiele dłuższa, niż z początku Ci się zdawało. Aby do niego dotrzeć nie przedłużając znacznie wyprawy, musisz zdecydować, czy zamierzasz udać się tam: przez Puszczę Elif czy przez Równinę Ifa?")
    obrana_droga = input()
    if obrana_droga == "przez Równinę Ifa":
        print("Droga przez równinę okazała się być dla Ciebie, podróżniku, zgubna. Niestety, nie wiedząc o tym, wkroczyłeś na teren Zgrai Możliwości, niebezpiecznej szajki przemytniczej, która również zajmuje się handlem żywym towarem. Ich przewaga liczebna spowodowałą, że nie byłeś w stanie się obronić, i zostałeś sprzedany jako niewolnik.")
    elif obrana_droga == "przez Puszczę Elif":
        print("Wchodząc między drzewa usłyszałeś szelest strzał, nacierających na ciebie od strony równiny. Całe szczęście, udało Ci się na czas zatopić w zaroślach i przeczekać noc. Następnego ranka ruszyłęj w dalszą drogę. Po kilku godzinach, usłyszałeś szelest w krzakach nieopodal. Co robisz? Wspinasz się na drzewo, zastygasz bez ruchu czy rzucasz się na ziemię?")
        wybór_gracza = input()
        if wybór_gracza == "zastygam bez ruchu":
            print("Zza krzaków wypadło na Ciebie stado dzikich świń, ogromnych, uzbrojonych w potężne kły dzików. Niestety, staranowały się, raniąc śmiertelnie zatrutymi kłami. W ciągu kilku dni zmarłeś, wijąc się w cierpieniach.")
        elif obrana_droga == "rzucam się na ziemię":
            print("Zza krzaków wypadło na Ciebie stado dzikich świń, ogromnych, uzbrojonych w potężne kły dzików. Niestety, staranowały się, raniąc śmiertelnie zatrutymi kłami. W ciągu kilku dni zmarłeś, wijąc się w cierpieniach.")
        else:
            print("Całe szczeście. Z gałęzi drzewa obserwowałeś szarżujące dziekie świnie, uzbrojone w zatrute kły. Gdybyś postąpił inaczej, mógłbyś zostać śmiertelnie raniony. Teraz jednak zszedłeś bezpiecznie i ruszyłeś dalej. Po następnych kilku godzinach natrafiłeś na niewielką drewnianą chatkę. Wyglądała naprawdę niepozornie, stojąc pośród tych gigantycznych drzew. Z kominka unosił się dym. Na co się decydujesz? Wchodzisz do środka? Chowasz się w zaroślach i obserwujesz chatkę z ukrycia? Czy może idziesz dalej?")
            decyzja_gracza = input()
            if decyzja_gracza == "chowam się w zaroślach i obserwuję chatkę z ukrycia":
                print("Obserwowałeś chatkę cały wieczór, ale ostatecznie zasnąłeś, a po obudzeniu dalej nic się nie działo. Zdecywałeś się pójść dalej. Bezpiecznie dotarłeś do Pythronu.")
            elif decyzja_gracza == "idę dalej":
                print("Dalsza droga przebiegła spokojnie i bezpiecznie dotarłeś do Pythronu")
            elif decyzja_gracza == "wchodzę do środka":
                print("Delikatnie uchyliłeś drzwi, a Twoim oczom ukazało się coś niesamowitego. Ta niepozorna chatka, okazała się magicznym domem elfów leśnych. Jej wnętrze okazało się ogromne w porównaniu z wyglądem z zewnątrz. Piękny salon, kilkanaście klatek schodowych rzeźbionych w drewnie, antrasole, balkony, podwieszane pod sufitem niby-klatki sypialne. Wszystko wyglądało niesamowicie. Same elfy przywitały Cię bardzo ciepło, kojarząc Cię z opowiadań swoich Górskich braci, z którymi miałeś okazję niegdyś współpracować i pomagać im. Zaproponowały Ci zostanie z nimi na jakiś czas lub wyprawienie Cię w dalszą drogę. Zostajesz czy wyruszasz?")
                choice = input()
                if choice == "zostaję":
                    print("Życie z elfami leśnymi okazało się pełne ciekawych przygód i bardzo miłe. Mieszkanie w magicznej chatce na pewno wspominać będziesz do końca swych dni.")
                else:
                    print("Elfy przygotowały Cię do dalszej drogi i przenocowały. Udało Ci się bezpiecznie dotrzeć do Pythronu, mogłeś rozpocząć tu nowe życie.")
import sys,time,os
def wystukaj(string):
    for char in string:
        if char != "\n" :
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.03)
        else:
            print()
            time.sleep(0.01)
