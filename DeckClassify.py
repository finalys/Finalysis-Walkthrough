## Function to determine deck archetype. Takes in Deck_URL after replacing cardhash with card names.
def DeckSearch(d, mode = 1):
    x = "" ## Target string container to replace sequentially
    y = [] ## Checking purposes to detect classifications
    
    ## Neutral Identifiers
    def IsMjerrabaine(d):
        return (d.count('Mjerrabaine, Great One') >= 3)
    
    ## Forestcraft
    def IsForest(d):
        return (d.count('.1.') >= 1)
    def IsHozumiForest(d):
        return (sum(d.count(x) for x in ["Hozumi, Enchanting Hostess", "Garuel, Seraphic Leo", "Freyja", "Ambitious Goblin Mage", "Tam Lin, Fey Knight"]) >= 7)
    def IsCondemnedForest(d):
        return (sum(d.count(x) for x in ["Magachiyo, Barbed Convict", "Verdant Lieutenant"]) >= 4)
    def IsFairyForest(d):
        return (sum(d.count(x) for x in ["Nobilis, Sable-Lily Queen", "Plumeria, Serene Goddess", "Shining Valkyrie"]) >= 6)
    
    if IsForest(d):
        x = "OTHER FOREST"
        y.append(x)
        if IsHozumiForest(d):
            x = "Hozumi Forest"
            y.append(x)
        if IsCondemnedForest(d):
            x = "Condemned Forest"
            y.append(x)
        if IsFairyForest(d):
            x = 'Fairy Forest'
            y.append(x)
        if IsMjerrabaine(d):
            x = "Jerry Forest"
            y.append(x)
    
    ## Swordcraft
    def IsSword(d):
        return (d.count('.2.') >= 1)
    def IsLootSword(d):
        return (sum(d.count(x) for x in ["Tidal Gunner", "Barbaros, Briny Convict", "Deep-Sea Scout", "Storm-Wracked First Mate", "Octrice, Hollow Usurpation"]) >= 10)
    def IsHeroicSword(d):
        return (sum(d.count(x) for x in ["Mach Knight", "Heroic Entry", "Valiant Fencer", "Windslasher", "Flame Soldier"]) >= 8)
    def IsCommanderSword(d):
        return (sum(d.count(x) for x in ["Royal Fortress", "General Maximus", "Radiant Luminous Mage"]) >= 7)

    
    if IsSword(d):
        x = "OTHER SWORD"
        y.append(x)
        if IsLootSword(d):
            x = "Loot Sword"
            y.append(x)
        if IsHeroicSword(d):
            x = "Heroic Sword"
            y.append(x)
        if IsCommanderSword(d):
            x = "Commander Sword"
            y.append(x)

    
    ## Runecraft
    def IsRune(d):
        return (d.count('.3.') >= 1)
    def IsSevenForcesRune(d):
        return (sum(d.count(x) for x in ["Sorcerer of Seven Forces"]) >= 2)
    def IsSpellboostRune(d):
        return ((sum(d.count(x) for x in ("Chakram Wizard", "Mari, Card Conjurer", "Meltina, Miracle Sorceress", "Simael, Cleansing Enforcer")) >= 8))
    def IsChessRune(d):
        return ((sum(d.count(x) for x in ["Magical Knight", "Magical Rook", "Magical Strategy", "Milady, Mystic Queen", "Mystic King", "Check"]) >= 8))
    def IsTestSubjectRune(d):
        return ((sum(d.count(x) for x in ["Volunteer Test Subject", "Devoted Researcher", "Sephie, Depraved Convict", "Obsessive Scholar"]) >= 8)) & ((sum(d.count(x) for x in ["Mystic King", "Check"]) < 3)) & ((sum(d.count(x) for x in ["Chakram Wizard", "Mari, Card Conjurer", "Meltina, Miracle Sorceress"]) < 3))
        
    
    if IsRune(d):
        x = "OTHER RUNE"
        y.append(x)
        if IsSevenForcesRune(d):
            x = "SevenForces Rune"
            y.append(x)
        if IsSpellboostRune(d):
            x = "Spellboost Rune"
            y.append(x)
        if IsChessRune(d):
            x = "Chess Rune"
            y.append(x)
        if IsTestSubjectRune(d):
            x = "TestSubject Rune"
            y.append(x)

    ## Dragoncraft
    def IsDragon(d):
        return (d.count('.4.') >= 1)
    def IsDiscardDragon(d):
        return ((sum(d.count(x) for x in ["Augite Wyrm", "Argente, Purest Silver", "Dragonewt's Might", "Lumiore, Prestigious Gold", "Noir & Blanc, Brothers"]) >= 10))
    def IsArmedDragon(d):
        return ((sum(d.count(x) for x in ["Draconic Armor", "Draconir, Knuckle Dragon", "Hammer Dragonewt", "Lævateinn Dragon"]) >= 8))
    def IsBahamutDragon(d):
        return ((sum(d.count(x) for x in ["Drazael, Ravening Enforcer", "Ultimate Bahamut", "Si Long, Draconic God-Queen"]) >= 5))  & ((sum(d.count(x) for x in ["Lævateinn Dragon", "Draconir, Knuckle Dragon"]) < 3))  & ((sum(d.count(x) for x in ["Argente, Purest Silver", "Lumiore, Prestigious Gold"]) < 3))

    if IsDragon(d):
        x = "OTHER DRAGON"
        y.append(x)
        if IsDiscardDragon(d):
            x = "Discard Dragon"
            y.append(x)
        if IsArmedDragon(d):
            x = "Armed Dragon"
            y.append(x)
        if IsDiscardDragon(d) & IsArmedDragon(d):
            x = "DisArm Dragon"
            y.append(x)
        if IsBahamutDragon(d):
            x = "Bahamut Dragon"
            y.append(x)
        if IsMjerrabaine(d):
            x = "Jerry Dragon"
            y.append(x)
    
    ## Shadowcraft
    def IsShadow(d):
        return (d.count('.5.') >= 1)
    def IsLWShadow(d):
        return (sum(d.count(x) for x in ["Istyndet, Soul Convict", "Abyssal Colonel", "Cerberus, Infernal Hound", "Huginn & Muninn"]) >= 8)
    def IsGhostShadow(d):
        return ((sum(d.count(x) for x in ["Ghastly Banishment", "Masquerade Ghost", "Baccherus, Peppy Ghostie"]) >= 5) & (sum(d.count(x) for x in ["Abyssal Colonel", "Cerberus, Infernal Hound", "Istyndet, Soul Convict"]) < 4))
    
    
    if IsShadow(d):
        x = "OTHER SHADOW"
        y.append(x)
        if IsLWShadow(d):
            x = "LW Shadow"
            y.append(x)
        if IsGhostShadow(d):
            x = "Ghost Shadow"
            y.append(x)
        if IsMjerrabaine(d):
            x = "Jerry Shadow"
            y.append(x)
    
    ## Bloodcraft
    def IsBlood(d):
        return (d.count('.6.') >= 1)
    def IsWrathBlood(d):
        return ((sum(d.count(x) for x in ["Garodeth, Insurgent Convict", "Howling Scream", "Raging Commander", "Scorching Grandiosity", "Howling Demon"]) >= 8) & (sum(d.count(x) for x in ["Paracelise, Demon of Greed"]) < 2))
    def IsHandlessBlood(d):
        return (sum(d.count(x) for x in ["Paracelise, Demon of Greed", "Room Service Demon"]) >= 4)
    def IsEvoBlood(d):
        return ((sum(d.count(x) for x in ["Alice, Wandering Dreamer", "Dancing Mini Soul Devil", "Tevali, Demonic Cat", "Kali", "Signa, Sealed Madwolf"]) >= 10) & (sum(d.count(x) for x in ["Paracelise, Demon of Greed"]) < 2))
    
    if IsBlood(d):
        x = "OTHER BLOOD"
        y.append(x)
        if IsWrathBlood(d):
            x = "Wrath Blood"
            y.append(x)
        if IsHandlessBlood(d):
            x = "Handless Blood"
            y.append(x)
        if IsEvoBlood(d):
            x = "Evo Blood"
            y.append(x)
        if IsMjerrabaine(d):
            x = "Jerry Blood"
            y.append(x)

    ## Havencraft
    def IsHaven(d):
        return (d.count('.7.') >= 1)
    def IsCrystaliseHaven(d):
        return (sum(d.count(x) for x in ("Wingy, Chirpy Gemstone", "Diamond Master", "Holy Lightning Bird", "Skullfane, the Defiled", "Emerald Maiden")) >= 8)
    # def IsControlHaven(d):
    #     return ((sum(d.count(x) for x in ("Sacred Ice-Crusher", "Perpetual Despair", "Bellerophon")) >= 5  & (sum(d.count(x) for x in ("Wingy, Chirpy Gemstone", "Diamond Master", "Holy Lightning Bird", "Skullfane, the Defiled", "Emerald Maiden")) <= 1)))

    if IsHaven(d):
        x = "OTHER HAVEN"
        y.append(x)
        if IsCrystaliseHaven(d):
            x = "Crystalise Haven"
            y.append(x)
        # if IsControlHaven(d):
        #     x = "Control Haven"
        #     y.append(x)
        if IsMjerrabaine(d):
            x = "Jerry Haven"
            y.append(x)
    
    ## Portalcraft
    def IsPortal(d):
        return (d.count('.8.') >= 1)
    def IsPuppetPortal(d):
        return ((sum(d.count(x) for x in ["Young Threadmaster", "Craftsman's Pride", "Orchis, the Limitless", "Blossoming Flower Doll"]) >= 8) & (sum(d.count(x) for x in ["Cutthroat, Discord Convict"]) < 2))
    def IsControlPortal(d):
        return ((sum(d.count(x) for x in ["Arc", "Shion, Immortal Aegis", "Summon Divine Treasure"]) >= 5) & (sum(d.count(x) for x in ["Orchis, the Limitless"]) < 2 & (sum(d.count(x) for x in ["Cutthroat, Discord Convict"]) < 2)))
    def IsEnhancePortal(d):
        return (sum(d.count(x) for x in ["Cutthroat, Discord Convict", "Smeltwork Bodyguard", "Ironforged Right Hand", "Judith, Cosmic Observer"]) >= 7)
    
    if IsPortal(d):
        x = "OTHER PORTAL"
        y.append(x)
        if IsPuppetPortal(d):
            x = "Puppet Portal"
            y.append(x)
        if IsControlPortal(d):
            x = "Control Portal"
            y.append(x)
        if IsEnhancePortal(d):
            x = "Enhance Portal"
            y.append(x)
        if IsMjerrabaine(d):
            x = "Jerry Portal"
            y.append(x)

    if mode == 1:
        return x
    if mode != 1:
        return y