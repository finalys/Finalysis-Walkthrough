## Function to determine deck archetype. Takes in Deck_URL after replacing cardhash with card names.
def DeckSearch(d, mode = 1):
    x = "" ## Target string container to replace sequentially
    x_output = "" ## Output string container
    y = [] ## Checking purposes to detect classifications
    
    ## Neutral Identifiers (if any)
    
    ## Forestcraft
    def IsForest(d):
        return (d.count('.1.') >= 1)
    def IsFairyForest(d):
        return (sum(d.count(x) for x in ["Nobilis, Sable-Lily Queen", "Plumeria, Serene Goddess", "Shining Valkyrie", "Filly, Mythmaster"]) >= 6  & ((sum(d.count(x) for x in ["Aqua Fairy", "Flying Mistletoe Squirrel", "Guidance of the Wise", "Fauna Handler", "Fairy Funfact"]) >= 10)) )
    
    if IsForest(d):
        x = "OTHER FOREST"
        if IsFairyForest(d):
            x = 'Fairy Forest'
            y.append(x)
    
    ## Swordcraft
    def IsSword(d):
        return (d.count('.2.') >= 1)
    def IsMarsSword(d):
        return (sum(d.count(x) for x in ["Mars, Belligerent Flame"]) >= 3)
    def IsLootSword(d):
        return (sum(d.count(x) for x in ["Tidal Gunner", "Barbaros, Briny Convict", "Deep-Sea Scout", "Storm-Wracked First Mate"]) >= 8)
    def IsAcademicSword(d):
        return (sum(d.count(x) for x in ["Weiss, Discerning Professor", 'Galdr, Heroic Headmaster', 'Lecia & Nano, Twilight Trainees', 'Lucius, Travelled Trainer']) >= 7)
    def IsHeroicSword(d):
        return (sum(d.count(x) for x in ["Flame Soldier", "Amerro, Spear Knight", "Mach Knight", "Ironwrought Defender", "Windslasher"]) >= 10)
    def IsCommanderSword(d):
        return (sum(d.count(x) for x in ["Royal Fortress", "General Maximus", "Warden of Honor", "Radiant Luminous Mage"]) >= 9)

    if IsSword(d):
        x = "OTHER SWORD"
        if IsMarsSword(d):
            x = "Mars Sword"
            y.append(x)
        if IsLootSword(d):
            x = "Loot Sword"
            y.append(x)
        if IsAcademicSword(d):
            x = "Academic Sword"
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
    def IsMysteriaRune(d):
        return ((sum(d.count(x) for x in ["Grea, Crimson Promise", "Anne, Brilliant Mage", "Mysteria, Magic Originator", "Craig, Mysterian Chanter", "Anne & Grea, Royal Duo", "Hanna, Mysterian Maid", "Mysterian Exchange Party", "Arcane Instruction"]) >= 15))
    def IsSpellboostRune(d):
        return ((sum(d.count(x) for x in ["Chakram Wizard", "Crushing Rain", "It's Raining Blades!", "Simael, Cleansing Enforcer"]) >= 8))
    def IsChessRune(d):
        return ((sum(d.count(x) for x in ["Magical Knight", "Magical Rook", "Magical Strategy", "Milady, Mystic Queen", "Mystic King", "Check"]) >= 8))
    def IsTestSubjectRune(d):
        return ((sum(d.count(x) for x in ["Volunteer Test Subject", "Devoted Researcher", "Sephie, Depraved Convict", "Obsessive Scholar"]) >= 8)) & ((sum(d.count(x) for x in ["Mystic King", "Check"]) < 3)) & ((sum(d.count(x) for x in ["Chakram Wizard", "Mari, Card Conjurer", "Meltina, Miracle Sorceress"]) < 3))
    
    if IsRune(d):
        x = "OTHER RUNE"
        if IsSevenForcesRune(d):
            x = "SevenForces Rune"
            y.append(x)
        if IsMysteriaRune(d):
            x = "Mysteria Rune"
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
    def IsBuffDragon(d):
        return ((sum(d.count(x) for x in ["Gunbein, Lofty Dragonewt", "Grand Slam Tamer", "Coach Joe, Fiery Counselor", "Dragonborn Striker"]) >= 8))
    def IsBahamutDragon(d):
        return ((sum(d.count(x) for x in ["Terra Finis", "Olivia & Sylvia, Wardens", "Drazael, Ravening Enforcer", "Si Long, Draconic God-Queen"]) >= 8) & (sum(d.count(x) for x in ["Ultimate Bahamut"]) >= 2))

    if IsDragon(d):
        x = "OTHER DRAGON"
        if IsDiscardDragon(d):
            x = "Discard Dragon"
            y.append(x)
        if IsArmedDragon(d):
            x = "Armed Dragon"
            y.append(x)
        if IsBuffDragon(d):
            x = "Buff Dragon"
            y.append(x)
        if IsBahamutDragon(d):
            x = "Bahamut Dragon"
            y.append(x)
    
    ## Shadowcraft
    def IsShadow(d):
        return (d.count('.5.') >= 1)
    def IsLastWordsShadow(d):
        return (sum(d.count(x) for x in ["Istyndet, Soul Convict", "Abyssal Colonel", "Cerberus, Infernal Hound", "Huginn & Muninn"]) >= 10)
    def IsBurialRiteShadow(d):
        return (sum(d.count(x) for x in ["Lakandula, Purgatory Inn", "Septic Shrink", "Memento, the Grim Teacher", "Inn Ghosthound", "Call of the Great Arm", "Sweetsoul Necromancer"]) >= 12)
    def IsGhostShadow(d):
        return ((sum(d.count(x) for x in ["Ghastly Banishment", "Masquerade Ghost"]) >= 5))
    def IsReanimateShadow(d):
        return ((sum(d.count(x) for x in ["Mordecai, Unending Duelist", "Ceridwen, Eternal Duality", "Charon, Stygian Demise"]) >= 5))
    
    if IsShadow(d):
        x = "OTHER SHADOW"
        if IsLastWordsShadow(d):
            x = "LastWords Shadow"
            y.append(x)
        if IsBurialRiteShadow(d):
            x = "BurialRite Shadow"
            y.append(x)
        if IsGhostShadow(d):
            x = "Ghost Shadow"
            y.append(x)
        if IsReanimateShadow(d):
            x = "Reanimate Shadow"
            y.append(x)
    
    ## Bloodcraft
    def IsBlood(d):
        return (d.count('.6.') >= 1)
    def IsWrathBlood(d):
        return ((sum(d.count(x) for x in ["Garodeth, Insurgent Convict", "Howling Scream", "Raging Commander", "Scorching Grandiosity", "Howling Demon"]) >= 8) & (sum(d.count(x) for x in ["Paracelise, Demon of Greed"]) < 2))
    def IsHandlessBlood(d):
        return (sum(d.count(x) for x in ["Paracelise, Demon of Greed", "Room Service Demon"]) >= 4)
    def IsEvoBlood(d):
        return ((sum(d.count(x) for x in ["Alice, Wandering Dreamer", "Dancing Mini Soul Devil", "Tevali, Demonic Cat", "Signa, Sealed Madwolf"]) >= 8) & (sum(d.count(x) for x in ["Paracelise, Demon of Greed"]) < 2))
    def IsVengeanceBlood(d):
        return ((sum(d.count(x) for x in ["Mach-Speed Maron", "Galom, Empress Fist", "Vulgus, Infernal Headmistress", "Doomlord of the Abyss", "Waltz, Moonlight Wolf-King"]) >= 9) & (sum(d.count(x) for x in ["Paracelise, Demon of Greed"]) < 2))
    
    if IsBlood(d):
        x = "OTHER BLOOD"
        if IsWrathBlood(d):
            x = "Wrath Blood"
            y.append(x)
        if IsHandlessBlood(d):
            x = "Handless Blood"
            y.append(x)
        if IsEvoBlood(d):
            x = "Evo Blood"
            y.append(x)
        if IsVengeanceBlood(d):
            x = "Vengeance Blood"
            y.append(x)

    ## Havencraft
    def IsHaven(d):
        return (d.count('.7.') >= 1)
    def IsCrystaliseHaven(d):
        return (sum(d.count(x) for x in ("Wingy, Chirpy Gemstone", "Diamond Master", "Holy Lightning Bird", "Skullfane, the Defiled", "Emerald Maiden")) >= 8)
    def IsHealHaven(d):
        return (sum(d.count(x) for x in ("Pureflame Lady", "Verdilia, Rogue Professor", "Prayer Urn", "Elluvia, Graceful Lady", "Lou, Lady-in-Training")) >= 8)

    if IsHaven(d):
        x = "OTHER HAVEN"
        if IsCrystaliseHaven(d):
            x = "Crystalise Haven"
            y.append(x)
        if IsHealHaven(d):
            x = "Heal Haven"
            y.append(x)
    
    ## Portalcraft
    def IsPortal(d):
        return (d.count('.8.') >= 1)
    def IsPuppetPortal(d):
        return ((sum(d.count(x) for x in ["Young Threadmaster", "Craftsman's Pride", "Orchis, the Limitless", "Blossoming Flower Doll", "Lyelth, Immaculate Idol"]) >= 10) & (sum(d.count(x) for x in ["Cutthroat, Discord Convict"]) < 2))
    def IsMachinaPortal(d):
        return ((sum(d.count(x) for x in ["Gretina, Champion Fighter", "Gioffre, Diligent Engineer", "Robotics Reporter", "Robotic-Arm Rescuer", "Hoverbiker", "Gullias, King of Beasts"]) >= 12) & (sum(d.count(x) for x in ["Cutthroat, Discord Convict"]) < 2))
    def IsEnhancePortal(d):
        return (sum(d.count(x) for x in ["Cutthroat, Discord Convict", "Smeltwork Bodyguard", "Ironforged Right Hand", "Judith, Cosmic Observer"]) >= 7)
    
    if IsPortal(d):
        x = "OTHER PORTAL"
        if IsPuppetPortal(d):
            x = "Puppet Portal"
            y.append(x)
        if IsMachinaPortal(d):
            x = "Machina Portal"
            y.append(x)
        if IsEnhancePortal(d):
            x = "Enhance Portal"
            y.append(x)

    ## Flag for OTHER, append to output list if no archetypes are identified
    if len(y) == 0:
        y.append(x)
    
    ## Append all satisfying archetypes into hybrid deck
    for i, d in enumerate(y):
        if i == len(y) - 1:
            x_output += d
        else:
            x_output += d.split(" ")[0]
        if i != len(y) - 1:
            x_output += "-"
    
    ## Return output depending on mode
    if mode == 1:
        return x_output
    if mode != 1:
        return y