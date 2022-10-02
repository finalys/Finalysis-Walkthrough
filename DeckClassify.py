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
        return (sum(d.count(x) for x in ["Carbuncle, Sacred Emerald", "Piercye, Queen of Frost", "Yggdrasil, Root of Life"]) >= 6) & (sum(d.count(x) for x in ["Nobilis, Sable-Lily Queen", "Forest Merchant"]) <= 1)
    def IsAggroForest(d):
        return (sum(d.count(x) for x in ["Nobilis, Sable-Lily Queen", "Phantombloom Predator", "Aqua Fairy", "Flying Mistletoe Squirrel", "Forest Merchant"]) >= 8) & (sum(d.count(x) for x in ["Piercye, Queen of Frost", "Carbuncle, Sacred Emerald"]) <= 0)
    
    if IsForest(d):
        x = "OTHER FOREST"
        if IsControlForest(d):
            x = "Control Forest"
        if IsAggroForest(d):
            x = "Aggro Forest"
        if IsMjerrabaine(d):
            x = "Jerry Forest"
    
    ## Swordcraft
    def IsSword(d):
        return (d.count('.2.') >= 1)
    def IsEvoRallySword(d):
        return ((sum(d.count(x) for x in ["Kagemitsu, Lost Samurai", "Taketsumi, Aconite Paladin", "Monochrome Endgame", "Musketeers' Vow"]) >= 8) & (sum(d.count(x) for x in ["Royal Fortress"]) <= 1))
    def IsCommanderSword(d):
        return ((sum(d.count(x) for x in ["Royal Fortress"]) >= 2) & (sum(d.count(x) for x in ("Kitty Sergeant", "Luminous Lancer", "Resplendent Knight", "Radiant Luminous Mage")) >= 8))
    def IsHeroicSword(d):
        return ((sum(d.count(x) for x in ("Amerro, Spear Knight", "Heroic Entry", "Valiant Fencer", "Mach Knight", "Flame Soldier")) >= 8))
    
    if IsSword(d):
        x = "OTHER SWORD"
        if IsEvoRallySword(d):
            x = "Evo-Rally Sword"
        if IsCommanderSword(d):
            x = "Commander Sword"
        if IsHeroicSword(d):
            x = "HeroiC Sword"
        if IsMjerrabaine(d):
            x = "Jerry Sword"
    
    ## Runecraft
    def IsRune(d):
        return (d.count('.3.') >= 1)
    def IsDirtRune(d):
        return (sum(d.count(x) for x in ("Acid Golem", "Superior Contractor", "Forbidden Archives Warden", "Juno, Atelier Alchemist", "Levi, Sapience Supreme", "Covetous Witch")) >= 10)
    def IsSpellboostRune(d):
        return ((sum(d.count(x) for x in ("Chakram Wizard", "Kuon, Wuxing Master", "Meltina, Miracle Sorceress")) >= 8))
    def IsYukishimaRune(d):
        return ((sum(d.count(x) for x in ["Yukishima, Master Biographer"]) >= 2) & (sum(d.count(x) for x in ["Orchestral Mage", "Superior Contractor"]) >= 2) & (sum(d.count(x) for x in ["Acid Golem", "Kuon, Wuxing Master", "Meltina, Miracle Sorceress", "Magical Strategy", "Milady, Mystic Queen", "Mystic King"]) <= 1))
    def IsChessRune(d):
        return ((sum(d.count(x) for x in ["Magical Knight", "Magical Rook", "Magical Strategy", "Milady, Mystic Queen", "Mystic King"]) >= 8))
    
    if IsRune(d):
        x = "OTHER RUNE"
        if IsDirtRune(d):
            x = "Dirt Rune"
        if IsSpellboostRune(d):
            x = "Spellboost Rune"
        if IsYukishimaRune(d):
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
        return (sum(d.count(x) for x in ("Terra Finis", "Ultimate Bahamut", "Gilnelise, Ravenous Craving")) >= 5)

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
    
    if IsShadow(d):
        x = "OTHER SHADOW"
        if IsFGShadow(d):
            x = "F&G Shadow"
        if IsLWShadow(d):
            x = "LW Shadow"
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
    def IsWardHaven(d):
        return (sum(d.count(x) for x in ("Holy Saber", "Teena, Sacred Sister", "Wilbert, Luminous Paladin", "Zeno, Paradoxical Shield", "Temple Healer")) >= 8)
    def IsHealHaven(d):
        return (sum(d.count(x) for x in ("Bellerophon", "Sacred Ice-Crusher", "Perpetual Despair")) >= 6)
    def IsCrystaliseHaven(d):
        return (sum(d.count(x) for x in ("Wingy, Chirpy Gemstone", "Diamond Master", "Holy Lightning Bird", "Skullfane, the Defiled", "Emerald Maiden")) >= 8)

    if IsHaven(d):
        x = "OTHER HAVEN"
        if IsCrystaliseHaven(d):
            x = "Crystalise Haven"
        if IsWardHaven(d):
            x = "Ward Haven"
        if IsHealHaven(d):
            x = "Heal Haven"
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