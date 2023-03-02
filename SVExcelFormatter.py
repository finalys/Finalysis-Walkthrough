def DeckBreakdownToExcel(deck_breakdown_dict, jwriter, jworkbook):
    # 1. Loop through fixed classes_order, create a new sheet for every deck archetype.
    classes_order = ["Forestcraft", "Swordcraft", "Runecraft", "Dragoncraft", "Shadowcraft", "Bloodcraft", "Havencraft", "Portalcraft"]
    for classes in classes_order:
        for deck, stats_df in deck_breakdown_dict[classes].items():
            stats_df.to_excel(jwriter, sheet_name=f"{deck}", index=True)
            # 2. Set active sheet to newly added sheet.
            jworksheet = jwriter.sheets[deck]
            # 3. Beautify active sheet
            decimal_fmt = jworkbook.add_format({'num_format': '0.00'})
            jworksheet.set_column('C:E', 10, decimal_fmt) ## set descriptive stats to decimal format.
            jworksheet.set_column('A:A', 30) ## set the width = 30 and bold for column A:A
            jworksheet.freeze_panes(0, 5) ## Freeze left columns, Cards and descriptive stats.
            # xlsxwriter requires format to be passed with .write(), which requires an input cell value too. Iterate through DataFrame.column
            descstats_header_format = jworkbook.add_format({'bold': True, 'text_wrap': False, 'align': 'center', 'valign': 'vcenter', 'font_size': 15, 'rotation':0})
            player_header_format = jworkbook.add_format({'bold': True, 'text_wrap': True, 'align': 'center', 'valign': 'vcenter', 'font_size': 12, 'rotation':90})
            for col_num, value in enumerate(stats_df.columns.values): ## Write the column headers with the defined format.
                if col_num+1 < 5:
                    jworksheet.write(0, col_num+1, value, descstats_header_format)
                else:
                    jworksheet.write(0, col_num+1, value, player_header_format)
            deck_header_format = jworkbook.add_format({'bold': True, 'text_wrap': True, 'align': 'center', 'valign': 'vcenter', 'font_size': 20, 'rotation':0, 'border':2})
            jworksheet.write(0, 0, deck, deck_header_format) ## Formatting for deck at cell A1
            # 4. Set tab colors
            tabcolours = {'Forestcraft': 'green', 'Swordcraft': 'yellow', 'Runecraft': 'blue', 'Dragoncraft': 'orange', 'Shadowcraft': 'purple', 'Bloodcraft': 'red', 'Havencraft': 'silver', 'Portalcraft': 'cyan'}
            for craft, colour in tabcolours.items():
                if classes == craft:
                    jworksheet.set_tab_color(colour)
                    
                    
                    
