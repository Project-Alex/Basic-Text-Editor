from os import system
import func

ordered_list = []
unordered_list = []

document_list = []

brkline = "=-"*13 + "=\n"

close = False
while not close:

    # Main Menu
    print(f"{brkline}"
          "Welcome to Basic Scribe\n"
          f"{brkline}"
          "Please select an option:\n"
          "1.\tAdd text\n"
          "2.\tEdit document\n"
          "3.\tApply styles\n"
          "4.\tFind and replace\n"
          "5.\tPreview\n"
          "6.\tPrint\n"
          "7.\tExit\n"
          f"{brkline}"
          )
    
    main_menu_selection = int(input("1 - 7 : "))
    system("cls")

# 1. Add Text =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
    
    while main_menu_selection == 1:
        print("Please select an option:\n"
              "1.\tRegular text\n"
              "2.\tHeader text\n"
              "3.\tItalics\n"
              "4.\tBold\n"
              "5.\tOrdered list\n"
              "6.\tUnordered list\n"
              "7.\tLinks\n"
              "8.\tBlockquotes\n"
              "9.\tBlocks of code\n"
              "10.\tInline quotes\n"
              )
        
        try:
            menu1 = int(input("[1 - 10] or [0 to go back]: "))
            system('cls')

            if menu1 not in range(0, 10):
                raise ValueError

            # Regular text          -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
            if menu1 == 1:
                regular_text_entry = input("Please enter text below and press enter to finish:\n")
                document_list.append(regular_text_entry)

            # Header text           -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
            if menu1 == 2:
                header_text = input("Please enter text below and press enter to finish:\n")
                header_number = int(input("Header number? [1, 2, 3, 4 etc]: "))
                header_final = header_number*"#" + " " + header_text + " " + header_number*"#"
                document_list.append(header_final)
            
            # Italics               -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
            if menu1 == 3:
                italic_text = input("Please enter text below and press enter to finish:\n")
                italic_final = f"*{italic_text}*"
                document_list.append(italic_final)

            # Bold                  -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
            if menu1 == 4:
                bold_text = input("Please enter text below and press enter to finish:\n")
                bold_final = f"__{bold_text}__"
                document_list.append(bold_final)
            
            # Ordered list          -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
            while menu1 == 5:
                ol_enum = input("Please enter digit or letter for list item eg. 1 / 2 / a / b: \n")
                ol_text = input("Please enter your list item's text:\n")
                ol_final = ol_enum + "\t" + ol_text
                ordered_list.append(ol_final)
                
                ol_finish = int(input("1 to add another item OR 2 to finish list: "))
                if ol_finish == 1:
                    continue
                else:
                    ordered_list = "\n".join(ordered_list)
                    document_list.append(ordered_list)
                    system("cls")
                    break
            
            # Unordered list        -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
            while menu1 == 6:
                uol_text = input("Please enter your list item's text:\n")
                uol_final = "*\t" + uol_text
                unordered_list.append(uol_final)
                
                uol_finish = int(input("1 to add another item OR 2 to finish list: "))
                if uol_finish == 1:
                    continue
                else:
                    unordered_list = "\n".join(unordered_list)
                    document_list.append(unordered_list)
                    system("cls")
                    break

            # Links                 -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
            if menu1 == 7:
                link_display_text = input("Please enter the text your link should display as: \n")
                link_actual = input("Please enter link e.g https://www.______.com: ")
                link_final = f"[{link_display_text}]({link_actual})"
                document_list.append(link_final)          
            
            # Blockquotes           -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
            if menu1 == 8:
                blockquotes_text = input("Please enter text below and press enter to finish:\n")
                blockquotes_number = int(input("Blockquotes indent? [1, 2, 3, 4 etc]"))
                blockquotes_final = ">"*blockquotes_number + blockquotes_text + ">"*blockquotes_number
                document_list.append(blockquotes_final)

            # Blocks of code        -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
            if menu1 == 9:
                block_code_text = input("Please enter text below and press enter to finish:\n")
                block_code_final = f"```\n{block_code_text}\n```"
                document_list.append(block_code_final)

            # Inline code           -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
            if menu1 == 10:
                inline_code_text = input("Please enter text below and press enter to finish:\n")
                inline_code_final = f"`{inline_code_text}`"
                document_list.append(inline_code_final)

            # Exit menu 1.0         -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
            system("cls")
            if menu1 == 0:
                main_menu_selection = 0

        except ValueError:
            print("ERROR: Invalid input\nPlease try again!\n")

# 2. Edit Document =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#            

    while main_menu_selection == 2:
        for i, x in enumerate(document_list, 1):
            print(f"{i}. {x}\n\n")
        
        edit_element = int(input(f"Please enter the number of the element you wish to move/delete: \n[1 to {len(document_list)}] or [0 to return]:\n"))
        if edit_element == 0:
            main_menu_selection = 0
        else:
            delete_move = int(input("1. Move entry \n"
                                    "2. Delete entry \n"
                                    "[1 or 2] or [0 to return]: "
                                    ))
        
            if delete_move == 1:
                move_to = int(input("Enter number of element you wish selected element will appear above:\n"
                                    "(e.g if 1, item will be moved to above 1): "))
                document_list.insert[move_to, edit_element-1]                

            if delete_move == 2:
                document_list.remove[edit_element-1]
                main_menu_selection = 0


#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
        
    while main_menu_selection == 3:
        main_menu_selection = input("Type 0 to return")

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#    
            
    while main_menu_selection == 4:
        main_menu_selection = input("Type 0 to return")

# Preview =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
                
    while main_menu_selection == 5:
        print("Preview:\n" + "\n\t-=-=-=-\n".join(document_list) + "\n")

        main_menu_selection = input("Type 0 to return")
        system("cls")

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#

    while main_menu_selection == 6:

        user_file = (input("Please enter the name of your file e.g file_name:\n") + ".txt")
        with open(f"{user_file}", "w") as f:
            f.write("\n\n".join(document_list))
        
        print("File successfully created!\n\n")

        return_to_main_menu = input("Please enter anything to return to main menu when ready.")
        system("cls")
        main_menu_selection = 0

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#

    while main_menu_selection == 7:
        print("Thank you for using Basic Scribe!")
        main_menu_selection = 0
        close = True

