## Function to determine deck archetype. Takes in Deck_URL after replacing cardhash with card names.
def DeckSearch(d):
    x = "" ## Target string container to replace sequentially
    
    ## Neutral Identifiers
    def IsMjerrabaine(d):
        return (d.count('Mjerrabaine, Great One') >= 3)
    
    ## Forestcraft
    def IsForest(d):
        return (d.count('.1.') >= 1)
    def IsHozumiForest(d):
        return (sum(d.count(x) for x in ["Hozumi, Enchanting Hostess", "Garuel, Seraphic Leo", "Freyja", "Ambitious Goblin Mage", "Tam Lin, Fey Knight"]) >= 7)
    def IsCondemnedForest(d):
        return (sum(d.count(x) for x in ["Magachiyo, Barbed Convict"]) >= 3)
    
    if IsForest(d):
        x = "OTHER FOREST"
        if IsHozumiForest(d):
            x = "Hozumi Forest"
        if IsCondemnedForest(d):
            x = "Condemned Forest"
        if IsMjerrabaine(d):
            x = "Jerry Forest"
    
    ## Swordcraft
    def IsSword(d):
        return (d.count('.2.') >= 1)
    def IsLootSword(d):
        return (sum(d.count(x) for x in ["Tidal Gunner", "Barbaros, Briny Convict", "Deep-Sea Scout", "Storm-Wracked First Mate", "Octrice, Hollow Usurpation"]) >= 10)
    def IsHeroicSword(d):
        return (sum(d.count(x) for x in ["Mach Knight", "Heroic Entry", "Valiant Fencer", "Windslasher", "Flame Soldier"]) >= 8)

    
    if IsSword(d):
        x = "OTHER SWORD"
        if IsLootSword(d):
            x = "Loot Sword"
        if IsHeroicSword(d):
            x = "Heroic Sword"

    
    ## Runecraft
    def IsRune(d):
        return (d.count('.3.') >= 1)
    def IsSpellboostRune(d):
        return ((sum(d.count(x) for x in ("Chakram Wizard", "Mari, Card Conjurer", "Meltina, Miracle Sorceress", "Simael, Cleansing Enforcer")) >= 8))
    def IsChessRune(d):
        return ((sum(d.count(x) for x in ["Magical Knight", "Magical Rook", "Magical Strategy", "Milady, Mystic Queen", "Mystic King", "Check"]) >= 8))
    def IsTestSubjectRune(d):
        return ((sum(d.count(x) for x in ["Volunteer Test Subject", "Devoted Researcher", "Sephie, Depraved Convict", "Obsessive Scholar"]) >= 8)) & ((sum(d.count(x) for x in ["Mystic King", "Check"]) < 3)) & ((sum(d.count(x) for x in ["Chakram Wizard", "Mari, Card Conjurer", "Meltina, Miracle Sorceress"]) < 3))
        
    
    if IsRune(d):
        x = "OTHER RUNE"
        if IsSpellboostRune(d):
            x = "Spellboost Rune"
        if IsChessRune(d):
            x = "Chess Rune"
        if IsTestSubjectRune(d):
            x = "TestSubject Rune"

    ## Dragoncraft
    def IsDragon(d):
        return (d.count('.4.') >= 1)
    def IsDiscardDragon(d):
        return ((sum(d.count(x) for x in ["Augite Wyrm", "Argente, Purest Silver", "Dragonewt's Might", "Lumiore, Prestigious Gold", "Noir & Blanc, Brothers"]) >= 10))
    def IsArmedDragon(d):
        return ((sum(d.count(x) for x in ["Draconic Armor", "Draconir, Knuckle Dragon", "Hammer Dragonewt", "Lævateinn Dragon"]) >= 8))
    def IsControlDragon(d):
        return ((sum(d.count(x) for x in ["Drazael, Ravening Enforcer", "Ultimate Bahamut", "Si Long, Draconic God-Queen"]) >= 5)) & ((sum(d.count(x) for x in ["Lævateinn Dragon", "Draconir, Knuckle Dragon"]) < 3)) & ((sum(d.count(x) for x in ["Argente, Purest Silver", "Lumiore, Prestigious Gold"]) < 3))

    if IsDragon(d):
        x = "OTHER DRAGON"
        if IsDiscardDragon(d):
            x = "Discard Dragon"
        if IsArmedDragon(d):
            x = "Armed Dragon"
        if IsControlDragon(d):
            x = "Control Dragon"
        if IsMjerrabaine(d):
            x = "Jerry Dragon"
    
    ## Shadowcraft
    def IsShadow(d):
        return (d.count('.5.') >= 1)
    def IsLWShadow(d):
        return (sum(d.count(x) for x in ["Istyndet, Soul Convict", "Abyssal Colonel", "Chaotic Doom", "Thunder God of the Tempest", "Huginn & Muninn"]) >= 8)
    def IsGhostShadow(d):
        return (sum(d.count(x) for x in ["Ghastly Banishment", "Masquerade Ghost", "Baccherus, Peppy Ghostie"]) >= 5) & (sum(d.count(x) for x in ["Abyssal Colonel", "Chaotic Doom", "Thunder God of the Tempest"]) < 3)
    
    
    if IsShadow(d):
        x = "OTHER SHADOW"
        if IsLWShadow(d):
            x = "LW Shadow"
        if IsGhostShadow(d):
            x = "Ghost Shadow"
        if IsMjerrabaine(d):
            x = "Jerry Shadow"
    
    ## Bloodcraft
    def IsBlood(d):
        return (d.count('.6.') >= 1)
    def IsWrathBlood(d):
        return (sum(d.count(x) for x in ["Garodeth, Insurgent Convict", "Howling Scream", "Raging Commander", "Demonic Drummer", "Demon Maestro"]) >= 8)
    def IsHandlessBlood(d):
        return (sum(d.count(x) for x in ("Paracelise, Demon of Greed", "Room Service Demon", "Bat Usher", "Silvernail Blaster")) >= 10)
    
    if IsBlood(d):
        x = "OTHER BLOOD"
        if IsWrathBlood(d):
            x = "Wrath Blood"
        if IsHandlessBlood(d):
            x = "Handless Blood"
        if IsMjerrabaine(d):
            x = "Jerry Blood"

    ## Havencraft
    def IsHaven(d):
        return (d.count('.7.') >= 1)
    def IsCrystaliseHaven(d):
        return (sum(d.count(x) for x in ("Wingy, Chirpy Gemstone", "Diamond Master", "Holy Lightning Bird", "Skullfane, the Defiled", "Emerald Maiden")) >= 8)
    def IsControlHaven(d):
        return (sum(d.count(x) for x in ("Sacred Ice-Crusher", "Perpetual Despair", "Bellerophon")) >= 5 & (sum(d.count(x) for x in ("Wingy, Chirpy Gemstone", "Diamond Master", "Holy Lightning Bird", "Skullfane, the Defiled", "Emerald Maiden")) <= 1))

    if IsHaven(d):
        x = "OTHER HAVEN"
        if IsCrystaliseHaven(d):
            x = "Crystalise Haven"
        if IsControlHaven(d):
            x = "Control Haven"
        if IsMjerrabaine(d):
            x = "Jerry Haven"
    
    ## Portalcraft
    def IsPortal(d):
        return (d.count('.8.') >= 1)
    def IsPuppetPortal(d):
        return (sum(d.count(x) for x in ["Young Threadmaster", "Craftsman's Pride", "Orchis, the Limitless", "Blossoming Flower Doll"]) >= 8)
    def IsControlPortal(d):
        return (sum(d.count(x) for x in ["Arc", "Shion, Immortal Aegis", "Summon Divine Treasure"]) >= 5) & (sum(d.count(x) for x in ["Orchis, the Limitless"]) < 2)
    def IsEnhancePortal(d):
        return (sum(d.count(x) for x in ["Kyrzael, Killshot Enforcer", "Cutthroat, Discord Convict", "Ironforged Right Hand"]) >= 5)
    
    if IsPortal(d):
        x = "OTHER PORTAL"
        if IsPuppetPortal(d):
            x = "Puppet Portal"
        if IsControlPortal(d):
            x = "Control Portal"
        if IsMjerrabaine(d):
            x = "Jerry Portal"

    return x