def SVOExcelFormatter(svowriter, svoworkbook, input_filename):
    # 1. Set the color conditional formatting for classes and decks.
    greenFill = svoworkbook.add_format({'bg_color': '#c6ffb3', 'font_color': '#000000'})
    yellowFill = svoworkbook.add_format({'bg_color': '#ffffb3', 'font_color': '#000000'})
    blueFill = svoworkbook.add_format({'bg_color': '#b3d9ff', 'font_color': '#000000'})
    orangeFill = svoworkbook.add_format({'bg_color': '#ffd9b3', 'font_color': '#000000'})
    purpleFill = svoworkbook.add_format({'bg_color': '#ecb3ff', 'font_color': '#000000'})
    redFill = svoworkbook.add_format({'bg_color': '#ffb3b3', 'font_color': '#000000'})
    greyFill = svoworkbook.add_format({'bg_color': '#e6e6e6', 'font_color': '#000000'})
    tealFill = svoworkbook.add_format({'bg_color': '#b3ffff', 'font_color': '#000000'})
    def ConditionFormatter(worksheet, lookuprange):
        worksheet.conditional_format(lookuprange, {'type': 'text', 'criteria': 'containing', 'value': 'Forest', 'format': greenFill})
        worksheet.conditional_format(lookuprange, {'type': 'text', 'criteria': 'containing', 'value': 'Sword', 'format': yellowFill})
        worksheet.conditional_format(lookuprange, {'type': 'text', 'criteria': 'containing', 'value': 'Rune', 'format': blueFill})
        worksheet.conditional_format(lookuprange, {'type': 'text', 'criteria': 'containing', 'value': 'Dragon', 'format': orangeFill})
        worksheet.conditional_format(lookuprange, {'type': 'text', 'criteria': 'containing', 'value': 'Shadow', 'format': purpleFill})
        worksheet.conditional_format(lookuprange, {'type': 'text', 'criteria': 'containing', 'value': 'Blood', 'format': redFill})
        worksheet.conditional_format(lookuprange, {'type': 'text', 'criteria': 'containing', 'value': 'Haven', 'format': greyFill})
        worksheet.conditional_format(lookuprange, {'type': 'text', 'criteria': 'containing', 'value': 'Portal', 'format': tealFill})
        
    # 2. Set active sheet and format accordingly.
    col_widths = {"Name": 20, 
                  "Player ID": 11,
                  "Deck_URL": 11,
                  "Deck": 20,
                  "Lineup": 55,
                  "C_Lineup": 38,
                  "Pos": 4,
                  "Count": 6,
                  "%ofPlayers": 10,
                  "Class": 18}
    
    svoworksheet = svowriter.sheets["Wide"]
    svoworksheet.set_column('A:A', col_widths["Name"]) ## Name
    svoworksheet.set_column('B:B', col_widths["Player ID"]) ## Player ID
    svoworksheet.set_column('C:E', col_widths["Deck_URL"]) ## Deck_URL 
    ConditionFormatter(svoworksheet, 'F1:H999') ## Deck 
    svoworksheet.set_column('F:H', col_widths["Deck"]) ## Deck 
    svoworksheet.set_column('I:I', col_widths["Lineup"]) ## Lineup 
    svoworksheet.set_column('J:J', col_widths["C_Lineup"]) ## C_Lineup
    # svoworksheet.set_column('I:I', col_widths["Pos"]) ## Pos
    
    svoworksheet = svowriter.sheets["Tall"]
    svoworksheet.set_column('A:A', col_widths["Name"]) ## Name
    svoworksheet.set_column('B:B', col_widths["Player ID"]) ## Player ID
    svoworksheet.set_column('C:C', col_widths["Deck_URL"]) ## Deck_URL 
    ConditionFormatter(svoworksheet, 'D1:E999') ## Deck, Class
    svoworksheet.set_column('D:D', col_widths["Deck"]) ## Deck 
    svoworksheet.set_column('E:E', col_widths["Class"]) ## Class 
    svoworksheet.set_column('F:F', col_widths["Pos"]) ## Pos
    
    svoworksheet = svowriter.sheets["Summary"]
    svoworksheet.set_column('A:A', col_widths["Deck"]) ## Deck 
    svoworksheet.set_column('B:B', col_widths["Class"]) ## Class 
    ConditionFormatter(svoworksheet, 'A2:B999') ## Deck, Class
    svoworksheet.set_column('C:C', col_widths["Count"]) ## Count
    svoworksheet.set_column('D:D', col_widths["%ofPlayers"], svoworkbook.add_format({'num_format': '0.00%'})) ## %ofPlayers 
    svoworksheet.set_column('E:E', 1) ## BLANK 
    svoworksheet.set_column('F:F', col_widths["Lineup"]) ## Lineup
    svoworksheet.set_column('G:G', col_widths["Count"]) ## Count
    svoworksheet.set_column('H:H', 10, svoworkbook.add_format({'num_format': '0.00%'})) ## %ofPlayers
    svoworksheet.set_column('I:I', 1) ## BLANK 
    svoworksheet.set_column('J:J', col_widths["C_Lineup"]) ## C_Lineup
    svoworksheet.set_column('K:K', col_widths["Count"]) ## Count
    svoworksheet.set_column('L:L', col_widths["%ofPlayers"], svoworkbook.add_format({'num_format': '0.00%'})) ## %ofPlayers
    merge_fmt = svoworkbook.add_format({'bold': 1, 'border': 1, 'align': 'center','valign': 'vcenter', 'font_size': 20})
    svoworksheet.merge_range('A1:L1', f'{input_filename} Summary - {rawdf_2.shape[0]} Players', merge_fmt)
    
    
