languages = ["English", "Spanish", "Indonesian", "French", "German", "Japanese", "Korean", "Chinese", "Italian", "Portuguese"]
print("Original list:", languages)

print(f"There are {len(languages)} languages in the list.\n")

languages.append("Russian")
print("After append():", languages)

languages.insert(1, "Latin")
print("After insert():", languages)

del languages[2]
print("After del:", languages)

popped_lang = languages.pop()
print(f"After pop() (removed {popped_lang}):", languages)

languages.remove("Indonesian")
print("After remove('Indonesian'):", languages)

print("\nTemporarily sorted with sorted():", sorted(languages))
print("List is still in its current order:", languages)

languages.reverse()
print("\nAfter reverse():", languages)

languages.sort()
print("After sort():", languages)

languages.sort(reverse=True)
print("After sort(reverse=True):", languages)