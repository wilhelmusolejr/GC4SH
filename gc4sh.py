from itertools import tee
import random
import asyncio
import asyncio
import os
import datetime
from re import T
from playwright.async_api import async_playwright

# implement when have free time
# creates notepad with corresponding information
# application = "lazada"
# DATABASE PATH
# path = "C:/Users/Administrator/Desktop/Automation/Accounts/Database"
# isExist = os.path.exists(path + "/"+ phone + "/"+application+".txt")
# print(isExist)

phone = "9972976807";

fNames = ["Harry","Angel","Bruce","Cook","Carolyn","Andrea","Albert","Joshua","Randy","Althea","Larry","Barnes","Nathalie","Wilson","Jesse","Samantha","Ernest","Princess","Sophia","Javier","Henry","Simmons","Michelle","David","Manalo","Shaina","Aguilar"];
mNames = ["Brooks","Rachel","Edwards","Christopher","Perez","Thomas","Baker","Sara","Moore","Chris","Bailey","Roger","Johnson","Marilyn","Thompson","Anthony","Evans","Julie","Hall","Paula","Phillips","Annie","Hernandez","Dorothy","Murphy","Alice","Howard"];
lNames = ["Flores","Bautista","Villanueva","Reyes","Gerald","Fernandez","Raymond","Carter","Jacqueline","Castro","Garcia","Nelson","Santos","Cruz","Castillo","Clark","Lopez","Alexander","Tolentino","Valdez","Eric","Long","Amanda","Diaz","Soriano","Diaz","Wanda","Santiago"];
cities = ["Abra", "Basilan", "Bohol", "Cebu", "Manila", "Leyte", "Masbate", "Tarlac"]
zips = ["2800", "7300", "6300", "6000", "1000", "6500", "5400", "2300"]


def getCurrentDateandTime():
    x = datetime.datetime.now()
    month = x.strftime("%B")
    day = x.strftime("%d")
    year = x.strftime("%Y")
    hourDate = x.strftime("%I")
    minuteDate = x.strftime("%M")
    secondDate = x.strftime("%S")
    ampm = x.strftime("%p")

    return [month, day, year, hourDate, minuteDate, secondDate, ampm]

class PersonInfo:
    def __init__(self, fNames, mNames, lNames, zips, cities, phone, dateTime):
        addressPicker = random.randint(0, len(cities)-1)
        self.fName = fNames[random.randint(0, len(fNames)-1)]
        self.mName = mNames[random.randint(0, len(mNames)-1)]
        self.lName = lNames[random.randint(0, len(lNames)-1)]
        self.username = self.fName + "." + self.lName + str(random.randint(10,99))
        self.email = self.username + "@gmail.com"
        self.password = str(len(self.lName)) + str(len(self.lName)) + self.fName[0:int(len(self.fName)/2)] + "!" + self.lName[0:int(len(self.fName)/2)] + str(len(self.lName))
        # MONTH- DAY - YEAR
        self.dobNum = ["199" + str(random.randint(0,9)), "0" + str(random.randint(1,9)), "0" + str(random.randint(1,9))]
        self.driverLicence = "D09-18-10" + str(random.randint(1000, 9999))
        self.zip = zips[addressPicker]
        self.city = cities[addressPicker]
        self.street = str(random.randint(10, 99)) + " compound " + self.city +" " + self.zip
        self.phone = phone
        self.currentDate = dateTime


async def main(person):
  async with async_playwright() as p:

    browser = await p.chromium.launch(headless=False)
    page = await browser.new_page()
        
    # TARGET SITE
    await page.goto("https://m.gcash.com/gcashapp/gcash-promotion-web/2.0.0/index.html#/")

    # ------------ PAGE -----------------
    # Number input
    # print("to wait for first page")
    await page.wait_for_selector(".mobile-input")
    # print("to fill text")
    await page.fill(".mobile-input", phone)
    # print("to press button")
    await page.click(".ap-button")

    # ------------ PAGE -----------------
    # OTP
    # print("to wait for otp page")
    # await page.wait_for_selector(".otp-message")
    # print("to put otp")
    otp = input("OTP: ")
    for i in otp:
        await page.fill("#app > div > div > div > div:nth-child(2) > div.page-item.otp-password-field > div > div > input", i)        
    print("to press submit")
    await page.click(".ap-button")

    # ------------ PAGE -----------------
    print("to wait for input data page")
    await page.wait_for_selector(".tittle-header")

    # INSERTS PERSONAL INFO
    # print("to put first name")
    await page.fill("//*[@id='app']/div/div/div/div/div/input[1]", person.fName)
    # print("to put middle name")
    await page.fill("//*[@id='app']/div/div/div/div/div/input[2]", person.mName)
    # print("to put last name")
    await page.fill("//*[@id='app']/div/div/div/div/div/input[3]", person.lName)

    await page.fill("//*[@id='app']/div/div/div/div/div/div[3]/input", person.dobNum[0]+person.dobNum[1]+person.dobNum[2]);

    # print("to put address")
    await page.fill("//*[@id='app']/div/div/div/div/div/input[4]", person.street)
    # print("to put email")
    await page.fill("//*[@id='app']/div/div/div/div/div/input[5]", person.email)

    # print("to press submit")
    await page.click(".ap-button")

    # ------------ PAGE -----------------
    # print("to wait for confimation page")
    await page.wait_for_selector(".tittle-header")

    # print("to press submit")
    await page.click(".ap-button")

     # ------------ PAGE -----------------
    # print("to wait for pin page")
    await page.wait_for_selector(".tittle-header")

    # print("to put pin code ")
    await page.fill("//*[@id='app']/div/div/div/div/div/input[1]", '1010');
    await page.fill("//*[@id='app']/div/div/div/div/div/input[2]", '1010');

    # print("to press submit")
    await page.click(".ap-button")

     # ------------ PAGE -----------------
    # print("to wait for final page")
    await page.wait_for_selector("//*[@id='app']/div/div/div/img")
    await page.wait_for_selector(".tittle-header")
    result = await page.inner_text(".tittle-header")

    print(result)
    print("-----------------------")
    print("-----------------------")
    print("Full name: " + person.fName + " " + person.lName)
    print("Phone: " + phone)
    print("Address: " + person.street)
    print("Email: " + person.email)
    print("Pin: 1010")
    print("-----------------------")
    print("-----------------------")
    await browser.close()