def ExcelFormatter(jwriter, jworkbook):
    # 1. Set the color conditional formatting for classes and decks.
    greenFill = jworkbook.add_format({'bg_color': '#c6ffb3', 'font_color': '#000000'})
    yellowFill = jworkbook.add_format({'bg_color': '#ffffb3', 'font_color': '#000000'})
    blueFill = jworkbook.add_format({'bg_color': '#b3d9ff', 'font_color': '#000000'})
    orangeFill = jworkbook.add_format({'bg_color': '#ffd9b3', 'font_color': '#000000'})
    purpleFill = jworkbook.add_format({'bg_color': '#ecb3ff', 'font_color': '#000000'})
    redFill = jworkbook.add_format({'bg_color': '#ffb3b3', 'font_color': '#000000'})
    greyFill = jworkbook.add_format({'bg_color': '#e6e6e6', 'font_color': '#000000'})
    tealFill = jworkbook.add_format({'bg_color': '#b3ffff', 'font_color': '#000000'})
    def ConditionFormatter(worksheet, lookuprange):
        worksheet.conditional_format(lookuprange, {'type': 'text', 'criteria': 'containing', 'value': 'Forest', 'format': greenFill})
        worksheet.conditional_format(lookuprange, {'type': 'text', 'criteria': 'containing', 'value': 'Sword', 'format': yellowFill})
        worksheet.conditional_format(lookuprange, {'type': 'text', 'criteria': 'containing', 'value': 'Rune', 'format': blueFill})
        worksheet.conditional_format(lookuprange, {'type': 'text', 'criteria': 'containing', 'value': 'Dragon', 'format': orangeFill})
        worksheet.conditional_format(lookuprange, {'type': 'text', 'criteria': 'containing', 'value': 'Shadow', 'format': purpleFill})
        worksheet.conditional_format(lookuprange, {'type': 'text', 'criteria': 'containing', 'value': 'Blood', 'format': redFill})
        worksheet.conditional_format(lookuprange, {'type': 'text', 'criteria': 'containing', 'value': 'Haven', 'format': greyFill})
        worksheet.conditional_format(lookuprange, {'type': 'text', 'criteria': 'containing', 'value': 'Portal', 'format': tealFill})
        
    # 2. Set active sheet and format accordingly.
    col_widths = {"Player": 20, 
                  "PlayerProfile": 11,
                  "Deck_URL": 11,
                  "Deck": 20,
                  "Lineup": 35,
                  "C_Lineup": 30,
                  "Pos": 4,
                  "Count": 6,
                  "%ofPlayers": 10,
                  "Class": 18}
    
    jworksheet = jwriter.sheets["Wide"]
    jworksheet.set_column('A:A', col_widths["PlayerProfile"]) ## PlayerProfile
    jworksheet.set_column('B:B', col_widths["Player"]) ## Player
    jworksheet.set_column('C:D', col_widths["Deck_URL"]) ## Deck_URL 
    ConditionFormatter(jworksheet, 'E1:F999') ## Deck 
    jworksheet.set_column('E:F', col_widths["Deck"]) ## Deck 
    jworksheet.set_column('G:G', col_widths["Lineup"]) ## Lineup 
    jworksheet.set_column('H:H', col_widths["C_Lineup"]) ## C_Lineup
    jworksheet.set_column('I:I', col_widths["Pos"]) ## Pos
    
    jworksheet = jwriter.sheets["Tall"]
    jworksheet.set_column('A:A', col_widths["PlayerProfile"]) ## PlayerProfile
    jworksheet.set_column('B:B', col_widths["Player"]) ## Player
    jworksheet.set_column('C:C', col_widths["Deck_URL"]) ## Deck_URL 
    ConditionFormatter(jworksheet, 'D1:E999') ## Deck, Class
    jworksheet.set_column('D:D', col_widths["Deck"]) ## Deck 
    jworksheet.set_column('E:E', col_widths["Class"]) ## Class 
    jworksheet.set_column('F:F', col_widths["Pos"]) ## Pos
    
    jworksheet = jwriter.sheets["Summary"]
    jworksheet.set_column('A:A', col_widths["Deck"]) ## Deck 
    jworksheet.set_column('B:B', col_widths["Class"]) ## Class 
    ConditionFormatter(jworksheet, 'A2:B999') ## Deck, Class
    jworksheet.set_column('C:C', col_widths["Count"]) ## Count
    jworksheet.set_column('D:D', col_widths["%ofPlayers"], jworkbook.add_format({'num_format': '0.00%'})) ## %ofPlayers 
    jworksheet.set_column('E:E', 1) ## BLANK 
    jworksheet.set_column('F:F', col_widths["Lineup"]) ## Lineup
    jworksheet.set_column('G:G', col_widths["Count"]) ## Count
    jworksheet.set_column('H:H', 10, jworkbook.add_format({'num_format': '0.00%'})) ## %ofPlayers
    jworksheet.set_column('I:I', 1) ## BLANK 
    jworksheet.set_column('J:J', col_widths["C_Lineup"]) ## C_Lineup
    jworksheet.set_column('K:K', col_widths["Count"]) ## Count
    jworksheet.set_column('L:L', col_widths["%ofPlayers"], jworkbook.add_format({'num_format': '0.00%'})) ## %ofPlayers
    merge_fmt = jworkbook.add_format({'bold': 1, 'border': 1, 'align': 'center','valign': 'vcenter', 'font_size': 20})
    jworksheet.merge_range('A1:L1', f'{jcg_name.split(" ロ")[0]} Summary', merge_fmt)
    
    jworksheet = jwriter.sheets["Matchup"]
    jworksheet.merge_range('A1:H1', 'Class Matchup', merge_fmt)
    jworksheet.merge_range('J1:Q1', 'Deck Matchup', merge_fmt)
    jworksheet.set_column('A:A', col_widths["C_Lineup"]) ## C_Lineup
    jworksheet.set_column('B:B', col_widths["C_Lineup"]) ## C_Lineup
    jworksheet.set_column('J:J', col_widths["Lineup"]) ## Lineup
    jworksheet.set_column('K:K', col_widths["Lineup"]) ## Lineup
    jworksheet.set_column('H:H', col_widths["%ofPlayers"], jworkbook.add_format({'num_format': '0.00%'})) ## %
    jworksheet.set_column('Q:Q', col_widths["%ofPlayers"], jworkbook.add_format({'num_format': '0.00%'})) ## %
    
    
