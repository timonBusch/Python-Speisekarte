import xml.etree.ElementTree as ET
from lxml import etree
from io import StringIO



def showSpeisekarte():
    printV = root.iter("vorspeisePosition")
    printH = root.iter("hauptspeisePosition")
    printN = root.iter("nachspeisePosition")
    printG = root.iter("getraenkPosition")

    i = 0
    for child in printV:
        i += 1
        print("\n")
        print("Position." + str(i))
        for element in child:
            print(element.tag + ": ", element.text)
    if (i == 0):
        print("Keine Vorspeisen vorhanden")

    i = 0
    for child in printH:
        i += 1
        print("\n")
        print("Position." + str(i))
        for element in child:
            print(element.tag + ": ", element.text)
    if (i == 0):
        print("Keine Hauptspeisen vorhanden")

    i = 0
    for child in printN:
        i += 1
        print("\n")
        print("Position." + str(i))
        for element in child:
            print(element.tag + ": ", element.text)
    if (i == 0):
        print("Keine Nachspeisen vorhanden")

    i = 0
    for child in printG:
        i += 1
        print("\n")
        print("Position." + str(i))
        for element in child:
            print(element.tag + ": ", element.text)
    if (i == 0):
        print("Keine Getränke vorhanden")


def validate(xmlDatei,xsdDatei):
    xml = xmlDatei
    xds = xsdDatei

    with open(xds, "r") as schema_file:
        schema_to_check = schema_file.read()

    with open(xml, "r") as xml_file:
        xml_to_check = xml_file.read()

    xmlschema_doc = etree.parse(StringIO(schema_to_check))
    xmlschema = etree.XMLSchema(xmlschema_doc)

    try:
        doc = etree.parse(StringIO(xml_to_check))
        print("XML well formed, syntax ok.")
    except IOError:
        print("Invalid File")
    except etree.XMLSyntaxError as err:
        print("XML Syntax Error, see error_syntax.log")
        with open("error_syntax.log", "w") as error_log_file:
            error_log_file.write(str(err.error_log))
        quit()

    except:
        print("Unknown error, exiting.")
        quit()

    try:
        xmlschema.assertValid(doc)
        print('XML valid, schema validation ok.')

    except etree.DocumentInvalid as err:
        print('Schema validation error, see error_schema.log')
        with open('error_schema.log', 'w') as error_log_file:
            error_log_file.write(str(err.error_log))
        quit()

    except:
        print('Unknown error, exiting!.')
        quit()


def addGericht():
    condition = True
    while condition == True:
        # Überprüfung auf Korrekter eingabe
        try:
            eingabe = input("\nv = Vorspeise hinzufügen\n" +
                            "h = Hauptspeise hinzufügen\n" +
                            "n = Nachspeise hinzufügen\n" +
                            "g = Getränk hinzufügen\n" +
                            "e = Zurück ins Hauptmenü\n" +
                            "Eingabe: ")
        except:
            print("Unzulässige Eingabe")

        findGerichte = root.find("gerichte")

        if eingabe == "v":
            findVorspeisen = findGerichte.find("vorspeisen")
            i = len(findVorspeisen.findall("vorspeisePosition"))

            vorspeise = input("Bitte geben Sie eine Vorspeise ein:")
            try:
                preisVorspeise = int(input("Bitte geben Sie den Preis der Vorspeise ein"))
                new_vorspeisePos = ET.SubElement(findVorspeisen, "vorspeisePosition", attrib={"nummer": str(i + 1)})
                new_vorspeise = ET.SubElement(new_vorspeisePos, "vorspeise")
                new_vorspeise.text = vorspeise
                new_preis = ET.SubElement(new_vorspeisePos, "preis")
                new_preis.text = str(preisVorspeise)
            except:
                print("Bitte geben Sie eine Zahl ein")
                addGericht()

        if eingabe == "h":
            findHauptspeisen = findGerichte.find("hauptspeisen")
            i = len(findHauptspeisen.findall("hauptspeisePosition"))

            hauptspeise = input("Bitte geben Sie eine Hauptspeise ein:")
            try:
                preisHauptspeise = int(input("Bitte geben Sie den Preis der Hauptspeise ein"))
                new_hauptspeisePos = ET.SubElement(findHauptspeisen, "hauptspeisePosition",
                                                   attrib={"nummer": str(i + 1)})
                new_hauptspeise = ET.SubElement(new_hauptspeisePos, "hauptspeise")
                new_hauptspeise.text = hauptspeise
                new_preis = ET.SubElement(new_hauptspeisePos, "preis")
                new_preis.text = str(preisHauptspeise)
            except:
                print("Bitte geben Sie eine Zahl ein")
                addGericht()

        if eingabe == "n":
            findNachspeisen = findGerichte.find("nachspeisen")
            i = len(findNachspeisen.findall("nachspeisePosition"))

            nachspeise = input("Bitte geben Sie eine Nachspeise ein:")
            try:
                preisNachspeise = int(input("Bitte geben Sie den Preis der Nachspeise ein"))
                new_nachspeisePos = ET.SubElement(findNachspeisen, "nachspeisePosition", attrib={"nummer": str(i + 1)})
                new_nachspeise = ET.SubElement(new_nachspeisePos, "nachspeise")
                new_nachspeise.text = nachspeise
                new_preis = ET.SubElement(new_nachspeisePos, "preis")
                new_preis.text = str(preisNachspeise)
            except:
                print("Bitte geben Sie eine Zahl ein")
                addGericht()

        if eingabe == "g":
            findGetraenk = findGerichte.find("getraenke")
            i = len(findGetraenk.findall("getraenkPosition"))

            getraenk = input("Bitte geben Sie ein Getränk ein:")
            try:
                preisGetraenk = int(input("Bitte geben Sie den Preis des Getränks ein"))
                new_getraenkPos = ET.SubElement(findGetraenk, "getraenkPosition", attrib={"nummer": str(i + 1)})
                new_getraenk = ET.SubElement(new_getraenkPos, "getraenk")
                new_getraenk.text = getraenk
                new_preis = ET.SubElement(new_getraenkPos, "preis")
                new_preis.text = str(preisGetraenk)
            except:
                print("Bitte geben Sie eine Zahl ein")
                addGericht()

        if eingabe == "e":
            condition = False


