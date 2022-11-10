## Function to determine deck archetype. Takes in Deck_URL after replacing cardhash with card names.
def DeckSearch(d):
    x = "" ## Target string container to replace sequentially
    
    ## Neutral Identifiers
    def IsMjerrabaine(d):
        return (d.count('Mjerrabaine, Great One') >= 3)
    
    ## Forestcraft
    def IsForest(d):
        return (d.count('.1.') >= 1)
    def IsControlForest(d):
        return (sum(d.count(x) for x in ['Adherent of Annihilation', 'Carbuncle, Sacred Emerald', 'Erosive Annihilation', 'Cosmos Fang', 'Ultimate Bahamut', 'Yggdrasil, Root of Life']) >= 7)
    def IsFairyForest(d):
        return (sum(d.count(x) for x in ["Nobilis, Sable-Lily Queen", "Phantombloom Predator", "Aqua Fairy", "Flying Mistletoe Squirrel", "Forest Merchant", "Tam Lin, Fey Knight"]) >= 10)
    
    if IsForest(d):
        x = "OTHER FOREST"
        if IsControlForest(d):
            x = "Control Forest"
        if IsFairyForest(d):
            x = "Fairy Forest"
        if IsMjerrabaine(d):
            x = "Jerry Forest"
    
    ## Swordcraft
    def IsSword(d):
        return (d.count('.2.') >= 1)
    def IsEvoRallySword(d):
        return ((sum(d.count(x) for x in ["Kagemitsu, Lost Samurai", "Taketsumi, Aconite Paladin", "Monochrome Endgame", "Musketeers' Vow"]) >= 8) & (sum(d.count(x) for x in ["Royal Fortress"]) <= 1))
    def IsQuickbladerSword(d):
        return ((sum(d.count(x) for x in ["Bumpkin Recruit", "Penguin Guardian", "Brave Vanguard", "Suave Bandit", "Wayfaring Goblin"]) >= 8) & (sum(d.count(x) for x in ["Swiftspeed Quickblader"]) >= 2) & (sum(d.count(x) for x in ["Golden Warrior", "Forge Weaponry", "Angel's Grace"]) >= 4))
    def IsCoinSword(d):
        return ((sum(d.count(x) for x in ("Jiemon, Thief Lord", "Masterful Musician", "Front Desk Frog", "Night on the Town")) >= 5) | (sum(d.count(x) for x in ("Jiemon, Thief Lord", "Swiftspeed Quickblader")) >= 4))
    def IsCommanderSword(d):
        return ((sum(d.count(x) for x in ["Royal Fortress"]) >= 2) & (sum(d.count(x) for x in ("Kitty Sergeant", "Luminous Lancer", "Resplendent Knight", "Radiant Luminous Mage")) >= 8))
    
    if IsSword(d):
        x = "OTHER SWORD"
        if IsEvoRallySword(d):
            x = "Evo-Rally Sword"
        if IsQuickbladerSword(d):
            x = "Quickblader Sword"
        if IsCoinSword(d):
            x = "Coin Sword"
        if IsCommanderSword(d):
            x = "Commander Sword"
        if IsMjerrabaine(d):
            x = "Jerry Sword"
    
    ## Runecraft
    def IsRune(d):
        return (d.count('.3.') >= 1)
    def IsDirtRune(d):
        return (sum(d.count(x) for x in ("Acid Golem", "Superior Contractor", "Forbidden Archives Warden", "Juno, Atelier Alchemist", "Levi, Sapience Supreme", "Covetous Witch")) >= 10)
    def IsSpellboostRune(d):
        return ((sum(d.count(x) for x in ("Chakram Wizard", "Kuon, Wuxing Master", "Meltina, Miracle Sorceress")) >= 8))
    def IsChessRune(d):
        return ((sum(d.count(x) for x in ["Magical Knight", "Magical Rook", "Magical Strategy", "Milady, Mystic Queen", "Mystic King"]) >= 8))
    
    if IsRune(d):
        x = "OTHER RUNE"
        if IsDirtRune(d):
            x = "Dirt Rune"
        if IsSpellboostRune(d):
            x = "Spellboost Rune"
        if IsChessRune(d):
            x = "Chess Rune"
        if IsMjerrabaine(d):
            x = "Jerry Rune"

    ## Dragoncraft
    def IsDragon(d):
        return (d.count('.4.') >= 1)
    def IsArmedDragon(d):
        return ((sum(d.count(x) for x in ("Draconic Armor", "Draconir, Knuckle Dragon", "Hammer Dragonewt", "Lance Lizard")) >= 7))
    def IsControlDragon(d):
        return (sum(d.count(x) for x in ("Terra Finis", "Ultimate Bahamut", "Gilnelise, Ravenous Craving", "Si Long, Draconic God-Queen")) >= 7)

    if IsDragon(d):
        x = "OTHER DRAGON"
        if IsArmedDragon(d):
            x = "Armed Dragon"
        if IsControlDragon(d):
            x = "Control Dragon"
        if IsMjerrabaine(d):
            x = "Jerry Dragon"
    
    ## Shadowcraft
    def IsShadow(d):
        return (d.count('.5.') >= 1)
    def IsFGShadow(d):
        return (sum(d.count(x) for x in ["Skeleton Raider", "Flame and Glass, Duality", "Suzy, Hexcaster", "Rulenye, Screaming Silence", "Spirit Invasion"]) >= 8)
    def IsLWShadow(d):
        return (sum(d.count(x) for x in ["Cerberus, Infernal Hound", "Deathcat Reaper", "Mino, Daydreaming Reaper", "Huginn & Muninn", "Thunder God of the Tempest"]) >= 8) & (sum(d.count(x) for x in ["Flame and Glass, Duality"]) <= 0)
    def IsHybridShadow(d):
        return (sum(d.count(x) for x in ["Cerberus, Infernal Hound", "Masquerade Ghost", "Skeleton Raider", "Huginn & Muninn", "Baccherus, Peppy Ghostie"]) >= 10)
    
    if IsShadow(d):
        x = "OTHER SHADOW"
        if IsFGShadow(d):
            x = "F&G Shadow"
        if IsLWShadow(d):
            x = "LW Shadow"
        if IsHybridShadow(d):
            x = "Hybrid Shadow"
        if IsMjerrabaine(d):
            x = "Jerry Shadow"
    
    ## Bloodcraft
    def IsBlood(d):
        return (d.count('.6.') >= 1)
    def IsEvoBlood(d):
        return (sum(d.count(x) for x in ("Kali", "Yuzuki, Bloodlord", "Dancing Mini Soul Devil", "Bloodlust Demon")) >= 8)
    def IsWrathBlood(d):
        return (sum(d.count(x) for x in ("Demonium, Punk Devil", "Dark Contract", "Bloodsucker of the Night", "Sanguine Necklace", "Demon Maestro", "Howling Demon")) >= 10)
    def IsHandlessBlood(d):
        return (sum(d.count(x) for x in ("Paracelise, Demon of Greed", "Room Service Demon", "Bat Usher", "Silvernail Blaster")) >= 10)
    
    if IsBlood(d):
        x = "OTHER BLOOD"
        if IsEvoBlood(d):
            x = "Evo Blood"
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
    def IsWardHaven(d):
        return (sum(d.count(x) for x in ("Holy Saber", "Teena, Sacred Sister", "Wilbert, Luminous Paladin", "Zeno, Paradoxical Shield", "Temple Healer")) >= 8)
    def IsControlHaven(d):
        return (sum(d.count(x) for x in ("Sacred Ice-Crusher", "Perpetual Despair", "Terra Finis", "Ultimate Bahamut", "Greater Will")) >= 8 & (sum(d.count(x) for x in ("Wingy, Chirpy Gemstone", "Diamond Master", "Holy Lightning Bird", "Skullfane, the Defiled", "Emerald Maiden")) <= 1))

    if IsHaven(d):
        x = "OTHER HAVEN"
        if IsCrystaliseHaven(d):
            x = "Crystalise Haven"
        if IsWardHaven(d):
            x = "Ward Haven"
        if IsControlHaven(d):
            x = "Control Haven"
        if IsMjerrabaine(d):
            x = "Jerry Haven"
    
    ## Portalcraft
    def IsPortal(d):
        return (d.count('.8.') >= 1)
    def IsPuppetPortal(d):
        return (sum(d.count(x) for x in ["Young Threadmaster", "Craftsman's Pride", "Orchis, the Limitless", "Blossoming Flower Doll"]) >= 8) & (sum(d.count(x) for x in ["Artifact Impulse", "Genesis Artifact"]) <= 0)
    def IsArtifactPortal(d):
        return (sum(d.count(x) for x in ["Artifact Impulse", "Genesis Artifact", "Vyrmedea, Synthetic Voice", "Ralmia, Astrowing", "Full Blast Gunner"]) >= 8)
    
    if IsPortal(d):
        x = "OTHER PORTAL"
        if IsPuppetPortal(d):
            x = "Puppet Portal"
        if IsArtifactPortal(d):
            x = "Artifact Portal"
        if IsMjerrabaine(d):
            x = "Jerry Portal"

    return x