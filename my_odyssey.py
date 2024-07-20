from Odyssey_data import themes, odyssey_data
from intro import print_intro
from linked_list import LinkedList

print_intro()

def insert_odyssey_themes():
    odyssey_theme_list = LinkedList()
    for odyssey_theme in themes:
        odyssey_theme_list.insert_beginning(odyssey_theme)
    return odyssey_theme_list

def insert_odyssey_data():
    odyssey_data_list = LinkedList()
    for odyssey_theme in themes:
        odyssey_sublist = LinkedList()
        for odyssey in odyssey_data:
            if odyssey[0] == odyssey_theme:
                odyssey_sublist.insert_beginning(odyssey)
        odyssey_data_list.insert_beginning(odyssey_sublist)
    return odyssey_data_list

my_odyssey_themes = insert_odyssey_themes()
my_odyssey_list = insert_odyssey_data()

selected_odyssey_theme = ""

for odyssey_theme in themes:
        print(odyssey_theme + "\n")

while len(selected_odyssey_theme) == 0:
    print("\n What type of odyssey would you like to go on?\n")
    
    user_input = str(input("\nStart typing the first letters of the theme you want and press enter to begin your odyssey. \n")).lower()

    matching_themes= []
    theme_list_head = my_odyssey_themes.get_head_node()
    while theme_list_head is not None:
        if str(theme_list_head.get_value()).startswith(user_input):
            matching_themes.append(theme_list_head.get_value())
        theme_list_head = theme_list_head.get_next_node()

    for theme in matching_themes:
        print(theme)

    if len(matching_themes) == 1:
        select_theme = str(input(
            "\nThe only matching theme is " + matching_themes[0] + ". \nDo you want to look at " + 
            matching_themes[0] + " odysseys? Enter y for yes or n for no\n")).lower()
        
        if select_theme == "y":
            selected_odyssey_theme = matching_themes[0]
            print("Selected odyssey theme: " + selected_odyssey_theme)
            odyssey_list_head = my_odyssey_list.get_head_node()
            while odyssey_list_head.get_next_node() is not None:
                sublist_head = odyssey_list_head.get_value().get_head_node()
                if sublist_head.get_value()[0] == selected_odyssey_theme:
                    while sublist_head.get_next_node() is not None:
                        print("|-|-|-|-||-|-|-|-||-|-|-|-||-|-|-|-||-|-|-|-|\n")
                        print("Point of interest: " + sublist_head.get_value()[1])
                        print("Type of Adventure: " + sublist_head.get_value()[2])
                        print("Where in the world: " + sublist_head.get_value()[3])
                        print("\n|-|-|-|-||-|-|-|-||-|-|-|-||-|-|-|-||-|-|-|-|\n")
                        sublist_head = sublist_head.get_next_node()
                odyssey_list_head = odyssey_list_head.get_next_node()

            repeat_loop = str(input("\n Do you want to find other odysseys? Enter y for yes or n for no.\n")).lower()
            if repeat_loop == "y":
              selected_odyssey_theme = ""