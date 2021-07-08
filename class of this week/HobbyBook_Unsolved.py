

pet1 = {
    "name":"Doubao",
    "age":4,
    "hobbies":["moewing","sleeping","purring","scratching"],
    "wake ups":{"Mon":5,"Tue":5}
}
print(f'{pet1["name"]} is {pet1["age"]} years old.')
print(f'"It has "{len(pet1["hobbies"])}"Hobbies"')
print(f'It loves {pet1["hobbies"][0]}"most.')
print(f'On Monday, it wakes up at {pet1["wake ups"]["Mon"]}')

