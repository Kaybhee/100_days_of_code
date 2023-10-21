travel_log = [
 {
 "country" : "france",
 "visits" : 5,
 "cities" : ["paris", "lille", "dijon"],
 },
 {
 "country" : "germany",
 "visits" : 12,
 "cities" : ["berlin", "frankfurt", "stuttgart"],
 }
 ]
def add_new_country(countries, number_visited, cities_list):
    new_travel_log = {}
    new_travel_log["country"] = countries
    new_travel_log["visits"] = number_visited
    new_travel_log["cities"] = cities_list
    travel_log.append(new_travel_log) 
add_new_country(countries = "Russia", number_visited = "2", cities_list = ["moscow", "st petersburg"])
print(travel_log)