def EdittedExcelFormatter(jwriter, jworkbook):
    # 1. Set the color conditional formatting for classes and decks.
    greenFill = jworkbook.add_format({'bg_color': '#c6ffb3', 'font_color': '#000000'})
    yellowFill = jworkbook.add_format({'bg_color': '#ffffb3', 'font_color': '#000000'})
    blueFill = jworkbook.add_format({'bg_color': '#b3d9ff', 'font_color': '#000000'})
    orangeFill = jworkbook.add_format({'bg_color': '#ffd9b3', 'font_color': '#000000'})
    purpleFill = jworkbook.add_format({'bg_color': '#ecb3ff', 'font_color': '#000000'})
    redFill = jworkbook.add_format({'bg_color': '#ffb3b3', 'font_color': '#000000'})
    greyFill = jworkbook.add_format({'bg_color': '#e6e6e6', 'font_color': '#000000'})
    tealFill = jworkbook.add_format({'bg_color': '#b3ffff', 'font_color': '#000000'})
    def ConditionFormatter(worksheet, lookuprange):
        worksheet.conditional_format(lookuprange, {'type': 'text', 'criteria': 'containing', 'value': 'Forest', 'format': greenFill})
        worksheet.conditional_format(lookuprange, {'type': 'text', 'criteria': 'containing', 'value': 'Sword', 'format': yellowFill})
        worksheet.conditional_format(lookuprange, {'type': 'text', 'criteria': 'containing', 'value': 'Rune', 'format': blueFill})
        worksheet.conditional_format(lookuprange, {'type': 'text', 'criteria': 'containing', 'value': 'Dragon', 'format': orangeFill})
        worksheet.conditional_format(lookuprange, {'type': 'text', 'criteria': 'containing', 'value': 'Shadow', 'format': purpleFill})
        worksheet.conditional_format(lookuprange, {'type': 'text', 'criteria': 'containing', 'value': 'Blood', 'format': redFill})
        worksheet.conditional_format(lookuprange, {'type': 'text', 'criteria': 'containing', 'value': 'Haven', 'format': greyFill})
        worksheet.conditional_format(lookuprange, {'type': 'text', 'criteria': 'containing', 'value': 'Portal', 'format': tealFill})
        
    # 2. Set active sheet and format accordingly.
    col_widths = {"Player": 20, 
                  "PlayerProfile": 11,
                  "Deck_URL": 11,
                  "Deck": 20,
                  "Lineup": 35,
                  "C_Lineup": 30,
                  "Pos": 4,
                  "Count": 6,
                  "%ofPlayers": 10,
                  "Class": 18}
    
    jworksheet = jwriter.sheets["Wide"]
    jworksheet.set_column('A:A', col_widths["Player"]) ## name
    jworksheet.set_column('B:B', col_widths["PlayerProfile"]) ## Player ID
    # jworksheet.set_column('C:D', col_widths["Deck_URL"]) ## Deck_URL 
    jworksheet.set_column('C:C', 9) ## SwissWins
    jworksheet.set_column('D:D', col_widths["Pos"]) ## top8
    ConditionFormatter(jworksheet, 'E1:G999') ## Deck 
    jworksheet.set_column('E:G', col_widths["Deck"]) ## Deck 
    jworksheet.set_column('H:H', 60) ## Lineup 
    jworksheet.set_column('I:I', 36) ## C_Lineup
    # jworksheet.set_column('I:I', col_widths["Pos"]) ## Pos
    
    # jworksheet = jwriter.sheets["Tall"]
    # jworksheet.set_column('A:A', col_widths["PlayerProfile"]) ## PlayerProfile
    # jworksheet.set_column('B:B', col_widths["Player"]) ## Player
    # jworksheet.set_column('C:C', col_widths["Deck_URL"]) ## Deck_URL 
    # ConditionFormatter(jworksheet, 'D1:E999') ## Deck, Class
    # jworksheet.set_column('D:D', col_widths["Deck"]) ## Deck 
    # jworksheet.set_column('E:E', col_widths["Class"]) ## Class 
    # jworksheet.set_column('F:F', col_widths["Pos"]) ## Pos
    
    jworksheet = jwriter.sheets["Summary"]
    jworksheet.set_column('A:A', col_widths["Deck"]) ## Deck 
    jworksheet.set_column('B:B', col_widths["Class"]) ## Class 
    ConditionFormatter(jworksheet, 'A2:B999') ## Deck, Class
    jworksheet.set_column('C:C', col_widths["Count"]) ## Count
    jworksheet.set_column('D:D', col_widths["%ofPlayers"], jworkbook.add_format({'num_format': '0.00%'})) ## %ofPlayers 
    jworksheet.set_column('E:E', 1) ## BLANK 
    jworksheet.set_column('F:F', 60) ## Lineup
    jworksheet.set_column('G:G', col_widths["Count"]) ## Count
    jworksheet.set_column('H:H', 10, jworkbook.add_format({'num_format': '0.00%'})) ## %ofPlayers
    jworksheet.set_column('I:I', 1) ## BLANK 
    jworksheet.set_column('J:J', 36) ## C_Lineup
    jworksheet.set_column('K:K', col_widths["Count"]) ## Count
    jworksheet.set_column('L:L', col_widths["%ofPlayers"], jworkbook.add_format({'num_format': '0.00%'})) ## %ofPlayers
    merge_fmt = jworkbook.add_format({'bold': 1, 'border': 1, 'align': 'center','valign': 'vcenter', 'font_size': 20})
    # jworksheet.merge_range('A1:L1', f'{jcg_name.split(" ロ")[0]} Summary', merge_fmt)
    
    jworksheet = jwriter.sheets["Matchup"]
    jworksheet.merge_range('A1:H1', 'Class Matchup', merge_fmt)
    jworksheet.merge_range('J1:Q1', 'Deck Matchup', merge_fmt)
    jworksheet.set_column('A:A', 36) ## C_Lineup
    jworksheet.set_column('B:B', 36) ## C_Lineup
    jworksheet.set_column('J:J', 60) ## Lineup
    jworksheet.set_column('K:K', 60) ## Lineup
    jworksheet.set_column('H:H', col_widths["%ofPlayers"], jworkbook.add_format({'num_format': '0.00%'})) ## %
    jworksheet.set_column('Q:Q', col_widths["%ofPlayers"], jworkbook.add_format({'num_format': '0.00%'})) ## %