def save():
    tree = ET.ElementTree(root)
    tree.write(xmlFile)
    return False


def openXML():
    try:
        tree = ET.parse(xmlFile)
        root = tree.getroot()
        validate(xmlFile, xsdFile)
        return root
    except:
        root = ET.Element("speisekarte")
        gerichte = ET.SubElement(root, "gerichte")
        vorspeisen = ET.SubElement(gerichte, "vorspeisen")
        hauptspeisen = ET.SubElement(gerichte, "hauptspeisen")
        nachspeisen = ET.SubElement(gerichte, "nachspeisen")
        getraenke = ET.SubElement(gerichte, "getraenke")
        tree = ET.ElementTree(root)
        root = tree.getroot()
        tree.write(xmlFile)
        print(xmlFile + " wurde nicht gefunden es wurde eine neue angelegt")
        validate(xmlFile, xsdFile)
        return root


def delGericht():
    condition = True
    while condition == True:
        # Überprüfung auf Korrekter eingabe
        try:
            eingabeDel = input("\nv = Vorspeise entfernen\n" +
                               "h = Hauptspeise entfernen\n" +
                               "n = Nachspeise entfernen\n" +
                               "g = Getränk entfernen\n" +
                               "e = Zurück ins Hauptmenü\n" +
                               "Eingabe: ")
        except:
            print("Unzulässige Eingabe")

        gerichte = root.find("gerichte")
        vorspeisen = gerichte.find("vorspeisen")
        nachspeisen = gerichte.find("nachspeisen")
        hauptspeisen = gerichte.find("hauptspeisen")
        getraenke = gerichte.find("getraenke")

        if gerichte == None:
            print("Keine Vorspeisen vorhanden")
        else:
            if (eingabeDel == "v"):
                if vorspeisen == None:
                    print("Keine Vorspeisen vorhanden")
                else:
                    delete = input("Welche Vorspeise soll gelöscht werden")
                    for vorspeise in vorspeisen.findall("vorspeisePosition"):
                        nummer = vorspeise.get("nummer")
                        if (delete == nummer):
                            vorspeisen.remove(vorspeise)

            if (eingabeDel == "h"):
                if vorspeisen == None:
                    print("Keine Hauptspeisen vorhanden")
                else:
                    delete = input("Welche Hauptspeisen soll gelöscht werden")
                    for hauptspeise in hauptspeisen.findall("hauptspeisePosition"):
                        nummer = hauptspeise.get("nummer")
                        if (delete == nummer):
                            vorspeisen.remove(hauptspeise)

            if (eingabeDel == "n"):
                if vorspeisen == None:
                    print("Keine Nachspeise vorhanden")
                else:
                    delete = input("Welche Nachspeise soll gelöscht werden")
                    for nachspeise in nachspeisen.findall("nachspeisePosition"):
                        nummer = nachspeise.get("nummer")
                        if (delete == nummer):
                            nachspeisen.remove(nachspeise)

            if (eingabeDel == "g"):
                if vorspeisen == None:
                    print("Kein Getränk vorhanden")
                else:
                    delete = input("Welches Getränk soll gelöscht werden")
                    for getraenk in getraenke.findall("getraenkPosition"):
                        nummer = getraenk.get("nummer")
                        if (delete == nummer):
                            getraenke.remove(getraenk)

        if (eingabeDel == "e"):
            condition = False


condition = True
xmlFile = 'Ratskeller_zur_alten_Post.xml'
xsdFile = 'Speisekarte_Schema.xsd'
root = openXML()


while condition == True:
    eingabe = ""

    # Überprüfung auf Korrekter eingabe
    try:
        eingabe = input("\na = Speisekarte anzeigen\n" +
                        "n = neues Gericht hinzufügen\n" +
                        "l = Gericht löschen\n" +
                        "e = Speichern und Programmende\n" +
                        "Eingabe: ")
    except:
        print("Unzulässige Eingabe")

    # Liste wird zeilenweise ausgegeben
    if eingabe == "a":
        showSpeisekarte()

    # Neues Gericht wird zur Liste hinzugefügt
    elif eingabe == "n":
        addGericht()

    # Gericht löschen
    elif eingabe == "l":
        delGericht()

    # Liste wird in Datei gespeichert
    elif eingabe == "e":
        condition = save()