dateTime = getCurrentDateandTime();
person = PersonInfo(fNames, mNames, lNames,cities, zips, phone, dateTime)
asyncio.run(main(person))

# PIN 56217969921339
# PIN 59333879943930
# PIN 39140770146971

# 300 - 6pcs
# PIN 45642468427248
# PIN 18947583635555
# PIN 71071545961111
# PIN 35458786951497
# PIN 33067616605817
# PIN 09405740449834

# 50
# PIN 44707855699203
# PIN 83120699040785
# PIN 79763738547398
# PIN 33526026177295
# PIN 57225685818998
# PIN 30933052480483

# 100
# PIN 02210869456912
# PIN 78023882843141
# PIN 84527374857066
# PIN 68674812817736
# PIN 87408014302804

# 150
# PIN 25244798194978
# PIN 15820445463741
# PIN 81210577580952
# PIN 39352015261342

# 300 - 5pcs
# PIN 38404911493475
# PIN 28417754817068
# PIN 32420135339956
# PIN 56501698477891
# PIN 82266720014206




# 50 - 34pcs 
# PIN 42682761886827
# PIN 48620697446628
# PIN 58033109097327
# PIN 72627912845289
# PIN 10032636919475
# PIN 99775521498419
# PIN 47809170830522
# PIN 37267741541652
# PIN 20752499549784
# PIN 10340324893660
# PIN 17577039614115
# PIN 99370260815144
# PIN 72674931042212
# PIN 92809564430470
# PIN 69096882588046
# PIN 43514676856219
# PIN 84325153419394
# PIN 40329188064852
# PIN 75009574051896
# PIN 50139655905515
# PIN 16463982524687
# PIN 28068493164676
# PIN 33018376186480
# PIN 64324697886120
# PIN 47543644154498
# PIN 96214185452411
# PIN 16975159152628
# PIN 24948855690899
# PIN 34361253050996
# PIN 80333945592006
# PIN 00041046153928
# PIN 16928098097798
# PIN 68827824858242
# PIN 41736574217752

# 100 - 21pcs
# PIN 78455801126055
# PIN 89287338473756
# PIN 95363831818988
# PIN 23125176420269
# PIN 77774052512057
# PIN 71060422692732
# PIN 73480805457321
# PIN 44293269156259
# PIN 66451162447354
# PIN 10905921872437
# PIN 71060422692732
# PIN 26107358166796
# PIN 63758475854852
# PIN 57880559051426
# PIN 78262313706296
# PIN 54711700445047
# PIN 29554524947654
# PIN 65593696554045
# PIN 40348624531838
# PIN 09053738042742
# PIN 88152547651712

# 150 - 21pcs
# PIN 16357239390623
# PIN 20581028440327
# PIN 73933818725826
# PIN 82538938698787
# PIN 73045980400139
# PIN 91509362219553
# PIN 55089080525616
# PIN 07417264447390
# PIN 84329489031846
# PIN 45640839296343
# PIN 22467014184792
# PIN 52477780007182
# PIN 36134676360226
# PIN 68738677503668
# PIN 51191427678025
# PIN 80555228530489
# PIN 94080778988669
# PIN 12790108852116
# PIN 83774983306500
# PIN 31899317735533
# PIN 93607697385254


# 300 - 20pcs
# PIN 58064634825043
# PIN 86564236317501
# PIN 78588853117534
# PIN 74398422975192
# PIN 96768443641550
# PIN 93056110974299
# PIN 18881540224053
# PIN 36872307240004
# PIN 32881310110088
# PIN 89377306572657
# PIN 53789109439053
# PIN 61964252870082
# PIN 62490475169158
# PIN 35781347665387
# PIN 04198741578243
# PIN 17905540174981
# PIN 97778824508491
# PIN 42130050733483
# PIN 38097030912224
# PIN 81539407571309

