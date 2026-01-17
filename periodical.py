# ============================================
#   Project Author : AX10M-PH4R4D0X
#   License        : GPLv3
# ============================================


def periodicaltable():
    world__elements = {


        "Alkali Metals": {
            "Lithium": "(Li)",
            "Sodium": "(Na)",
            "Potasium": "(K)",
            "Rubidium":"(RB)",
            "Cesium":"(Cz)",
            "Francium":"(Fr)",

        },


        "Alkaline Earth Metals":{
            "Beryllium":"(Be)",
            "Magnesium":"(Mg)",
            "Calcium":"(Ca)",
            "Strontium":"(Sr)", 
            "Barium":"(Ba)", 
            "Radium":"(Ra)",
         
        },


        "Transition Metals":{
            "Scandium":"(Sc)",
            "Titanium":"(Ti)",
            "Vanadium":"(V)",
            "Chromium":"(Kr)",
            "Manganese":"(Mn)",
            "Iron": "(Fe)",
            "Cobalt":"(Co)",
            "Nickel":"(Ni)",
            "Copper":"(Cu)",
            "Zinc":"(Zn)",
            "Silver": "(Ag)",
            "Gold": "(Au)",
            "Platinum": "(Pt)",
            "Mercury": "(Hg)",
        },


        "İnner Transition Metals":{
             "Lanthanum":"(La)",
             "Cerium":"(Ce)",
             "Neodymium":"(Nd)",
             "Actinium":"(Ac)",
             "Uranium":"(U)",
             "Plutonium":"(Pu)",

        },


        "Post-Transition Metals":{
            "Aluminum":"(Al)",
            "Gallium":"(Ga)", 
            "Indium":"(In)", 
            "Thallium":"(Tl)", 
            "Tin":"(Sn)", 
            "Lead" :"(Pb)", 
            "Bismuth": "(Bi)",
            "Polonium":"(Po)",

        },


        "Metalloids":{
            "Boron":"(B)", 
            "Silicon":"(Si)", 
            "Arsenic":"(As)", 
            "Antimony":"(Sb)", 
            "Tellurium":"(Te)",
            
            },
            

        "Non-Metals": {
            "Hydrogen": "(H)",
            "Carbon": "(C)",
            "Nitrogen": "(N)",
            "Oxygen": "(O)",
            "Phoshorus": "(P)",
            "Sulfur": "(S)",
            "Selenium": "(Se)",
        },


        "Halogens":{
            "Flourine":"(F)",
            "Chlorine":"(Cl)",
            "Bromine":"(Br)",
            "Iodine":"(I)",
            "Astatine":"(At)",
            "Tennessine":"(Ts)",

        },


        "Noble gases": {
            "Helium": "(He)",
            "Neon": "(Ne)",
            "Argon": "(Ar)",
            "Krypton": "(Kr)",
            "Xenon": "(Xe)",
            "Radon": "(Rn)",
            "Oganesson": "(Og)",
        },
    }


    return world__elements


def searchit():
    import time


    world__elements = periodicaltable()
    search =str(input("Enter element name: ")).lower().capitalize() 
    time.sleep(1)
    print("Please wait, scanning the periodic table...")
    time.sleep(3)




    found = False
    for category , elements in world__elements.items():
        if search in elements:
            print(f"{search} The (IUPAC) symbol of the element is: {elements[search]}")
            found = True
            break

    if not found:
        print("--No such element found, please try again--")



searchit()
