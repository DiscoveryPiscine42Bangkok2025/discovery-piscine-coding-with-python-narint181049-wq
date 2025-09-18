def array_of_names(name_dict):
   full_names= []
   for first, last in name_dict.items():
        full_name = f"{first.capitalize()} {last.capitalize()}"
        full_name.append(full_name)
   return full_name
   
persons = {
        "jean": "valjean",
        "grace": "hopper",
        "xavier": "niel",
        "fifi": "brindacier"
    }
    print(array_of_name(persons))