#Print the following information in the following
countries_and_capitals = [
("Afghanistan", "Kabul"),
("Albania", "Tirana"),
("Algeria", "Algiers"),
("Andorra", "Andorra la Vella"),
("Angola", "Luanda"),
("Antigua and Barbuda", "Saint John's"),
("Argentina", "Buenos Aires"),
("Armenia", "Yerevan"),
("Australia", "Canberra"),
("Austria", "Vienna"),
("Azerbaijan", "Baku"),
("Bahamas", "Nassau"),
("Bahrain", "Manama"),
("Bangladesh", "Dhaka")]
for index,(country,capital) in enumerate(countries_and_capitals,1):
    print(f"{index}. {country}: {capital}")